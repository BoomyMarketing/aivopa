#!/usr/bin/env python3
"""
Fix navbar display in core pages:
- .navbar missing display:flex height:64px (all 4 pages)
- services.html also missing .navbar__logo/.navbar__links/.navbar__cta CSS
"""
import re, os

BASE = os.path.dirname(__file__)

# CSS to inject after .navbar rule (for pages missing navbar__ rules)
NAVBAR_CLASS_RULES = """
    .navbar__logo { font-family: var(--font-heading); font-size: 1.5rem; color: #0A0A0F; letter-spacing: -0.03em; }
    .navbar__logo span { color: var(--primary); }
    .navbar__links { display: flex; gap: 2.5rem; list-style: none; align-items: center; }
    .navbar__links a { font-size: 0.875rem; font-weight: 500; color: #374151; position: relative; padding-bottom: 2px; }
    .navbar__links a::after { content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 1.5px; background: var(--primary); transition: width 0.3s ease; }
    .navbar__links a:hover::after { width: 100%; }
    .navbar__cta { font-size: 0.85rem; font-weight: 700 !important; color: #fff !important; background: var(--primary) !important; padding: 10px 22px !important; border-radius: 8px; display: inline-flex !important; align-items: center; justify-content: center; line-height: 1; transition: background var(--transition); }
    .navbar__cta::after { display: none !important; }
    .navbar__cta:hover { background: var(--primary-dark) !important; }"""

def fix_file(path, inject_navbar_classes=False):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. Add display:flex + height to .navbar rule
    def add_flex_to_navbar(m):
        rule = m.group(0)
        if 'display:flex' in rule or 'display: flex' in rule:
            return rule
        # inject before the closing brace
        rule = rule.rstrip()
        if rule.endswith('}'):
            rule = rule[:-1] + ' height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; }'
        return rule

    content = re.sub(
        r'\.navbar\s*\{[^}]+\}',
        add_flex_to_navbar,
        content,
        count=1
    )

    # 2. Inject navbar__ class rules if missing
    if inject_navbar_classes and '.navbar__logo' not in content:
        # insert after the .navbar { } block ends
        content = re.sub(
            r'(\.navbar\s*\{[^}]+\})',
            r'\1' + NAVBAR_CLASS_RULES,
            content,
            count=1
        )

    # 3. Ensure mobile media query hides .navbar__links too
    content = re.sub(
        r'(\.navbar__links|\.nav-links)\s*\{\s*display:\s*none',
        '.navbar__links, .nav-links { display: none',
        content
    )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

files = {
    'services.html': True,
    'about.html':    True,
    'contact.html':  True,
    'pricing.html':  True,
}

for fname, inject in files.items():
    path = os.path.join(BASE, fname)
    changed = fix_file(path, inject_navbar_classes=inject)
    print(f"{'fixed' if changed else 'no change'}: {fname}")
