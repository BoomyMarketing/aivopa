#!/usr/bin/env python3
"""Generate ~180 SEO pages for Vora (aivopa.com) from scale_list_vora_2-5.txt"""

import os
import re
from pathlib import Path

BASE_DIR = Path("C:/Boomy Marketing/vora")
KW_DIR = Path("C:/Boomy Marketing/keyword-research")

# ── Read all source files ──────────────────────────────────────────────────
def read_pages(path):
    pages = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # strip leading number+tab
            line = re.sub(r"^\d+\t", "", line)
            parts = line.split("|")
            if len(parts) < 3:
                continue
            content_type = parts[0].strip()
            url = parts[1].strip()
            keyword = parts[2].strip()
            pillar_url = parts[3].strip() if len(parts) > 3 else ""
            # map "supporting" → "guides"
            if content_type == "supporting":
                content_type = "guides"
            pages.append((content_type, url, keyword, pillar_url))
    return pages

all_pages = []
for fname in ["scale_list_vora_2.txt", "scale_list_vora_3.txt",
              "scale_list_vora_4.txt", "scale_list_vora_5.txt"]:
    all_pages.extend(read_pages(KW_DIR / fname))

print(f"Total source entries: {len(all_pages)}")

# ── HTML Template ──────────────────────────────────────────────────────────
CSS_VARS = """
  --primary: #0070F3;
  --bg: #FFFFFF;
  --bg-surface: #F8F9FC;
  --dark: #0A0A0F;
  --text-heading: #13023E;
  --text: #1F2937;
  --text-muted: #6B7280;
  --secondary: #7928CA;
  --radius: 8px;
  --font-heading: 'Space Grotesk', sans-serif;
  --font-body: 'Inter', sans-serif;
"""

def title_case(s):
    stop = {"a","an","the","and","but","or","for","nor","on","at","to","by","in","of","with"}
    words = s.split()
    result = []
    for i, w in enumerate(words):
        result.append(w.capitalize() if (i == 0 or w.lower() not in stop) else w.lower())
    return " ".join(result)

def slug_to_label(slug):
    return title_case(slug.replace("-", " "))

# Content library – unique paragraphs keyed by theme
PERF_INTROS = [
    ("roas", "Every dollar you spend on paid advertising should return measurable revenue. At Vora, we engineer campaigns around one north star: ROAS. Our ex-Facebook Ads team, led by Jordan Blake, has managed over $50M in ad spend and knows exactly which levers move the needle — bidding logic, audience segmentation, creative fatigue cycles, and post-click conversion architecture."),
    ("cac", "Customer Acquisition Cost is the single metric that determines whether a business scales or stalls. Vora builds performance systems that systematically compress CAC while expanding LTV ratios. We don't run ads — we run revenue engines. Every campaign we touch comes with a full CAC/LTV dashboard so you always know the unit economics in real time."),
    ("ltv", "Lifetime Value optimization is where the real profit hides. While most agencies obsess over clicks and impressions, Vora maps the full customer journey: acquisition cost, first-purchase margin, retention rate, and 12-month LTV. We then back-engineer the media mix that funds growth sustainably. Google Premier Partner status means we get priority betas before your competitors do."),
    ("conversions", "Conversion rate is the multiplier on every ad dollar. A 2× CRO improvement effectively halves your CAC overnight. Vora couples paid media management with conversion architecture — landing page audits, A/B test pipelines, and offer framing — so the traffic we buy actually turns into revenue. That's the performance difference."),
    ("revenue", "Revenue attribution is broken at most companies. Teams celebrate clicks, ignore returns, and can't answer 'which channel actually drove profit?' Vora installs multi-touch attribution from day one, giving you a single source of truth across Google Ads, Meta, YouTube, and programmatic — so every budget decision is data-driven, not gut-driven."),
]

STAT_BLOCKS = [
    "According to <a href='https://www.wordstream.com/google-ads' rel='nofollow noopener' target='_blank'>WordStream</a>, the average Google Ads conversion rate across industries is 3.75% — but top-quartile advertisers hit 11.45%. The difference is systematic optimization, not luck.",
    "HubSpot research shows that companies with documented ROI tracking for paid media are 2.8× more likely to increase their ad budgets confidently year-over-year. Source: <a href='https://www.hubspot.com/marketing-statistics' rel='nofollow noopener' target='_blank'>HubSpot Marketing Statistics</a>.",
    "Global digital advertising spend exceeded $600 billion in 2023 according to <a href='https://www.statista.com/topics/1745/digital-advertising/' rel='nofollow noopener' target='_blank'>Statista</a>. Yet 62% of marketers can't accurately attribute revenue to specific channels — a gap Vora closes with our attribution stack.",
    "WordStream data shows the average cost-per-click on Google Search is $2.69 across all industries, but eCommerce, legal, and SaaS verticals regularly exceed $5–$15 CPC. Knowing your industry benchmark is table stakes for competitive bidding. <a href='https://www.wordstream.com/blog/ws/2015/05/21/how-much-does-adwords-cost' rel='nofollow noopener' target='_blank'>See full benchmarks</a>.",
    "Email-driven paid audiences (customer match) deliver 2–5× higher ROAS than cold prospecting alone, per HubSpot's <a href='https://www.hubspot.com/marketing-statistics' rel='nofollow noopener' target='_blank'>State of Marketing 2024</a>. Vora integrates your CRM data directly into every campaign's audience architecture.",
]

def pick(lst, idx):
    return lst[idx % len(lst)]

def make_faq(keyword, idx):
    keyword_tc = title_case(keyword)
    faqs = [
        [
            (f"How does Vora measure {keyword_tc} performance?",
             f"We build a custom ROAS dashboard for every client that tracks {keyword} metrics in real time — impressions, clicks, conversions, revenue, CAC, and 30/60/90-day LTV. You always know exactly what your ad spend is returning."),
            (f"What budget do I need to start {keyword_tc}?",
             f"Most clients see meaningful results starting at $5,000/month in ad spend. For {keyword}, optimal performance typically requires enough data volume (300+ conversions/month) for algorithmic bidding to function correctly. We help you right-size from day one."),
            (f"How long before I see ROI from {keyword_tc}?",
             f"Expect the first 30 days to be a data-gathering phase. By day 60, our optimization cycles typically push ROAS above breakeven. Full performance maturity — where we're outperforming industry benchmarks — usually happens at the 90-day mark."),
            (f"Does Vora handle creative for {keyword_tc} campaigns?",
             f"Yes. Our performance creative team produces ad copy, static visuals, and video scripts optimized for conversion, not just aesthetics. Every creative asset is tested in a structured A/B framework tied directly to your {keyword} KPIs."),
            (f"Is Vora a Google Premier Partner?",
             f"Yes. Google Premier Partner status gives Vora clients access to beta features, dedicated Google support, and advanced audience signals unavailable to standard partners — a competitive edge in {keyword} and all paid search campaigns."),
        ],
        [
            (f"What makes Vora different for {keyword_tc}?",
             f"Most agencies report vanity metrics. Vora reports revenue. Our entire {keyword} practice is built around CAC/LTV economics — we won't scale spend until unit economics are proven, which protects your margin as you grow."),
            (f"Can Vora take over existing {keyword_tc} campaigns?",
             f"Absolutely. Our onboarding process includes a full account audit — quality scores, bid strategies, audience segmentation, negative keyword gaps, and attribution setup. Most inherited accounts show 20-40% efficiency gains within the first 60 days."),
            (f"How do you track conversions for {keyword_tc}?",
             f"We implement enhanced conversion tracking via Google Tag Manager, server-side tagging for iOS privacy, and multi-touch attribution modeling. Every {keyword} conversion is tied to a specific ad, audience segment, and creative variant."),
            (f"What reporting cadence does Vora use?",
             f"Weekly performance snapshots, monthly deep-dive strategy reviews, and a live dashboard you can check 24/7. For {keyword} campaigns, we add channel-specific ROAS breakdowns and cohort LTV analysis quarterly."),
            (f"Do you offer performance guarantees?",
             f"We guarantee full transparency and measurable progress — not magic numbers. Every {keyword} engagement starts with a 90-day performance roadmap with clear KPIs, and we hold ourselves accountable to those targets in every monthly review."),
        ],
    ]
    chosen = faqs[idx % 2]
    return chosen[:5]

def make_h2_sections(keyword, content_type, idx):
    kw_tc = title_case(keyword)
    if content_type == "guides":
        sections = [
            (f"What Is {kw_tc} and Why Does It Matter for ROI?",
             f"Understanding {keyword} starts with connecting it to revenue impact. Whether you're a startup trying to scale paid acquisition or an enterprise managing eight-figure ad budgets, the principles remain the same: every tactic must be evaluated through a CAC/LTV lens. At Vora, we've seen campaigns that looked great on CTR metrics but destroyed margin — and campaigns that looked 'expensive' on CPCs but delivered 8× ROAS. The difference is always attribution clarity."),
            (f"The Performance Marketing Approach to {kw_tc}",
             f"Traditional marketing treats {keyword} as a brand exercise. Performance marketing treats it as a revenue lever. Vora's methodology: (1) establish baseline conversion economics, (2) identify the highest-leverage audience segments, (3) deploy structured creative testing, (4) optimize bidding algorithms with clean signal data, and (5) reinvest into the combinations that compound returns. This loop runs every 7 days."),
            (f"Common {kw_tc} Mistakes That Kill ROAS",
             f"The most expensive {keyword} mistakes we see: broad match overkill burning budget on irrelevant queries, single landing pages with no personalization by audience segment, attribution models that overcount last-click, and creative burnout from running the same assets for 90+ days. Each of these can reduce ROAS by 30-60%. Vora's audit process catches all of them within the first two weeks."),
            (f"How to Measure {kw_tc} Success",
             f"Measurement starts before the first dollar is spent. For {keyword}, we establish: primary conversion goals (purchases, leads, sign-ups), secondary micro-conversions (add-to-cart, scroll depth, video views), revenue attribution windows, and CAC targets by customer cohort. Without this foundation, optimization is guesswork. With it, every weekly review tells a clear story about what to scale and what to cut."),
            (f"Vora's {kw_tc} Process — From Audit to Scale",
             f"Week 1: Account audit and tracking verification. Week 2: Audience architecture rebuild and negative keyword expansion. Weeks 3–4: Creative A/B launch with performance baselines. Month 2: Algorithmic bidding optimization with clean conversion data. Month 3: Scale winners, cut losers, and expand to new audience segments. Most clients see meaningful ROAS improvement by the end of month 2 — and compounding returns through month 6 and beyond."),
        ]
    elif content_type == "comparison":
        sections = [
            (f"What to Look for in {kw_tc}",
             f"When evaluating {keyword}, the metrics that matter most are proven ROAS track records, transparent reporting, and attribution sophistication. Any agency or tool that can't show you actual revenue attribution (not just click reports) is operating in the dark. Vora's evaluation framework: Does it integrate with your CRM? Does it support multi-touch attribution? Does it optimize for revenue, not vanity metrics?"),
            (f"Performance Benchmarks for {kw_tc}",
             f"Industry benchmarks for {keyword} vary widely by vertical. eCommerce campaigns typically target 3–8× ROAS. Lead generation targets $20–$150 CPL depending on deal size. SaaS acquisition targets CAC that's ≤33% of 12-month LTV. Understanding where you sit relative to these benchmarks is the first step to knowing whether your current {keyword} approach is working."),
            (f"Why Most {kw_tc} Solutions Fall Short",
             f"The core failure mode for most {keyword} solutions: they optimize for platform metrics (Google's conversion count, Meta's cost-per-result) rather than business outcomes (revenue, margin, LTV). Platform algorithms are designed to spend your budget — not maximize your profit. Vora layers business logic on top of platform optimization to align ad spend with actual financial outcomes."),
            (f"The ROAS-First Framework for {kw_tc}",
             f"Vora's ROAS-first evaluation of {keyword}: Step 1 — can this solution be connected to revenue data, not just click data? Step 2 — does it support incrementality testing (would you have gotten these conversions anyway)? Step 3 — what's the CAC trend over 90 days, not just the first week? These three questions eliminate 80% of the noise in the {keyword} decision."),
            (f"How Vora Approaches {kw_tc} for Clients",
             f"For every {keyword} decision, Vora runs a structured analysis: current performance baseline, opportunity sizing, implementation cost, expected ROAS impact, and time-to-ROI estimate. We don't recommend anything we can't attach a revenue number to. This rigor — built over $50M+ in managed ad spend — is what separates performance-driven decisions from marketing speculation."),
        ]
    elif content_type == "industry":
        sections = [
            (f"Performance Marketing for {kw_tc}: The Revenue Opportunity",
             f"The {keyword} sector has unique CAC/LTV dynamics that most generalist agencies miss. Vora specializes in understanding the specific conversion cycles, sales processes, and customer lifetime values inherent to {keyword} — and building paid media strategies that optimize around those economics, not generic industry averages."),
            (f"Paid Advertising Strategy for {kw_tc}",
             f"Effective paid advertising in {keyword} requires platform-channel alignment. Google Search captures high-intent buyers. Meta/Instagram builds awareness and retargets middle-funnel prospects. YouTube drives brand trust at scale. For {keyword} specifically, the mix depends on average deal size, sales cycle length, and attribution window — Vora calibrates this in week one."),
            (f"CAC Benchmarks in {kw_tc}",
             f"Every {keyword} vertical has different CAC norms, and what looks expensive in one context is exceptional ROI in another. Vora benchmarks your current CAC against industry data from our client base ($50M+ managed spend across verticals) and sets targets that are ambitious but achievable based on real performance data."),
            (f"Lead Generation and Conversion in {kw_tc}",
             f"Lead quality is as important as lead volume in {keyword}. Vora implements lead scoring, CRM integration, and offline conversion tracking to ensure we're optimizing for leads that actually convert to revenue — not just form fills. This distinction alone typically improves qualified lead ROAS by 40–80% within 60 days."),
            (f"Scaling {kw_tc} Campaigns Without Burning Budget",
             f"The most dangerous phase for {keyword} campaigns is the scale phase — when performance looks strong and the instinct is to pour in budget. Vora uses controlled scaling: +20% budget increments, weekly ROAS monitoring, and audience expansion protocols that maintain efficiency as reach grows. This disciplined approach protects margin while capturing growth."),
        ]
    else:  # service
        sections = [
            (f"What Is {kw_tc}?",
             f"{kw_tc} is a core component of modern performance marketing. For businesses that want measurable ROI from every marketing dollar, {keyword} represents both an opportunity and a challenge: done right, it compounds returns; done wrong, it burns budget with nothing to show. Vora's team has spent years mastering the performance fundamentals that separate profitable {keyword} from expensive experimentation."),
            (f"How {kw_tc} Drives Revenue",
             f"The path from {keyword} to revenue runs through three checkpoints: audience quality (are we reaching buyers, not browsers?), creative relevance (does the message match where the buyer is in their journey?), and conversion architecture (does the landing experience convert traffic into customers?). Vora optimizes all three simultaneously, which is why our ROAS benchmarks consistently outperform industry averages."),
            (f"Common {kw_tc} Mistakes",
             f"The most common {keyword} pitfalls: over-reliance on last-click attribution, neglecting negative audience exclusions, creative fatigue ignored until CTR collapses, and landing pages disconnected from ad messaging. Each mistake has a measurable cost — Vora's account audits quantify exactly how much budget each issue is wasting so you can see the ROI of fixing it."),
            (f"Vora's Approach to {kw_tc}",
             f"Our {keyword} methodology starts with revenue math: what's your target CAC? What LTV does that CAC imply? What conversion rate do we need at the current traffic cost? This arithmetic tells us exactly what the campaign needs to achieve before we write a single ad. It's the difference between performance marketing and hopeful marketing."),
            (f"Measuring {kw_tc} Success",
             f"Success metrics for {keyword}: primary ROAS target (revenue ÷ ad spend), CAC trend (is cost-per-acquisition improving over time?), LTV:CAC ratio (are we acquiring customers worth more than they cost?), and conversion rate index (how does our rate compare to industry benchmarks?). Vora tracks all four and reviews them weekly so optimization never stalls."),
        ]
    return sections

def make_page(content_type, url, keyword, pillar_url, idx):
    kw_tc = title_case(keyword)
    slug = url.strip("/").split("/")[-1]
    page_title = f"{kw_tc} | Vora Performance Marketing Agency — New York"
    meta_desc = f"Vora's performance-first approach to {keyword}. Ex-Facebook Ads team, $50M+ managed spend, Google Premier Partner. Get your free ROAS audit."
    canonical = f"https://aivopa.com{url}"
    date = "2026-01-15" if idx % 2 == 0 else "2026-02-15"

    _, intro_para = pick(PERF_INTROS, idx)
    stat_block = pick(STAT_BLOCKS, idx + 1)
    h2_sections = make_h2_sections(keyword, content_type, idx)
    faqs = make_faq(keyword, idx)

    # Build H2 content HTML
    sections_html = ""
    for h2, body in h2_sections:
        sections_html += f"""
  <section class="content-section">
    <h2>{h2}</h2>
    <p>{body}</p>
  </section>
"""

    # Build FAQ HTML + schema
    faq_html = ""
    faq_schema_items = []
    for q, a in faqs:
        faq_html += f"""
    <div class="faq-item">
      <h3 class="faq-q">{q}</h3>
      <p class="faq-a">{a}</p>
    </div>
"""
        faq_schema_items.append(f"""    {{
      "@type": "Question",
      "name": "{q.replace('"', '&quot;')}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{a.replace('"', '&quot;')}"
      }}
    }}""")

    # Internal links
    internal_links = ["/google-ads-agency/", "/performance-marketing-agency/"]
    if pillar_url and pillar_url not in internal_links:
        internal_links.append(pillar_url)

    internal_links_html = " | ".join(
        f'<a href="{l}">{title_case(l.strip("/").replace("-"," "))}</a>'
        for l in internal_links
    )

    # Breadcrumb
    if content_type == "guides":
        breadcrumb_label = "Guides"
        breadcrumb_parent = "/guides/"
    elif content_type == "comparison":
        breadcrumb_label = "Best"
        breadcrumb_parent = "/best/"
    elif content_type == "industry":
        breadcrumb_label = "Industries"
        breadcrumb_parent = "/industries/"
    else:
        breadcrumb_label = "Services"
        breadcrumb_parent = "/services/"

    schema_json = f"""{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Vora Performance Marketing Agency",
  "url": "https://aivopa.com",
  "description": "{meta_desc.replace('"','&quot;')}",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "New York",
    "addressRegion": "NY",
    "addressCountry": "US"
  }},
  "telephone": "+1-212-555-0170",
  "areaServed": "US",
  "datePublished": "{date}"
}}"""

    faq_schema_json = f"""{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{chr(10).join(faq_schema_items)}
  ]
}}"""

    breadcrumb_schema_json = f"""{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type":"ListItem","position":1,"name":"Home","item":"https://aivopa.com/"}},
    {{"@type":"ListItem","position":2,"name":"{breadcrumb_label}","item":"https://aivopa.com{breadcrumb_parent}"}},
    {{"@type":"ListItem","position":3,"name":"{kw_tc}","item":"{canonical}"}}
  ]
}}"""

    html = f"""<!DOCTYPE html>
<html lang="en" class="site-vora">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="/assets/css/main.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{{CSS_VARS}}}
    body {{ font-family: var(--font-body); background: var(--bg); color: var(--text); margin: 0; }}
    h1,h2,h3 {{ font-family: var(--font-heading); color: var(--text-heading); }}
    .hero {{ background: var(--bg-surface); padding: 64px 24px 48px; text-align: center; border-bottom: 1px solid #E5E7EB; }}
    .hero h1 {{ font-size: clamp(1.8rem,4vw,2.8rem); margin-bottom: 16px; }}
    .hero p {{ font-size: 1.125rem; color: var(--text-muted); max-width: 700px; margin: 0 auto 28px; }}
    .btn-primary {{ background: var(--primary); color: #fff; padding: 14px 28px; border-radius: var(--radius); text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }}
    .btn-secondary {{ background: var(--secondary); color: #fff; padding: 14px 28px; border-radius: var(--radius); text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }}
    .container {{ max-width: 900px; margin: 0 auto; padding: 0 24px; }}
    .content-section {{ padding: 40px 0; border-bottom: 1px solid #E5E7EB; }}
    .content-section h2 {{ font-size: 1.5rem; margin-bottom: 16px; color: var(--text-heading); }}
    .faq-section {{ background: var(--bg-surface); padding: 48px 0; }}
    .faq-item {{ max-width: 900px; margin: 24px auto; padding: 0 24px; }}
    .faq-q {{ font-size: 1.1rem; color: var(--text-heading); margin-bottom: 8px; }}
    .faq-a {{ color: var(--text); line-height: 1.7; }}
    .stat-block {{ background: #EFF6FF; border-left: 4px solid var(--primary); padding: 20px 24px; border-radius: var(--radius); margin: 32px 0; font-size: 0.95rem; }}
    .author-box {{ background: var(--bg-surface); border: 1px solid #E5E7EB; border-radius: var(--radius); padding: 24px; margin: 40px 0; display: flex; gap: 20px; align-items: flex-start; }}
    .author-box .author-name {{ font-weight: 700; color: var(--text-heading); }}
    .author-box .author-bio {{ color: var(--text-muted); font-size: 0.9rem; margin-top: 4px; }}
    .internal-links {{ padding: 24px 0; font-size: 0.9rem; color: var(--text-muted); }}
    .internal-links a {{ color: var(--primary); text-decoration: none; margin: 0 4px; }}
    nav.breadcrumb {{ font-size: 0.85rem; color: var(--text-muted); padding: 12px 24px; max-width: 900px; margin: 0 auto; }}
    nav.breadcrumb a {{ color: var(--primary); text-decoration: none; }}
    .cta-box {{ background: linear-gradient(135deg,var(--primary),var(--secondary)); color: #fff; padding: 48px 24px; text-align: center; border-radius: var(--radius); margin: 40px 0; }}
    .cta-box h2 {{ color: #fff; margin-bottom: 12px; }}
    .cta-box p {{ margin-bottom: 24px; opacity: 0.9; }}
  </style>
  <script type="application/ld+json">{schema_json}</script>
  <script type="application/ld+json">{faq_schema_json}</script>
  <script type="application/ld+json">{breadcrumb_schema_json}</script>
</head>
<body>

<!-- NAV PLACEHOLDER -->
<nav aria-label="Main" style="background:#13023E;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;">
  <a href="/" style="color:#fff;font-family:var(--font-heading);font-weight:700;font-size:1.25rem;text-decoration:none;">VORA</a>
  <div style="display:flex;gap:20px;">
    <a href="/google-ads-agency/" style="color:#CBD5E1;font-size:0.9rem;text-decoration:none;">Google Ads</a>
    <a href="/performance-marketing-agency/" style="color:#CBD5E1;font-size:0.9rem;text-decoration:none;">Performance</a>
    <a href="/contact/" style="background:var(--primary);color:#fff;padding:8px 18px;border-radius:var(--radius);font-size:0.9rem;text-decoration:none;">Free ROAS Audit</a>
  </div>
</nav>

<nav class="breadcrumb" aria-label="Breadcrumb">
  <a href="/">Home</a> › <a href="{breadcrumb_parent}">{breadcrumb_label}</a> › {kw_tc}
</nav>

<div class="hero">
  <h1>{kw_tc}</h1>
  <p>{intro_para[:280]}…</p>
  <a href="/contact/" class="btn-primary">Get Your Free ROAS Audit</a>
  <a href="/roi-calculator/" class="btn-secondary">Calculate Your CAC</a>
</div>

<div class="container">

  <div class="author-box">
    <div>
      <div class="author-name">Jordan Blake — Performance Marketing Lead</div>
      <div class="author-bio">Ex-Facebook Ads team · $50M+ managed ad spend · Google Premier Partner · Based in New York</div>
    </div>
  </div>

  <div class="content-section">
    <p>{intro_para}</p>
    <div class="stat-block">{stat_block}</div>
  </div>

  {sections_html}

  <div class="cta-box">
    <h2>Ready to Maximize Your {kw_tc} ROI?</h2>
    <p>Vora's performance team will audit your current setup and show you exactly how much ROAS you're leaving on the table — in 48 hours, free.</p>
    <a href="/contact/" style="background:#fff;color:var(--primary);padding:14px 32px;border-radius:var(--radius);text-decoration:none;font-weight:700;display:inline-block;">Get Free ROAS Audit →</a>
  </div>

</div>

<section class="faq-section">
  <h2 style="text-align:center;font-family:var(--font-heading);color:var(--text-heading);margin-bottom:8px;">Frequently Asked Questions</h2>
  {faq_html}
</section>

<div class="container">
  <div class="internal-links">
    Related: {internal_links_html}
  </div>
</div>

<!-- FOOTER PLACEHOLDER -->
<footer style="background:#13023E;color:#94A3B8;padding:40px 24px;text-align:center;font-size:0.85rem;margin-top:48px;">
  <p style="color:#fff;font-family:var(--font-heading);font-weight:700;font-size:1rem;margin-bottom:8px;">VORA</p>
  <p>Performance Marketing Agency · New York, NY · Google Premier Partner</p>
  <p style="margin-top:16px;">
    <a href="/google-ads-agency/" style="color:#94A3B8;margin:0 12px;">Google Ads</a>
    <a href="/performance-marketing-agency/" style="color:#94A3B8;margin:0 12px;">Performance Marketing</a>
    <a href="/contact/" style="color:#94A3B8;margin:0 12px;">Contact</a>
    <a href="/privacy-policy/" style="color:#94A3B8;margin:0 12px;">Privacy</a>
  </p>
  <p style="margin-top:16px;">© 2026 Vora Performance Marketing Agency. All rights reserved.</p>
</footer>

</body>
</html>"""

    return html

# ── Determine output path ──────────────────────────────────────────────────
def get_output_path(content_type, url):
    slug_parts = url.strip("/").split("/")
    if content_type == "guides":
        # url like /guides/some-slug/
        slug = slug_parts[-1] if len(slug_parts) > 1 else slug_parts[0]
        return BASE_DIR / "guides" / slug / "index.html"
    elif content_type == "comparison":
        slug = slug_parts[-1] if len(slug_parts) > 1 else slug_parts[0]
        return BASE_DIR / "best" / slug / "index.html"
    elif content_type == "industry":
        slug = slug_parts[-1] if len(slug_parts) > 1 else slug_parts[0]
        return BASE_DIR / "industries" / slug / "index.html"
    else:  # service
        slug = slug_parts[-1] if len(slug_parts) > 0 else "service"
        return BASE_DIR / slug / "index.html"

# ── Generate all pages ─────────────────────────────────────────────────────
created = 0
skipped = 0
errors = []

for idx, (content_type, url, keyword, pillar_url) in enumerate(all_pages):
    try:
        out_path = get_output_path(content_type, url)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        html = make_page(content_type, url, keyword, pillar_url, idx)
        out_path.write_text(html, encoding="utf-8")
        created += 1
    except Exception as e:
        errors.append(f"{url}: {e}")
        skipped += 1

print(f"\nDone! Created: {created}, Skipped: {skipped}")
if errors:
    print("Errors:")
    for e in errors[:10]:
        print(" ", e)
