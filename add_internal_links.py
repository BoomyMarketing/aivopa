#!/usr/bin/env python3
"""Add 6th FAQ + Related Industries section to all 74 industry pages."""

from pathlib import Path

BASE = Path(r"C:\Users\Инна\Desktop\projects\aivopa\industries")

META = {
    'saas':             ('💻', 'SaaS',              'Product-led & demo lead generation'),
    'fintech':          ('📈', 'Fintech',            'Compliant growth for financial products'),
    'tech-startups':    ('🚀', 'Tech Startups',      'ICP targeting & SQL pipeline growth'),
    'accounting':       ('📊', 'Accounting',         'Tax season campaigns & SMB lead gen'),
    'staffing':         ('🤝', 'Staffing',           'Employer client & candidate acquisition'),
    'mortgage':         ('🏦', 'Mortgage Brokers',   'Purchase & refinance lead generation'),
    'healthcare':       ('🏥', 'Healthcare',         'Patient acquisition & HIPAA-compliant tracking'),
    'dental':           ('🦷', 'Dental',             'New patient generation for dental practices'),
    'mental-health':    ('🧠', 'Mental Health',      'Ethical, HIPAA-compliant patient marketing'),
    'senior-care':      ('🤲', 'Senior Care',        'Family decision-maker targeting'),
    'childcare':        ('👶', 'Childcare',          'Enrollment campaigns & waitlist generation'),
    'fitness':          ('💪', 'Fitness',            'Gym & studio member acquisition'),
    'spa':              ('💆', 'Spa & Med Spa',      'Booking & membership growth campaigns'),
    'chiropractic':     ('🦴', 'Chiropractic',       'New patient generation for chiro practices'),
    'physical-therapy': ('🏃', 'Physical Therapy',   'Referral & direct patient acquisition'),
    'yoga-studio':      ('🧘', 'Yoga Studio',        'Membership & class pack growth'),
    'personal-trainer': ('🏋️', 'Personal Training',  'Client acquisition for trainers & studios'),
    'plastic-surgery':  ('💉', 'Plastic Surgery',    'Consultation booking for aesthetic practices'),
    'urgent-care':      ('🚑', 'Urgent Care',        'Walk-in patient volume & local visibility'),
    'optometry':        ('👁️', 'Optometry',          'Eye exam bookings & eyewear retail growth'),
    'veterinary':       ('🐾', 'Veterinary',         'New pet patient acquisition for vet clinics'),
    'massage-therapy':  ('💆', 'Massage Therapy',    'Membership & recurring client acquisition'),
    'acupuncture':      ('🪡', 'Acupuncture',        'Patient acquisition for TCM practices'),
    'home-services':    ('🏠', 'Home Services',      'Multi-service lead generation & LSA'),
    'cleaning':         ('🧹', 'Cleaning',           'Recurring client acquisition via LSA & Google'),
    'plumbing':         ('🔧', 'Plumbing',           '24/7 emergency & scheduled service leads'),
    'roofing':          ('🏗️', 'Roofing',            'Storm response & replacement lead gen'),
    'landscaping':      ('🌿', 'Landscaping',        'Seasonal campaigns & commercial accounts'),
    'solar':            ('☀️', 'Solar',              'Exclusive homeowner lead generation'),
    'electrician':      ('⚡', 'Electrician',        'Residential & commercial electrical leads'),
    'hvac':             ('❄️', 'HVAC',               'Seasonal install & repair lead generation'),
    'pest-control':     ('🪲', 'Pest Control',       'Recurring service & emergency call leads'),
    'painting':         ('🖌️', 'Painting',           'Interior & exterior painting project leads'),
    'locksmith':        ('🔑', 'Locksmith',          'Emergency & scheduled locksmith leads'),
    'junk-removal':     ('🗑️', 'Junk Removal',       'Residential & commercial haul-away leads'),
    'remodeling':       ('🛠️', 'Remodeling',         'Kitchen, bath & whole-home project leads'),
    'window-cleaning':  ('🪟', 'Window Cleaning',    'Residential & commercial window service leads'),
    'pressure-washing': ('💦', 'Pressure Washing',   'Residential & commercial pressure wash leads'),
    'garage-door':      ('🚪', 'Garage Door',        'Repair & installation lead generation'),
    'tree-service':     ('🌳', 'Tree Service',       'Storm response & residential tree care leads'),
    'appliance-repair': ('🔌', 'Appliance Repair',   'Same-day service calls & technician bookings'),
    'fence-installation':('🪵','Fence Installation', 'Residential & commercial fence project leads'),
    'dumpster-rental':  ('🚛', 'Dumpster Rental',    'Residential & contractor roll-off bookings'),
    'carpet-cleaning':  ('🧺', 'Carpet Cleaning',    'Recurring residential & commercial accounts'),
    'security-systems': ('🔒', 'Security Systems',   'Installation leads & monitoring contracts'),
    'ecommerce':        ('🛒', 'E-commerce',         'ROAS-focused DTC & Shopify growth'),
    'beauty':           ('💄', 'Beauty',             'DTC beauty brand scaling & retention'),
    'fashion':          ('👗', 'Fashion',            'Seasonal campaigns & brand awareness'),
    'luxury':           ('✨', 'Luxury',             'HNW audience targeting & brand positioning'),
    'pet':              ('🐾', 'Pet Brands',         'DTC & Amazon pet product growth'),
    'automotive':       ('🚗', 'Automotive',         'Dealer & service center lead generation'),
    'nail-salon':       ('💅', 'Nail Salon',         'Booking growth & repeat client retention'),
    'barbershop':       ('✂️', 'Barbershop',         'Local visibility & appointment generation'),
    'tattoo-studio':    ('🖊️', 'Tattoo Studio',      'Instagram portfolio & consultation bookings'),
    'restaurants':      ('🍽️', 'Restaurants',        'Reservation & delivery growth campaigns'),
    'food-beverage':    ('🍷', 'Food & Beverage',    'Retail distribution & DTC brand growth'),
    'travel':           ('✈️', 'Travel',             'Booking & inquiry campaigns for travel brands'),
    'event-planning':   ('🎉', 'Event Planning',     'Corporate & social event inquiry generation'),
    'wedding':          ('💍', 'Wedding',            'Couple inquiry generation for wedding vendors'),
    'catering':         ('🍱', 'Catering',           'Corporate & social event catering leads'),
    'real-estate':      ('🏢', 'Real Estate',        'Buyer, seller & renter lead generation'),
    'interior-design':  ('🛋️', 'Interior Design',    'Pinterest & HNW client acquisition'),
    'construction':     ('🔨', 'Construction',       'Commercial & residential project leads'),
    'photography':      ('📸', 'Photography',        'Wedding, portrait & commercial bookings'),
    'moving':           ('📦', 'Moving',             'Residential & commercial move lead gen'),
    'florist':          ('🌸', 'Florist',            'Event, wedding & daily order growth'),
    'legal':            ('⚖️', 'Legal',              'Practice area lead generation for law firms'),
    'insurance':        ('🛡️', 'Insurance',          'Policy quote lead generation'),
    'education':        ('🎓', 'Education',          'Enrollment campaigns for schools & courses'),
    'nonprofit':        ('❤️', 'Nonprofit',          'Donor acquisition & volunteer campaigns'),
    'tutoring':         ('📚', 'Tutoring',           'Student enrollment & parent lead generation'),
    'financial-advisor':('💼', 'Financial Advisor',  'HNW client acquisition & AUM growth'),
    'car-detailing':    ('🚗', 'Car Detailing',      'Mobile & studio detailing booking growth'),
    'dog-grooming':     ('🐕', 'Dog Grooming',       'Recurring grooming client acquisition'),
}

RELATED = {
    'saas':             ['fintech', 'tech-startups', 'accounting', 'staffing', 'ecommerce'],
    'fintech':          ['saas', 'mortgage', 'accounting', 'insurance', 'legal'],
    'tech-startups':    ['saas', 'fintech', 'accounting', 'staffing', 'ecommerce'],
    'accounting':       ['fintech', 'legal', 'insurance', 'mortgage', 'financial-advisor'],
    'staffing':         ['saas', 'tech-startups', 'accounting', 'legal', 'education'],
    'mortgage':         ['real-estate', 'insurance', 'financial-advisor', 'accounting', 'fintech'],
    'healthcare':       ['dental', 'mental-health', 'urgent-care', 'senior-care', 'chiropractic'],
    'dental':           ['healthcare', 'mental-health', 'urgent-care', 'plastic-surgery', 'optometry'],
    'mental-health':    ['healthcare', 'senior-care', 'childcare', 'yoga-studio', 'fitness'],
    'senior-care':      ['healthcare', 'childcare', 'mental-health', 'home-services', 'veterinary'],
    'childcare':        ['senior-care', 'tutoring', 'education', 'healthcare', 'fitness'],
    'fitness':          ['yoga-studio', 'personal-trainer', 'massage-therapy', 'chiropractic', 'healthcare'],
    'spa':              ['massage-therapy', 'nail-salon', 'fitness', 'beauty', 'plastic-surgery'],
    'chiropractic':     ['physical-therapy', 'massage-therapy', 'healthcare', 'acupuncture', 'fitness'],
    'physical-therapy': ['chiropractic', 'massage-therapy', 'healthcare', 'fitness', 'acupuncture'],
    'yoga-studio':      ['fitness', 'massage-therapy', 'personal-trainer', 'chiropractic', 'mental-health'],
    'personal-trainer': ['fitness', 'yoga-studio', 'massage-therapy', 'chiropractic', 'healthcare'],
    'plastic-surgery':  ['spa', 'healthcare', 'dental', 'beauty', 'optometry'],
    'urgent-care':      ['healthcare', 'dental', 'mental-health', 'chiropractic', 'optometry'],
    'optometry':        ['healthcare', 'dental', 'urgent-care', 'plastic-surgery', 'senior-care'],
    'veterinary':       ['dog-grooming', 'pet', 'senior-care', 'healthcare', 'childcare'],
    'massage-therapy':  ['spa', 'chiropractic', 'physical-therapy', 'yoga-studio', 'acupuncture'],
    'acupuncture':      ['massage-therapy', 'chiropractic', 'physical-therapy', 'mental-health', 'healthcare'],
    'home-services':    ['cleaning', 'plumbing', 'electrician', 'landscaping', 'pest-control'],
    'cleaning':         ['carpet-cleaning', 'window-cleaning', 'pressure-washing', 'home-services', 'moving'],
    'plumbing':         ['hvac', 'electrician', 'roofing', 'home-services', 'appliance-repair'],
    'roofing':          ['construction', 'plumbing', 'solar', 'home-services', 'remodeling'],
    'landscaping':      ['tree-service', 'fence-installation', 'pressure-washing', 'pest-control', 'home-services'],
    'solar':            ['roofing', 'electrician', 'home-services', 'construction', 'remodeling'],
    'electrician':      ['hvac', 'plumbing', 'appliance-repair', 'security-systems', 'home-services'],
    'hvac':             ['plumbing', 'electrician', 'appliance-repair', 'home-services', 'roofing'],
    'pest-control':     ['cleaning', 'home-services', 'landscaping', 'tree-service', 'carpet-cleaning'],
    'painting':         ['remodeling', 'construction', 'roofing', 'home-services', 'cleaning'],
    'locksmith':        ['security-systems', 'garage-door', 'home-services', 'electrician', 'plumbing'],
    'junk-removal':     ['dumpster-rental', 'cleaning', 'moving', 'remodeling', 'construction'],
    'remodeling':       ['construction', 'painting', 'plumbing', 'electrician', 'interior-design'],
    'window-cleaning':  ['pressure-washing', 'cleaning', 'carpet-cleaning', 'home-services', 'painting'],
    'pressure-washing': ['window-cleaning', 'cleaning', 'carpet-cleaning', 'fence-installation', 'tree-service'],
    'garage-door':      ['locksmith', 'home-services', 'electrician', 'security-systems', 'plumbing'],
    'tree-service':     ['landscaping', 'fence-installation', 'pest-control', 'home-services', 'pressure-washing'],
    'appliance-repair': ['plumbing', 'electrician', 'hvac', 'locksmith', 'cleaning'],
    'fence-installation':['landscaping', 'remodeling', 'construction', 'tree-service', 'pressure-washing'],
    'dumpster-rental':  ['junk-removal', 'remodeling', 'construction', 'roofing', 'cleaning'],
    'carpet-cleaning':  ['cleaning', 'window-cleaning', 'pressure-washing', 'home-services', 'moving'],
    'security-systems': ['electrician', 'locksmith', 'garage-door', 'home-services', 'appliance-repair'],
    'ecommerce':        ['beauty', 'fashion', 'luxury', 'pet', 'food-beverage'],
    'beauty':           ['ecommerce', 'fashion', 'luxury', 'nail-salon', 'spa'],
    'fashion':          ['ecommerce', 'beauty', 'luxury', 'photography', 'tattoo-studio'],
    'luxury':           ['beauty', 'fashion', 'real-estate', 'interior-design', 'photography'],
    'pet':              ['veterinary', 'dog-grooming', 'ecommerce', 'food-beverage', 'car-detailing'],
    'automotive':       ['car-detailing', 'home-services', 'electrician', 'cleaning', 'moving'],
    'nail-salon':       ['beauty', 'barbershop', 'spa', 'tattoo-studio', 'massage-therapy'],
    'barbershop':       ['nail-salon', 'tattoo-studio', 'beauty', 'fitness', 'personal-trainer'],
    'tattoo-studio':    ['barbershop', 'nail-salon', 'beauty', 'photography', 'ecommerce'],
    'restaurants':      ['food-beverage', 'catering', 'event-planning', 'wedding', 'ecommerce'],
    'food-beverage':    ['restaurants', 'catering', 'ecommerce', 'beauty', 'event-planning'],
    'travel':           ['event-planning', 'wedding', 'photography', 'luxury', 'restaurants'],
    'event-planning':   ['wedding', 'catering', 'photography', 'restaurants', 'travel'],
    'wedding':          ['event-planning', 'catering', 'photography', 'florist', 'travel'],
    'catering':         ['event-planning', 'wedding', 'restaurants', 'food-beverage', 'cleaning'],
    'real-estate':      ['interior-design', 'construction', 'mortgage', 'moving', 'photography'],
    'interior-design':  ['real-estate', 'construction', 'photography', 'luxury', 'remodeling'],
    'construction':     ['real-estate', 'interior-design', 'roofing', 'plumbing', 'electrician'],
    'photography':      ['wedding', 'event-planning', 'real-estate', 'interior-design', 'beauty'],
    'moving':           ['junk-removal', 'dumpster-rental', 'cleaning', 'real-estate', 'home-services'],
    'florist':          ['wedding', 'event-planning', 'restaurants', 'catering', 'photography'],
    'legal':            ['accounting', 'insurance', 'real-estate', 'staffing', 'fintech'],
    'insurance':        ['legal', 'accounting', 'mortgage', 'fintech', 'healthcare'],
    'education':        ['tutoring', 'childcare', 'nonprofit', 'staffing', 'mental-health'],
    'nonprofit':        ['education', 'legal', 'insurance', 'healthcare', 'mental-health'],
    'tutoring':         ['education', 'childcare', 'nonprofit', 'mental-health', 'fitness'],
    'financial-advisor':['accounting', 'insurance', 'mortgage', 'fintech', 'legal'],
    'car-detailing':    ['automotive', 'dog-grooming', 'cleaning', 'pressure-washing', 'moving'],
    'dog-grooming':     ['veterinary', 'pet', 'car-detailing', 'cleaning', 'home-services'],
}

# Marker for new-format pages (batches 13+) — have <section class="cta-section">
MARKER_NEW = '    </div>\n  </div>\n</section>\n\n<section class="cta-section">'

# Marker for old-format pages (batches 1-12) — have <div class="cta-band">
MARKER_OLD = '    </div>\n  </section>\n\n  <div class="cta-band">'


def build_faq6_new(slug):
    name = META[slug][1]
    rels = [META[r][1] for r in RELATED[slug] if r in META][:3]
    rel_str = ', '.join(rels)
    return (
        '      <div class="faq-item">\n'
        '        <button class="faq-q">What other industries does Vora serve in New York?</button>\n'
        f'        <div class="faq-a">Beyond {name}, Vora runs performance marketing across 74 industries in New York — including {rel_str}, and many more. Each vertical gets a dedicated campaign built around its specific funnel, buyer intent, and competitive landscape. Browse the full catalog at our <a href="../industries" style="color:var(--ca)">Industries page</a>.</div>\n'
        '      </div>'
    )


def build_faq6_old(slug):
    name = META[slug][1]
    rels = [META[r][1] for r in RELATED[slug] if r in META][:3]
    rel_str = ', '.join(rels)
    return (
        '      <div class="faq-item">\n'
        '        <div class="faq-q">What other industries does Vora serve in New York?</div>\n'
        f'        <div class="faq-a"><p>Beyond {name}, Vora runs performance marketing across 74 industries in New York — including {rel_str}, and many more. Each vertical gets a dedicated campaign built around its specific funnel, buyer intent, and competitive landscape. Browse the full catalog at our <a href="../industries" style="text-decoration:underline">Industries page</a>.</p></div>\n'
        '      </div>'
    )


def build_related_new(slug):
    cards = []
    for r in RELATED[slug][:5]:
        if r not in META:
            continue
        emoji, name, subtitle = META[r]
        cards.append(
            f'      <a href="../{r}" class="ch-card" style="display:block;color:inherit;text-decoration:none">\n'
            f'        <div class="ch-icon">{emoji}</div>\n'
            f'        <div class="ch-name">{name}</div>\n'
            f'        <div class="ch-desc">{subtitle}</div>\n'
            f'      </a>'
        )
    cards_html = '\n'.join(cards)
    return (
        '<section>\n'
        '  <div class="section-inner">\n'
        '    <div class="section-label">Explore More</div>\n'
        '    <h2 class="section-title">Related Industries We Serve in New York</h2>\n'
        '    <div class="channels-grid" style="margin-top:0">\n'
        f'{cards_html}\n'
        '    </div>\n'
        '    <p style="margin-top:24px;font-size:14px;color:var(--cs)">Browse all <a href="../industries" style="color:var(--ca);text-decoration:none">74 industries we serve in New York →</a></p>\n'
        '  </div>\n'
        '</section>\n'
    )


def build_related_old(slug):
    cards = []
    for r in RELATED[slug][:5]:
        if r not in META:
            continue
        emoji, name, subtitle = META[r]
        cards.append(
            f'    <a href="{r}.html" style="display:block;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:20px;color:inherit;text-decoration:none;transition:border-color .2s">\n'
            f'      <div style="font-size:24px;margin-bottom:8px">{emoji}</div>\n'
            f'      <div style="font-weight:700;font-size:.9rem;margin-bottom:4px">{name}</div>\n'
            f'      <div style="font-size:.8rem;opacity:.6">{subtitle}</div>\n'
            f'    </a>'
        )
    cards_html = '\n'.join(cards)
    return (
        '  <section style="margin-bottom:3rem">\n'
        '    <p style="text-transform:uppercase;letter-spacing:.1em;font-size:.75rem;opacity:.5;margin-bottom:.5rem">Explore More</p>\n'
        '    <h2 style="font-size:clamp(1.4rem,2.5vw,2rem);font-weight:700;margin-bottom:1.5rem">Related Industries We Serve in New York</h2>\n'
        '    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:1rem">\n'
        f'{cards_html}\n'
        '    </div>\n'
        '    <p style="font-size:13px;opacity:.5">Browse all <a href="../industries" style="text-decoration:underline">74 industries we serve in New York →</a></p>\n'
        '  </section>'
    )


processed = 0
skipped = 0

for slug in META:
    html_file = BASE / f'{slug}.html'
    if not html_file.exists():
        print(f'  SKIP (no file): {slug}')
        skipped += 1
        continue

    content = html_file.read_text(encoding='utf-8')

    if 'What other industries does Vora serve' in content:
        print(f'  SKIP (already done): {slug}')
        skipped += 1
        continue

    if MARKER_NEW in content:
        faq6 = build_faq6_new(slug)
        related = build_related_new(slug)
        replacement = f'{faq6}\n    </div>\n  </div>\n</section>\n\n{related}\n<section class="cta-section">'
        content = content.replace(MARKER_NEW, replacement, 1)
        html_file.write_text(content, encoding='utf-8')
        print(f'  OK (new): {slug}')
        processed += 1

    elif MARKER_OLD in content:
        faq6 = build_faq6_old(slug)
        related = build_related_old(slug)
        replacement = f'{faq6}\n    </div>\n  </section>\n\n{related}\n\n  <div class="cta-band">'
        content = content.replace(MARKER_OLD, replacement, 1)
        html_file.write_text(content, encoding='utf-8')
        print(f'  OK (old): {slug}')
        processed += 1

    else:
        print(f'  SKIP (marker not found): {slug}')
        skipped += 1

print(f'\nDone: {processed} updated, {skipped} skipped.')
