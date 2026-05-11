#!/usr/bin/env python3
"""Fix purple (#7928CA) pages → blue (#0070F3) + full footer CSS + nav fixes.
Usage: python fix_purple_pages.py pricing.html [contact.html ...]
"""
import sys, re

FILES = sys.argv[1:] if len(sys.argv) > 1 else ['pricing.html', 'contact.html']

FOOTER_CSS = """\
    .footer { background: #060606; }
    .footer-inner { max-width: var(--max-w); margin: 0 auto; }
    .footer-top { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; padding: 4rem 3rem 3rem; border-bottom: 1px solid #1e1e1e; }
    .footer-brand {}
    .footer-logo { font-family: var(--font-heading); font-size: 1.6rem; color: #fff; display: inline-block; margin-bottom: 1rem; }
    .footer-logo span { color: var(--primary); }
    .footer-tagline { font-size: 0.85rem; color: rgba(255,255,255,0.4); line-height: 1.7; max-width: 280px; margin-bottom: 1.5rem; }
    .footer-socials { display: flex; gap: 0.75rem; }
    .footer-col h4 { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(255,255,255,0.55); margin-bottom: 1.25rem; }
    .footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 0.65rem; }
    .footer-col ul a { font-size: 0.82rem; color: rgba(255,255,255,0.3); transition: color var(--transition); }
    .footer-col ul a:hover { color: var(--primary); }
    .footer-contact-item { margin-top: 0.65rem; }
    .footer-contact-item a { font-size: 0.82rem; color: rgba(255,255,255,0.3); transition: color var(--transition); }
    .footer-contact-item a:hover { color: var(--primary); }
    .footer-bottom { display: flex; align-items: center; justify-content: space-between; padding: 1.5rem 3rem; flex-wrap: wrap; gap: 1rem; }
    .footer-copy { font-size: 0.75rem; color: rgba(255,255,255,0.2); letter-spacing: 0.05em; }
    .footer-bl { display: flex; gap: 1.5rem; }
    .footer-bl a { font-size: 0.75rem; color: rgba(255,255,255,0.25); transition: color var(--transition); }
    .footer-bl a:hover { color: var(--primary); }"""

def transform(html):
    # 1. Primary color purple → blue
    html = html.replace('--primary: #7928CA', '--primary: #0070F3')
    html = html.replace('--primary: #6C47FF', '--primary: #0070F3')
    html = html.replace('--bg-soft: #F5F3FF', '--bg-soft: #EEF4FF')
    html = html.replace('--bg-soft: #EEF0FF', '--bg-soft: #EEF4FF')

    # 2. Inline purple → blue
    for purple, blue in [('#7928CA','#0070F3'),('#6C47FF','#0070F3'),('#5535e0','#0052CC'),('#5409C5','#0052CC'),('#4527a0','#003EA8')]:
        html = html.replace(purple, blue)

    # 3. Purple rgba → blue rgba
    html = html.replace('rgba(108,71,255,', 'rgba(0,112,243,')
    html = html.replace('rgba(108, 71, 255,', 'rgba(0, 112, 243,')
    html = html.replace('rgba(121,40,202,', 'rgba(0,112,243,')
    html = html.replace('rgba(121, 40, 202,', 'rgba(0, 112, 243,')

    # 4. Nav outer: remove flex layout, make it a shell with bg
    html = html.replace(
        '.navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; display: flex; align-items: center; justify-content: space-between; padding: 1.25rem 3rem; transition: background var(--transition), padding var(--transition); }',
        '.navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; background: rgba(255,255,255,0.97); -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,112,243,0.1); transition: background var(--transition), box-shadow var(--transition); }'
    )
    # 5. Nav scrolled
    html = html.replace(
        '.navbar.scrolled { background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); padding: 0.85rem 3rem; box-shadow: 0 1px 0 rgba(0,112,243,0.1); }',
        '.navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }'
    )
    # 6. Add .nav-inner CSS after .navbar.scrolled if missing
    SCROLLED = '.navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }'
    NAV_INNER = '\n    .nav-inner { height: 64px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; }'
    if SCROLLED in html and 'nav-inner { height: 64px' not in html:
        html = html.replace(SCROLLED, SCROLLED + NAV_INNER)

    # 7. Nav CTA → blue with !important
    html = html.replace(
        '.nav-cta { font-size: 0.875rem; font-weight: 600; color: #fff; background: var(--primary); padding: 0.6rem 1.4rem; border-radius: var(--radius); transition: background var(--transition), transform var(--transition); }',
        '.nav-cta { font-size: 0.85rem; font-weight: 700; color: #fff !important; background: #0070F3 !important; padding: 10px 22px !important; border-radius: 8px; display: inline-flex !important; align-items: center; justify-content: center; line-height: 1; transition: background var(--transition), transform var(--transition); }'
    )
    html = html.replace(
        '.nav-cta:hover { background: #0052CC; transform: translateY(-1px); }',
        '.nav-cta:hover { background: #0052CC !important; transform: translateY(-1px); }'
    )

    # 8. CSS class rename: .navbar__menu-btn → .nav-hamburger
    html = html.replace('.navbar__menu-btn { display: none;', '.nav-hamburger { display: none;')
    html = html.replace('.navbar__menu-btn span {', '.nav-hamburger span {')
    html = html.replace('.navbar__menu-btn { display: flex; }', '.nav-hamburger { display: flex; }')

    # 9. Mobile media query hide rule
    html = html.replace('.navbar__links, .nav-cta { display: none; }', '.nav-links { display: none; }')

    # 10. Mobile menu CSS
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
    # Inject BEFORE the @media block (find the last CSS rule before @media)
    if 'mobile-menu { display: none' not in html:
        html = re.sub(
            r'(\n    @media \(max-width: 768px\) \{)',
            MOBILE_CSS + r'\1',
            html, count=1
        )

    # 11. Old simple footer → full column footer
    html = re.sub(
        r'    footer \{ background: var\(--dark\)[^}]+\}\n'
        r'    \.footer-inner \{ [^}]+display: flex[^}]+\}\n'
        r'    \.footer-logo \{ [^}]+\}\n'
        r'    \.footer-logo span \{ [^}]+\}\n'
        r'    \.footer-links \{ [^}]+\}\n'
        r'    \.footer-links a \{ [^}]+\}\n'
        r'    \.footer-links a:hover \{ [^}]+\}\n'
        r'    \.footer-copy \{ [^}]+\}',
        FOOTER_CSS,
        html, count=1
    )

    # 12. Media query footer → grid
    html = html.replace(
        '      footer { padding: 2rem 1.5rem; }',
        '      .footer-top { grid-template-columns: 1fr; gap: 2rem; padding: 2.5rem 1.5rem 2rem; }\n      .footer-bottom { padding: 1.25rem 1.5rem; flex-direction: column; text-align: center; }'
    )

    return html


for fname in FILES:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            original = f.read()
        updated = transform(original)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        diff = sum(1 for a, b in zip(original.splitlines(), updated.splitlines()) if a != b)
        print(f"OK {fname} ({diff} lines changed)")
    except FileNotFoundError:
        print(f"MISSING {fname}")

print("Done.")
