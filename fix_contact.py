#!/usr/bin/env python3
"""One-shot patch: contact.html purple→blue, nav CSS fixes, dark trust-stat→light."""

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# 1. Primary color
html = html.replace('--primary: #7928CA', '--primary: #0070F3')
html = html.replace('--bg-soft: #F5F3FF', '--bg-soft: #EEF4FF')

# 2. Purple rgba → blue rgba
html = html.replace('rgba(108,71,255,', 'rgba(0,112,243,')
html = html.replace('rgba(108, 71, 255,', 'rgba(0, 112, 243,')

# 3. Purple hover hex
html = html.replace('#5535e0', '#0052CC')
html = html.replace('#7928CA', '#0070F3')

# 4. Nav outer: remove flex layout + padding + replace with sticky transparent shell
html = html.replace(
    '.navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; display: flex; align-items: center; justify-content: space-between; padding: 1.25rem 3rem; transition: background var(--transition), padding var(--transition); }',
    '.navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; background: rgba(255,255,255,0.97); -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,112,243,0.1); transition: background var(--transition), box-shadow var(--transition); }'
)

# 5. Nav scrolled
html = html.replace(
    '.navbar.scrolled { background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); padding: 0.85rem 3rem; box-shadow: 0 1px 0 rgba(0,112,243,0.1); }',
    '.navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }'
)

# 6. Add .nav-inner CSS after the .navbar.scrolled rule (if not there already)
NAV_INNER_CSS = '\n    .nav-inner { height: 64px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; }'
SCROLLED_RULE = '.navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }'
if SCROLLED_RULE in html and 'nav-inner { height: 64px' not in html:
    html = html.replace(SCROLLED_RULE, SCROLLED_RULE + NAV_INNER_CSS)

# 7. Nav CTA: fix to use !important overrides like design system
html = html.replace(
    '.nav-cta { font-size: 0.875rem; font-weight: 600; color: #fff; background: var(--primary); padding: 0.6rem 1.4rem; border-radius: var(--radius); transition: background var(--transition), transform var(--transition); }',
    '.nav-cta { font-size: 0.85rem; font-weight: 700; color: #fff !important; background: #0070F3 !important; padding: 10px 22px !important; border-radius: 8px; display: inline-flex !important; align-items: center; justify-content: center; line-height: 1; transition: background var(--transition), transform var(--transition); }'
)
html = html.replace(
    '.nav-cta:hover { background: #0052CC; transform: translateY(-1px); }',
    '.nav-cta:hover { background: #0052CC !important; transform: translateY(-1px); }'
)

# 8. Hamburger CSS class rename: .navbar__menu-btn → .nav-hamburger
html = html.replace('.navbar__menu-btn { display: none;', '.nav-hamburger { display: none;')
html = html.replace('.navbar__menu-btn span {', '.nav-hamburger span {')
html = html.replace('.navbar__menu-btn { display: flex; }', '.nav-hamburger { display: flex; }')

# 9. Mobile query: .navbar__links → .nav-links (the hide rule)
html = html.replace('.navbar__links, .nav-cta { display: none; }', '.nav-links { display: none; }')

# 10. Add mobile-menu CSS if missing
MOBILE_CSS = (
    '\n    .mobile-menu { display: none; position: absolute; top: 100%; left: 0; right: 0;'
    ' background: #fff; box-shadow: 0 8px 24px rgba(0,0,0,0.1); padding: 1.5rem;'
    ' flex-direction: column; gap: 0.5rem; border-bottom: 1px solid rgba(0,112,243,0.1); }'
    '\n    .mobile-menu.open { display: flex; }'
    '\n    .mobile-menu a { font-size: 0.9rem; font-weight: 500; color: #374151;'
    ' padding: 0.65rem 0; border-bottom: 1px solid rgba(0,0,0,0.06); transition: color 0.3s; }'
    '\n    .mobile-menu a:last-child { color: #fff !important; background: #0070F3;'
    ' border: none; padding: 10px 22px; border-radius: 8px; text-align: center;'
    ' font-weight: 700; margin-top: 0.5rem; display: flex; justify-content: center; }'
)
if 'mobile-menu { display: none' not in html:
    html = html.replace('.nav-hamburger { display: flex; }', '.nav-hamburger { display: flex; }' + MOBILE_CSS)

# 11. Dark trust-stat card → light
html = html.replace('.trust-stat { background: #0a0a0a;', '.trust-stat { background: #fff;')
# trust-stat span text color: #666 is fine on white

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

diff = sum(1 for a, b in zip(original.splitlines(), html.splitlines()) if a != b)
print(f"OK contact.html ({diff} lines changed)")
