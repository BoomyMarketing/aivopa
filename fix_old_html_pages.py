#!/usr/bin/env python3
"""Fix 15 OLD_HTML service pages: nav CSS + nav HTML + media query + hamburger JS."""
import re

FILES = [
    'services/affiliate-marketing.html',
    'services/amazon-ads.html',
    'services/b2b-marketing.html',
    'services/conversion-rate-optimization.html',
    'services/dtc-marketing.html',
    'services/ecommerce-marketing.html',
    'services/influencer-marketing.html',
    'services/linkedin-ads.html',
    'services/performance-creative.html',
    'services/programmatic-advertising.html',
    'services/retargeting.html',
    'services/shopify-marketing.html',
    'services/tiktok-ads.html',
    'services/ugc-ads.html',
    'services/youtube-ads.html',
]

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

NEW_NAV_HTML = (
    '<nav class="navbar" id="navbar" role="navigation" aria-label="Main navigation">\n'
    '  <div class="nav-inner">\n'
    '    <a href="../index.html" class="nav-logo" aria-label="Vora &mdash; Home">Vora<span>.</span></a>\n'
    '    <ul class="nav-links" role="menubar">\n'
    '      <li role="none"><a href="../services.html" role="menuitem">Services</a></li>\n'
    '      <li role="none"><a href="../about.html" role="menuitem">About</a></li>\n'
    '      <li role="none"><a href="../pricing.html" role="menuitem">Pricing</a></li>\n'
    '      <li role="none"><a href="../contact.html" role="menuitem">Contact</a></li>\n'
    '      <li role="none"><a href="../contact.html" class="nav-cta" role="menuitem">Get Started</a></li>\n'
    '    </ul>\n'
    '    <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">\n'
    '      <span></span><span></span><span></span>\n'
    '    </button>\n'
    '  </div>\n'
    '  <div class="mobile-menu" id="mobile-menu" role="menu" aria-hidden="true">\n'
    '    <a href="../services.html" role="menuitem">Services</a>\n'
    '    <a href="../about.html" role="menuitem">About</a>\n'
    '    <a href="../pricing.html" role="menuitem">Pricing</a>\n'
    '    <a href="../contact.html" role="menuitem">Contact</a>\n'
    '    <a href="../contact.html" role="menuitem">Get Started &rarr;</a>\n'
    '  </div>\n'
    '</nav>'
)

JS_HAMBURGER = (
    "\n"
    "  const hamburger = document.querySelector('.nav-hamburger');\n"
    "  const mobileMenu = document.getElementById('mobile-menu');\n"
    "  if (hamburger && mobileMenu) {\n"
    "    hamburger.addEventListener('click', () => {\n"
    "      const open = mobileMenu.classList.toggle('open');\n"
    "      hamburger.setAttribute('aria-expanded', String(open));\n"
    "      mobileMenu.setAttribute('aria-hidden', String(!open));\n"
    "    });\n"
    "  }"
)

RE_MINI_CSS = re.compile(
    r'\.navbar\{position:fixed.*?\.navbar\.scrolled \.navbar__menu-btn span\{[^}]+\}',
    re.DOTALL
)
RE_SPAC_CSS = re.compile(
    r'\.navbar \{ position: fixed.*?\.navbar\.scrolled \.navbar__menu-btn span \{[^}]+\}',
    re.DOTALL
)
RE_NAV_HTML = re.compile(r'<nav class="navbar".*?</nav>', re.DOTALL)

# JS scroll listener variants
SCROLL_MINI = "window.addEventListener('scroll',()=>nb.classList.toggle('scrolled',window.scrollY>40));"
SCROLL_SPAC = "  window.addEventListener('scroll', () => navbar.classList.toggle('scrolled', window.scrollY > 40));"


def transform(html):
    if 'nav-hamburger' in html:
        return html, ['already_done']

    changes = []

    # 1. Nav CSS
    if RE_MINI_CSS.search(html):
        html = RE_MINI_CSS.sub(NEW_NAV_CSS, html, count=1)
        changes.append('css-mini')
    elif RE_SPAC_CSS.search(html):
        html = RE_SPAC_CSS.sub(NEW_NAV_CSS, html, count=1)
        changes.append('css-spac')
    else:
        changes.append('css-MISS')

    # 2. Nav HTML
    if RE_NAV_HTML.search(html):
        html = RE_NAV_HTML.sub(lambda m: NEW_NAV_HTML, html, count=1)
        changes.append('html')
    else:
        changes.append('html-MISS')

    # 3. Media query — MINI (minified, no spaces)
    html = re.sub(r'\.navbar\{padding:1rem 1\.5rem\}', '', html)
    html = re.sub(
        r'\.navbar__links,\.navbar__cta\{display:none\}\.navbar__menu-btn\{display:flex\}',
        '.nav-links,.nav-cta{display:none}.nav-hamburger{display:flex}',
        html
    )
    # Media query — SPAC (spaces, semicolons)
    html = re.sub(r'\.navbar \{ padding: 1rem 1\.5rem; \} ?', '', html)
    html = re.sub(
        r'\.navbar__links, \.navbar__cta \{ display: none; \} \.navbar__menu-btn \{ display: flex; \}',
        '.nav-links, .nav-cta { display: none; } .nav-hamburger { display: flex; }',
        html
    )
    changes.append('media')

    # 4. JS hamburger handler
    if SCROLL_MINI in html:
        html = html.replace(SCROLL_MINI, SCROLL_MINI + JS_HAMBURGER)
        changes.append('js-mini')
    elif SCROLL_SPAC in html:
        html = html.replace(SCROLL_SPAC, SCROLL_SPAC + JS_HAMBURGER)
        changes.append('js-spac')
    else:
        changes.append('js-MISS')

    # 5. Remaining purple color cleanup
    for old, new in [
        ('#6C47FF', '#0070F3'),
        ('#7928CA', '#0070F3'),
        ('rgba(108,71,255,', 'rgba(0,112,243,'),
        ('rgba(121,40,202,', 'rgba(0,112,243,'),
    ]:
        html = html.replace(old, new)

    return html, changes


for fname in FILES:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            original = f.read()
        updated, changes = transform(original)
        if updated == original:
            print(f'SKIP {fname} — {changes}')
            continue
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        n = sum(1 for a, b in zip(original.splitlines(), updated.splitlines()) if a != b)
        print(f'OK   {fname} ({n} lines) — {changes}')
    except FileNotFoundError:
        print(f'MISS {fname}')
    except Exception as e:
        print(f'ERR  {fname}: {e}')

print('\nDone.')
