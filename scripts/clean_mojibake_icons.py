#!/usr/bin/env python3
"""Replace mojibake-only decorative icons with an ASCII-safe marker."""

import os
import re
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
MOJIBAKE_ICON_RE = re.compile(r'(<div class="ch-icon">)[^<]*[\u0400-\u04FF][^<]*(</div>)')


def main():
    files = replacements = 0
    for root, directories, names in os.walk(SITE_ROOT):
        directories[:] = [name for name in directories if name not in {".git", "node_modules"}]
        for name in names:
            if not name.endswith(".html"):
                continue
            path = Path(root) / name
            content = path.read_text(encoding="utf-8")
            updated, count = MOJIBAKE_ICON_RE.subn(r'\1&#8226;\2', content)
            if count:
                path.write_text(updated, encoding="utf-8")
                files += 1
                replacements += count
    print(f"replaced {replacements} mojibake icons in {files} HTML files")


if __name__ == "__main__":
    main()
