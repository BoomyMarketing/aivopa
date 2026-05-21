# SEO Audit Report — Vora (aivopa.com)
**Date:** 2026-05-22
**Pages audited:** 387 HTML files (10 root, 29 services, 105 industries, 243 local)
**Audit type:** Full site — local files (pre-deploy)

---

## Overall SEO Health Score: 56 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Content Quality (E-E-A-T) | 23% | 41/100 | 9.4 |
| Technical SEO | 22% | 61/100 | 13.4 |
| On-Page SEO | 20% | 72/100 | 14.4 |
| Schema / Structured Data | 10% | 54/100 | 5.4 |
| Performance (CWV) | 10% | ~55/100 | 5.5 |
| AI Search Readiness (GEO) | 10% | 61/100 | 6.1 |
| Images | 5% | ~45/100 | 2.25 |
| **TOTAL** | **100%** | | **56/100** |

**Local SEO (supplemental):** 31/100

---

## Top 5 Critical Issues

1. **robots.txt blocks 44 published pages** — YouTube Ads + Amazon Ads local pages are in sitemap but blocked by `Disallow: /local/` (no Allow rules for these service types)
2. **243 local pages are near-duplicate city-swap templates** — Doorway page risk, production errors (duplicate bullets, SEO language on Google Ads pages), hidden dates
3. **`MarketingAgency` is not a valid Schema.org type** — Used on all 387 pages; Google ignores it; correct type is `AdvertisingAgency`
4. **Canadian phone number (+1-647) on a New York business** — Hard NAP trust failure across all local signals and citation aggregators
5. **No Google Business Profile signals** — GBP is the #1 local ranking factor; zero GBP embeds, links, or review schema anywhere

## Top 5 Quick Wins

1. Fix robots.txt — add Allow rules for youtube-ads-agency and amazon-ads-agency (30 min)
2. Replace `MarketingAgency` → `AdvertisingAgency` in all JSON-LD (1 script, 30 min)
3. Fix OG image — create og-image.jpg (Facebook/LinkedIn don't render SVG)
4. Fix render-blocking Google Fonts on 181 local pages (1 script, 1 hr)
5. Replace Canadian phone with a US number sitewide (1 hr)

---

## 1. Technical SEO — 61/100

### Critical
- **robots.txt blocks 44 published pages**: All 22 youtube-ads-agency + 22 amazon-ads-agency local pages are in sitemap with `index, follow` but blocked by `Disallow: /local/`. 17/22 TikTok cities also blocked.
- **OG image in SVG format**: `og:image` points to `og-image.svg` — Facebook, LinkedIn, Slack do not render SVG social cards.

### High Priority
- **Render-blocking Google Fonts on 181+ local pages**: Homepage uses the correct non-blocking pattern. Local pages use plain `<link rel="stylesheet">` — direct LCP/FCP impact.
- **No nav links to /industries/ or /local/ hubs**: Main nav only links to Services, About, Pricing, Contact. Zero PageRank flows to 348 pages (104 industries + 243 local).
- **Missing security headers**: vercel.json has only 3 basic headers. Missing: `Content-Security-Policy`, `Strict-Transport-Security`, `Permissions-Policy`.

### Medium Priority
- Sitemap count: 385 entries vs 387 HTML files (2-page gap)
- GSAP loaded from CDN without `integrity` SRI attribute
- Meta descriptions truncated mid-sentence in HTML source on local pages

### Passed
- Canonical tags correct on all sampled pages (HTTPS, no trailing slash, self-referencing)
- `cleanUrls: true`, `trailingSlash: false` in vercel.json matches canonical format
- Google Fonts non-blocking on homepage
- All AI crawlers explicitly allowed (GPTBot, ClaudeBot, Google-Extended, PerplexityBot, anthropic-ai)
- Static asset caching: `Cache-Control: public, max-age=31536000, immutable`
- GSAP deferred (not render-blocking)

---

## 2. Content Quality / E-E-A-T — 41/100

### Critical
- **243 local pages are city-swap templates** — Identical body copy, only city name replaced. Production errors visible: duplicate sidebar bullets, SEO terminology in Google Ads FAQ answers ("domain authority", "keyword rankings"), same stats bar on every service type. Google's Helpful Content system targets this pattern.
- **No verifiable author attribution** — `<meta name="author" content="Vora Ads Team">` only. Team bios use first-name-last-initial (Alex V., Chris D.) with no LinkedIn profiles.
- **Self-reported unverified statistics** — "$100M+ ad spend", "300+ brands", "4.2x ROAS", "38% CPC reduction" on all pages with no third-party verification. Inconsistent values (42% CAC on local pages vs 38% CPC on main site).

### High Priority
- **Unverifiable trust claims** — "Google Premier Partner-certified" stated with no badge or verification link
- **Anonymous testimonials with extraordinary ROAS claims** — No company names, no review platform links (Jake R. 11.4x, Sarah M. 7.6x)
- **Canadian phone (+647) for a New York agency** — 350 Fifth Avenue address + Toronto phone = credibility problem
- **No blog, case studies, or freshness signals** on a site in a rapidly-changing paid media category

### Medium Priority
- `services.html` ~400 words for a hub page with 14+ services
- Broken internal link: `href="/vora/contact.html"` on services page CTA
- `<time>` dates hidden with `display:none`

### Strengths
- Healthcare industry page demonstrates genuine technical expertise (HIPAA CAPI, CPL benchmarks, BAA documentation)
- Homepage FAQ high-quality with specific numerical claims and `faq-citation` block
- Public pricing ($1,500/$4,000/$8,000/mo) is a transparency signal
- Privacy Policy, Terms, Cookie Policy consistently linked in all footers

**E-E-A-T:** Experience 28/50 · Expertise 60/100 · Authoritativeness 25/100 · Trustworthiness 55/100

---

## 3. On-Page SEO — 72/100

### Critical
- **Meta descriptions truncated mid-word in HTML source** — e.g., `"Get your free strate..."`. Google rewrites, losing keyword control.
- **Industry page titles exceed 60 chars** — Accounting (80), Automotive (80), Beauty (84) — truncated in SERPs.

### High Priority
- **Local pages: templated H1s** with only city name swapped across 22 cities × 11 services
- **Title-case errors** — "Ppc Agency" instead of "PPC Agency" in titles and hero badges

### Medium Priority
- Pricing page title only 44 chars (short)
- Service pages missing `serviceType` in Service schema

### Strengths
- Homepage: title 61 chars, meta 157 chars, H1 strong, OG complete — Grade A
- About: 50 chars, 140 chars meta — Grade A
- Canonical tags, viewport meta, robots meta correct on all pages

| Page Type | Title | Meta | Grade |
|---|---|---|---|
| Homepage | 61 chars | 157 chars | A |
| About | 50 chars | 140 chars | A |
| Pricing | 44 chars | 156 chars | B+ |
| Services | 49-51 chars | 158 chars | B |
| Industries | 80+ chars | good | C+ |
| Local | 51-69 chars | truncated | D+ |

---

## 4. Schema / Structured Data — 54/100

### Validation Errors (Critical)
- **`MarketingAgency` invalid type** on all 387 pages — replace with `AdvertisingAgency`
- **`servedArea` typo** on all 243 local pages — should be `areaServed`
- **`datePublished` on `LocalBusiness` node** — wrong entity type (belongs on WebPage/Article)
- **Breadcrumb `item` URLs point to non-existent paths** — `/services/google-ads-agency` should be `/services/google-ads.html`
- **Homepage `@graph` missing `@id` cross-references** between entity nodes

### Missing Required Fields (High)
- Local pages missing `geo` coordinates
- Local pages missing `openingHoursSpecification`
- Service pages `provider` should reference org by `@id` not inline object
- `Service` type missing `serviceType` property

### Enhancement Opportunities (Medium)
- No `AggregateRating` or `Review` schema anywhere (3 testimonials on homepage, none marked up)
- No `Person` schema for team members
- `ImageObject` missing `width`, `height`, `license`
- `openingHoursSpecification` should be array not object

### Strengths
- `@context: "https://schema.org"` (HTTPS) on all pages
- `@graph` pattern correctly used on homepage/service/industry pages
- `PostalAddress` complete (all 5 required fields)
- `BreadcrumbList` present on all page types
- `hasOfferCatalog` with pricing tiers on local pages
- Homepage FAQ: strong, specific, citation-ready content

---

## 5. GEO / AI Search Readiness — 61/100

### Critical
- **`llms-full.txt` missing** — highest-value file for AI citation pipelines; AI systems must parse noisy HTML without it
- **No Wikipedia/Wikidata entity** — "Vora" is a generic word with no trusted third-party anchor; AI may omit or misattribute
- **robots.txt wildcard Disallow affects unlisted AI crawlers** — Known bots have named stanzas but `User-agent: *` blocks `/local/` for any new/unknown crawler

### High Priority
- No `<link rel="ai-content-description" href="/llms.txt">` in `<head>`
- `llms.txt` covers only 14 URLs — 366 service/industry/local pages invisible to AI manifest parsers
- Statistics lack date attribution (only one "2023-2025" instance)
- Testimonials unverifiable — AI systems discount anonymous extraordinary claims

### Medium Priority
- FAQ in `<details>` elements — may not expand in static HTML parsers
- No author bylines
- Brand/domain mismatch: "Vora" vs "aivopa.com"
- No YouTube channel (0.737 citation correlation — strongest missing signal)

### Strengths
- `llms.txt` exists, well-structured with pricing, team, stats, "For AI Systems" section
- Static HTML — full SSR, no JS gating — AI crawlers get complete content on first request
- All 5 major AI crawlers explicitly allowed in robots.txt
- `FAQPage` JSON-LD provides clean extractable passages without HTML noise
- Public pricing surfaces in AI "how much does X cost" queries
- Google Ads service page has specific citable thresholds ("300-500 negatives", "50 conversions/30 days")

---

## 6. Local SEO — 31/100

### Critical
- **No Google Business Profile signals** — GBP is the #1 local ranking factor (Whitespark 2026); zero embeds, links, or review schema
- **NYC address on all non-NYC local pages** — `addressLocality: "New York"` in schema on Chicago, LA, Miami, etc. pages — Google anchors to NYC, suppresses other city rankings
- **Canadian phone number (+1-647)** — Toronto area code for NY business, fails citation aggregator NAP validation
- **Doorway page risk** — 243 near-identical city-swap pages with production errors

### High Priority
- No `AggregateRating` anywhere — no star ratings in SERPs
- Local page schema `@id` not linked to canonical org entity
- Breadcrumb hrefs broken on all 243 pages
- Meta descriptions truncated

### Medium Priority
- `servedArea` typo (→ `areaServed`)
- `geo` coordinates missing on local pages
- Duplicate sidebar bullets (template bug)
- No city-specific testimonials or local market data

### Strengths
- Consistent "Vora" brand name, address text, and email across all pages
- `BreadcrumbList` schema on all local pages
- `FAQPage` with city-specific Q&A on every local page
- `hasOfferCatalog` with 3 pricing tiers on all local pages
- `canonical` + `robots: index, follow` on all pages
