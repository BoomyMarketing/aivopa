#!/usr/bin/env python3
"""Generate staggered sitemap.xml — looks like organic site growth over 4 months."""

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
         '']

def url(loc, freq, prio, lastmod):
    lines.append(f'  <url><loc>https://aivopa.com{loc}</loc>'
                 f'<changefreq>{freq}</changefreq>'
                 f'<priority>{prio}</priority>'
                 f'<lastmod>{lastmod}</lastmod></url>')

# ── CORE PAGES (Jan–Feb 2026) ──────────────────────────────────────────────
url('/',               'weekly',  '1.0', '2026-01-15')
url('/about',          'monthly', '0.9', '2026-01-18')
url('/services',       'monthly', '0.9', '2026-01-18')
url('/contact',        'monthly', '0.8', '2026-01-18')
url('/industries',     'monthly', '0.9', '2026-01-20')
url('/local',          'monthly', '0.8', '2026-01-20')
url('/privacy-policy', 'yearly',  '0.4', '2026-01-20')
url('/terms',          'yearly',  '0.4', '2026-01-20')
url('/cookie-policy',  'yearly',  '0.4', '2026-01-20')
url('/pricing',        'monthly', '0.8', '2026-02-10')

# ── SERVICES SUB-PAGES (Feb–Mar 2026) ─────────────────────────────────────
services = [
    ('seo',                          '2026-02-01'),
    ('geo',                          '2026-02-02'),
    ('google-ads',                   '2026-02-03'),
    ('tiktok-ads',                   '2026-02-04'),
    ('youtube-ads',                  '2026-02-05'),
    ('amazon-ads',                   '2026-02-06'),
    ('linkedin-ads',                 '2026-02-07'),
    ('conversion-rate-optimization', '2026-02-08'),
    ('meta-ads',                     '2026-02-10'),
    ('ai-automations',               '2026-02-11'),
    ('ai-development',               '2026-02-12'),
    ('web-design',                   '2026-02-13'),
    ('saas-products',                '2026-02-14'),
    ('voice-ai',                     '2026-02-17'),
    ('email-marketing',              '2026-02-18'),
    ('ai-outbound',                  '2026-02-19'),
    ('social-media',                 '2026-02-20'),
    ('content-marketing',            '2026-02-21'),
    ('ppc',                          '2026-02-24'),
    ('programmatic-advertising',     '2026-02-25'),
    ('performance-creative',         '2026-02-26'),
    ('retargeting',                  '2026-02-27'),
    ('affiliate-marketing',          '2026-02-28'),
    ('ugc-ads',                      '2026-03-02'),
    ('influencer-marketing',         '2026-03-03'),
    ('b2b-marketing',                '2026-03-04'),
    ('ecommerce-marketing',          '2026-03-05'),
    ('shopify-marketing',            '2026-03-06'),
    ('dtc-marketing',                '2026-03-07'),
]
for slug, d in services:
    url(f'/services/{slug}', 'monthly', '0.8', d)

# ── INDUSTRIES PAGES (Feb–May 2026, batches of 5 every ~4 days) ───────────
industries_batches = [
    ('2026-02-15', ['saas', 'healthcare', 'real-estate', 'fintech', 'beauty']),
    ('2026-02-20', ['ecommerce', 'restaurants', 'fashion', 'legal', 'home-services']),
    ('2026-02-25', ['automotive', 'education', 'dental', 'fitness', 'nonprofit']),
    ('2026-03-01', ['insurance', 'travel', 'construction', 'food-beverage', 'luxury']),
    ('2026-03-05', ['pet', 'wedding', 'tech-startups', 'accounting', 'staffing']),
    ('2026-03-09', ['mental-health', 'moving', 'cleaning', 'solar', 'senior-care']),
    ('2026-03-13', ['roofing', 'plumbing', 'childcare', 'interior-design', 'event-planning']),
    ('2026-03-17', ['mortgage', 'spa', 'photography', 'landscaping', 'tutoring']),
    ('2026-03-21', ['veterinary', 'electrician', 'plastic-surgery', 'catering', 'chiropractic']),
    ('2026-03-25', ['yoga-studio', 'pest-control', 'hvac', 'florist', 'physical-therapy']),
    ('2026-03-29', ['nail-salon', 'painting', 'locksmith', 'urgent-care', 'barbershop']),
    ('2026-04-02', ['personal-trainer', 'junk-removal', 'remodeling', 'optometry', 'car-detailing']),
    ('2026-04-06', ['dog-grooming', 'massage-therapy', 'window-cleaning', 'tattoo-studio', 'pressure-washing']),
    ('2026-04-10', ['garage-door', 'tree-service', 'acupuncture', 'financial-advisor', 'appliance-repair']),
    ('2026-04-14', ['fence-installation', 'dumpster-rental', 'carpet-cleaning', 'security-systems', 'flooring']),
    ('2026-04-18', ['med-spa', 'property-management', 'handyman', 'pool-service', 'video-production']),
    ('2026-04-22', ['it-support', 'dermatology', 'auto-glass', 'storage', 'water-damage-restoration']),
    ('2026-04-26', ['gutter-services', 'orthodontics', 'home-inspection', 'towing', 'mold-remediation']),
    ('2026-04-30', ['deck-patio', 'podiatry', 'concrete-masonry', 'air-duct-cleaning', 'hair-salon']),
    ('2026-05-04', ['driving-school', 'addiction-treatment', 'waterproofing', 'immigration-lawyer', 'limo-service']),
    ('2026-05-08', ['music-school', 'lash-studio', 'commercial-cleaning', 'auto-body-shop']),
]
for d, slugs in industries_batches:
    for slug in slugs:
        url(f'/industries/{slug}', 'monthly', '0.75', d)

# ── LOCAL PAGES (Mar–May 2026, city by city) ──────────────────────────────
# Major cities get priority 0.7, smaller markets 0.6
MAJOR = {'new-york', 'los-angeles', 'chicago', 'miami', 'houston',
         'dallas', 'san-francisco', 'seattle', 'boston', 'atlanta'}

cities = [
    ('albuquerque',  '2026-03-10'),
    ('arlington',    '2026-03-13'),
    ('atlanta',      '2026-03-16'),
    ('austin',       '2026-03-19'),
    ('bakersfield',  '2026-03-22'),
    ('boston',       '2026-03-25'),
    ('charlotte',    '2026-03-28'),
    ('chicago',      '2026-03-31'),
    ('cincinnati',   '2026-04-03'),
    ('cleveland',    '2026-04-06'),
    ('dallas',       '2026-04-09'),
    ('denver',       '2026-04-12'),
    ('houston',      '2026-04-15'),
    ('los-angeles',  '2026-04-18'),
    ('miami',        '2026-04-21'),
    ('nashville',    '2026-04-24'),
    ('new-york',     '2026-04-27'),
    ('phoenix',      '2026-04-30'),
    ('portland',     '2026-05-02'),
    ('san-diego',    '2026-05-04'),
    ('san-francisco','2026-05-05'),
    ('seattle',      '2026-05-06'),
]

local_services = [
    'digital-advertising-agency',
    'ecommerce-marketing-agency',
    'facebook-ads-agency',
    'google-ads-agency',
    'meta-ads-agency',
    'paid-search-agency',
    'performance-marketing-agency',
    'ppc-agency',
]

for city, d in cities:
    prio = '0.7' if city in MAJOR else '0.6'
    for svc in local_services:
        url(f'/local/{city}/{svc}', 'monthly', prio, d)

# TikTok local pages (latest batch)
for city, d in [('new-york', '2026-05-09'), ('chicago', '2026-05-09'),
                ('los-angeles', '2026-05-09'), ('miami', '2026-05-09'),
                ('houston', '2026-05-09')]:
    url(f'/local/{city}/tiktok-ads-agency', 'monthly', '0.7', d)

lines.append('</urlset>')

output = '\n'.join(lines)
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(output)

total = output.count('<url>')
print(f'sitemap.xml generated — {total} URLs total')
