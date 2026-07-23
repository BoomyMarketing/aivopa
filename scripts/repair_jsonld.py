#!/usr/bin/env python3
"""Repair two legacy JSON-LD serialization defects without changing visible content."""

import json
import os
import re
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
JSON_LD_TYPE_RE = re.compile(r'\btype\s*=\s*["\']application/ld\+json["\']', re.IGNORECASE)


def repair(data_text):
    repaired = data_text.replace("\\'", "'")
    repaired = re.sub(r"([}\]])(\s*)(?=[{\[])", r"\1,\2", repaired)
    return repaired


def repair_content(content):
    parts = []
    cursor = 0
    lowered = content.lower()
    changed = False
    invalid = 0
    while True:
        start = lowered.find("<script", cursor)
        if start == -1:
            parts.append(content[cursor:])
            break
        tag_end = content.find(">", start)
        close_start = lowered.find("</script>", tag_end)
        if tag_end == -1 or close_start == -1:
            parts.append(content[cursor:])
            break
        close_end = close_start + len("</script>")
        opening = content[start:tag_end + 1]
        data_text = content[tag_end + 1:close_start]
        parts.append(content[cursor:start])
        if not JSON_LD_TYPE_RE.search(opening):
            parts.append(content[start:close_end])
        else:
            repaired = repair(data_text)
            try:
                data = json.loads(repaired)
            except json.JSONDecodeError:
                invalid += 1
                parts.append(content[start:close_end])
            else:
                if repaired != data_text:
                    parts.append(f"{opening}{json.dumps(data, ensure_ascii=False, separators=(', ', ': '))}</script>")
                    changed = True
                else:
                    parts.append(content[start:close_end])
        cursor = close_end
    return "".join(parts), changed, invalid


def main():
    files = invalid = 0
    for root, directories, names in os.walk(SITE_ROOT):
        directories[:] = [name for name in directories if name not in {".git", "node_modules"}]
        for name in names:
            if not name.endswith(".html"):
                continue
            path = Path(root) / name
            updated, changed, remaining = repair_content(path.read_text(encoding="utf-8"))
            invalid += remaining
            if changed:
                path.write_text(updated, encoding="utf-8")
                files += 1
    print(f"repaired JSON-LD in {files} HTML files; remaining invalid blocks: {invalid}")
    return 1 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
