# Full SEO Audit Report — Vora (aivopa.com)

**Дата аудиту:** 2026-04-26
**Бізнес:** Vora — Performance Marketing Agency
**Домен:** https://aivopa.com
**Платформа:** Vercel (static HTML)
**Аудитори:** 8 паралельних SEO-спеціалістів

---

## ЗАГАЛЬНИЙ SEO HEALTH SCORE: 52 / 100

| Категорія | Вага | Бал | Зважений |
|---|---|---|---|
| Technical SEO | 22% | 65/100 | 14.3 |
| Content Quality | 23% | 40/100 | 9.2 |
| On-Page SEO (SXO) | 20% | 51/100 | 10.2 |
| Schema / Structured Data | 10% | 61/100 | 6.1 |
| Performance (CWV) | 10% | 63/100 | 6.3 |
| AI Search Readiness (GEO) | 10% | 61/100 | 6.1 |
| Images & Media | 5% | 45/100 | 2.3 |
| **РАЗОМ** | **100%** | | **54.5 → 52\*** |

\* Штраф -2.5 за три критичні довірчі проблеми: фальшивий AggregateRating, канадський телефонний код для NY-агенції, несуперечливі метрики між сторінками.

---

## ТОП-5 КРИТИЧНИХ ПРОБЛЕМ

| # | Проблема | Ризик | Файл(и) |
|---|---|---|---|
| 1 | **Фальшивий AggregateRating** на 176 local pages (4.9/127 відгуків, яких не існує) | Manual Action від Google | Всі `/local/` сторінки |
| 2 | **Телефон (647) — Toronto area code** для NY-агенції | Блокує Local Pack | Всі сторінки |
| 3 | **Broken CTA** на about.html → `/vora/contact.html` (404) | Конверсійний провал | `about.html:368` |
| 4 | **Cross-city copy contamination** — 20+ міст мають текст "New York, NY area" | Doorway page risk | Всі non-NY local pages |
| 5 | **Несуперечливі метрики** (9.1x vs 4.2x ROAS; $50M vs $100M; 400+ vs 300+ brands) | E-E-A-T, довіра | `index.html`, `about.html`, local pages |

---

## ТОП-5 ШВИДКИХ ПЕРЕМОГ (Quick Wins)

| # | Дія | Час | Impact |
|---|---|---|---|
| 1 | Виправити `/vora/contact.html` → `contact.html` в about.html | 2 хв | Конверсія |
| 2 | Додати `defer` до обох GSAP `<script>` тегів | 5 хв | LCP -0.6...-1.2s |
| 3 | Виправити `streetAddress: "New York"` на contact.html | 5 хв | Schema |
| 4 | Додати OAI-SearchBot та Applebot-Extended до robots.txt | 5 хв | AI crawlers |
| 5 | Виправити числовий формат `price` в local page schema | 30 хв | Rich results |

---

## РОЗДІЛ 1 — TECHNICAL SEO (65/100)

### ✅ Що працює
- HTTPS активний на всьому сайті
- Canonical tags присутні на всіх сторінках
- Brotli compression активний (HTML стискається на 76%)
- robots.txt правильно структурований (Allow перед Disallow)
- Sitemap.xml присутній і вказаний у robots.txt
- Статичний HTML — ідеальна основа для SEO і AI-crawling
- Vercel Edge Network — глобальний CDN

### ❌ Критичні проблеми

**T-C1: logo.png повертає 404**
```
https://aivopa.com/logo.png → 404 Not Found
```
Файл вказаний у schema.org `logo` на всіх сторінках. Google Rich Results Validator відхилить організацію без валідного логотипу. Або додати файл, або оновити URL в схемі.

**T-C2: Render-blocking GSAP в `<head>` (41KB)**
```html
<!-- ЗАРАЗ (БЛОКУЄ рендеринг) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- ВИПРАВЛЕННЯ — додати defer -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
```

### ⚠️ Високі проблеми

**T-H1: Google Fonts блокує рендеринг**

Поточний `<link rel="stylesheet">` для Google Fonts є синхронним. Виправлення:
```html
<!-- Замінити на non-blocking патерн -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;900&display=swap" as="style" />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;900&display=swap" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Berkshire+Swash&family=Inter:wght@300;400;500;600;700;900&display=swap" /></noscript>
```

**T-H2: Static assets кешуються 0 секунд (max-age=0)**

Зображення та статичні файли повинні кешуватись. Додати в `vercel.json`:
```json
{
  "headers": [
    {
      "source": "/(.*\\.(png|jpg|jpeg|webp|avif|svg|ico|woff2))",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}
```

**T-H3: robots.txt потребує доповнення**

OAI-SearchBot і Applebot-Extended відсутні:
```
User-agent: OAI-SearchBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: CCBot
Allow: /
```

**T-H4: Відсутні Security Headers**

Налаштувати в `vercel.json`:
```json
{
  "source": "/(.*)",
  "headers": [
    { "key": "X-Content-Type-Options", "value": "nosniff" },
    { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
    { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
  ]
}
```

**T-H5: robots.txt потребує оновлення при додаванні нових local pages**

При кожному новому місті / послузі потрібно вручну додавати Allow рядки. Розглянути більш гнучкий підхід: окремий sitemap для local pages як сигнал замість Allow-списку.

### 🔵 Середні проблеми

**T-M1:** Немає GA4 або інших analytics у статичному HTML (не підтверджено — може бути в GTM, але GTM теж не виявлено). Критично для GSC/GA4 інтеграції.

**T-M2:** about.html має `lang="en"`, а index.html — `lang="en-US"`. Потрібна консистентність.

**T-M3:** BreadcrumbList на about.html та деяких service pages посилається на `.html` URLs, тоді як canonical — без розширення.

---

## РОЗДІЛ 2 — CONTENT QUALITY (40/100)

### Стан контенту по сторінках

| Сторінка | Слів (видимий текст) | Статус | E-E-A-T |
|---|---|---|---|
| index.html | ~1,300 | ⚠️ Середньо | Слабкий |
| about.html | ~900 | ⚠️ Тонко | Слабкий |
| contact.html | ~200 | ✅ Ок для типу | Н/Д |
| local pages | ~900-1,100 | 🔴 Thin+Generic | Відсутній |

### Критичні E-E-A-T проблеми

**C-C1: Несуперечливі статистики між сторінками**

| Метрика | index.html | about.html | local pages |
|---|---|---|---|
| Average ROAS | **9.1x** | **4.2x** | **4.2x** |
| Ad Spend | **$50M+** | **$100M+** | **$100M+** |
| Brands | **400+** | **300+** | **300+** |
| CAC Reduction | **40%** | **38%** | **42%** |

Це найбільша проблема довіри на сайті. Потрібно визначити один канонічний набір цифр і застосувати скрізь.

**C-C2: Команда — тільки ініціали, без фото, без LinkedIn**

Поточний стан: "Alex V.", "Chris D." тощо. Google E-E-A-T вимагає ідентифікованих, верифікованих людей. Конкуренти показують повні імена, фото, LinkedIn.

**C-C3: Відсутні кейси з числами**

Немає жодної сторінки з детальним кейсом: клієнт → проблема → що зробили → результати з цифрами і датами. Конкурент Consultus Digital має 1,100+ верифікованих відгуків.

**C-C4: Відсутній блог / ресурси**

Нуль контентних сторінок для topical authority. Конкуренти мають статті типу "How to Optimize Google Ads ROAS", "Performance Max vs Standard Shopping".

**C-C5: Жодної FAQ на homepage та about**

Homepage і About — сторінки з найбільшим трафіком — не мають FAQPage schema і FAQ-секцій. Це прямо знижує AI citation readiness та AEO.

### AI Citation Readiness: Низький

Проблеми:
- Статистика в marquee є `aria-hidden="true"` — AI crawlers не можуть її парсити як цитовані дані
- H1 "Maximize ROAS. Minimize CAC." — жодного ключового слова, жодної цитованої інформації
- Немає "Key Takeaways" блоків
- Немає питань-відповідей на head-сторінках
- Єдиний добрий citable paragraph: "Vora was built in New York by performance marketers..." (~67 слів на about.html)

---

## РОЗДІЛ 3 — ON-PAGE SEO / SXO (51/100)

### Page-Type Mismatch аналіз

| Keyword | Домінуючий SERP тип | Vora тип | Мисматч |
|---|---|---|---|
| "performance marketing agency New York" | Agency homepage / service page | Homepage | ✅ Aligned |
| "Google Ads agency New York" | Dedicated service+location page (/google-ads-agency-new-york/) | `/local/new-york/google-ads-agency/` (у subfolder) | 🔴 HIGH |

**Vora не ранжується в топ-10 для жодного з цих ключових слів.**

### Критичні On-Page проблеми

**OP-C1: H1 без ключових слів**
```html
<!-- ЗАРАЗ -->
<h1>Maximize ROAS. Minimize CAC.</h1>

<!-- ВИПРАВЛЕННЯ -->
<h1>New York Performance Marketing Agency</h1>
<p class="hero-tagline">Maximize ROAS. Minimize CAC.</p>
```

**OP-C2: Broken CTA link на about.html**
```html
<!-- ЗАРАЗ (404 в production) -->
<a href="/vora/contact.html" class="btn-primary">Get a Free Proposal</a>

<!-- ВИПРАВЛЕННЯ -->
<a href="contact.html" class="btn-primary">Get a Free Proposal</a>
```
Файл: `about.html`, рядок 368.

**OP-C3: Назва "#1" без підтвердження**
```html
<!-- index.html title tag -->
<title>Vora | New York's #1 Performance Marketing Agency</title>
```
Неспростована заява "#1" ризикує Editorial Review від Google. Замінити на верифіковане: "Award-Winning" або прибрати.

**OP-C4: Service cards — `<div>` замість `<h3>`**

14 service cards на index.html використовують `<div class="service-card__title">`. Це семантично неправильно і знижує keyword relevance.

**OP-C5: Stats в marquee приховані від скрін-рідерів і пошукових ботів**
```html
<div class="marquee-band" aria-hidden="true" role="presentation">
```
Ключові метрики (9.1x ROAS, $50M+) невидимі для accessibility і частково для ботів.

### Відсутні елементи у порівнянні з конкурентами

| Елемент | Taktical | AdVenture | Consultus | Vora |
|---|---|---|---|---|
| Google Partner badge | ✅ | ✅ | ✅ | ❌ |
| Clutch rating widget | ✅ | ✅ | ✅ | ❌ |
| Client logo strip | ✅ | ✅ | ✅ | ❌ |
| Named case studies | ✅ | ✅ | ✅ | ❌ |
| Review count (verified) | ✅ | ✅ | ✅ | ❌ |
| Dedicated keyword URL | - | ✅ | ✅ | ❌ |

---

## РОЗДІЛ 4 — SCHEMA / STRUCTURED DATA (61/100)

### Знайдені схеми по типу сторінок

| Сторінка | Schema типи |
|---|---|
| index.html | Organization + LocalBusiness + MarketingAgency + WebSite |
| about.html | MarketingAgency + BreadcrumbList |
| contact.html | MarketingAgency + BreadcrumbList |
| services.html | MarketingAgency + hasOfferCatalog + BreadcrumbList |
| pricing.html | MarketingAgency + FAQPage + BreadcrumbList |
| service pages | Service + FAQPage + BreadcrumbList |
| local pages | LocalBusiness + MarketingAgency + FAQPage + BreadcrumbList |

### Критичні помилки

**SC-C1: contact.html — `streetAddress: "New York"` (місто замість вулиці)**
```json
// ЗАРАЗ (НЕПРАВИЛЬНО)
"address": { "streetAddress": "New York", "addressLocality": "New York" }

// ВИПРАВЛЕННЯ
"address": {
  "streetAddress": "350 Fifth Avenue",
  "addressLocality": "New York",
  "addressRegion": "NY",
  "postalCode": "10118",
  "addressCountry": "US"
}
```

**SC-C2: Offer price як рядок на 176 local pages**
```json
// ЗАРАЗ (НЕПРАВИЛЬНО)
{"@type": "Offer", "price": "$1,500/mo", "priceCurrency": "USD"}

// ВИПРАВЛЕННЯ
{"@type": "Offer", "price": "1500", "priceCurrency": "USD", "description": "Per month"}
```

**SC-C3: Порожній geo об'єкт на всіх local pages**
```json
// ЗАРАЗ (НЕПРАВИЛЬНО)
"geo": {"@type": "GeoCoordinates"}

// ВИПРАВЛЕННЯ
"geo": {"@type": "GeoCoordinates", "latitude": "40.74840", "longitude": "-73.99670"}
```

**SC-C4: Фальшивий AggregateRating на 176 local pages**
```json
// ВИДАЛИТИ ПОВНІСТЮ (або замінити реальними даними після збору відгуків)
"aggregateRating": {"ratingValue": "4.9", "reviewCount": "127"}
```

**SC-C5: SearchAction вказує на неіснуючий пошук**
```json
// ВИДАЛИТИ (немає функції пошуку на сайті)
"target": "https://aivopa.com/?s={search_term_string}"
```

**SC-C6: BreadcrumbList uses .html vs canonical без розширення**

Всі BreadcrumbList items: замінити `about.html` → `about`, `contact.html` → `contact`, і т.д.

### NAP Consistency: FAIL

| Поле | index.html | contact.html | about.html | local pages |
|---|---|---|---|---|
| Phone | `+16473701888` (E.164) ✅ | Відсутній ❌ | Відсутній ❌ | `(647) 370-1888` ❌ |
| Street | 350 Fifth Avenue ✅ | "New York" ❌ | Відсутній ❌ | Відсутній ❌ |
| ZIP | 10118 ✅ | Відсутній ❌ | Відсутній ❌ | Відсутній ❌ |

**Додаткова критична проблема:** Область телефону (647) — це Toronto, Ontario, Canada. Для New York потрібен код 212, 646, або 917.

---

## РОЗДІЛ 5 — PERFORMANCE / CORE WEB VITALS (63/100)

### CWV Summary

| Метрика | Homepage | About | Ціль | Статус |
|---|---|---|---|---|
| LCP | ~2.8–3.5s | ~2.8–3.5s | ≤2.5s | 🔴 Needs Improvement |
| INP | ~50–120ms | ~50–120ms | ≤200ms | ✅ Good |
| CLS | ~0.02–0.05 | ~0.02–0.05 | ≤0.1 | ✅ Good |
| TTFB | ~172ms (warm) | ~623ms (cold) | ≤800ms | ✅/⚠️ |

### Детальний аналіз

**LCP Проблема:** Заголовок H1 рендериться у шрифті `Berkshire Swash` з Google Fonts. Браузер не може намалювати H1 до завантаження шрифту. При цьому GSAP блокує рендеринг до завантаження (41KB з зовнішнього CDN).

**Виправлення 1 — Defer GSAP (найвищий пріоритет):**
```html
<script src="...gsap.min.js" defer></script>
<script src="...ScrollTrigger.min.js" defer></script>
```
Очікуваний ефект: LCP -0.6...-1.2s

**Виправлення 2 — Preload LCP font:**
```html
<link rel="preload" 
      href="https://fonts.gstatic.com/s/berkshireswash/v19/ptRRTi-cavZOGqCvnNJDl5m5XmNPrcQybX4pQA.woff2"
      as="font" type="font/woff2" crossorigin>
```
Очікуваний ефект: LCP -0.3...-0.6s

**Виправлення 3 — Non-blocking Google Fonts:**
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/..." media="print" onload="this.media='all'" />
```

**Позитивне:** Жодних зображень у body (тільки CSS-ефекти) → CLS практично нульовий. Жодних tracking scripts → INP відмінний.

**Очікуваний результат після виправлень:** Performance Score 82–88/100.

---

## РОЗДІЛ 6 — AI SEARCH READINESS / GEO (61/100)

### AI Crawler Accessibility

| Bot | Призначення | Статус |
|---|---|---|
| GPTBot | ChatGPT training | ✅ Явно дозволений |
| ClaudeBot | Anthropic crawling | ✅ Явно дозволений |
| Google-Extended | Gemini / AI Overviews | ✅ Явно дозволений |
| PerplexityBot | Perplexity AI | ✅ Явно дозволений |
| anthropic-ai | Anthropic training | ✅ Явно дозволений |
| OAI-SearchBot | ChatGPT live search | ⚠️ Тільки через wildcard |
| Applebot-Extended | Apple Intelligence | ⚠️ Тільки через wildcard |
| CCBot | Common Crawl | ⚠️ Тільки через wildcard |

### llms.txt

Файл існує — це перевага над більшістю конкурентів. Але: **немає жодного URL-запису** (`## Pages` секція відсутня), що є основним призначенням файлу за специфікацією.

**Шаблон для оновлення llms.txt:** (повна версія надана GEO-агентом у попередньому звіті)

### Головні GEO прогалини

1. **Відсутній YouTube-канал** — найсильніший сигнал AI-цитування (кореляція ~0.737)
2. **Немає Wikipedia/Wikidata entity** для Vora
3. **Метрики не в citable prose** — числа в marquee є `aria-hidden`, не можуть цитуватись
4. **Жодного FAQPage на homepage/about** — AI системи сканують питання-відповіді

### Перевага

Статичний HTML — найкраща технічна база для AI-crawling. Весь контент доступний без JS.

---

## РОЗДІЛ 7 — LOCAL SEO (34/100)

### Критична проблема: Телефон з кодом Торонто

**(647) area code = Toronto, Ontario, Canada**

New York area codes: 212, 332, 646, 718, 917, 929

Це підриває:
- Місцевий Local Pack рейтинг
- NAP validation у citation aggregators
- Довіру користувачів

**Рішення:** Придбати US номер через Google Voice, Grasshopper або Twilio. Оновити скрізь.

### Google Business Profile: 0 сигналів

Жодного GBP embed, reference, Place ID на будь-якій сторінці. GBP — фактор #1 для Local Pack (Whitespark 2026). Без верифікованого GBP — Vora не може з'явитись у Local Pack.

### Local Pages якість: КРИТИЧНО

**Проблема 1: Cross-city copy contamination**
20+ non-NY сторінок містять текст: *"Vora serves businesses throughout the entire New York, NY area"*

Це означає:
- Контентна помилка видима користувачам
- Entity confusion для Google NLP (LA page класифікується як NY page)
- Doorway page risk при масштабі 176 сторінок

**Проблема 2: Broken nearby city links (404)**

На сторінках є посилання на:
- `/local/newark/performance-marketing-agency` → 404
- `/local/jersey-city/performance-marketing-agency` → 404
- `/local/yonkers/performance-marketing-agency` → 404

**Проблема 3: Future-dated schema**
`"datePublished": "2026-05-01"` на NY PMA page (сьогодні 2026-04-26). Google може відтермінувати індексацію.

**Проблема 4: Відсутня /local/ hub-сторінка**
Немає `/local/` index що лінкує на всі міста — PageRank не розподіляється ефективно.

---

## РОЗДІЛ 8 — SITEMAP / CRAWLABILITY

### Sitemap.xml

- Файл існує ✅
- Вказаний у robots.txt ✅
- Потребує аудиту: чи включені всі 176 local pages + 5 core pages + service pages

### robots.txt архітектура

Поточна: 176 явних Allow рядків + `Disallow: /local/`

Ризик: При кожному новому місті/послузі потрібно ручне оновлення. При помилці — нова сторінка заблокована.

**Рекомендація:** Перейти на allowlist через sitemap замість Allow-рядків у robots.txt. Або генерувати robots.txt автоматично.

### Crawl depth

Проблема: Немає `/local/` hub-сторінки. Local pages доступні тільки через:
- Footer (8 міст × послуги)
- Sitemap.xml
- Посилання із сусідніх сторінок (що самі мають проблеми 404)

Для 176 сторінок глибина > 3 кліки від homepage — субоптимально.

---

## РОЗДІЛ 9 — IMAGES & MEDIA (45/100)

### Позитивне
- Жодних `<img>` у body сторінок → нульовий CLS ризик
- Brotli compression на HTML

### Проблеми
- `logo.png` → 404 (вказаний у JSON-LD schema на всіх сторінках)
- `og-image.jpg` → JPEG (застарілий формат для OG)
- Emoji використовуються як service icons (не семантично, не доступно)
- Жодних реальних фото команди
- Жодних client logo images (конкуренти всі показують)

---

## ПОВНИЙ СПИСОК ПРОБЛЕМ ЗА ПРІОРИТЕТАМИ

### 🔴 CRITICAL (виправити негайно)

| # | Проблема | Файл / URL | Fix |
|---|---|---|---|
| 1 | Broken CTA `/vora/contact.html` | `about.html:368` | Замінити на `contact.html` |
| 2 | Фальшивий AggregateRating (4.9/127) | Всі 176 local pages | Видалити block |
| 3 | Cross-city copy contamination ("New York, NY area" на non-NY pages) | Всі non-NY local pages | Template regex fix |
| 4 | `streetAddress: "New York"` замість вулиці | `contact.html` schema | Виправити |
| 5 | logo.png → 404 | Всі сторінки (schema) | Додати файл або виправити URL |

### 🟠 HIGH (виправити протягом тижня)

| # | Проблема | Файл | Fix |
|---|---|---|---|
| 6 | Render-blocking GSAP (41KB в `<head>`) | Всі HTML | Додати `defer` |
| 7 | Google Fonts блокує рендеринг (LCP) | Всі HTML | media="print" onload |
| 8 | Немає preload для LCP font (Berkshire Swash) | Всі HTML | `<link rel="preload">` |
| 9 | Offer price як string `"$1,500/mo"` | Всі local pages | Замінити на `"1500"` |
| 10 | Порожній `geo: {}` на local pages | Всі local pages | Додати координати або видалити |
| 11 | NAP inconsistency: phone format E.164 vs display | Всі local pages schema | Стандартизувати на E.164 |
| 12 | NAP: streetAddress та postalCode відсутні в about/contact/local | Всі ці сторінки | Додати повну адресу |
| 13 | H1 без ключових слів на homepage | `index.html` | Реструктурувати H1/span |
| 14 | Service card titles — `<div>` замість `<h3>` | `index.html` | Змінити теги |
| 15 | Неузгоджені метрики між сторінками | `index.html`, `about.html`, local pages | Обрати один набір, застосувати скрізь |
| 16 | Broken nearby city links (Newark, Jersey City, Yonkers → 404) | Всі local pages | Видалити або створити сторінки |
| 17 | `"datePublished": "2026-05-01"` у майбутньому | NY local pages | Виправити на поточну дату |
| 18 | SearchAction → неіснуючий `?s=` endpoint | `index.html` schema | Видалити блок |
| 19 | BreadcrumbList: `.html` URL vs canonical без розширення | Всі inner pages | Прибрати `.html` |
| 20 | `about.html` `lang="en"` vs `index.html` `lang="en-US"` | `about.html` | Змінити на `en-US` |

### 🟡 MEDIUM (виправити протягом місяця)

| # | Проблема | Дія |
|---|---|---|
| 21 | Телефон (647) — Toronto area code | Придбати US номер (212/646/917) |
| 22 | Відсутній Google Business Profile | Створити та верифікувати GBP |
| 23 | Жодних верифікованих відгуків (Clutch, Google) | Зареєструватись на Clutch, зібрати 10+ відгуків |
| 24 | llms.txt без URL-записів | Оновити з `## Pages` секцією |
| 25 | OAI-SearchBot і Applebot-Extended відсутні в robots.txt | Додати explicit Allow |
| 26 | Static assets max-age=0 | Налаштувати Cache-Control в vercel.json |
| 27 | Security Headers відсутні | Додати в vercel.json |
| 28 | FAQPage schema відсутня на homepage та about | Додати FAQ секції + schema |
| 29 | Stats в marquee `aria-hidden="true"` | Зробити доступними або дублювати в prose |
| 30 | Title tag містить "#1" без підтвердження | Замінити на верифіковане твердження |
| 31 | `local page url` вказує на локальну URL замість org root | Виправити в template |
| 32 | Person schema без `sameAs` LinkedIn для команди | Додати LinkedIn URLs |
| 33 | Відсутній `/local/` hub-сторінка | Створити index сторінку всіх міст |
| 34 | cursor: none на всіх `<a>` — accessibility ризик на mobile | Обмежити до desktop only |

### 🔵 LOW (backlog)

| # | Проблема | Дія |
|---|---|---|
| 35 | Жодного YouTube каналу (найбільший AI citation сигнал) | Створити канал, додати в sameAs |
| 36 | Немає Wikipedia/Wikidata entity для Vora | Створити при наявності notability |
| 37 | Emoji як service icons — не семантично | Замінити на SVG або реальні icons |
| 38 | Команда без фото та повних імен | Додати реальні фото та повні імена |
| 39 | Немає client logo strip | Додати з дозволу клієнтів |
| 40 | Немає case studies сторінок | Створити мінімум 3 детальних кейси |
| 41 | Немає блогу / topical authority контенту | Запустити blog з 4-6 статтями/квартал |
| 42 | Inter font — 6 weights можна скоротити | Self-host з subsetting |
| 43 | RAFLoop cursor на mobile (зайве навантаження) | Вимкнути на touch devices |
| 44 | og:type "website" на about — краще "profile" | Оновити OG type |
| 45 | WebPage schema відсутня на terms.html, cookie-policy.html | Додати базову WebPage schema |
