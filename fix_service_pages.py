#!/usr/bin/env python3
"""Redesign service subpages: purple #6C47FF -> blue #0070F3 + fix nav/footer CSS.
Usage: python fix_service_pages.py [files...]
Defaults to all services/*.html
"""
import sys, glob, re

FILES = sys.argv[1:] if len(sys.argv) > 1 else sorted(glob.glob('services/*.html'))

OLD_NAV_CSS = (
    '    /* NAV */\n'
    '    .navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 100; display: flex; align-items: center; justify-content: space-between; padding: 1.25rem 2rem; transition: background var(--transition), box-shadow var(--transition); }\n'
    '    .navbar.scrolled { background: rgba(10,10,15,0.97); box-shadow: 0 2px 24px rgba(0,0,0,0.3); }\n'
    '    .navbar__logo { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; color: #fff; }\n'
    '    .navbar__logo span { color: var(--primary); }\n'
    '    .navbar__links { display: flex; gap: 2rem; list-style: none; }\n'
    '    .navbar__links a { color: rgba(255,255,255,0.8); font-size: 0.95rem; font-weight: 500; transition: color var(--transition); }\n'
    '    .navbar__links a:hover { color: #fff; }\n'
    '    .navbar__cta { background: var(--primary); color: #fff; font-weight: 600; font-size: 0.9rem; padding: 0.6rem 1.4rem; border-radius: var(--radius); transition: opacity var(--transition); }\n'
    '    .navbar__cta:hover { opacity: 0.88; }'
)

NEW_NAV_CSS = (
    '    /* NAV */\n'
    '    .navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; background: rgba(255,255,255,0.97); -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,112,243,0.1); transition: background var(--transition), box-shadow var(--transition); }\n'
    '    .nav-inner { height: 64px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; }\n'
    '    .navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }\n'
    '    .nav-hamburger { display: none; background: none; border: none; padding: 0; flex-direction: column; gap: 5px; cursor: pointer; }\n'
    '    .nav-hamburger span { display: block; width: 24px; height: 2px; background: #374151; border-radius: 2px; }\n'
    '    .mobile-menu { display: none; position: absolute; top: 100%; left: 0; right: 0; background: #fff; box-shadow: 0 8px 24px rgba(0,0,0,0.1); padding: 1.5rem; flex-direction: column; gap: 0.5rem; border-bottom: 1px solid rgba(0,112,243,0.1); }\n'
    '    .mobile-menu.open { display: flex; }\n'
    '    .mobile-menu a { font-size: 0.9rem; font-weight: 500; color: #374151; padding: 0.65rem 0; border-bottom: 1px solid rgba(0,0,0,0.06); transition: color 0.3s; }\n'
    "    .mobile-menu a:last-child { color: #fff !important; background: #0070F3; border: none; padding: 10px 22px; border-radius: 8px; text-align: center; font-weight: 700; margin-top: 0.5rem; display: flex; justify-content: center; }\n"
    '    .nav-logo { font-family: var(--font-heading); font-size: 1.5rem; color: #0A0A0F; letter-spacing: -0.03em; }\n'
    '    .nav-logo span { color: var(--primary); }\n'
    '    .nav-links { display: flex; gap: 2.5rem; list-style: none; }\n'
    '    .nav-links a { font-size: 0.875rem; font-weight: 500; color: #374151; position: relative; padding-bottom: 2px; }\n'
    "    .nav-links a::after { content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 1.5px; background: var(--primary); transition: width 0.3s ease; }\n"
    '    .nav-links a:hover::after { width: 100%; }\n'
    '    .nav-cta { font-size: 0.85rem; font-weight: 700; color: #fff !important; background: #0070F3 !important; padding: 10px 22px !important; border-radius: 8px; display: inline-flex !important; align-items: center; justify-content: center; line-height: 1; transition: background var(--transition), transform var(--transition); }\n'
    '    .nav-cta:hover { background: #0052CC !important; transform: translateY(-1px); }'
)

OLD_FOOTER_CSS = (
    '    /* FOOTER */\n'
    '    footer { background: var(--dark); color: rgba(255,255,255,0.6); padding: 3rem 2rem; }\n'
    '    .footer-inner { max-width: var(--max-w); margin: 0 auto; display: flex; flex-wrap: wrap; gap: 2rem; align-items: center; justify-content: space-between; }\n'
    '    .footer-logo { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 700; color: #fff; }\n'
    '    .footer-logo span { color: var(--primary); }\n'
    '    .footer-links { display: flex; gap: 1.5rem; flex-wrap: wrap; }\n'
    '    .footer-links a { font-size: 0.88rem; color: rgba(255,255,255,0.6); transition: color var(--transition); }\n'
    '    .footer-links a:hover { color: #fff; }\n'
    '    .footer-copy { font-size: 0.82rem; width: 100%; text-align: center; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.08); }'
)

NEW_FOOTER_CSS = (
    '    /* FOOTER */\n'
    '    .footer { background: #060606; }\n'
    '    .footer-inner { max-width: var(--max-w); margin: 0 auto; }\n'
    '    .footer-top { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; padding: 4rem 3rem 3rem; border-bottom: 1px solid #1e1e1e; }\n'
    '    .footer-brand {}\n'
    '    .footer-logo { font-family: var(--font-heading); font-size: 1.6rem; color: #fff; display: inline-block; margin-bottom: 1rem; }\n'
    '    .footer-logo span { color: var(--primary); }\n'
    '    .footer-tagline { font-size: 0.85rem; color: rgba(255,255,255,0.4); line-height: 1.7; max-width: 280px; margin-bottom: 1.5rem; }\n'
    '    .footer-socials { display: flex; gap: 0.75rem; }\n'
    '    .footer-col h4 { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(255,255,255,0.55); margin-bottom: 1.25rem; }\n'
    '    .footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 0.65rem; }\n'
    '    .footer-col ul a { font-size: 0.82rem; color: rgba(255,255,255,0.3); transition: color var(--transition); }\n'
    '    .footer-col ul a:hover { color: var(--primary); }\n'
    '    .footer-contact-item { margin-top: 0.65rem; }\n'
    '    .footer-contact-item a { font-size: 0.82rem; color: rgba(255,255,255,0.3); transition: color var(--transition); }\n'
    '    .footer-contact-item a:hover { color: var(--primary); }\n'
    '    .footer-bottom { display: flex; align-items: center; justify-content: space-between; padding: 1.5rem 3rem; flex-wrap: wrap; gap: 1rem; }\n'
    '    .footer-copy { font-size: 0.75rem; color: rgba(255,255,255,0.2); letter-spacing: 0.05em; }\n'
    '    .footer-bl { display: flex; gap: 1.5rem; }\n'
    '    .footer-bl a { font-size: 0.75rem; color: rgba(255,255,255,0.25); transition: color var(--transition); }\n'
    '    .footer-bl a:hover { color: var(--primary); }'
)

OLD_MEDIA = (
    '    @media (max-width: 768px) {\n'
    '      .navbar__links { display: none; }\n'
    '      .stats-bar { gap: 1.5rem; }\n'
    '    }'
)

NEW_MEDIA = (
    '    @media (max-width: 768px) {\n'
    '      .nav-links, .nav-cta { display: none; }\n'
    '      .nav-hamburger { display: flex; }\n'
    '      .stats-bar { gap: 1.5rem; flex-wrap: wrap; }\n'
    '      .footer-top { grid-template-columns: 1fr; gap: 2rem; padding: 2.5rem 1.5rem 2rem; }\n'
    '      .footer-bottom { padding: 1.25rem 1.5rem; flex-direction: column; text-align: center; }\n'
    '    }'
)

OLD_JS_SCROLL = (
    "    const navbar = document.getElementById('navbar');\n"
    "    window.addEventListener('scroll', () => navbar.classList.toggle('scrolled', window.scrollY > 40));"
)

NEW_JS_SCROLL = (
    "    const navbar = document.getElementById('navbar');\n"
    "    window.addEventListener('scroll', () => navbar.classList.toggle('scrolled', window.scrollY > 40));\n"
    "    const hamburger = document.querySelector('.nav-hamburger');\n"
    "    const mobileMenu = document.getElementById('mobile-menu');\n"
    "    if (hamburger && mobileMenu) {\n"
    "      hamburger.addEventListener('click', () => {\n"
    "        const open = mobileMenu.classList.toggle('open');\n"
    "        hamburger.setAttribute('aria-expanded', String(open));\n"
    "        mobileMenu.setAttribute('aria-hidden', String(!open));\n"
    "      });\n"
    "    }"
)


def transform(html):
    # 1. Structural CSS/JS blocks FIRST — before any color substitutions corrupt the match strings
    # Use regex for nav CSS: handles both single-line and multi-line .navbar{} variants
    if '.navbar__logo' in html:
        html = re.sub(
            r'/\* NAV \*/.*?\.navbar__cta:hover \{ opacity: 0\.88; \}',
            NEW_NAV_CSS,
            html, count=1, flags=re.DOTALL
        )
    elif OLD_NAV_CSS in html:
        html = html.replace(OLD_NAV_CSS, NEW_NAV_CSS)
    if OLD_FOOTER_CSS in html:
        html = html.replace(OLD_FOOTER_CSS, NEW_FOOTER_CSS)
    if OLD_MEDIA in html:
        html = html.replace(OLD_MEDIA, NEW_MEDIA)
    if OLD_JS_SCROLL in html and "querySelector('.nav-hamburger')" not in html:
        html = html.replace(OLD_JS_SCROLL, NEW_JS_SCROLL)

    # 2. CSS variable replacements
    html = html.replace('--primary: #6C47FF', '--primary: #0070F3')
    html = html.replace('--primary: #7928CA', '--primary: #0070F3')
    html = html.replace('--dark: #0F0F1A', '--dark: #0A0A0F')
    html = html.replace('--bg-soft: #F5F3FF', '--bg-soft: #EEF4FF')
    html = html.replace('--bg-soft: #F5F0FF', '--bg-soft: #EEF4FF')
    html = html.replace('--text: #1A1A2E', '--text: #374151')

    # 3. Inline color replacements
    for old, new in [
        ('#6C47FF', '#0070F3'),
        ('#7928CA', '#0070F3'),
        ('#F5F3FF', '#EEF4FF'),
        ('#F5F0FF', '#EEF4FF'),
        ('#e8e4ff', 'rgba(0,112,243,0.08)'),
        ('#E8E4FF', 'rgba(0,112,243,0.08)'),
        ('#0F0F1A', '#0A0A0F'),
        ('#1A1A2E', '#374151'),
    ]:
        html = html.replace(old, new)

    # 4. rgba purple -> blue
    html = html.replace('rgba(108,71,255,', 'rgba(0,112,243,')
    html = html.replace('rgba(108, 71, 255,', 'rgba(0, 112, 243,')
    html = html.replace('rgba(121,40,202,', 'rgba(0,112,243,')
    html = html.replace('rgba(121, 40, 202,', 'rgba(0, 112, 243,')
    html = html.replace('rgba(15,15,26,', 'rgba(10,10,15,')

    return html


for fname in FILES:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            original = f.read()
        updated = transform(original)
        if updated == original:
            print(f'SKIP {fname} (no changes)')
            continue
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        n = sum(1 for a, b in zip(original.splitlines(), updated.splitlines()) if a != b)
        print(f'OK   {fname} ({n} lines changed)')
    except FileNotFoundError:
        print(f'MISSING {fname}')

print('Done.')
