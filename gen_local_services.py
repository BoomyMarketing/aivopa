#!/usr/bin/env python3
"""Generate YouTube Ads Agency and Amazon Ads Agency local pages for all 22 cities."""
import os, re

BASE = os.path.dirname(__file__)
LOCAL = os.path.join(BASE, 'local')

ALL_22_CITIES = [
    # (slug, display_name, state_abbr, zip, street)
    ('albuquerque', 'Albuquerque', 'NM', '87102', '201 Third St NW'),
    ('arlington',   'Arlington',   'TX', '76010', '101 W Abram St'),
    ('atlanta',     'Atlanta',     'GA', '30303', '55 Trinity Ave SW'),
    ('austin',      'Austin',      'TX', '78701', '301 W 2nd St'),
    ('bakersfield', 'Bakersfield', 'CA', '93301', '1501 Truxtun Ave'),
    ('boston',      'Boston',      'MA', '02110', '1 Financial Center'),
    ('charlotte',   'Charlotte',   'NC', '28202', '600 E Trade St'),
    ('chicago',     'Chicago',     'IL', '60602', '121 N LaSalle St'),
    ('cincinnati',  'Cincinnati',  'OH', '45202', '525 Vine St'),
    ('cleveland',   'Cleveland',   'OH', '44114', '601 Lakeside Ave E'),
    ('dallas',      'Dallas',      'TX', '75201', '1601 Elm St'),
    ('denver',      'Denver',      'CO', '80202', '1700 Lincoln St'),
    ('houston',     'Houston',     'TX', '77002', '901 Bagby St'),
    ('los-angeles', 'Los Angeles', 'CA', '90012', '200 N Spring St'),
    ('miami',       'Miami',       'FL', '33128', '444 SW 2nd Ave'),
    ('nashville',   'Nashville',   'TN', '37201', '1 Public Square'),
    ('new-york',    'New York',    'NY', '10118', '350 Fifth Avenue'),
    ('phoenix',     'Phoenix',     'AZ', '85004', '200 W Washington St'),
    ('portland',    'Portland',    'OR', '97201', '1120 SW 5th Ave'),
    ('san-diego',   'San Diego',   'CA', '92101', '202 C St'),
    ('san-francisco','San Francisco','CA','94105', '1 Dr Carlton B Goodlett Pl'),
    ('seattle',     'Seattle',     'WA', '98101', '600 4th Ave'),
]

NEARBY_MAP = {
    'albuquerque':   ['dallas', 'phoenix', 'denver'],
    'arlington':     ['dallas', 'houston', 'austin'],
    'atlanta':       ['charlotte', 'miami', 'nashville'],
    'austin':        ['dallas', 'houston', 'san-antonio'],
    'bakersfield':   ['los-angeles', 'san-diego', 'san-francisco'],
    'boston':        ['new-york', 'chicago', 'miami'],
    'charlotte':     ['atlanta', 'miami', 'nashville'],
    'chicago':       ['houston', 'dallas', 'new-york'],
    'cincinnati':    ['chicago', 'cleveland', 'nashville'],
    'cleveland':     ['chicago', 'cincinnati', 'new-york'],
    'dallas':        ['houston', 'austin', 'arlington'],
    'denver':        ['phoenix', 'seattle', 'austin'],
    'houston':       ['dallas', 'austin', 'arlington'],
    'los-angeles':   ['san-diego', 'san-francisco', 'phoenix'],
    'miami':         ['atlanta', 'charlotte', 'new-york'],
    'nashville':     ['atlanta', 'charlotte', 'chicago'],
    'new-york':      ['boston', 'miami', 'chicago'],
    'phoenix':       ['los-angeles', 'denver', 'san-diego'],
    'portland':      ['seattle', 'san-francisco', 'denver'],
    'san-diego':     ['los-angeles', 'phoenix', 'san-francisco'],
    'san-francisco': ['los-angeles', 'san-diego', 'portland'],
    'seattle':       ['portland', 'san-francisco', 'denver'],
}

CITY_NAMES = {
    'albuquerque': 'Albuquerque', 'arlington': 'Arlington', 'atlanta': 'Atlanta',
    'austin': 'Austin', 'bakersfield': 'Bakersfield', 'boston': 'Boston',
    'charlotte': 'Charlotte', 'chicago': 'Chicago', 'cincinnati': 'Cincinnati',
    'cleveland': 'Cleveland', 'dallas': 'Dallas', 'denver': 'Denver',
    'houston': 'Houston', 'los-angeles': 'Los Angeles', 'miami': 'Miami',
    'nashville': 'Nashville', 'new-york': 'New York', 'phoenix': 'Phoenix',
    'portland': 'Portland', 'san-antonio': 'San Antonio', 'san-diego': 'San Diego',
    'san-francisco': 'San Francisco', 'seattle': 'Seattle',
}

# ─────────────────────────────────────────────
# SERVICE CONFIGS
# ─────────────────────────────────────────────
SERVICES = {
    'youtube-ads-agency': {
        'title_svc':   'YouTube Ads Agency',
        'slug_svc':    'youtube-ads-agency',
        'svc_lower':   'youtube ads agency',
        'platform':    'YouTube',
        'price_low':   '1500', 'price_mid': '4000', 'price_high': '8000',
        'hero_sub':    'Grow your {city} business with data-driven YouTube advertising that reaches high-intent audiences at every stage of the funnel.',
        'badge':       'YouTube Ads Agency · {city}',
        'hero_h1':     'Expert YouTube Ads Agency Services in <span class="accent-word">{city}</span>',
        'stat_roas':   '4.1x',
        'float_spend': '$80M+',
        'float_brands':'250+',
        'float_roas':  '4.1x',
        'metric_roas': '4.1x',
        'metric_cac':  '-38%',
        'ticker_items': ['youtube ads agency', '{city}', 'YouTube Advertising', 'In-Stream Ads', 'Discovery Ads', 'Data-Driven Growth'],
        'intro_p1':    'The {city} market demands advertising that does more than interrupt — it has to educate, inspire, and convert. Vora brings YouTube-first strategy built around intent signals, audience layering, and creative formats that perform at every stage of the funnel.',
        'intro_p2':    'YouTube is the second-largest search engine in the world and the highest-reach video platform for {city} businesses looking to build lasting brand equity alongside direct-response results. With TrueView in-stream, Discovery, and Shorts placements, Vora constructs YouTube campaigns that match the right message to the right viewer at the exact moment they are ready to engage.',
        'intro_p3':    "What separates Vora from other youtube ads agency providers in {city} is our obsession with audience intent. We layer first-party data, custom intent audiences, and in-market segments to ensure your {city} YouTube budget reaches people who are actively researching solutions — not just passively scrolling.",
        'intro_p4':    'Our onboarding process is designed to move fast. Within two weeks of engagement, {city} businesses have a completed creative brief, audience architecture, and initial campaigns live collecting real performance data. We iterate weekly based on view-through rate, skip rate, and cost-per-view.',
        'intro_p5':    'Every {city} industry has its own YouTube audience behaviour: search queries, content preferences, and competitor creative landscape. Vora builds YouTube campaigns tailored to your specific {city} market rather than applying a generic paid video playbook.',
        'intro_p6':    '{city} businesses winning on YouTube right now share one trait: they invested in audience strategy and creative quality before the channel became saturated in their niche. Vora gives you that first-mover advantage — structured, data-driven YouTube advertising built to scale.',
        'aside_title': 'Why {city} Businesses Choose Vora for YouTube',
        'aside_items': [
            'YouTube-native audience strategy',
            'In-stream, Discovery & Shorts formats',
            'Dedicated account manager in your timezone',
            'Transparent monthly reporting',
            'No long-term lock-in contracts',
            'Results-focused — revenue, not just views',
            '$80M+ in ad spend managed',
            '250+ brands scaled',
            '4.1x average ROAS',
            'Serving {city}, United States & beyond',
        ],
        'faq': [
            ('How much does youtube ads agency cost in {city}?',
             'The cost of youtube ads agency in {city} depends on your ad spend level, creative production needs, and campaign objectives. Vora offers flexible packages starting from $1,500/mo. YouTube CPMs in {city} are typically competitive with Meta placements while delivering higher purchase intent, making it one of the strongest ROI channels for {city} businesses running video-first strategies. Book a free consultation so we can assess your specific situation and provide an accurate quote.'),
            ('How long does youtube ads agency take to show results in {city}?',
             'Most {city} businesses begin seeing meaningful YouTube campaign results within 30 to 60 days of launch. YouTube\'s algorithm learns faster when campaigns launch with sufficient creative variation and structured audience segmentation. Vora provides detailed monthly reporting so every metric is fully transparent.'),
            ('Why choose Vora for youtube ads agency in {city}?',
             'Vora combines deep knowledge of the {city} market with YouTube-native audience strategy and a genuine commitment to client outcomes. Our team understands how to build creative that performs across TrueView in-stream, Discovery, and Shorts formats — matching the right message to the right viewer at the right moment. We become a long-term growth partner, not just a vendor, with no lock-in contracts and full decision transparency.'),
            ('What types of businesses benefit most from YouTube ads in {city}?',
             'YouTube advertising works exceptionally well for {city} businesses with visual products or services, strong brand stories, considered-purchase sales cycles, and audiences actively researching solutions. This includes e-commerce brands, SaaS companies, local service businesses, healthcare providers, real estate agents, and any brand wanting to build lasting equity alongside direct-response results.'),
            ('What makes {city} businesses different in terms of youtube ads agency needs?',
             '{city} has a unique business ecosystem with specific demographic concentrations, local search patterns, and competitive creative landscape. Effective youtube ads agency in {city} requires understanding which video content formats resonate with the local audience and how to position against {city} competitors who are increasingly active on YouTube.'),
            ('How does Vora approach youtube ads agency for {city}\'s market?',
             'Vora\'s approach to youtube ads agency in {city} begins with a creative audit, audience analysis, and competitor research specific to your {city} market. We build YouTube campaigns structured around the full funnel: awareness creative that earns views, consideration content that builds trust, and conversion campaigns that drive direct action. Every campaign is optimised based on view-through rate, skip rate, and cost-per-result — with creative refreshes every 3 to 4 weeks to stay ahead of frequency fatigue.'),
        ],
        'nearby_label': 'YouTube Ads Agency',
        'nearby_heading': 'YouTube Ads Agency in Nearby Areas',
        'nearby_sub':  'We serve high-growth businesses across the United States — not just {city}.',
        'cta_heading': 'Ready to Grow Your {city} Business with YouTube Ads?',
        'cta_sub':     'Get a free strategy consultation. No commitment, no pressure — just actionable insights.',
        'footer_tagline': "{city}'s performance marketing agency. YouTube Ads, Meta Ads &amp; Google Ads engineered for ROAS.",
        'footer_svc_label': 'YouTube Ads',
        'footer_svc_href':  'youtube-ads',
        'services_h2': 'Performance Marketing Services in {city}',
    },

    'amazon-ads-agency': {
        'title_svc':   'Amazon Ads Agency',
        'slug_svc':    'amazon-ads-agency',
        'svc_lower':   'amazon ads agency',
        'platform':    'Amazon',
        'price_low':   '2000', 'price_mid': '5000', 'price_high': '10000',
        'hero_sub':    'Grow your {city} business with Amazon advertising that puts your products in front of ready-to-buy shoppers at the exact moment they\'re searching.',
        'badge':       'Amazon Ads Agency · {city}',
        'hero_h1':     'Expert Amazon Ads Agency Services in <span class="accent-word">{city}</span>',
        'stat_roas':   '5.3x',
        'float_spend': '$60M+',
        'float_brands':'200+',
        'float_roas':  '5.3x',
        'metric_roas': '5.3x',
        'metric_cac':  '-35%',
        'ticker_items': ['amazon ads agency', '{city}', 'Sponsored Products', 'DSP Advertising', 'Amazon PPC', 'Data-Driven Growth'],
        'intro_p1':    'The {city} market is full of Amazon sellers and vendors fighting for the Buy Box and top-of-search placements. Vora brings structured Amazon PPC strategy built around keyword architecture, bid optimisation, and conversion-rate improvements that compound over time.',
        'intro_p2':    'Amazon Advertising is the highest-intent paid channel available to {city} product businesses. Shoppers arrive with credit card in hand, actively searching for exactly what you sell. Vora builds Sponsored Products, Sponsored Brands, and DSP campaigns that capture this demand efficiently and profitably.',
        'intro_p3':    "What separates Vora from other amazon ads agency providers in {city} is our obsession with profitability metrics. We don't chase impressions or clicks — we optimise for ACoS, TACoS, and net revenue growth. Every campaign decision is grounded in your {city} business's actual margin structure.",
        'intro_p4':    'Our onboarding process for {city} Amazon advertisers is designed to audit, structure, and launch fast. Within two weeks, you have a complete keyword architecture, optimised listing recommendations, and initial campaigns live collecting real performance data. We iterate weekly based on search term reports and conversion data.',
        'intro_p5':    'Every {city} product category on Amazon has its own competitive dynamics: seasonal demand patterns, top competitor ad strategies, and price elasticity. Vora builds Amazon campaigns tailored to your specific {city} category rather than applying a one-size-fits-all PPC playbook.',
        'intro_p6':    '{city} Amazon sellers winning right now share one trait: they invested in structured PPC strategy and listing quality before their category became fully saturated. Vora gives you that structural advantage — data-driven Amazon advertising built to compound ROAS over time.',
        'aside_title': 'Why {city} Amazon Sellers Choose Vora',
        'aside_items': [
            'Sponsored Products, Brands & Display',
            'ACoS & TACoS optimisation',
            'Dedicated account manager in your timezone',
            'Transparent monthly reporting',
            'No long-term lock-in contracts',
            'Profitability-focused — ROAS over vanity metrics',
            '$60M+ in ad spend managed',
            '200+ brands scaled',
            '5.3x average ROAS',
            'Serving {city}, United States & beyond',
        ],
        'faq': [
            ('How much does amazon ads agency cost in {city}?',
             'The cost of amazon ads agency in {city} depends on your monthly ad spend, product catalog size, and campaign complexity. Vora offers flexible packages starting from $2,000/mo. Amazon advertising delivers some of the highest purchase-intent traffic available to {city} product businesses — shoppers arrive ready to buy, which makes efficient PPC management highly profitable at scale. Book a free consultation so we can assess your specific situation and provide an accurate quote.'),
            ('How long does amazon ads agency take to show results in {city}?',
             'Most {city} Amazon sellers begin seeing meaningful PPC improvements within 30 to 45 days of Vora\'s structured keyword architecture and bid optimisation going live. Amazon\'s campaign learning phase is shorter than most platforms because purchase intent is explicit — we see real conversion data quickly and can iterate with confidence. Vora provides detailed monthly reporting so every ACoS and revenue metric is fully transparent.'),
            ('Why choose Vora for amazon ads agency in {city}?',
             'Vora combines deep knowledge of Amazon\'s advertising ecosystem with a genuine commitment to {city} seller profitability. Our team understands how to structure Sponsored Products, Brands, and DSP campaigns that drive organic rank improvement alongside direct-response revenue. We become a long-term growth partner, not just a vendor, with no lock-in contracts and full decision transparency.'),
            ('What types of businesses benefit most from Amazon ads in {city}?',
             'Amazon advertising works exceptionally well for {city} businesses with physical products sold on Amazon, whether as first-party vendors or third-party sellers. This includes e-commerce brands, consumer goods manufacturers, private label sellers, and any product business with strong demand on the Amazon marketplace. If your {city} customers are searching Amazon for your category, Vora can capture that demand profitably.'),
            ('What makes {city} businesses different in terms of amazon ads agency needs?',
             '{city} has a unique business ecosystem with specific product categories, competitive dynamics, and seasonal demand patterns that shape Amazon advertising strategy. Effective amazon ads agency in {city} requires understanding your product category\'s specific search term landscape, competitor bidding behaviour, and conversion rate benchmarks so every campaign dollar is deployed at maximum efficiency.'),
            ('How does Vora approach amazon ads agency for {city}\'s market?',
             'Vora\'s approach to amazon ads agency in {city} begins with a full account audit, keyword gap analysis, and competitor research specific to your product category. We build Amazon campaigns structured around the full funnel: Sponsored Products for high-intent search capture, Sponsored Brands for consideration and shelf presence, and DSP retargeting for conversion optimisation. Every campaign is continuously optimised based on search term data, bid efficiency, and ACoS targets — with weekly adjustments to stay ahead of competitor activity.'),
        ],
        'nearby_label': 'Amazon Ads Agency',
        'nearby_heading': 'Amazon Ads Agency in Nearby Areas',
        'nearby_sub':  'We serve product businesses across the United States — not just {city}.',
        'cta_heading': 'Ready to Grow Your {city} Amazon Sales?',
        'cta_sub':     'Get a free Amazon PPC audit. No commitment, no pressure — just actionable insights.',
        'footer_tagline': "{city}'s Amazon advertising agency. Sponsored Products, Brands &amp; DSP engineered for ROAS.",
        'footer_svc_label': 'Amazon Ads',
        'footer_svc_href':  'amazon-ads',
        'services_h2': 'Performance Marketing Services in {city}',
    },
}


def fmt(template, city, city_slug):
    return template.replace('{city}', city).replace('{city_slug}', city_slug)


def make_page(svc_cfg, city_slug, city_name, state, zipcode, street):
    c = city_name
    s = city_slug
    cfg = svc_cfg
    svc_slug = cfg['slug_svc']
    svc_title = cfg['title_svc']
    svc_lower = cfg['svc_lower']
    platform = cfg['platform']

    nearby3 = NEARBY_MAP.get(city_slug, ['new-york', 'chicago', 'los-angeles'])
    nearby_html = '\n'.join(
        f'  <li><a href="https://aivopa.com/local/{ns}/{svc_slug}">{cfg["nearby_label"]} in {CITY_NAMES.get(ns, ns.replace("-"," ").title())}</a></li>'
        for ns in nearby3
    )

    ticker_items = cfg['ticker_items']
    ticker_html = '\n'.join(
        f'            <div class="ticker-item">{fmt(ti, c, s)} <span class="ticker-sep">&#x2726;</span></div>'
        for ti in (ticker_items * 2)
    )

    faq_items_schema = []
    for q, a in cfg['faq']:
        q2 = fmt(q, c, s)
        a2 = fmt(a, c, s).replace("'", "\\'")
        faq_items_schema.append(
            f'{{"@type": "Question", "name": "{q2}", "acceptedAnswer": {{"@type": "Answer", "text": "{a2}"}}}}'
        )

    faq_items_html = ''
    for i, (q, a) in enumerate(cfg['faq']):
        q2 = fmt(q, c, s)
        a2 = fmt(a, c, s)
        faq_items_html += f'''                    <div class="faq-item">
                        <button class="faq-question" aria-expanded="false" aria-controls="faq-{i}">{q2}</button>
                        <div class="faq-answer" id="faq-{i}"><p>{a2}</p></div>
                    </div>\n'''

    aside_items_html = '\n'.join(
        f'                    <li>{fmt(item, c, s)}</li>'
        for item in cfg['aside_items']
    )

    price_low = cfg['price_low']
    price_mid = cfg['price_mid']
    price_high = cfg['price_high']
    roas = cfg['stat_roas']
    spend = cfg['float_spend']
    brands = cfg['float_brands']

    schema_ldjson = f'{{"@context": "https://schema.org", "@type": ["LocalBusiness", "MarketingAgency"], "name": "Vora", "description": "{svc_title} services in {c}", "url": "https://aivopa.com/local/{s}/{svc_slug}", "telephone": "+16473701888", "email": "hello@aivopa.com", "address": {{"@type": "PostalAddress", "streetAddress": "{street}", "addressLocality": "{c}", "addressRegion": "{state}", "postalCode": "{zipcode}", "addressCountry": "US"}}, "priceRange": "$$", "servedArea": {{"@type": "City", "name": "{c}"}}, "hasOfferCatalog": {{"@type": "OfferCatalog", "name": "{svc_title}", "itemListElement": [{{"@type": "Offer", "name": "{svc_title} - Starter", "price": "{price_low}", "priceCurrency": "USD"}}, {{"@type": "Offer", "name": "{svc_title} - Growth", "price": "{price_mid}", "priceCurrency": "USD"}}, {{"@type": "Offer", "name": "{svc_title} - Scale", "price": "{price_high}", "priceCurrency": "USD"}}]}}, "datePublished": "2026-05-12", "dateModified": "2026-05-12"}}'

    faq_schema = '{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [' + ', '.join(faq_items_schema) + ']}'

    breadcrumb_schema = f'{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://aivopa.com"}}, {{"@type": "ListItem", "position": 2, "name": "Local", "item": "https://aivopa.com/local/"}}, {{"@type": "ListItem", "position": 3, "name": "{svc_title} in {c}", "item": "https://aivopa.com/local/{s}/{svc_slug}"}}]}}'

    intro_p = ''.join(
        f'                <p>{fmt(cfg[k], c, s)}</p>\n'
        for k in ['intro_p1','intro_p2','intro_p3','intro_p4','intro_p5','intro_p6']
    )

    svc_href = cfg['footer_svc_href']
    svc_label = cfg['footer_svc_label']

    html = f'''<!DOCTYPE html>
<html lang="en" class="site-vora">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow">
    <title>Best {svc_title} Services in {c} | Vora</title>
    <meta name="description" content="Looking for expert {svc_lower} in {c}? Vora delivers proven {platform} advertising results for businesses across the United States. Transparent reporting. Get your free strategy session today.">
    <link rel="canonical" href="https://aivopa.com/local/{s}/{svc_slug}">

    <!-- Open Graph -->
    <meta property="og:title" content="Best {svc_title} Services in {c} | Vora">
    <meta property="og:description" content="Looking for expert {svc_lower} in {c}? Vora delivers proven {platform} advertising results for businesses across the United States. Transparent reporting.">
    <meta property="og:url" content="https://aivopa.com/local/{s}/{svc_slug}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://aivopa.com/img/og-default.jpg">
    <meta property="og:site_name" content="Vora">
    <meta property="og:locale" content="en_US">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Best {svc_title} Services in {c} | Vora">
    <meta name="twitter:description" content="Looking for expert {svc_lower} in {c}? Vora delivers proven {platform} advertising results for businesses across the United States.">
    <meta name="twitter:image" content="https://aivopa.com/img/og-default.jpg">

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <!-- Schema: LocalBusiness + Service -->
    <script type="application/ld+json">
{schema_ldjson}
    </script>

    <!-- Schema: FAQPage -->
    <script type="application/ld+json">
{faq_schema}
    </script>

    <!-- Schema: BreadcrumbList -->
    <script type="application/ld+json">
{breadcrumb_schema}
    </script>

    <style>
        :root {{
            --primary: #0070F3;
            --primary-dark: #0052CC;
            --primary-glow: rgba(0,112,243,0.3);
            --secondary: #7928CA;
            --accent: #00C2FF;
            --bg: #FFFFFF;
            --bg-surface: #F7F9FC;
            --bg-soft: #EEF4FF;
            --dark: #0A0A0F;
            --hero-bg: linear-gradient(135deg, #0A0A0F 0%, #0d1a3a 60%, #0A0A0F 100%);
            --text-heading: #0A0A0F;
            --text: #374151;
            --text-muted: #9CA3AF;
            --text-on-primary: #FFFFFF;
            --logo-color: #0A0A0F;
            --border-color: rgba(0,0,0,0.08);
            --gradient-primary: linear-gradient(135deg, #0070F3 0%, #7928CA 100%);
            --radius: 8px;
            --radius-sm: 4px;
            --radius-lg: 16px;
            --radius-btn: 8px;
            --shadow: 0 2px 16px rgba(0,0,0,0.06);
            --shadow-lg: 0 16px 48px rgba(0,112,243,0.15);
            --shadow-primary: 0 8px 32px rgba(0,112,243,0.4);
            --transition: 0.3s cubic-bezier(0.4,0,0.2,1);
            --font-heading: 'Space Grotesk', system-ui, sans-serif;
            --font-body: 'Inter', system-ui, sans-serif;
            --max-w: 1160px;
        }}
        *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; font-size: 16px; -webkit-font-smoothing: antialiased; }}
        body {{ font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.7; overflow-x: clip; }}
        h1, h2, h3, h4 {{ font-family: var(--font-heading); line-height: 1.15; letter-spacing: -0.02em; color: var(--text-heading); }}
        a {{ color: var(--primary); text-decoration: none; transition: color var(--transition); }}
        a:hover {{ opacity: 0.85; }}
        img {{ max-width: 100%; height: auto; display: block; }}
        .container {{ max-width: var(--max-w); margin: 0 auto; padding: 0 24px; }}
        #vora-scroll-progress {{ position: fixed; top: 0; left: 0; width: 0%; height: 3px; background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%); z-index: 9999; transition: width 0.1s linear; }}
        .site-nav {{ position: sticky; top: 0; z-index: 500; background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,112,243,0.1); padding: 0; transition: box-shadow var(--transition); }}
        .site-nav.scrolled {{ box-shadow: 0 2px 20px rgba(0,112,243,0.08); }}
        .nav-inner {{ max-width: var(--max-w); margin: 0 auto; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; height: 64px; gap: 24px; }}
        .nav-logo {{ font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; color: var(--dark); text-decoration: none; letter-spacing: -0.03em; white-space: nowrap; }}
        .nav-logo span {{ color: var(--primary); }}
        .nav-links {{ display: flex; align-items: center; gap: 28px; list-style: none; }}
        .nav-links a {{ font-size: 0.875rem; font-weight: 500; color: var(--text); position: relative; padding-bottom: 2px; }}
        .nav-links a::after {{ content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 1.5px; background: var(--primary); transition: width var(--transition); }}
        .nav-links a:hover {{ color: var(--primary); opacity: 1; }}
        .nav-links a:hover::after {{ width: 100%; }}
        .nav-cta {{ background: var(--primary) !important; color: #fff !important; padding: 10px 22px; border-radius: var(--radius-btn); font-weight: 600; font-size: 0.875rem; white-space: nowrap; box-shadow: var(--shadow-primary); }}
        .nav-cta::after {{ display: none !important; }}
        .nav-cta:hover {{ background: var(--primary-dark) !important; transform: translateY(-1px); opacity: 1 !important; }}
        .nav-hamburger {{ display: none; background: none; border: none; cursor: pointer; padding: 4px; color: var(--dark); }}
        .mobile-menu {{ display: none; flex-direction: column; gap: 0; background: #fff; border-top: 1px solid var(--border-color); padding: 8px 24px 16px; }}
        .mobile-menu a {{ padding: 12px 0; font-size: 0.95rem; font-weight: 500; color: var(--text); border-bottom: 1px solid var(--border-color); }}
        .mobile-menu a:last-child {{ border-bottom: none; }}
        .mobile-menu.open {{ display: flex; }}
        .breadcrumb {{ background: var(--bg-surface); padding: 10px 0; font-size: 0.82rem; border-bottom: 1px solid var(--border-color); }}
        .breadcrumb .container {{ display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }}
        .breadcrumb a {{ color: var(--text-muted); font-weight: 500; }}
        .breadcrumb a:hover {{ color: var(--primary); opacity: 1; }}
        .breadcrumb .sep {{ color: var(--text-muted); }}
        .breadcrumb .current {{ color: var(--primary); font-weight: 600; }}
        .hero {{ background: var(--hero-bg); color: #fff; padding: 80px 0 72px; position: relative; overflow: hidden; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; }}
        .hero::before {{ content: ''; position: absolute; top: -120px; right: -100px; width: 700px; height: 700px; border-radius: 50%; background: radial-gradient(circle, rgba(0,112,243,0.22) 0%, transparent 70%); pointer-events: none; }}
        .hero::after {{ content: ''; position: absolute; bottom: -80px; left: -80px; width: 480px; height: 480px; border-radius: 50%; background: radial-gradient(circle, rgba(121,40,202,0.18) 0%, transparent 70%); pointer-events: none; }}
        .hero .container {{ position: relative; z-index: 1; width: 100%; }}
        .hero-content {{ opacity: 0; transform: translateY(28px); filter: blur(10px); animation: heroFadeUp 0.7s cubic-bezier(0.22,1,0.36,1) 0.1s forwards; }}
        @keyframes heroFadeUp {{ to {{ opacity: 1; transform: translateY(0); filter: blur(0); }} }}
        .hero-meta-badge {{ display: inline-flex; align-items: center; gap: 8px; background: rgba(0,112,243,0.15); border: 1px solid rgba(0,112,243,0.3); color: var(--accent); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; padding: 6px 14px; border-radius: 20px; margin-bottom: 22px; }}
        .hero h1 {{ color: #fff; font-size: clamp(3rem,7vw,5.5rem); max-width: 720px; margin-bottom: 20px; letter-spacing: -0.03em; line-height: 1.1; }}
        .hero h1 em {{ font-style: normal; background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}
        .accent-word {{ color: var(--primary); text-shadow: 0 0 24px rgba(0,112,243,0.5); animation: accent-pulse 3.5s ease-in-out infinite 1.2s; }}
        @keyframes accent-pulse {{ 0%,100% {{ text-shadow: 0 0 24px rgba(0,112,243,0.5); }} 50% {{ text-shadow: 0 0 50px rgba(0,112,243,0.85), 0 0 80px rgba(0,112,243,0.3); }} }}
        .hero-subtitle {{ font-size: 1.05rem; color: rgba(255,255,255,0.72); max-width: 580px; margin-bottom: 38px; line-height: 1.7; }}
        .hero-actions {{ display: flex; gap: 14px; flex-wrap: wrap; align-items: center; }}
        .btn-primary {{ background: var(--primary); color: #fff; padding: 14px 32px; border-radius: var(--radius-btn); font-weight: 700; font-size: 0.95rem; display: inline-block; transition: background var(--transition), transform var(--transition), box-shadow var(--transition); box-shadow: var(--shadow-primary); position: relative; overflow: hidden; }}
        .btn-primary::before {{ content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 60%); pointer-events: none; }}
        .btn-primary:hover {{ background: var(--primary-dark); transform: translateY(-2px); box-shadow: 0 12px 36px rgba(0,112,243,0.45); opacity: 1; color: #fff; }}
        .btn-ghost {{ color: rgba(255,255,255,0.8); border: 1.5px solid rgba(255,255,255,0.2); padding: 13px 26px; border-radius: var(--radius-btn); font-size: 0.92rem; font-weight: 500; display: inline-block; transition: background var(--transition), border-color var(--transition); }}
        .btn-ghost:hover {{ background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.4); opacity: 1; color: #fff; }}
        .btn-outline {{ border: 1.5px solid var(--primary); color: var(--primary); padding: 12px 28px; border-radius: var(--radius-btn); font-weight: 600; font-size: 0.9rem; display: inline-block; transition: background var(--transition), color var(--transition); }}
        .btn-outline:hover {{ background: var(--primary); color: #fff; opacity: 1; }}
        .hero-float-cards {{ position: absolute; right: 40px; top: 50%; transform: translateY(-50%); display: flex; flex-direction: column; gap: 16px; z-index: 2; }}
        .float-card {{ background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 12px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; backdrop-filter: blur(10px); min-width: 200px; }}
        .float-icon {{ width: 38px; height: 38px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; }}
        .fi-blue {{ background: rgba(0,112,243,0.2); }}
        .fi-purple {{ background: rgba(121,40,202,0.2); }}
        .fi-cyan {{ background: rgba(0,194,255,0.2); }}
        .float-num {{ font-family: var(--font-heading); font-size: 1.1rem; font-weight: 700; color: #fff; }}
        .float-num.p {{ color: #c084fc; }}
        .float-num.c {{ color: var(--accent); }}
        .float-lbl {{ font-size: 0.72rem; color: rgba(255,255,255,0.5); }}
        .ticker-section {{ background: rgba(0,0,0,0.4); overflow: hidden; padding: 14px 0; border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05); }}
        .ticker-track {{ display: flex; gap: 0; white-space: nowrap; animation: ticker 22s linear infinite; }}
        .ticker-item {{ font-size: 0.82rem; font-weight: 500; color: rgba(255,255,255,0.45); padding: 0 18px; letter-spacing: 0.04em; text-transform: uppercase; }}
        .ticker-sep {{ color: var(--primary); margin-left: 18px; }}
        @keyframes ticker {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-50%); }} }}
        .stats-bar {{ background: var(--primary); padding: 22px 0; position: relative; overflow: hidden; }}
        .stats-bar::before {{ content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); opacity: 0.92; }}
        .stats-bar .container {{ position: relative; z-index: 1; display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 40px; }}
        .stat-item {{ text-align: center; color: #fff; }}
        .stat-value {{ display: block; font-family: var(--font-heading); font-size: 1.35rem; font-weight: 700; }}
        .stat-label {{ font-size: 0.72rem; opacity: 0.75; letter-spacing: 0.06em; text-transform: uppercase; }}
        .section-intro {{ padding: 80px 0; }}
        .section-intro .container {{ display: grid; grid-template-columns: 1fr 380px; gap: 56px; align-items: start; }}
        .intro-content h2 {{ font-size: clamp(1.6rem,3vw,2.4rem); margin-bottom: 22px; }}
        .intro-content p {{ color: var(--text); margin-bottom: 18px; font-size: 0.97rem; line-height: 1.8; }}
        .intro-aside {{ background: var(--bg-soft); border-radius: var(--radius-lg); padding: 32px; border: 1px solid rgba(0,112,243,0.12); }}
        .intro-aside h3 {{ font-size: 1rem; margin-bottom: 18px; color: var(--primary); }}
        .feature-list {{ list-style: none; display: flex; flex-direction: column; gap: 12px; }}
        .feature-list li {{ font-size: 0.88rem; color: var(--text); display: flex; align-items: center; gap: 10px; }}
        .feature-list li::before {{ content: '&#x2713;'; color: var(--primary); font-weight: 700; font-size: 0.9rem; flex-shrink: 0; }}
        .metrics-strip {{ background: var(--dark); padding: 48px 0; }}
        .metrics-strip .container {{ display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; }}
        .metric-card {{ text-align: center; }}
        .metric-number {{ font-family: var(--font-heading); font-size: 2.8rem; font-weight: 700; color: var(--primary); line-height: 1; margin-bottom: 8px; }}
        .metric-label {{ font-size: 0.82rem; color: rgba(255,255,255,0.55); letter-spacing: 0.06em; text-transform: uppercase; }}
        .section-results {{ padding: 56px 0; background: var(--bg-surface); }}
        .results-grid {{ max-width: var(--max-w); margin: 0 auto; padding: 0 24px; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; }}
        .result-item {{ text-align: center; }}
        .result-num {{ font-family: var(--font-heading); font-size: 2.5rem; font-weight: 700; color: var(--dark); display: block; line-height: 1; margin-bottom: 6px; }}
        .result-num.p {{ color: var(--secondary); }}
        .result-num.c {{ color: var(--primary); }}
        .result-label {{ font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.06em; }}
        .section-services {{ padding: 80px 0; }}
        .section-header {{ margin-bottom: 48px; }}
        .section-label {{ display: inline-block; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--primary); margin-bottom: 10px; }}
        .section-header h2 {{ font-size: clamp(1.6rem,3vw,2.5rem); margin-bottom: 12px; }}
        .section-header .subtitle {{ color: var(--text-muted); max-width: 560px; font-size: 0.97rem; }}
        .services-grid {{ display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }}
        .service-card {{ background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 28px; transition: border-color var(--transition), box-shadow var(--transition); }}
        .service-card:hover {{ border-color: rgba(0,112,243,0.3); box-shadow: var(--shadow-lg); }}
        .service-icon {{ font-size: 1.8rem; margin-bottom: 14px; }}
        .service-card h3 {{ font-size: 1.05rem; margin-bottom: 8px; }}
        .service-card p {{ font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px; }}
        .service-card a {{ font-size: 0.85rem; font-weight: 600; color: var(--primary); }}
        .section-pricing {{ background: var(--dark); padding: 80px 0; }}
        .section-pricing .section-header h2 {{ color: #fff; }}
        .section-pricing .section-label {{ color: var(--accent); }}
        .section-pricing .subtitle {{ color: rgba(255,255,255,0.55); }}
        .pricing-cards {{ display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }}
        .price-card {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: var(--radius-lg); padding: 32px 28px; text-align: center; min-width: 220px; flex: 1; max-width: 280px; transition: border-color var(--transition); }}
        .price-card.featured {{ border-color: var(--primary); background: rgba(0,112,243,0.1); }}
        .price-name {{ font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent); margin-bottom: 12px; }}
        .price-amount {{ font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: #fff; margin-bottom: 4px; }}
        .price-period {{ font-size: 0.78rem; color: rgba(255,255,255,0.45); margin-bottom: 22px; }}
        .price-cta {{ background: var(--primary); color: #fff; padding: 11px 24px; border-radius: var(--radius-btn); font-weight: 600; font-size: 0.875rem; display: inline-block; transition: background var(--transition); }}
        .price-cta:hover {{ background: var(--primary-dark); opacity: 1; color: #fff; }}
        .section-faq {{ padding: 80px 0; }}
        .faq-accordion {{ display: flex; flex-direction: column; gap: 12px; max-width: 780px; }}
        .faq-item {{ background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius); overflow: hidden; transition: border-color var(--transition); }}
        .faq-question {{ width: 100%; background: none; border: none; font-family: var(--font-body); font-size: 0.97rem; font-weight: 600; color: var(--text-heading); text-align: left; padding: 18px 22px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; gap: 14px; }}
        .faq-question::after {{ content: '+'; font-size: 1.2rem; color: var(--primary); flex-shrink: 0; transition: transform 0.2s; }}
        .faq-question[aria-expanded="true"]::after {{ transform: rotate(45deg); }}
        .faq-answer {{ display: none; padding: 0 22px 18px; font-size: 0.92rem; color: var(--text); line-height: 1.75; }}
        .faq-answer.open {{ display: block; }}
        .section-nearby {{ padding: 64px 0; background: var(--bg-surface); }}
        .nearby-grid {{ margin-top: 8px; }}
        .nearby-cities {{ list-style: none; display: flex; flex-wrap: wrap; gap: 12px; }}
        .nearby-cities li a {{ display: inline-block; background: #fff; border: 1px solid var(--border-color); border-radius: 30px; padding: 8px 20px; font-size: 0.88rem; font-weight: 500; color: var(--text); transition: border-color var(--transition), color var(--transition); }}
        .nearby-cities li a:hover {{ border-color: var(--primary); color: var(--primary); opacity: 1; }}
        .section-cta {{ background: linear-gradient(135deg, #0A0A0F 0%, #0d1a3a 60%, #0A0A0F 100%); padding: 100px 0; text-align: center; position: relative; overflow: hidden; }}
        .section-cta::before {{ content: ''; position: absolute; top: -80px; left: 50%; transform: translateX(-50%); width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(circle, rgba(0,112,243,0.18) 0%, transparent 70%); pointer-events: none; }}
        .section-cta .container {{ position: relative; z-index: 1; }}
        .section-cta h2 {{ font-size: clamp(1.8rem,4vw,3rem); color: #fff; margin-bottom: 16px; }}
        .section-cta p {{ color: rgba(255,255,255,0.65); margin-bottom: 16px; font-size: 1rem; }}
        .cta-group {{ display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }}
        .btn-ghost-white {{ color: rgba(255,255,255,0.8); border: 1.5px solid rgba(255,255,255,0.25); padding: 12px 26px; border-radius: var(--radius-btn); font-size: 0.92rem; font-weight: 500; display: inline-block; transition: background var(--transition), border-color var(--transition); }}
        .btn-ghost-white:hover {{ background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.45); opacity: 1; color: #fff; }}
        .footer {{ background: #0A0A0F; color: rgba(255,255,255,0.65); padding: 64px 0 32px; }}
        .footer-inner {{ max-width: var(--max-w); margin: 0 auto; padding: 0 24px; }}
        .footer-top {{ display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }}
        .footer-logo {{ font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; color: #fff; text-decoration: none; letter-spacing: -0.03em; display: block; margin-bottom: 12px; }}
        .footer-logo span {{ color: var(--primary); }}
        .footer-tagline {{ font-size: 0.85rem; line-height: 1.7; color: rgba(255,255,255,0.45); margin-bottom: 18px; }}
        .footer-socials {{ display: flex; gap: 10px; }}
        .social-link {{ width: 34px; height: 34px; border-radius: 8px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 0.82rem; color: rgba(255,255,255,0.6); transition: background var(--transition), color var(--transition); }}
        .social-link:hover {{ background: var(--primary); color: #fff; border-color: var(--primary); opacity: 1; }}
        .footer-col h4 {{ font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.35); margin-bottom: 16px; }}
        .footer-col ul {{ list-style: none; display: flex; flex-direction: column; gap: 10px; }}
        .footer-col ul li a {{ font-size: 0.875rem; color: rgba(255,255,255,0.55); transition: color var(--transition); }}
        .footer-col ul li a:hover {{ color: #fff; opacity: 1; }}
        .footer-contact-item {{ display: flex; align-items: center; gap: 10px; font-size: 0.875rem; color: rgba(255,255,255,0.55); margin-bottom: 8px; }}
        .footer-contact-item a {{ color: rgba(255,255,255,0.55); }}
        .footer-contact-item a:hover {{ color: #fff; opacity: 1; }}
        .footer-bottom {{ border-top: 1px solid rgba(255,255,255,0.08); padding-top: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; font-size: 0.8rem; color: rgba(255,255,255,0.3); }}
        .footer-bl {{ display: flex; gap: 20px; }}
        .footer-bl a {{ color: rgba(255,255,255,0.3); }}
        .footer-bl a:hover {{ color: rgba(255,255,255,0.7); opacity: 1; }}
        .btn-white {{ background: #fff; color: var(--primary); padding: 14px 32px; border-radius: var(--radius-btn); font-weight: 700; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 8px; transition: background var(--transition), transform var(--transition); }}
        .btn-white:hover {{ background: #f0f7ff; transform: translateY(-1px); opacity: 1; color: var(--primary); }}
        .reveal {{ opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }}
        .reveal.visible {{ opacity: 1; transform: none; }}
        .reveal-delay-1 {{ transition-delay: 0.1s; }}
        .reveal-delay-2 {{ transition-delay: 0.2s; }}
        @media (max-width: 900px) {{
            .hero-float-cards {{ display: none; }}
            .section-intro .container {{ grid-template-columns: 1fr; gap: 32px; }}
            .services-grid {{ grid-template-columns: 1fr 1fr; }}
            .footer-top {{ grid-template-columns: 1fr 1fr; }}
        }}
        @media (max-width: 640px) {{
            .nav-links {{ display: none; }}
            .nav-hamburger {{ display: flex; }}
            .services-grid {{ grid-template-columns: 1fr; }}
            .footer-top {{ grid-template-columns: 1fr; }}
            .metrics-strip .container {{ gap: 32px; }}
        }}
    </style>
</head>
<body>

    <div id="vora-scroll-progress" aria-hidden="true"></div>

    <nav class="site-nav" id="site-nav" role="navigation" aria-label="Main navigation">
      <div class="nav-inner">
        <a href="../../../index.html" class="nav-logo" aria-label="Vora Home">Vora<span>.</span></a>
        <ul class="nav-links" role="menubar">
          <li role="none"><a href="../../../services.html" role="menuitem">Services</a></li>
          <li role="none"><a href="../../../about.html" role="menuitem">About</a></li>
          <li role="none"><a href="../../../pricing.html" role="menuitem">Pricing</a></li>
          <li role="none"><a href="../../../contact.html" role="menuitem">Contact</a></li>
          <li role="none"><a href="../../../contact.html" class="nav-cta" role="menuitem">Get Started</a></li>
        </ul>
        <button class="nav-hamburger" id="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
          <span></span><span></span><span></span>
        </button>
      </div>
      <div class="mobile-menu" id="mobile-menu" role="menu" aria-hidden="true">
        <a href="../../../services.html" role="menuitem">Services</a>
        <a href="../../../about.html" role="menuitem">About</a>
        <a href="../../../pricing.html" role="menuitem">Pricing</a>
        <a href="../../../contact.html" role="menuitem">Contact</a>
        <a href="../../../contact.html" role="menuitem">Get Started &rarr;</a>
      </div>
    </nav>

    <nav class="breadcrumb" aria-label="Breadcrumb">
        <div class="container">
            <a href="https://aivopa.com/">Vora</a>
            <span class="sep" aria-hidden="true">&rsaquo;</span>
            <a href="https://aivopa.com/services/{svc_href}">{svc_lower}</a>
            <span class="sep" aria-hidden="true">&rsaquo;</span>
            <span class="current" aria-current="page">{c}</span>
        </div>
    </nav>

    <section class="hero" aria-labelledby="hero-heading">
        <div class="container">
            <div class="hero-content">
                <div class="hero-meta-badge">{fmt(cfg["badge"], c, s)}</div>
                <h1 id="hero-heading">{fmt(cfg["hero_h1"], c, s)}</h1>
                <p class="hero-subtitle">{fmt(cfg["hero_sub"], c, s)}</p>
                <div class="hero-actions">
                    <a href="https://aivopa.com/contact" class="btn-primary">Get Free Performance Audit</a>
                    <a href="https://aivopa.com/pricing" class="btn-ghost">View Pricing</a>
                </div>
            </div>
        </div>
        <div class="hero-float-cards" aria-hidden="true">
            <div class="float-card">
                <div class="float-icon fi-blue">&#x1F4CA;</div>
                <div><div class="float-num">{spend}</div><div class="float-lbl">in ad spend managed</div></div>
            </div>
            <div class="float-card">
                <div class="float-icon fi-purple">&#x1F4C8;</div>
                <div><div class="float-num p">{brands}</div><div class="float-lbl">brands scaled</div></div>
            </div>
            <div class="float-card">
                <div class="float-icon fi-cyan">&#x2605;</div>
                <div><div class="float-num c">{roas}</div><div class="float-lbl">Average ROAS</div></div>
            </div>
        </div>
    </section>

    <div class="ticker-section" aria-hidden="true">
        <div class="ticker-track">
{ticker_html}
        </div>
    </div>

    <div class="stats-bar" aria-label="Key performance statistics">
        <div class="container">
            <div class="stat-item"><span class="stat-value">{spend}</span><span class="stat-label">ad spend managed</span></div>
            <div class="stat-item"><span class="stat-value">{brands}</span><span class="stat-label">brands scaled</span></div>
            <div class="stat-item"><span class="stat-value">{roas}</span><span class="stat-label">average ROAS</span></div>
            <div class="stat-item"><span class="stat-value">{c}</span><span class="stat-label">Service Area</span></div>
        </div>
    </div>

    <section class="section-intro" aria-labelledby="intro-heading">
        <div class="container">
            <div class="intro-content reveal">
                <h2 id="intro-heading">{svc_lower} in {c} &mdash; Built for Performance</h2>
{intro_p}            </div>
            <aside class="intro-aside reveal reveal-delay-2">
                <h3>{fmt(cfg["aside_title"], c, s)}</h3>
                <ul class="feature-list">
{aside_items_html}
                </ul>
            </aside>
        </div>
    </section>

    <div class="metrics-strip" aria-label="Agency performance metrics">
        <div class="container">
            <div class="metric-card reveal"><div class="metric-number">{roas}</div><div class="metric-label">Average ROAS Delivered</div></div>
            <div class="metric-card reveal reveal-delay-1"><div class="metric-number">{cfg["metric_cac"]}</div><div class="metric-label">Average CAC Reduction</div></div>
            <div class="metric-card reveal reveal-delay-2"><div class="metric-number">30d</div><div class="metric-label">To First Measurable Results</div></div>
        </div>
    </div>

    <section class="section-results" aria-label="Key results">
        <div class="results-grid">
            <div class="result-item reveal"><span class="result-num">{spend}</span><div class="result-label">in ad spend managed</div></div>
            <div class="result-item reveal reveal-d1"><span class="result-num p">{brands}</span><div class="result-label">brands scaled</div></div>
            <div class="result-item reveal reveal-d2"><span class="result-num c">{roas}</span><div class="result-label">average ROAS</div></div>
            <div class="result-item reveal reveal-d3"><span class="result-num">{c}</span><div class="result-label">Service Area</div></div>
        </div>
    </section>

    <section class="section-services" aria-labelledby="services-heading">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-label">What We Do</span>
                <h2 id="services-heading">{fmt(cfg["services_h2"], c, s)}</h2>
                <p class="subtitle">Every channel, every metric &mdash; optimized for revenue. No vanity metrics, no bloated retainers.</p>
            </div>
            <div class="services-grid">
                <div class="service-card"><div class="service-icon" aria-hidden="true">&#x1F50D;</div><h3>SEO</h3><p>Rank higher on Google and capture {c} customers actively searching for your services.</p><a href="https://aivopa.com/services/seo">Learn more &rarr;</a></div>
                <div class="service-card"><div class="service-icon" aria-hidden="true">&#x1F916;</div><h3>AI Automations</h3><p>Automate repetitive tasks and scale your {c} operations without hiring more staff.</p><a href="https://aivopa.com/services/ai-automations">Learn more &rarr;</a></div>
                <div class="service-card"><div class="service-icon" aria-hidden="true">&#x25B6;</div><h3>YouTube Ads</h3><p>Drive qualified leads from {c} with YouTube campaigns built around high-intent video creative.</p><a href="https://aivopa.com/services/youtube-ads">Learn more &rarr;</a></div>
                <div class="service-card"><div class="service-icon" aria-hidden="true">&#x1F4F1;</div><h3>Meta Ads</h3><p>Reach your ideal {c} audience on Facebook and Instagram with high-converting ads.</p><a href="https://aivopa.com/services/meta-ads">Learn more &rarr;</a></div>
                <div class="service-card"><div class="service-icon" aria-hidden="true">&#x1F310;</div><h3>Web Design</h3><p>Fast, conversion-focused websites that turn {c} visitors into paying customers.</p><a href="https://aivopa.com/services/web-design">Learn more &rarr;</a></div>
                <div class="service-card"><div class="service-icon" aria-hidden="true">&#x2709;&#xFE0F;</div><h3>Email Marketing</h3><p>Build relationships and drive repeat business from your {c} customer base.</p><a href="https://aivopa.com/services/email-marketing">Learn more &rarr;</a></div>
            </div>
        </div>
    </section>

    <section class="section-pricing" aria-labelledby="pricing-heading">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-label">Investment</span>
                <h2 id="pricing-heading">Flat-Fee Pricing for {c} Businesses</h2>
                <p class="subtitle">No percentage-of-spend fees. No hidden costs. Every retainer is tied to your ROAS targets &mdash; not our activity level.</p>
            </div>
            <div class="pricing-cards">
                <div class="price-card"><div class="price-name">Starter</div><div class="price-amount">${price_low}/mo</div><div class="price-period">per month</div><a href="https://aivopa.com/contact" class="price-cta">Get Started</a></div>
                <div class="price-card featured"><div class="price-name">Growth</div><div class="price-amount">${price_mid}/mo</div><div class="price-period">per month</div><a href="https://aivopa.com/contact" class="price-cta">Most Popular</a></div>
                <div class="price-card"><div class="price-name">Scale</div><div class="price-amount">${price_high}/mo</div><div class="price-period">per month</div><a href="https://aivopa.com/contact" class="price-cta">Let&rsquo;s Scale</a></div>
            </div>
            <div style="text-align:center;margin-top:32px;">
                <a href="https://aivopa.com/pricing" class="btn-outline" style="border-color:rgba(255,255,255,0.25);color:rgba(255,255,255,0.75);">Compare All Features &rarr;</a>
            </div>
        </div>
    </section>

    <section class="section-faq" aria-labelledby="faq-heading">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-label">FAQ</span>
                <h2 id="faq-heading">{svc_title} Questions Answered &mdash; {c}</h2>
                <p class="subtitle">Everything you need to know before working with a {platform} advertising agency in {c}.</p>
            </div>
            <div class="faq-list" role="list">
                <div class="faq-accordion">
{faq_items_html}                </div>
            </div>
        </div>
    </section>

    <section class="section-nearby" aria-labelledby="nearby-heading">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-label">Coverage</span>
                <h2 id="nearby-heading">{fmt(cfg["nearby_heading"], c, s)}</h2>
                <p class="subtitle">{fmt(cfg["nearby_sub"], c, s)}</p>
            </div>
            <div class="nearby-grid">
                <ul class="nearby-cities">
{nearby_html}
                </ul>
            </div>
        </div>
    </section>

    <section class="section-cta" aria-labelledby="cta-heading">
        <div class="container">
            <h2 id="cta-heading">{fmt(cfg["cta_heading"], c, s)}</h2>
            <p>{fmt(cfg["cta_sub"], c, s)}</p>
            <p style="font-size:0.9rem;color:rgba(255,255,255,0.55);margin-bottom:32px;">&#x1F4AC; Prefer to message? Fill the form below &mdash; we reply within a few hours.</p>
            <form id="bookingForm" action="/api/submit.php" method="POST" style="background:rgba(108,71,255,0.12);border:1px solid rgba(108,71,255,0.3);border-radius:16px;padding:32px;text-align:left;max-width:560px;margin:0 auto 28px;">
                <input type="hidden" name="subject" value="NEW LEAD &mdash; {svc_lower} in {c}">
                <input type="hidden" name="service" value="{svc_lower}">
                <input type="hidden" name="city" value="{c}">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
                    <div>
                        <label style="display:block;font-size:0.75rem;color:rgba(255,255,255,0.6);margin-bottom:5px;text-transform:uppercase;letter-spacing:0.06em;">Your Name *</label>
                        <input type="text" name="name" required placeholder="Jane Smith" style="width:100%;padding:11px 13px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);border-radius:8px;color:#fff;font-size:0.9rem;outline:none;box-sizing:border-box;">
                    </div>
                    <div>
                        <label style="display:block;font-size:0.75rem;color:rgba(255,255,255,0.6);margin-bottom:5px;text-transform:uppercase;letter-spacing:0.06em;">Email *</label>
                        <input type="email" name="email" required placeholder="jane@company.com" style="width:100%;padding:11px 13px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);border-radius:8px;color:#fff;font-size:0.9rem;outline:none;box-sizing:border-box;">
                    </div>
                </div>
                <div style="margin-bottom:14px;">
                    <label style="display:block;font-size:0.75rem;color:rgba(255,255,255,0.6);margin-bottom:5px;text-transform:uppercase;letter-spacing:0.06em;">Phone (optional)</label>
                    <input type="tel" name="phone" placeholder="(647) 370-1888" style="width:100%;padding:11px 13px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);border-radius:8px;color:#fff;font-size:0.9rem;outline:none;box-sizing:border-box;">
                </div>
                <div style="margin-bottom:22px;">
                    <label style="display:block;font-size:0.75rem;color:rgba(255,255,255,0.6);margin-bottom:5px;text-transform:uppercase;letter-spacing:0.06em;">Tell us about your business</label>
                    <textarea name="message" rows="3" placeholder="What ROAS are you targeting? Current challenges?" style="width:100%;padding:11px 13px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);border-radius:8px;color:#fff;font-size:0.9rem;outline:none;resize:vertical;font-family:inherit;box-sizing:border-box;"></textarea>
                </div>
                <button type="submit" class="btn-white" style="width:100%;justify-content:center;font-size:0.98rem;padding:15px 24px;border:none;cursor:pointer;">
                    Book Free Online Consultation &rarr;
                </button>
                <div id="formSuccess" style="display:none;margin-top:14px;padding:12px;background:rgba(46,213,115,0.12);border:1px solid rgba(46,213,115,0.3);border-radius:8px;color:#2ed573;text-align:center;font-size:0.92rem;">
                    &#x2705; Thank you! We&rsquo;ll be in touch within a few hours.
                </div>
            </form>
            <div class="cta-group">
                <a href="https://aivopa.com/pricing" class="btn-ghost-white">See Pricing</a>
                <a href="tel:+16473701888" class="btn-ghost-white" style="opacity:0.65;">&#x1F4DE; (647) 370-1888</a>
            </div>
        </div>
    </section>

    <footer class="footer" role="contentinfo">
      <div class="footer-inner">
        <div class="footer-top">
          <div class="footer-brand">
            <a href="../../../index.html" class="footer-logo" aria-label="Vora home">Vora<span>.</span></a>
            <p class="footer-tagline">{fmt(cfg["footer_tagline"], c, s)}</p>
            <div class="footer-socials">
              <a href="https://instagram.com/aivopa" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Vora on Instagram">&#9679;</a>
              <a href="https://linkedin.com/company/aivopa" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Vora on LinkedIn">in</a>
              <a href="https://twitter.com/aivopa" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Vora on X">&#120143;</a>
            </div>
          </div>
          <div class="footer-col">
            <h4>Services</h4>
            <ul>
              <li><a href="../../../services/google-ads.html">Google Ads</a></li>
              <li><a href="../../../services/meta-ads.html">Meta Ads</a></li>
              <li><a href="../../../services/ppc.html">PPC Management</a></li>
              <li><a href="../../../services/seo.html">SEO &amp; Content</a></li>
              <li><a href="../../../services/{svc_href}.html">{svc_label}</a></li>
              <li><a href="../../../services/web-design.html">Web Design</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Top Locations</h4>
            <ul>
              <li><a href="../../../local/new-york/{svc_slug}/index.html">{svc_label} New York</a></li>
              <li><a href="../../../local/chicago/{svc_slug}/index.html">{svc_label} Chicago</a></li>
              <li><a href="../../../local/los-angeles/{svc_slug}/index.html">{svc_label} Los Angeles</a></li>
              <li><a href="../../../local/miami/{svc_slug}/index.html">{svc_label} Miami</a></li>
              <li><a href="../../../local/houston/{svc_slug}/index.html">{svc_label} Houston</a></li>
              <li><a href="../../../local/new-york/google-ads-agency/index.html">Google Ads New York</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Company</h4>
            <ul>
              <li><a href="../../../about.html">About Us</a></li>
              <li><a href="../../../services.html">All Services</a></li>
              <li><a href="../../../pricing.html">Pricing</a></li>
              <li><a href="../../../contact.html">Contact</a></li>
            </ul>
            <h4 style="margin-top:24px">Contact</h4>
            <div class="footer-contact-item"><span class="fc-text"><a href="tel:+16473701888">(647) 370-1888</a></span></div>
            <div class="footer-contact-item"><span class="fc-text"><a href="mailto:hello@aivopa.com">hello@aivopa.com</a></span></div>
          </div>
        </div>
        <div class="footer-bottom">
          <span class="footer-copy">&copy; 2026 Vora. All rights reserved.</span>
          <div class="footer-bl">
            <a href="../../../contact.html">Privacy Policy</a>
            <a href="../../../contact.html">Terms of Service</a>
          </div>
        </div>
      </div>
    </footer>

    <script>
    (function () {{
        'use strict';
        var progressBar = document.getElementById('vora-scroll-progress');
        function updateProgress() {{
            var scrollTop = window.scrollY || document.documentElement.scrollTop;
            var docHeight = document.documentElement.scrollHeight - window.innerHeight;
            var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
            if (progressBar) progressBar.style.width = pct + '%';
        }}
        var nav = document.getElementById('site-nav');
        function updateNav() {{
            if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
        }}
        window.addEventListener('scroll', function () {{ updateProgress(); updateNav(); }}, {{ passive: true }});
        updateProgress(); updateNav();

        var toggle = document.getElementById('nav-toggle');
        var mobileMenu = document.getElementById('mobile-menu');
        if (toggle && mobileMenu) {{
            toggle.addEventListener('click', function () {{
                var open = mobileMenu.classList.toggle('open');
                toggle.setAttribute('aria-expanded', open);
                mobileMenu.setAttribute('aria-hidden', !open);
            }});
        }}

        var questions = document.querySelectorAll('.faq-question');
        questions.forEach(function (btn) {{
            btn.addEventListener('click', function () {{
                var answer = this.nextElementSibling;
                var isOpen = this.getAttribute('aria-expanded') === 'true';
                questions.forEach(function (q) {{
                    q.setAttribute('aria-expanded', 'false');
                    if (q.nextElementSibling) q.nextElementSibling.classList.remove('open');
                }});
                if (!isOpen) {{
                    this.setAttribute('aria-expanded', 'true');
                    if (answer) answer.classList.add('open');
                }}
            }});
        }});
        if (questions.length > 0) {{
            questions[0].setAttribute('aria-expanded', 'true');
            if (questions[0].nextElementSibling) questions[0].nextElementSibling.classList.add('open');
        }}

        if ('IntersectionObserver' in window) {{
            var revealObserver = new IntersectionObserver(function (entries) {{
                entries.forEach(function (entry) {{
                    if (entry.isIntersecting) {{ entry.target.classList.add('visible'); revealObserver.unobserve(entry.target); }}
                }});
            }}, {{ threshold: 0.12, rootMargin: '0px 0px -40px 0px' }});
            document.querySelectorAll('.reveal').forEach(function (el) {{ revealObserver.observe(el); }});
        }} else {{
            document.querySelectorAll('.reveal').forEach(function (el) {{ el.classList.add('visible'); }});
        }}
    }})();
    </script>
</body>
</html>'''
    return html


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
total = 0
for svc_key, svc_cfg in SERVICES.items():
    created = 0
    for city_slug, city_name, state, zipcode, street in ALL_22_CITIES:
        dest_dir = os.path.join(LOCAL, city_slug, svc_key)
        dest = os.path.join(dest_dir, 'index.html')
        if os.path.exists(dest):
            print(f'skip: {city_slug}/{svc_key}')
            continue
        os.makedirs(dest_dir, exist_ok=True)
        html = make_page(svc_cfg, city_slug, city_name, state, zipcode, street)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'created: {city_slug}/{svc_key}')
        created += 1
        total += 1
    print(f'  [{svc_key}] done: {created} pages\n')

print(f'Total created: {total}')
