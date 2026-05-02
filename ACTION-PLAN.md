# SEO Action Plan — Vora (aivopa.com)
**Складений:** 2026-04-26 | **На основі:** Full SEO Audit (8 агентів)
**Поточний score:** 52/100 | **Ціль:** 80+/100

---

## ФАЗА 0 — Термінові виправлення (сьогодні, до 2 годин)

### 0.1 Виправити broken CTA на about.html
**Файл:** `about.html`, рядок 368
```html
<!-- ЗАРАЗ (404 в production) -->
<a href="/vora/contact.html" class="btn-primary">

<!-- ВИПРАВЛЕННЯ -->
<a href="contact.html" class="btn-primary">
```

### 0.2 Виправити streetAddress на contact.html
**Файл:** `contact.html` — знайти в JSON-LD schema
```json
// ЗАРАЗ
"streetAddress": "New York"

// ВИПРАВЛЕННЯ
"streetAddress": "350 Fifth Avenue"
// + додати "postalCode": "10118"
```

### 0.3 Видалити фальшивий AggregateRating з шаблону local pages
**Файли:** Всі 176 `/local/{city}/{service}/index.html`

Знайти та видалити блок:
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.9",
  "reviewCount": "127"
}
```

### 0.4 Виправити cross-city contamination
**Файли:** Всі non-NY local pages

Замінити hardcoded:
> "Vora serves businesses throughout the entire **New York, NY** area"

На динамічний варіант з правильним містом. Перевірити всі FAQ відповіді на наявність "New York" у non-NY сторінках.

### 0.5 Додати OAI-SearchBot та Applebot-Extended до robots.txt
**Файл:** `robots.txt` — після `anthropic-ai` блоку:
```
User-agent: OAI-SearchBot
Allow: /

User-agent: Applebot-Extended
Allow: /
```

---

## ФАЗА 1 — Технічна оптимізація (тиждень 1)

### 1.1 Виправити GSAP render-blocking — LCP Priority
**Файли:** `index.html`, `about.html`, всі service pages

```html
<!-- Додати defer до обох тегів -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
```
**Очікуваний ефект:** LCP -0.6...-1.2s → переходить у "Good"

### 1.2 Non-blocking Google Fonts
**Файли:** `index.html`, `about.html`, всі HTML

Замінити:
```html
<link href="https://fonts.googleapis.com/css2?..." rel="stylesheet" />
```
На:
```html
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;900&display=swap" as="style" />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;900&display=swap" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;900&display=swap" /></noscript>
```

### 1.3 Preload LCP font (Berkshire Swash)
**Файли:** `index.html`, `about.html` — після preconnect тегів:
```html
<link rel="preload"
      href="https://fonts.gstatic.com/s/berkshireswash/v19/ptRRTi-cavZOGqCvnNJDl5m5XmNPrcQybX4pQA.woff2"
      as="font" type="font/woff2" crossorigin>
```
**Очікуваний ефект:** LCP -0.3...-0.6s

### 1.4 Cache-Control для статичних assets
**Файл:** `vercel.json`
```json
{
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/(.*\\.(png|jpg|jpeg|webp|avif|svg|ico|woff2|woff|ttf))",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
```

### 1.5 Виправити logo.png (404)

Або додати файл `logo.png` у корінь, або оновити schema URL на існуючий логотип.

### 1.6 BreadcrumbList URL clean-up
**Файли:** `about.html`, `contact.html`, `services.html`, service pages

Замінити у всіх BreadcrumbList items:
- `about.html` → `about`
- `contact.html` → `contact`
- `services.html` → `services`
- `services/google-ads.html` → `services/google-ads`
- тощо

### 1.7 Виправити about.html lang attribute
```html
<!-- ЗАРАЗ -->
<html lang="en">
<!-- ВИПРАВЛЕННЯ -->
<html lang="en-US">
```

---

## ФАЗА 2 — Schema cleanup (тиждень 2)

### 2.1 Оновити homepage schema (index.html)

Замінити поточний Organization schema block на виправлений (повний шаблон у FULL-AUDIT-REPORT.md, Розділ 4, Fix 1):
- Виправити geo координати (40.7484 / -73.9967 замість 40.7128 / -74.0060)
- Видалити SearchAction (немає пошуку на сайті)
- Додати `@id` для entity linking
- Додати openingHoursSpecification
- Додати sameAs для YouTube (як тільки буде канал)

### 2.2 Оновити шаблон local pages schema

Для всіх 176 local pages застосувати виправлений шаблон:
- Виправити `price` format: `"$1,500/mo"` → `"1500"`
- Виправити порожній `geo`: додати реальні координати або видалити
- Виправити `url`: вказувати на `https://aivopa.com` (не на локальну URL)
- Видалити `aggregateRating` (вже зроблено у Фазі 0)
- Додати повну адресу: streetAddress, postalCode, addressRegion
- Стандартизувати телефон на E.164: `+16473701888`
- Виправити майбутню дату: `"2026-05-01"` → поточна дата

### 2.3 Виправити contact.html schema

Повний шаблон у FULL-AUDIT-REPORT.md, Розділ 4, Fix 2.

### 2.4 Виправити about.html schema

Повний шаблон у FULL-AUDIT-REPORT.md, Розділ 4, Fix 4.
- Додати streetAddress, postalCode
- Додати telephone
- Розглянути Person schema з LinkedIn sameAs для команди

---

## ФАЗА 3 — On-Page SEO (тиждень 3)

### 3.1 Реструктурувати H1 на homepage

```html
<!-- ЗАРАЗ -->
<span class="hero__label">New York's Performance Marketing Agency</span>
<h1 class="hero__title">Maximize ROAS. Minimize CAC.</h1>

<!-- ВИПРАВЛЕННЯ (візуально ідентично, семантично правильно) -->
<h1 class="hero__title">New York Performance Marketing Agency</h1>
<p class="hero__tagline">Maximize ROAS. Minimize CAC.</p>
```

### 3.2 Виправити title tag

```html
<!-- ЗАРАЗ -->
<title>Vora | New York's #1 Performance Marketing Agency</title>

<!-- ВИПРАВЛЕННЯ -->
<title>Vora | New York Performance Marketing Agency — ROAS-Focused</title>
```

### 3.3 Service cards — `<div>` → `<h3>`

```html
<!-- ЗАРАЗ -->
<div class="service-card__title">Google Ads</div>

<!-- ВИПРАВЛЕННЯ -->
<h3 class="service-card__title">Google Ads</h3>
```

### 3.4 Stats marquee — зробити доступним

```html
<!-- ЗАРАЗ -->
<div class="marquee-band" aria-hidden="true" role="presentation">

<!-- ВИПРАВЛЕННЯ -->
<div class="marquee-band" role="region" aria-label="Key performance statistics">
```

### 3.5 Узгодити всі метрики

Обрати один авторитетний набір статистик і застосувати на ВСІХ сторінках:

| Метрика | Рекомендація | Логіка |
|---|---|---|
| Average ROAS | **4.2x** (about.html) | Більш консервативна, більш довірена |
| Ad Spend Managed | **$100M+** (about.html) | Більша цифра більш підкріплена контекстом |
| Brands Scaled | **300+** (about.html) | Узгоджена з ad spend |
| CPC Reduction | **38%** | Унікальна метрика, виглядає реальною |

### 3.6 Broken nearby city links

Або створити сторінки, або замінити на реально існуючі сусідні міста зі списку.

---

## ФАЗА 4 — Content & E-E-A-T (тиждень 4)

### 4.1 Додати FAQ на homepage

Мінімум 5 питань + FAQPage schema:
- What is performance marketing?
- What ROAS can I expect from a New York performance marketing agency?
- How much does performance marketing management cost?
- What's the difference between Google Ads and Meta Ads?
- How long does it take to see results from paid media?

### 4.2 Розширити команду на about.html

- Повні імена (з дозволу)
- Реальні фото або якісні ілюстрації
- LinkedIn посилання
- Короткі credentials рядки

### 4.3 Оновити llms.txt

Додати `## Pages` секцію з URL + описами всіх ключових сторінок (повний шаблон у GEO-звіті).

### 4.4 Prose paragraph для AI citation (homepage)

Перетворити stat block marquee на citable prose:
> "Vora manages $100M+ in annual ad spend across Google, Meta, and programmatic channels for 300+ brands, achieving a 4.2x average ROAS and 38% average CPC reduction across its managed portfolio (2023–2025)."

---

## ФАЗА 5 — Local SEO foundation (місяць 2)

### 5.1 Придбати US телефонний номер
- Google Voice (безкоштовно, 212/646/917 area codes)
- Grasshopper або Twilio (платно, але більше функцій)
- Оновити скрізь: schema, footer, contact page, GBP

### 5.2 Створити та верифікувати Google Business Profile
- Primary category: Marketing Agency
- Заповнити description, фото, hours
- Додати service area для всіх US міст
- Після верифікації — embed Google Maps на contact.html

### 5.3 Зареєструватись на Clutch.co
- Профіль агенції: безкоштовно
- Запросити 5-10 клієнтів залишити відгуки
- Після накопичення відгуків — додати Clutch widget на homepage

### 5.4 Створити /local/ hub-сторінку

Нова сторінка `/local/index.html` зі списком всіх 22 міст + 8 послуг:
- Допомагає розподілу PageRank на 176 сторінок
- Дає Google чіткий crawl path
- Можливість внутрішньої перелінковки

---

## ФАЗА 6 — AI & GEO (місяць 2-3)

### 6.1 Створити YouTube канал
- Назва: Vora | Performance Marketing
- Перше відео: "How to Calculate ROAS for Google Ads" (5-7 хв)
- Додати YouTube URL в sameAs на index.html

### 6.2 FAQPage на всіх ключових сторінках
- Homepage: 5+ питань (загальні про performance marketing)
- About: 3-5 питань (про агенцію, команду, процес)
- Service pages: вже є, перевірити answer length (40-70 слів)

### 6.3 Bing Webmaster Tools
- Верифікувати сайт
- Подати sitemap.xml
- Налаштувати IndexNow

---

## МЕТРИКИ УСПІХУ (3 місяці)

| Метрика | Зараз | Ціль |
|---|---|---|
| SEO Health Score | 52/100 | 78+/100 |
| LCP (homepage) | ~3.0s | ≤2.5s |
| Schema validation errors | 6 Critical | 0 Critical |
| Local SEO Score | 34/100 | 65+/100 |
| GEO Score | 61/100 | 75+/100 |
| Clutch reviews | 0 | 10+ |
| GBP verified | ❌ | ✅ |
| Ranking "performance marketing NYC" | Not in top 10 | Top 10 |

---

## ПРІОРИТЕТНА МАТРИЦЯ

```
HIGH IMPACT + LOW EFFORT → Робити першими (Фаза 0-1):
  ✅ Fix broken CTA (2 хв)
  ✅ Add defer to GSAP (5 хв)
  ✅ Fix streetAddress schema (5 хв)
  ✅ Remove fake AggregateRating (30 хв)
  ✅ Non-blocking Google Fonts (15 хв)
  ✅ BreadcrumbList URL cleanup (30 хв)
  ✅ Reconcile stats across pages (1 год)

HIGH IMPACT + HIGH EFFORT → Планувати (Фаза 2-4):
  ⏳ H1 restructure + on-page keyword optimization
  ⏳ FAQ sections + FAQPage schema on homepage/about
  ⏳ Schema template fix for 176 local pages
  ⏳ llms.txt complete rewrite
  ⏳ Team section expansion (photos, full names, LinkedIn)

HIGH IMPACT + BUSINESS DEPENDENCY → Координувати (Фаза 5-6):
  📋 US phone number acquisition
  📋 Google Business Profile creation
  📋 Clutch profile + reviews
  📋 YouTube channel launch

LOW IMPACT + ANY EFFORT → Backlog:
  📌 Wikipedia/Wikidata entity
  📌 Blog launch
  📌 Client logo strip
  📌 Dedicated /google-ads-agency-new-york/ page
```

---

*Аудит проведено: 2026-04-26*
*Наступний аудит: 2026-07-26 (через 3 місяці)*
