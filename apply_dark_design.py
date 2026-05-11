#!/usr/bin/env python3
"""
Apply the industries dark design system to core pages:
  Dark bg (#0a0a0a) + Syne font + lime green (#d4ff00)
  — matches industries/accounting.html style.
"""
import re

FILES = ['index.html', 'about.html', 'pricing.html', 'contact.html', 'services.html']

def transform(html):
    # ── 1. FONT: Space Grotesk → Syne ──────────────────────────────────────
    html = html.replace(
        'Space+Grotesk:wght@400;500;600;700&family=Inter',
        'Syne:wght@700;800&family=Inter'
    )
    html = html.replace(
        "Space+Grotesk:wght@400;500;600;700&amp;family=Inter",
        "Syne:wght@700;800&amp;family=Inter"
    )
    html = html.replace("'Space Grotesk', sans-serif", "'Syne', sans-serif")
    html = html.replace('"Space Grotesk", sans-serif', '"Syne", sans-serif')

    # ── 2. CSS VARIABLES ───────────────────────────────────────────────────
    html = html.replace("--primary: #0070F3",   "--primary: #d4ff00")
    html = html.replace("--bg: #FFFFFF",         "--bg: #0a0a0a")
    html = html.replace("--bg: #ffffff",         "--bg: #0a0a0a")
    html = html.replace("--text: #374151",       "--text: #ffffff")
    html = html.replace("--accent: #EEF4FF",     "--accent: #1a1a1a")
    html = html.replace("--accent: #eef4ff",     "--accent: #1a1a1a")
    html = html.replace("--gray-mid: #9CA3AF",   "--gray-mid: #a3a3a3")
    html = html.replace("--gray-light: #F7F9FC", "--gray-light: #111111")
    html = html.replace("--gray-light: #f7f9fc", "--gray-light: #111111")
    html = html.replace("--navy: #0A0A0F",       "--navy: #0a0a0a")

    # ── 3. INLINE HEX ─────────────────────────────────────────────────────
    html = html.replace("#0070F3", "#d4ff00")
    html = html.replace("#0052CC", "#b8e000")  # primary-dark
    html = html.replace("#050810", "#0a0a0a")  # old footer dark

    # ── 4. RGBA BLUE → LIME ────────────────────────────────────────────────
    html = html.replace("rgba(0,112,243,",    "rgba(212,255,0,")
    html = html.replace("rgba(0, 112, 243,",  "rgba(212, 255, 0,")

    # ── 5. RGBA DARK TEXT → LIGHT (17,24,39 was navy text on white bg)
    #    On dark bg these become near-invisible — invert to white-based
    html = html.replace("rgba(17,24,39,0.08)",  "rgba(255,255,255,0.07)")
    html = html.replace("rgba(17,24,39,0.1)",   "rgba(255,255,255,0.08)")
    html = html.replace("rgba(17,24,39,0.12)",  "rgba(255,255,255,0.1)")
    html = html.replace("rgba(17,24,39,0.25)",  "rgba(212,255,0,0.25)")
    html = html.replace("rgba(17,24,39,0.3)",   "rgba(255,255,255,0.3)")
    html = html.replace("rgba(17,24,39,0.4)",   "rgba(255,255,255,0.4)")
    html = html.replace("rgba(17,24,39,0.55)",  "rgba(255,255,255,0.5)")
    html = html.replace("rgba(17,24,39,0.6)",   "rgba(255,255,255,0.55)")
    html = html.replace("rgba(17,24,39,0.65)",  "rgba(255,255,255,0.6)")
    html = html.replace("rgba(17,24,39,0.7)",   "rgba(255,255,255,0.65)")
    html = html.replace("rgba(17,24,39,0.75)",  "rgba(255,255,255,0.7)")
    html = html.replace("rgba(17,24,39,0.8)",   "rgba(255,255,255,0.75)")
    # spaced versions
    html = html.replace("rgba(17, 24, 39, 0.08)", "rgba(255,255,255,0.07)")
    html = html.replace("rgba(17, 24, 39, 0.6)",  "rgba(255,255,255,0.55)")
    html = html.replace("rgba(17, 24, 39, 0.7)",  "rgba(255,255,255,0.65)")

    # ── 6. WHITE BACKGROUNDS → DARK ────────────────────────────────────────
    # body
    html = re.sub(r'body\s*\{([^}]*?)\}',
                  lambda m: m.group(0).replace('background: var(--bg);', 'background: #0a0a0a;')
                                      .replace('color: var(--text);', 'color: #fff;'),
                  html)
    # sections with explicit white
    html = html.replace("background: #fff;",      "background: #111;")
    html = html.replace("background: #ffffff;",   "background: #111;")
    html = html.replace("background: #FFFFFF;",   "background: #111;")
    html = html.replace("background: var(--bg);", "background: #0a0a0a;")
    # Accent section (light blue) → dark surface
    html = html.replace("background: var(--accent);", "background: #1a1a1a;")

    # ── 7. NAV: white → dark ───────────────────────────────────────────────
    html = html.replace(
        "background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,112,243,0.08)",
        "background: rgba(10,10,10,0.95); backdrop-filter: blur(8px); border-bottom: 1px solid #1e1e1e"
    )
    html = html.replace(
        "background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(212,255,0,0.08)",
        "background: rgba(10,10,10,0.95); backdrop-filter: blur(8px); border-bottom: 1px solid #1e1e1e"
    )
    # Nav scrolled state
    html = html.replace(
        ".navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(0,112,243,0.08); }",
        ".navbar.scrolled { background: rgba(10,10,10,0.95); backdrop-filter: blur(8px); box-shadow: 0 2px 16px rgba(0,0,0,0.4); }"
    )
    html = html.replace(
        ".navbar.scrolled { background: rgba(255,255,255,0.97); box-shadow: 0 2px 20px rgba(212,255,0,0.08); }",
        ".navbar.scrolled { background: rgba(10,10,10,0.95); backdrop-filter: blur(8px); box-shadow: 0 2px 16px rgba(0,0,0,0.4); }"
    )
    # Nav logo color: dark → lime
    html = html.replace(
        "color: var(--dark, #0A0A0F);",
        "color: var(--primary);"
    )
    html = html.replace(
        "color: var(--dark, #0a0a0f);",
        "color: var(--primary);"
    )
    # Nav link colors
    html = html.replace("color: #374151;", "color: #a3a3a3;")
    # Nav CTA button: blue → lime
    html = html.replace(
        "background: var(--primary) !important; color: #fff !important;",
        "background: var(--primary) !important; color: #0a0a0a !important;"
    )
    html = html.replace(
        "background: var(--primary-dark) !important;",
        "background: #b8e000 !important;"
    )

    # ── 8. HERO gradient adjust for dark style ─────────────────────────────
    # The hero already has dark bg from --navy, just make it pure black
    html = html.replace(
        "background: var(--navy);",
        "background: #0a0a0a;"
    )
    html = html.replace(
        "background: var(--navy)",
        "background: #0a0a0a"
    )

    # ── 9. CARDS: light → dark surfaces ────────────────────────────────────
    html = html.replace("background: var(--bg);",      "background: #111;")
    # stat cards, testi cards borders
    html = html.replace(
        "border: 1px solid rgba(255,255,255,0.07);",
        "border: 1px solid #222;"
    )
    html = html.replace(
        "border: 1px solid rgba(255,255,255,0.08);",
        "border: 1px solid #222;"
    )
    # Card text color adjustments (was dark on white, now needs to be light)
    html = html.replace("color: var(--text-heading);",  "color: #fff;")
    html = html.replace("color: var(--text-muted);",    "color: #a3a3a3;")
    html = html.replace('--text-heading: #0A0A0F',      '--text-heading: #ffffff')
    html = html.replace('--text-heading: #0a0a0f',      '--text-heading: #ffffff')
    html = html.replace('--text: #374151',               '--text: #ffffff')

    # ── 10. PRIMARY BUTTON text: was white, now needs to be dark ──────────
    # lime on dark bg button: text should be #0a0a0a not white
    html = html.replace(
        "background: var(--primary); padding: 1rem 2rem; border-radius: 2px; position: relative; overflow: hidden; transition: transform 0.2s ease; }",
        "background: var(--primary); padding: 1rem 2rem; border-radius: 2rem; position: relative; overflow: hidden; transition: transform 0.2s ease; } .btn-primary span { color: #0a0a0a !important; }"
    )
    html = html.replace(
        ".nav-cta { background: var(--primary) !important; color: #fff !important;",
        ".nav-cta { background: var(--primary) !important; color: #0a0a0a !important;"
    )

    # ── 11. FOOTER dark bg ─────────────────────────────────────────────────
    html = html.replace(".footer { background: #0a0a0a; }", ".footer { background: #060606; }")

    # ── 12. SECTION-TITLE: dark → light ────────────────────────────────────
    html = html.replace("color: #0A0A0F;", "color: #fff;")
    html = html.replace("color: #0a0a0a;", "color: #fff;")

    # ── 13. BORDER colors for sections ─────────────────────────────────────
    html = html.replace(
        "border: 1px solid rgba(255,255,255,0.07); border-top: 3px solid var(--primary);",
        "border: 1px solid #222; border-top: 3px solid var(--primary);"
    )
    html = html.replace(
        "border-top: 1px solid rgba(255,255,255,0.07);",
        "border-top: 1px solid #222;"
    )
    html = html.replace(
        "border-bottom: 1px solid rgba(255,255,255,0.07);",
        "border-bottom: 1px solid #222;"
    )
    html = html.replace(
        "border-bottom: 1px solid rgba(255,255,255,0.06);",
        "border-bottom: 1px solid #1e1e1e;"
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
