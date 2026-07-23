#!/usr/bin/env python3
"""Replace legacy .html and /local/ internal links with canonical Vercel URLs."""

import argparse
import json
import os
import posixpath
import re
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

SITE_ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://aivopa.com"
HREF_RE = re.compile(r"(?P<prefix>\bhref\s*=\s*[\"'])(?P<url>[^\"']+)(?P<suffix>[\"'])", re.IGNORECASE)
MISSING_LOCAL_CITY_FALLBACKS = {
    "akron": "cleveland",
    "dublin": "columbus",
    "grove-city": "columbus",
    "lakewood": "cleveland",
    "parma": "cleveland",
    "san-antonio": "austin",
    "westerville": "columbus",
}


def page_url(html_path: Path) -> str:
    relative = html_path.relative_to(SITE_ROOT).as_posix()
    if relative == "index.html":
        return "/index.html"
    return "/" + relative


def canonical_path(path: str) -> str:
    if path.endswith("/index.html"):
        return path[: -len("/index.html")] or "/"
    if path.endswith(".html"):
        return path[: -len(".html")] or "/"
    return path or "/"


def load_redirects() -> dict[str, str]:
    config = json.loads((SITE_ROOT / "vercel.json").read_text(encoding="utf-8"))
    return {
        item["source"].rstrip("/") or "/": item["destination"].rstrip("/") or "/"
        for item in config.get("redirects", [])
    }


def target_exists(href: str) -> bool:
    path = urlsplit(href).path.rstrip("/") or "/"
    relative = path.strip("/")
    candidates = [SITE_ROOT / "index.html"] if not relative else [
        SITE_ROOT / relative / "index.html",
        SITE_ROOT / (relative + ".html"),
    ]
    return any(candidate.exists() for candidate in candidates)


def normalize_href(source: Path, href: str, redirects: dict[str, str]) -> str:
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return href

    parsed = urlsplit(href)
    if parsed.scheme and parsed.netloc and parsed.netloc != "aivopa.com":
        return href
    if parsed.netloc and parsed.netloc != "aivopa.com":
        return href

    resolved = urlsplit(urljoin(DOMAIN + page_url(source), href))
    if resolved.netloc != "aivopa.com":
        return href

    path = canonical_path(posixpath.normpath(resolved.path))
    path = redirects.get(path, path)
    parts = path.strip("/").split("/")
    if len(parts) == 3 and parts[0] == "local" and parts[1] in MISSING_LOCAL_CITY_FALLBACKS:
        path = f"/{parts[2]}/{MISSING_LOCAL_CITY_FALLBACKS[parts[1]]}"
    return urlunsplit(("", "", path, resolved.query, resolved.fragment))


def process_file(path: Path, redirects: dict[str, str], write: bool) -> tuple[int, int]:
    content = path.read_text(encoding="utf-8")
    changed = 0
    legacy = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changed, legacy
        href = match.group("url")
        if ".html" not in href and "/local/" not in href:
            return match.group(0)
        normalized = normalize_href(path, href, redirects)
        if normalized == href or not target_exists(normalized):
            return match.group(0)
        legacy += 1
        changed += 1
        return f"{match.group('prefix')}{normalized}{match.group('suffix')}"

    updated = HREF_RE.sub(replace, content)
    if write and updated != content:
        path.write_text(updated, encoding="utf-8")
    return changed, legacy


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Report legacy internal links without editing files.")
    args = parser.parse_args()

    redirects = load_redirects()
    files_changed = 0
    links_changed = 0
    for root, directories, names in os.walk(SITE_ROOT):
        directories[:] = [name for name in directories if name not in {".git", "node_modules"}]
        for name in names:
            if not name.endswith(".html"):
                continue
            changed, _ = process_file(Path(root) / name, redirects, write=not args.check)
            if changed:
                files_changed += 1
                links_changed += changed

    label = "legacy links found" if args.check else "links normalized"
    print(f"{label}: {links_changed} across {files_changed} HTML files")
    return 1 if args.check and links_changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
