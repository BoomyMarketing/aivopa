#!/usr/bin/env python3
"""Generate TikTok Ads Agency local pages for 17 missing cities."""
import os, re, shutil

BASE = os.path.dirname(__file__)
LOCAL = os.path.join(BASE, 'local')
TEMPLATE_DIR = os.path.join(LOCAL, 'new-york', 'tiktok-ads-agency')

CITIES = [
    # (slug, display_name, state_abbr, zip, street, nearby3)
    ('albuquerque', 'Albuquerque', 'NM', '87102', '201 Third St NW',
     ['dallas', 'phoenix', 'denver']),
    ('arlington', 'Arlington', 'TX', '76010', '101 W Abram St',
     ['dallas', 'houston', 'austin']),
    ('atlanta', 'Atlanta', 'GA', '30303', '55 Trinity Ave SW',
     ['charlotte', 'miami', 'nashville']),
    ('austin', 'Austin', 'TX', '78701', '301 W 2nd St',
     ['dallas', 'houston', 'san-antonio']),
    ('bakersfield', 'Bakersfield', 'CA', '93301', '1501 Truxtun Ave',
     ['los-angeles', 'san-diego', 'san-francisco']),
    ('boston', 'Boston', 'MA', '02110', '1 Financial Center',
     ['new-york', 'chicago', 'miami']),
    ('charlotte', 'Charlotte', 'NC', '28202', '600 E Trade St',
     ['atlanta', 'miami', 'nashville']),
    ('cincinnati', 'Cincinnati', 'OH', '45202', '525 Vine St',
     ['chicago', 'cleveland', 'nashville']),
    ('cleveland', 'Cleveland', 'OH', '44114', '601 Lakeside Ave E',
     ['chicago', 'cincinnati', 'new-york']),
    ('dallas', 'Dallas', 'TX', '75201', '1601 Elm St',
     ['houston', 'austin', 'arlington']),
    ('denver', 'Denver', 'CO', '80202', '1700 Lincoln St',
     ['phoenix', 'seattle', 'austin']),
    ('nashville', 'Nashville', 'TN', '37201', '1 Public Square',
     ['atlanta', 'charlotte', 'chicago']),
    ('phoenix', 'Phoenix', 'AZ', '85004', '200 W Washington St',
     ['los-angeles', 'denver', 'san-diego']),
    ('portland', 'Portland', 'OR', '97201', '1120 SW 5th Ave',
     ['seattle', 'san-francisco', 'denver']),
    ('san-diego', 'San Diego', 'CA', '92101', '202 C St',
     ['los-angeles', 'phoenix', 'san-francisco']),
    ('san-francisco', 'San Francisco', 'CA', '94105', '1 Dr Carlton B Goodlett Pl',
     ['los-angeles', 'san-diego', 'portland']),
    ('seattle', 'Seattle', 'WA', '98101', '600 4th Ave',
     ['portland', 'san-francisco', 'denver']),
]

# City display names for nearby link labels
CITY_NAMES = {
    'new-york': 'New York',
    'chicago': 'Chicago',
    'los-angeles': 'Los Angeles',
    'miami': 'Miami',
    'houston': 'Houston',
    'dallas': 'Dallas',
    'austin': 'Austin',
    'arlington': 'Arlington',
    'atlanta': 'Atlanta',
    'boston': 'Boston',
    'charlotte': 'Charlotte',
    'cincinnati': 'Cincinnati',
    'cleveland': 'Cleveland',
    'albuquerque': 'Albuquerque',
    'bakersfield': 'Bakersfield',
    'denver': 'Denver',
    'nashville': 'Nashville',
    'phoenix': 'Phoenix',
    'portland': 'Portland',
    'san-antonio': 'San Antonio',
    'san-diego': 'San Diego',
    'san-francisco': 'San Francisco',
    'seattle': 'Seattle',
}

def make_nearby_html(nearby3):
    items = []
    for slug in nearby3:
        name = CITY_NAMES.get(slug, slug.replace('-', ' ').title())
        items.append(
            f'  <li><a href="https://aivopa.com/local/{slug}/tiktok-ads-agency">TikTok Ads Agency in {name}</a></li>'
        )
    return '\n'.join(items)

def generate(slug, name, state, zipcode, street, nearby3):
    with open(os.path.join(TEMPLATE_DIR, 'index.html'), encoding='utf-8') as f:
        html = f.read()

    # Replace city name (order matters: longest first)
    html = html.replace('New York', name)
    html = html.replace('new-york', slug)

    # Fix state in schema address
    html = html.replace('"addressRegion": "NY"', f'"addressRegion": "{state}"')
    html = html.replace('"postalCode": "10118"', f'"postalCode": "{zipcode}"')
    html = html.replace('"streetAddress": "350 Fifth Avenue"', f'"streetAddress": "{street}"')
    html = html.replace('"addressLocality": "' + name + '"', f'"addressLocality": "{name}"')

    # Replace nearby cities block
    html = re.sub(
        r'(<ul class="nearby-cities">)\s*.*?\s*(</ul>)',
        lambda m: m.group(1) + '\n' + make_nearby_html(nearby3) + '\n                </ul>',
        html,
        count=1,
        flags=re.DOTALL
    )

    # Write file
    dest_dir = os.path.join(LOCAL, slug, 'tiktok-ads-agency')
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, 'index.html')
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(html)
    return dest

created = 0
for city_data in CITIES:
    slug = city_data[0]
    dest_dir = os.path.join(LOCAL, slug, 'tiktok-ads-agency')
    if os.path.exists(os.path.join(dest_dir, 'index.html')):
        print(f'skip (exists): {slug}')
        continue
    path = generate(*city_data)
    print(f'created: {path}')
    created += 1

print(f'\nDone. Created {created} pages.')
