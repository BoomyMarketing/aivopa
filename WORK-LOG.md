# Vora (aivopa.com) — Work Log

**Project:** SEO content expansion for Vora — NYC performance marketing agency  
**Site:** https://aivopa.com  
**Stack:** Static HTML on Vercel (cleanUrls: true, trailingSlash: false)  
**Last updated:** 2026-05-06

---

## Completed Work

### Infrastructure & Core Pages

| Item | Description | Commit |
|------|-------------|--------|
| Contact form | Switched to Resend HTTP API, per-recipient delivery to both leads inboxes | `76e005a` |
| Footer social icons | Constrained SVG icon size | `2bd10d7` |
| Trust pages | Privacy Policy, Terms, Cookie Policy + fixed schema streetAddress | `e761cbd` |

---

### Industry Vertical Pages — `/industries/{slug}`

59 SEO landing pages targeting low-frequency long-tail keywords ("X marketing agency New York"). Each page includes:
- Unique `<title>` + `<meta description>` + canonical
- Schema.org JSON-LD `@graph`: `Service` + `BreadcrumbList` + `FAQPage`
- 6 marketing channel cards specific to the industry
- 3 "Why Vora" differentiators specific to the industry
- 5 FAQ items with full answers
- Dark theme consistent with main site (Syne + Inter, `--ca:#d4ff00`)
- Non-blocking Google Fonts load
- Pure JS FAQ accordion

#### industries/index.html — Catalog page (`63dcdd2`)
Full directory of all industry verticals. Schema: `BreadcrumbList` + `ItemList`. Priority 0.9 in sitemap.

#### Batch 4 (`a8dff89`) — 5 pages
`saas` · `healthcare` · `real-estate` · `fintech` · `beauty`

#### Batches 5–6 — 10 pages
`ecommerce` · `restaurants` · `fashion` · `legal` · `home-services`  
`automotive` · `education` · `dental` · `fitness` · `nonprofit`

#### Batch 7 (`2b23a7e`) — 5 pages
`insurance` · `travel` · `construction` · `food-beverage` · `luxury`

#### Batch 8 (`4bceff9`) — 5 pages
`pet` · `wedding` · `tech-startups` · `accounting` · `staffing`

#### Batch 9 (`6d4fbaa`) — 5 pages
`mental-health` · `moving` · `cleaning` · `solar` · `senior-care`

#### Batch 10 (`dc615a4`) — 4 pages
`roofing` · `plumbing` · `childcare` · `interior-design`

#### Batch 11 (`011ccad`) — 5 pages
`event-planning` · `mortgage` · `spa` · `photography` · `landscaping`

#### Batch 12 (`c429955`) — 5 pages
`tutoring` · `veterinary` · `electrician` · `plastic-surgery` · `catering`

#### Batch 13 (`5834200`) — 5 pages
`chiropractic` · `yoga-studio` · `pest-control` · `hvac` · `florist`

#### Batch 14 (`5f760c1`) — 5 pages
`physical-therapy` · `nail-salon` · `painting` · `locksmith` · `urgent-care`

#### Batch 15 (`025c8c1`) — 5 pages
`barbershop` · `personal-trainer` · `junk-removal` · `remodeling` · `optometry`

#### Batch 16 — 5 pages
`car-detailing` · `dog-grooming` · `massage-therapy` · `window-cleaning` · `tattoo-studio`

#### Batch 17 (`eb50f46`) — 5 pages
`pressure-washing` · `garage-door` · `tree-service` · `acupuncture` · `financial-advisor`

#### Batch 18 (`a9952f1`) — 5 pages
`appliance-repair` · `fence-installation` · `dumpster-rental` · `carpet-cleaning` · `security-systems`

---

### SEO Optimization — All 74 Pages (2026-05-06)

Applied to every industry page:

1. **6th FAQ added** — "What other industries does Vora serve in New York?" with cross-links to 3 related industries + `/industries` index
2. **"Related Industries" section added** — 5 internal link cards to related verticals + link to `/industries` index
3. **`industries/index.html` updated** — counter and meta updated to 74 verticals; all new slugs added as cards

Two legacy page formats were updated:
- **Old format (47 pages, `.cta-band`)** — inline CSS grid, `div`-based FAQ items
- **New format (27 pages, `.cta-section`)** — `.ch-card` / `.channels-grid` classes, `button`-based FAQ items

---

### Industry Vertical Pages — Batch 19 (local only, not yet deployed)

#### Batch 19 — 5 pages
`flooring` · `med-spa` · `property-management` · `handyman` · `pool-service`

#### Batch 20 — 5 pages
`video-production` · `it-support` · `dermatology` · `auto-glass` · `storage`

> **Note:** Batches 19–20 exist locally only. Pages reference "84 industries" in cross-link FAQs and related sections.

---

### Sitemap (`sitemap.xml`)

All 74 deployed industry pages added with:
- `<changefreq>monthly</changefreq>`
- `<priority>0.8</priority>`
- `<lastmod>2026-05-06</lastmod>`

`/industries` catalog page at priority 0.9.

> Batches 19–20 (10 pages) not yet added to sitemap — add when deploying.

---

## Full List of Industry Pages (84 total locally / 74 deployed)

| # | Slug | Target keyword |
|---|------|----------------|
| 1 | saas | saas marketing agency new york |
| 2 | healthcare | healthcare marketing agency new york |
| 3 | real-estate | real estate marketing agency new york |
| 4 | fintech | fintech marketing agency new york |
| 5 | beauty | beauty marketing agency new york |
| 6 | ecommerce | ecommerce marketing agency new york |
| 7 | restaurants | restaurant marketing agency new york |
| 8 | fashion | fashion marketing agency new york |
| 9 | legal | legal marketing agency new york |
| 10 | home-services | home services marketing agency new york |
| 11 | automotive | automotive marketing agency new york |
| 12 | education | education marketing agency new york |
| 13 | dental | dental marketing agency new york |
| 14 | fitness | fitness marketing agency new york |
| 15 | nonprofit | nonprofit marketing agency new york |
| 16 | insurance | insurance marketing agency new york |
| 17 | travel | travel marketing agency new york |
| 18 | construction | construction marketing agency new york |
| 19 | food-beverage | food and beverage marketing agency new york |
| 20 | luxury | luxury marketing agency new york |
| 21 | pet | pet business marketing agency new york |
| 22 | wedding | wedding marketing agency new york |
| 23 | tech-startups | tech startup marketing agency new york |
| 24 | accounting | accounting marketing agency new york |
| 25 | staffing | staffing agency marketing new york |
| 26 | mental-health | mental health marketing agency new york |
| 27 | moving | moving company marketing agency new york |
| 28 | cleaning | cleaning company marketing agency new york |
| 29 | solar | solar marketing agency new york |
| 30 | senior-care | senior care marketing agency new york |
| 31 | roofing | roofing marketing agency new york |
| 32 | plumbing | plumbing marketing agency new york |
| 33 | childcare | childcare marketing agency new york |
| 34 | interior-design | interior design marketing agency new york |
| 35 | event-planning | event planning marketing agency new york |
| 36 | mortgage | mortgage broker marketing agency new york |
| 37 | spa | spa & med spa marketing agency new york |
| 38 | photography | photography marketing agency new york |
| 39 | landscaping | landscaping marketing agency new york |
| 40 | tutoring | tutoring marketing agency new york |
| 41 | veterinary | veterinary marketing agency new york |
| 42 | electrician | electrician marketing agency new york |
| 43 | plastic-surgery | plastic surgery marketing agency new york |
| 44 | catering | catering marketing agency new york |
| 45 | chiropractic | chiropractic marketing agency new york |
| 46 | yoga-studio | yoga studio marketing agency new york |
| 47 | pest-control | pest control marketing agency new york |
| 48 | hvac | hvac marketing agency new york |
| 49 | florist | florist marketing agency new york |
| 50 | physical-therapy | physical therapy marketing agency new york |
| 51 | nail-salon | nail salon marketing agency new york |
| 52 | painting | painting contractor marketing agency new york |
| 53 | locksmith | locksmith marketing agency new york |
| 54 | urgent-care | urgent care marketing agency new york |
| 55 | barbershop | barbershop marketing agency new york |
| 56 | personal-trainer | personal trainer marketing agency new york |
| 57 | junk-removal | junk removal marketing agency new york |
| 58 | remodeling | home remodeling marketing agency new york |
| 59 | optometry | optometry marketing agency new york |
| 60 | car-detailing | car detailing marketing agency new york |
| 61 | dog-grooming | dog grooming marketing agency new york |
| 62 | massage-therapy | massage therapy marketing agency new york |
| 63 | window-cleaning | window cleaning marketing agency new york |
| 64 | tattoo-studio | tattoo studio marketing agency new york |
| 65 | pressure-washing | pressure washing marketing agency new york |
| 66 | garage-door | garage door marketing agency new york |
| 67 | tree-service | tree service marketing agency new york |
| 68 | acupuncture | acupuncture marketing agency new york |
| 69 | financial-advisor | financial advisor marketing agency new york |
| 70 | appliance-repair | appliance repair marketing agency new york |
| 71 | fence-installation | fence installation marketing agency new york |
| 72 | dumpster-rental | dumpster rental marketing agency new york |
| 73 | carpet-cleaning | carpet cleaning marketing agency new york |
| 74 | security-systems | security systems marketing agency new york |
| 75 | flooring | flooring marketing agency new york |
| 76 | med-spa | med-spa marketing agency new york |
| 77 | property-management | property management marketing agency new york |
| 78 | handyman | handyman marketing agency new york |
| 79 | pool-service | pool service marketing agency new york |
| 80 | video-production | video production marketing agency new york |
| 81 | it-support | it support marketing agency new york |
| 82 | dermatology | dermatology marketing agency new york |
| 83 | auto-glass | auto glass marketing agency new york |
| 84 | storage | self-storage marketing agency new york |

> **Rows 75–84** — local only, not yet deployed to production.

---

## Pending / Next Steps

### Immediate (when ready to deploy)
- Deploy batches 19–20 (10 pages: rows 75–84 above)
- Add 10 new sitemap entries before `<!-- Published Local Pages -->`, `lastmod: 2026-05-06`
- Update `industries/index.html` — counter from 74 → 84, add 10 new cards

### Batch 21+ — More industry verticals
Candidates (not yet built): `commercial-cleaning`, `nutrition-coaching`, `life-coach`, `event-venue`, `pool-installation`, `tile-installation`, `siding`, `gutters`, `drywall`, `foundation-repair`

### City pages — 66 pages (not yet started)
Pattern: `/local/{city}/{service}` — 22 cities × 3 new service slugs:
- `tiktok-ads-agency`
- `youtube-ads-agency`
- `amazon-ads-agency`

Cities (same 22 as existing local pages):
albuquerque · arlington · atlanta · austin · bakersfield · boston · charlotte · chicago · cincinnati · cleveland · dallas · denver · houston · los-angeles · miami · nashville · new-york · phoenix · portland · san-diego · san-francisco · seattle

---

## Technical Notes

- All pages: dark theme (`--c0:#0a0a0a`, `--ca:#d4ff00`, `--ct:#fff`, `--cs:#a3a3a3`)
- Fonts: Syne 700/800 (headings) + Inter (body) — loaded non-blocking
- Schema: JSON-LD `@graph` with Service + BreadcrumbList + FAQPage on every page
- Internal links: all use `../` relative prefix (e.g. `../` for home, `../industries` for catalog)
- Sitemap entries inserted before `<!-- Published Local Pages -->` comment
- CRLF warnings on Windows git commits are cosmetic, do not affect deployment
