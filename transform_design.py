#!/usr/bin/env python3
"""
Transform core pages from old design (Berkshire Swash + pink) to
new design (Space Grotesk + blue) — matching local/ pages style.
"""
import re

FILES = ['index.html', 'about.html', 'pricing.html', 'contact.html', 'services.html']

def transform(html: str, filename: str) -> str:
    # 1. Replace font imports — Berkshire Swash → Space Grotesk
    html = html.replace(
        'Berkshire+Swash&family=Inter',
        'Space+Grotesk:wght@400;500;600;700&family=Inter'
    )
    html = html.replace(
        "Berkshire+Swash&amp;family=Inter",
        "Space+Grotesk:wght@400;500;600;700&amp;family=Inter"
    )
    # Remove preload for berkshireswash woff2 (not needed, slows LCP)
    html = re.sub(
        r'<link rel="preload" href="https://fonts\.gstatic\.com/s/berkshireswash[^"]*"[^>]*/>\s*\n?',
        '',
        html
    )
    # Also remove preload for the stylesheet that references it
    html = re.sub(
        r'<link rel="preload" href="https://fonts\.googleapis\.com/css2\?family=Berkshire[^"]*"[^>]*/>\s*\n?',
        '',
        html
    )

    # 2. CSS variable changes
    html = html.replace("--primary: #D2085C", "--primary: #0070F3")
    html = html.replace("--navy: #13023E",    "--navy: #0A0A0F")
    html = html.replace("--text: #13023E",    "--text: #374151")
    html = html.replace("--purple: #6C47FF",  "--purple: #7928CA")
    html = html.replace("--accent: #F5F0FF",  "--accent: #EEF4FF")
    html = html.replace("--gray-mid: #9b97aa","--gray-mid: #9CA3AF")
    html = html.replace("--gray-light: #f0eef8", "--gray-light: #F7F9FC")

    # 3. Font family declarations
    html = html.replace("'Berkshire Swash', serif", "'Space Grotesk', sans-serif")
    html = html.replace('"Berkshire Swash", serif', '"Space Grotesk", sans-serif')

    # 4. Inline hex colors
    html = html.replace("#D2085C", "#0070F3")
    html = html.replace("#13023E", "#0A0A0F")
    html = html.replace("#080016", "#050810")
    html = html.replace("#6C47FF", "#7928CA")

    # 5. RGBA pink → blue (210,8,92 → 0,112,243)
    html = html.replace("rgba(210,8,92,",   "rgba(0,112,243,")
    html = html.replace("rgba(210, 8, 92,", "rgba(0, 112, 243,")

    # 6. RGBA navy → dark neutral (19,2,62 → 17,24,39)
    # Used as body text / border colors — switch to neutral dark
    html = html.replace("rgba(19,2,62,",   "rgba(17,24,39,")
    html = html.replace("rgba(19, 2, 62,", "rgba(17, 24, 39,")

    # 7. Remove cursor: none (bad UX, bad CWV)
    html = re.sub(r'\s*cursor:\s*none\s*;', '', html)

    # 8. Remove custom cursor CSS blocks
    html = re.sub(
        r'/\* ── CURSOR ──[^*]*\*/(.*?)(?=/\* ── SCROLL|/\* ──)',
        '',
        html,
        flags=re.DOTALL
    )
    html = re.sub(r'\s*#cursor\s*\{[^}]+\}\s*', '\n', html)
    html = re.sub(r'\s*#cursor::before\s*,\s*#cursor::after\s*\{[^}]+\}\s*', '\n', html)
    html = re.sub(r'\s*#cursor::before\s*\{[^}]+\}\s*', '\n', html)
    html = re.sub(r'\s*#cursor::after\s*\{[^}]+\}\s*', '\n', html)
    html = re.sub(r'\s*#cursor\.cursor-hover[^{]*\{[^}]+\}\s*', '\n', html)
    html = re.sub(r'\s*#cursor-dot\s*\{[^}]+\}\s*', '\n', html)

    # 9. Remove cursor HTML elements
    html = re.sub(r'\s*<div id="cursor"[^>]*/>\s*\n?', '\n', html)
    html = re.sub(r'\s*<div id="cursor-dot"[^>]*/>\s*\n?', '\n', html)

    # 10. Hero gradient: update navy-based gradients to blue-dark
    html = html.replace(
        "background: radial-gradient(circle, rgba(0,112,243,0.18) 0%, transparent 70%)",
        "background: radial-gradient(circle, rgba(0,112,243,0.15) 0%, transparent 70%)"
    )

    # 11. Navbar: make it white by default (not transparent-first), matching local pages
    # The navbar starts transparent and becomes white on scroll — invert this
    html = html.replace(
        ".navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; display: flex; align-items: center; justify-content: space-between; padding: 1.5rem 3rem; transition: background var(--transition), padding var(--transition); }",
        ".navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; display: flex; align-items: center; justify-content: space-between; padding: 1rem 3rem; background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,112,243,0.08); transition: background var(--transition), padding var(--transition), box-shadow var(--transition); }"
    )
    html = html.replace(
        ".navbar.scrolled { background: rgba(255,255,255,0.95); backdrop-filter: blur(12px); padding: 1rem 3rem; box-shadow: 0 1px 0 rgba(17,24,39,0.08); }",
        ".navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }"
    )
    # Nav logo color — change from navy to dark
    html = html.replace(
        ".navbar__logo { font-family: var(--font-heading); font-size: 1.5rem; color: var(--navy); letter-spacing: -0.02em; }",
        ".navbar__logo { font-family: var(--font-heading); font-size: 1.5rem; color: var(--dark, #0A0A0F); letter-spacing: -0.03em; }"
    )
    # Nav links color
    html = html.replace(
        ".navbar__links a { font-size: 0.85rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--navy); position: relative; padding-bottom: 3px; }",
        ".navbar__links a { font-size: 0.875rem; font-weight: 500; color: #374151; position: relative; padding-bottom: 2px; }"
    )

    # 12. Section title color update (was navy/dark purple, now clean dark)
    html = html.replace(
        ".section-title { font-family: var(--font-heading); font-size: clamp(1.8rem, 4vw, 3rem); color: var(--navy); line-height: 1.1; margin-bottom: 2rem; }",
        ".section-title { font-family: var(--font-heading); font-size: clamp(1.8rem, 4vw, 3rem); color: #0A0A0F; line-height: 1.1; margin-bottom: 2rem; }"
    )

    return html


for fname in FILES:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = transform(content, fname)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changed = content != new_content
        print(f"{'OK' if changed else '=='} {fname}")
    except FileNotFoundError:
        print(f"MISSING {fname}")

print("Done.")
