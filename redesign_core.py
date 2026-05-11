#!/usr/bin/env python3
"""
Redesign core pages: Syne+lime dark → Space Grotesk+blue light.
Usage: python redesign_core.py about.html contact.html
       python redesign_core.py about.html contact.html pricing.html services.html
"""
import sys

FILES = sys.argv[1:] if len(sys.argv) > 1 else ['about.html', 'contact.html']

def transform(html):

    # ── 1. FONT: Syne → Space Grotesk ────────────────────────────────────────
    html = html.replace(
        'Syne:wght@700;800&family=Inter',
        'Space+Grotesk:wght@400;500;600;700&family=Inter'
    )
    html = html.replace(
        "Syne:wght@700;800&amp;family=Inter",
        "Space+Grotesk:wght@400;500;600;700&amp;family=Inter"
    )
    html = html.replace("'Syne', sans-serif", "'Space Grotesk', sans-serif")
    html = html.replace('"Syne", sans-serif', '"Space Grotesk", sans-serif')

    # ── 2. CSS VARIABLES ─────────────────────────────────────────────────────
    html = html.replace("--primary: #4ADE80",   "--primary: #0070F3")
    html = html.replace("--navy: #0a0a0a",       "--navy: #0A0A0F")
    html = html.replace("--bg: #0a0a0a",         "--bg: #FFFFFF")
    html = html.replace("--accent: #1a1a1a",     "--accent: #EEF4FF")
    html = html.replace("--gray-mid: #a3a3a3",   "--gray-mid: #9CA3AF")
    html = html.replace("--text: #ffffff",       "--text: #374151")
    html = html.replace("--text: #fff",          "--text: #374151")

    # ── 3. LIME → BLUE ───────────────────────────────────────────────────────
    html = html.replace("#4ADE80",               "#0070F3")
    html = html.replace("rgba(74,222,128,",      "rgba(0,112,243,")
    html = html.replace("rgba(74, 222, 128,",    "rgba(0, 112, 243,")

    # ── 4. BODY ───────────────────────────────────────────────────────────────
    html = html.replace(
        "body { font-family: var(--font-body); background: #0a0a0a; color: #fff; overflow-x: hidden; }",
        "body { font-family: var(--font-body); background: #fff; color: #374151; overflow-x: hidden; }"
    )

    # ── 5. NAV: dark → white sticky ──────────────────────────────────────────
    # Nav container
    html = html.replace(
        "background: rgba(10,10,10,0.95); backdrop-filter: blur(8px); border-bottom: 1px solid #1e1e1e;",
        "background: rgba(255,255,255,0.97); -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,112,243,0.1);"
    )
    # Nav scrolled
    html = html.replace(
        ".navbar.scrolled { background: rgba(10,10,10,0.95); backdrop-filter: blur(8px); box-shadow: 0 2px 16px rgba(0,0,0,0.4); }",
        ".navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }"
    )
    # Nav: replace old flex on .navbar → add .nav-inner, rename BEM classes
    html = html.replace(
        ".navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500; display: flex; align-items: center; justify-content: space-between; padding: 1rem 3rem;",
        ".navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 500;"
    )
    # Insert nav-inner after the navbar block ends
    html = html.replace(
        "transition: background var(--transition), padding var(--transition), box-shadow var(--transition); }\n    .navbar.scrolled {",
        "transition: background var(--transition), box-shadow var(--transition); }\n    .nav-inner { height: 64px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; }\n    .navbar.scrolled {"
    )
    # CSS class renames: BEM → flat (match the HTML classes)
    html = html.replace(".navbar__logo {", ".nav-logo {")
    html = html.replace(".navbar__logo span {", ".nav-logo span {")
    html = html.replace(".navbar__links {", ".nav-links {")
    html = html.replace(".navbar__links a {", ".nav-links a {")
    html = html.replace(".navbar__links a::", ".nav-links a::")
    html = html.replace(".navbar__cta {", ".nav-cta {")
    html = html.replace(".navbar__cta:hover {", ".nav-cta:hover {")
    # Nav logo: lime → dark
    html = html.replace(
        ".nav-logo { font-family: var(--font-heading); font-size: 1.5rem; color: var(--primary); letter-spacing: -0.03em; }",
        ".nav-logo { font-family: var(--font-heading); font-size: 1.5rem; color: #0A0A0F; letter-spacing: -0.03em; }"
    )
    # Nav links: muted gray → dark
    html = html.replace(
        ".nav-links a { font-size: 0.875rem; font-weight: 500; color: #a3a3a3; position: relative; padding-bottom: 2px; }",
        ".nav-links a { font-size: 0.875rem; font-weight: 500; color: #374151; position: relative; padding-bottom: 2px; }"
    )
    # Nav CTA: dark pill → blue button
    html = html.replace(
        ".nav-cta { font-size: 0.8rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--bg); background: #0a0a0a; padding: 0.65rem 1.4rem; border-radius: 2px; transition: background var(--transition); }",
        ".nav-cta { font-size: 0.85rem; font-weight: 700; color: #fff !important; background: #0070F3 !important; padding: 10px 22px !important; border-radius: 8px; display: inline-flex !important; align-items: center; justify-content: center; line-height: 1; transition: background var(--transition), transform var(--transition); }"
    )
    html = html.replace(
        ".nav-cta:hover { background: var(--primary); }",
        ".nav-cta:hover { background: #0052CC !important; transform: translateY(-1px); }"
    )
    # Responsive: rename classes in media queries too
    html = html.replace(".navbar__links { display: none; }", ".nav-links { display: none; }")
    html = html.replace(".navbar__links { display: flex; }", ".nav-links { display: flex; }")
    # Inject hamburger + mobile-menu CSS after .navbar.scrolled if not already present
    MOBILE_CSS = (
        "\n    .nav-hamburger { display: none; background: none; border: none; padding: 0;"
        " flex-direction: column; gap: 5px; cursor: pointer; }"
        "\n    .nav-hamburger span { display: block; width: 24px; height: 2px;"
        " background: #374151; border-radius: 2px; }"
        "\n    .mobile-menu { display: none; position: absolute; top: 100%; left: 0; right: 0;"
        " background: #fff; box-shadow: 0 8px 24px rgba(0,0,0,0.1); padding: 1.5rem;"
        " flex-direction: column; gap: 0.5rem; border-bottom: 1px solid rgba(0,112,243,0.1); }"
        "\n    .mobile-menu.open { display: flex; }"
        "\n    .mobile-menu a { font-size: 0.9rem; font-weight: 500; color: #374151;"
        " padding: 0.65rem 0; border-bottom: 1px solid rgba(0,0,0,0.06);"
        " transition: color 0.3s; }"
        "\n    .mobile-menu a:last-child { color: #fff !important; background: #0070F3;"
        " border: none; padding: 10px 22px; border-radius: 8px; text-align: center;"
        " font-weight: 700; margin-top: 0.5rem; display: flex; justify-content: center; }"
    )
    ANCHOR = ".navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }"
    if ANCHOR in html and ".mobile-menu { display: none;" not in html:
        html = html.replace(ANCHOR, ANCHOR + MOBILE_CSS)
    # Hamburger spans: dark → gray
    html = html.replace(
        "background: #0a0a0a; border-radius: 2px; transition: background var(--transition); }",
        "background: #374151; border-radius: 2px; transition: background var(--transition); }"
    )
    # Mobile menu: dark → white
    html = html.replace(
        "background: #111; box-shadow: 0 8px 24px rgba(255,255,255,0.1);",
        "background: #fff; box-shadow: 0 8px 24px rgba(0,0,0,0.1);"
    )
    html = html.replace(
        "color: #fff; padding: 0.5rem 0; border-bottom: 1px solid rgba(17,24,39,0.06); }",
        "color: #374151; padding: 0.65rem 0; border-bottom: 1px solid rgba(0,0,0,0.06); }"
    )
    html = html.replace(
        ".mobile-menu a:last-child { color: var(--primary); border-bottom: none; }",
        ".mobile-menu a:last-child { color: #fff !important; background: #0070F3; border: none; padding: 10px 22px; border-radius: 8px; text-align: center; font-weight: 700; margin-top: 0.5rem; }"
    )

    # ── 6. SECTIONS ───────────────────────────────────────────────────────────
    html = html.replace(".section--accent { background: #1a1a1a; }", ".section--accent { background: #F7F9FC; }")
    html = html.replace("section--accent { background: #1a1a1a; }",  "section--accent { background: #F7F9FC; }")
    # Section title: white → dark
    html = html.replace(
        "; color: #fff; line-height: 1.1; margin-bottom: 2rem; }",
        "; color: #0A0A0F; line-height: 1.1; margin-bottom: 2rem; }"
    )

    # ── 7. CARD BORDERS: dark → light ────────────────────────────────────────
    html = html.replace("border: 1px solid #222;",         "border: 1px solid rgba(0,0,0,0.08);")
    html = html.replace("border-bottom: 1px solid #222;",  "border-bottom: 1px solid rgba(0,0,0,0.08);")
    html = html.replace("border-top: 1px solid #222;",     "border-top: 1px solid rgba(0,0,0,0.08);")
    html = html.replace("border-left: 1px solid #222;",    "border-left: 1px solid rgba(0,0,0,0.08);")

    # ── 8. DARK CARD BACKGROUNDS → LIGHT ─────────────────────────────────────
    html = html.replace("background: #111;",   "background: #fff;")
    html = html.replace("background: #1a1a1a;","background: #F7F9FC;")

    # ── 9. TEXT COLORS: white → dark (content sections) ──────────────────────
    html = html.replace("color: rgba(255,255,255,0.65);", "color: #374151;")
    html = html.replace("color: rgba(255,255,255,0.55);", "color: #6B7280;")
    html = html.replace("color: rgba(255,255,255,0.6);",  "color: #374151;")
    html = html.replace("color: rgba(255,255,255,0.7);",  "color: #374151;")
    html = html.replace("color: rgba(255,255,255,0.45);", "color: #9CA3AF;")
    html = html.replace("color: rgba(255,255,255,0.4);",  "color: #9CA3AF;")
    html = html.replace("color: rgba(255,255,255,0.3);",  "color: #9CA3AF;")
    html = html.replace("color: rgba(255,255,255,0.25);", "color: #D1D5DB;")
    html = html.replace("color: rgba(255,255,255,0.2);",  "color: #D1D5DB;")
    html = html.replace("color: rgba(17,24,39,0.45);",    "color: #9CA3AF;")
    # Strong text in paragraphs
    html = html.replace("p strong { color: #fff; }",      "p strong { color: #0A0A0F; }")

    # ── 10. CARD TITLES: white → dark ────────────────────────────────────────
    # Catch common title patterns that should be dark on white card
    for tag in ['.team-card__name', '.value-item__title', '.pillar__title',
                '.service-card__title', '.testi-card__name', '.stat-card__num']:
        old = f"{tag} " + "{ font-family: var(--font-heading);"
        if old in html:
            # Find and replace color:#fff in that declaration
            import re
            html = re.sub(
                re.escape(old) + r'([^}]*?)color: #fff;',
                old + r'\1color: #0A0A0F;',
                html, count=1
            )

    # ── 11. STAT CARD NUM: white → primary ───────────────────────────────────
    html = html.replace(
        ".stat-card__num { font-family: var(--font-heading); font-size: 2.8rem; color: #fff;",
        ".stat-card__num { font-family: var(--font-heading); font-size: 2.8rem; color: var(--primary);"
    )
    html = html.replace(
        ".stat-card__num { font-family: var(--font-heading); font-size: 3rem; color: #fff;",
        ".stat-card__num { font-family: var(--font-heading); font-size: 3rem; color: var(--primary);"
    )

    # ── 12. BTN-PRIMARY: lime → blue style ───────────────────────────────────
    html = html.replace(
        "border-radius: 2rem; position: relative; overflow: hidden; transition: transform 0.2s ease; } .btn-primary span { color: #0a0a0a !important; }",
        "border-radius: 8px; box-shadow: 0 8px 32px rgba(0,112,243,0.4); position: relative; overflow: hidden; transition: transform 0.2s ease, box-shadow 0.2s ease; } .btn-primary span { color: #fff !important; }"
    )
    html = html.replace(
        ".btn-primary::before { content: ''; position: absolute; inset: 0; background: #0a0a0a;",
        ".btn-primary::before { content: ''; position: absolute; inset: 0; background: #0052CC;"
    )

    # ── 13. CTA BAND GLOW ────────────────────────────────────────────────────
    # rgba already handled in step 3; keep dark bg for cta-band (looks fine)

    # ── 14. FOOTER: replace simple old-style footer CSS with full column footer ─
    FOOTER_FULL = (
        ".footer { background: #060606; }\n"
        "    .footer-inner { max-width: var(--max-w); margin: 0 auto; }\n"
        "    .footer-top { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; padding: 4rem 3rem 3rem; border-bottom: 1px solid #1e1e1e; }\n"
        "    .footer-brand {}\n"
        "    .footer-logo { font-family: var(--font-heading); font-size: 1.6rem; color: #fff; display: inline-block; margin-bottom: 1rem; }\n"
        "    .footer-logo span { color: var(--primary); }\n"
        "    .footer-tagline { font-size: 0.85rem; color: rgba(255,255,255,0.4); line-height: 1.7; max-width: 280px; margin-bottom: 1.5rem; }\n"
        "    .footer-socials { display: flex; gap: 0.75rem; }\n"
        "    .footer-col h4 { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(255,255,255,0.55); margin-bottom: 1.25rem; }\n"
        "    .footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 0.65rem; }\n"
        "    .footer-col ul a { font-size: 0.82rem; color: rgba(255,255,255,0.3); transition: color var(--transition); }\n"
        "    .footer-col ul a:hover { color: var(--primary); }\n"
        "    .footer-contact-item { margin-top: 0.65rem; }\n"
        "    .footer-contact-item a { font-size: 0.82rem; color: rgba(255,255,255,0.3); transition: color var(--transition); }\n"
        "    .footer-contact-item a:hover { color: var(--primary); }\n"
        "    .footer-bottom { display: flex; align-items: center; justify-content: space-between; padding: 1.5rem 3rem; flex-wrap: wrap; gap: 1rem; }\n"
        "    .footer-copy { font-size: 0.75rem; color: rgba(255,255,255,0.2); letter-spacing: 0.05em; }\n"
        "    .footer-bl { display: flex; gap: 1.5rem; }\n"
        "    .footer-bl a { font-size: 0.75rem; color: rgba(255,255,255,0.25); transition: color var(--transition); }\n"
        "    .footer-bl a:hover { color: var(--primary); }"
    )
    OLD_FOOTER = (
        ".footer { background: #0a0a0a; padding: 2.5rem 3rem; display: flex; align-items: center;"
        " justify-content: space-between; flex-wrap: wrap; gap: 1rem; }\n"
        "    .footer__logo { font-family: var(--font-heading); font-size: 1.2rem; color: #374151; }\n"
        "    .footer__logo span { color: var(--primary); }\n"
        "    .footer__copy { font-size: 0.75rem; color: #D1D5DB; letter-spacing: 0.05em; }\n"
        "    .footer__links { display: flex; gap: 1.5rem; list-style: none; }\n"
        "    .footer__links a { font-size: 0.75rem; color: rgba(255,255,255,0.35); letter-spacing: 0.08em; transition: color 0.2s; }\n"
        "    .footer__links a:hover { color: var(--primary); }"
    )
    if OLD_FOOTER in html:
        html = html.replace(OLD_FOOTER, FOOTER_FULL)
    # Nav logo: white on white → dark
    html = html.replace(
        ".nav-logo { font-family: var(--font-heading); font-size: 1.5rem; color: #fff; }",
        ".nav-logo { font-family: var(--font-heading); font-size: 1.5rem; color: #0A0A0F; letter-spacing: -0.03em; }"
    )
    # Media query footer → grid
    html = html.replace(
        ".footer { padding: 2rem 1.5rem; flex-direction: column; text-align: center; }",
        ".footer-top { grid-template-columns: 1fr; gap: 2rem; padding: 2.5rem 1.5rem 2rem; } .footer-bottom { padding: 1.25rem 1.5rem; flex-direction: column; text-align: center; }"
    )

    return html


for fname in FILES:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            original = f.read()
        updated = transform(original)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        diffs = sum(1 for a, b in zip(original.splitlines(), updated.splitlines()) if a != b)
        print(f"{'OK' if diffs else '=='} {fname} ({diffs} lines changed)")
    except FileNotFoundError:
        print(f"MISSING {fname}")

print("Done.")
