#!/usr/bin/env python3
"""Fix local pages nav bugs:
1. .mobile-menu has no CSS → always visible
2. .navbar has no CSS → not sticky, no background
3. .nav-hamburger has no CSS
4. JS uses getElementById('site-nav') but HTML has id='navbar'
"""
import os, re

BASE = os.path.dirname(__file__)
LOCAL = os.path.join(BASE, 'local')

# CSS to insert after .nav-toggle block
NAV_FIX_CSS = """
        .navbar {
            position: sticky;
            top: 0;
            z-index: 500;
            background: rgba(255, 255, 255, 0.97);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(0, 112, 243, 0.1);
            transition: box-shadow var(--transition);
        }
        .navbar.scrolled {
            box-shadow: 0 2px 20px rgba(0, 112, 243, 0.08);
        }
        .nav-hamburger {
            display: none;
            background: none;
            border: none;
            padding: 0;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
        }
        .nav-hamburger span {
            display: block;
            width: 24px;
            height: 2px;
            background: #374151;
            border-radius: 2px;
        }
        .mobile-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: #fff;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            padding: 1.5rem;
            flex-direction: column;
            gap: 0.5rem;
            border-bottom: 1px solid rgba(0, 112, 243, 0.1);
            z-index: 499;
        }
        .mobile-menu.open { display: flex; }
        .mobile-menu a {
            font-size: 0.9rem;
            font-weight: 500;
            color: #374151;
            padding: 0.65rem 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.06);
            transition: color 0.3s;
        }
        .mobile-menu a:last-child {
            color: #fff !important;
            background: var(--primary);
            border: none;
            padding: 10px 22px;
            border-radius: 8px;
            text-align: center;
            font-weight: 700;
            margin-top: 0.5rem;
            display: flex;
            justify-content: center;
        }"""

HAMBURGER_JS = """
        /* ── Mobile nav: hamburger ── */
        var hamburger = document.querySelector('.nav-hamburger');
        var mobileMenu = document.getElementById('mobile-menu');
        if (hamburger && mobileMenu) {
            hamburger.addEventListener('click', function () {
                var open = mobileMenu.classList.toggle('open');
                hamburger.setAttribute('aria-expanded', String(open));
                mobileMenu.setAttribute('aria-hidden', String(!open));
            });
            document.addEventListener('click', function (e) {
                if (mobileMenu.classList.contains('open') &&
                    !mobileMenu.contains(e.target) &&
                    !hamburger.contains(e.target)) {
                    mobileMenu.classList.remove('open');
                    hamburger.setAttribute('aria-expanded', 'false');
                    mobileMenu.setAttribute('aria-hidden', 'true');
                }
            });
        }"""

def fix_file(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. Add .navbar + .nav-hamburger + .mobile-menu CSS after .nav-toggle block
    if '.navbar {' not in content and '.nav-toggle {' in content:
        content = content.replace(
            '.nav-toggle {',
            NAV_FIX_CSS + '\n        .nav-toggle {',
            1
        )

    # 2. Update media query: replace .nav-toggle with .nav-hamburger, hide .nav-cta
    content = re.sub(
        r'\.nav-toggle\s*\{\s*display:\s*block;?\s*\}',
        '.nav-hamburger { display: flex; }\n            .nav-cta { display: none !important; }',
        content
    )

    # 3. Remove .nav-links.open dropdown block (replaced by .mobile-menu.open)
    content = re.sub(
        r'\.nav-links\.open\s*\{[^}]+\}',
        '',
        content,
        flags=re.DOTALL
    )

    # 4. Fix JS: site-nav → navbar
    content = content.replace(
        "document.getElementById('site-nav')",
        "document.getElementById('navbar')"
    )

    # 5. Add hamburger JS (replace old mobile nav close handler)
    OLD_CLOSE = re.compile(
        r'/\* ── Mobile nav: close on outside click ── \*/.*?}\s*\}\s*\)\s*;',
        re.DOTALL
    )
    if OLD_CLOSE.search(content):
        content = OLD_CLOSE.sub(HAMBURGER_JS, content)
    elif 'nav-hamburger' not in content.split('<script')[1] if '<script' in content else True:
        # Inject before closing IIFE
        content = content.replace(
            '\n    }());',
            HAMBURGER_JS + '\n    }();',
            1
        )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated = skipped = 0
for city in sorted(os.listdir(LOCAL)):
    city_path = os.path.join(LOCAL, city)
    if not os.path.isdir(city_path): continue
    for svc in sorted(os.listdir(city_path)):
        svc_path = os.path.join(city_path, svc)
        if not os.path.isdir(svc_path): continue
        idx = os.path.join(svc_path, 'index.html')
        if not os.path.exists(idx): continue
        if fix_file(idx):
            updated += 1
        else:
            skipped += 1

print(f"Updated: {updated}  Skipped: {skipped}")
