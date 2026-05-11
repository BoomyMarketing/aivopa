#!/usr/bin/env python3
import os, re

INDUSTRIES_DIR = os.path.join(os.path.dirname(__file__), "industries")

NEW_FONTS = '''  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" as="style" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" /></noscript>'''

NEW_CSS = '''<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--primary:#0070F3;--primary-dark:#0052CC;--bg:#FFFFFF;--bg-soft:#F7F9FC;--bg-blue:#EEF4FF;--text:#0A0A0F;--muted:#6B7280;--font-heading:'Space Grotesk',sans-serif;--font-body:'Inter',sans-serif;--radius:10px;--transition:0.3s cubic-bezier(0.4,0,0.2,1)}
body{font-family:var(--font-body);color:var(--text);background:var(--bg);line-height:1.6;overflow-x:hidden}
a{color:inherit;text-decoration:none}
.navbar{position:fixed;top:0;left:0;right:0;z-index:500;background:rgba(255,255,255,0.97);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border-bottom:1px solid rgba(0,112,243,0.1);transition:background var(--transition),box-shadow var(--transition)}
.nav-inner{height:64px;padding:0 24px;display:flex;align-items:center;justify-content:space-between}
.navbar.scrolled{background:rgba(255,255,255,0.97);box-shadow:0 2px 20px rgba(0,112,243,0.08)}
.nav-hamburger{display:none;background:none;border:none;padding:0;flex-direction:column;gap:5px;cursor:pointer}
.nav-hamburger span{display:block;width:24px;height:2px;background:#374151;border-radius:2px}
.mobile-menu{display:none;position:absolute;top:100%;left:0;right:0;background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.1);padding:1.5rem;flex-direction:column;gap:.5rem;border-bottom:1px solid rgba(0,112,243,0.1)}
.mobile-menu.open{display:flex}
.mobile-menu a{font-size:.9rem;font-weight:500;color:#374151;padding:.65rem 0;border-bottom:1px solid rgba(0,0,0,.06);transition:color .3s}
.mobile-menu a:last-child{color:#fff!important;background:var(--primary);border:none;padding:10px 22px;border-radius:8px;text-align:center;font-weight:700;margin-top:.5rem;display:flex;justify-content:center}
.nav-logo{font-family:var(--font-heading);font-size:1.5rem;color:var(--text);letter-spacing:-.03em}
.nav-logo span{color:var(--primary)}
.nav-links{display:flex;gap:2.5rem;list-style:none}
.nav-links a{font-size:.875rem;font-weight:500;color:#374151;position:relative;padding-bottom:2px}
.nav-links a::after{content:'';position:absolute;bottom:0;left:0;width:0;height:1.5px;background:var(--primary);transition:width .3s ease}
.nav-links a:hover::after{width:100%}
.nav-cta{font-size:.85rem;font-weight:700;color:#fff!important;background:var(--primary)!important;padding:10px 22px!important;border-radius:8px;display:inline-flex!important;align-items:center;justify-content:center;line-height:1;transition:background var(--transition)}
.nav-cta:hover{background:var(--primary-dark)!important}
@media(max-width:640px){.nav-links,.nav-cta{display:none!important}.nav-hamburger{display:flex}}
.page-hero{background:linear-gradient(135deg,#0A0A0F 0%,#0d1a3a 60%,#0A0A0F 100%);color:#fff;padding:9rem 2rem 5rem;min-height:480px;display:flex;align-items:center;justify-content:center;text-align:center}
.page-hero>div{max-width:860px;width:100%}
.breadcrumb{font-size:.8rem;color:rgba(255,255,255,.5);margin-bottom:1.25rem;display:flex;align-items:center;justify-content:center;gap:.4rem}
.breadcrumb a{color:rgba(255,255,255,.5)}
.breadcrumb a:hover{color:#fff}
.breadcrumb span{opacity:.5}
.hero-tag{display:inline-block;background:rgba(0,112,243,.2);color:var(--primary);border:1px solid rgba(0,112,243,.35);border-radius:20px;padding:.3rem .9rem;font-size:.78rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin-bottom:1.2rem}
.page-hero h1{font-family:var(--font-heading);font-size:clamp(2rem,4.5vw,3.2rem);font-weight:700;line-height:1.18;letter-spacing:-.03em;margin:0 auto 1.25rem}
.page-hero h1 em{font-style:normal;color:var(--primary);background:none;-webkit-text-fill-color:unset}
.page-hero__sub{font-size:1.05rem;color:rgba(255,255,255,.75);max-width:620px;margin:0 auto 2.5rem;line-height:1.7}
.hero-stats{display:flex;gap:2.5rem;flex-wrap:wrap;justify-content:center}
.hs{display:flex;flex-direction:column;gap:.2rem}
.hs strong{font-size:1.6rem;font-weight:700;color:var(--primary);font-family:var(--font-heading)}
.hs span{font-size:.8rem;color:rgba(255,255,255,.6)}
main{max-width:1180px;margin:0 auto;padding:0 5%}
section{padding:80px 0}
section+section{border-top:1px solid rgba(0,112,243,.08)}
.section-label{font-size:.75rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--primary);margin-bottom:.75rem}
.section-heading{font-family:var(--font-heading);font-size:clamp(1.5rem,3vw,2.2rem);font-weight:700;letter-spacing:-.025em;margin-bottom:1rem}
.section-body{font-size:1rem;color:var(--muted);max-width:640px;line-height:1.75;margin-bottom:2.5rem}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.25rem}
.card{background:var(--bg-soft);border:1px solid rgba(0,112,243,.08);border-radius:var(--radius);padding:1.5rem;transition:box-shadow var(--transition),transform var(--transition)}
.card:hover{box-shadow:0 8px 32px rgba(0,112,243,.1);transform:translateY(-2px)}
.card.feat{border-color:rgba(0,112,243,.25);background:var(--bg-blue)}
.card h3{font-family:var(--font-heading);font-size:1rem;font-weight:600;margin-bottom:.6rem}
.card p{font-size:.875rem;color:var(--muted);line-height:1.65}
.ci{font-size:1.5rem;margin-bottom:.75rem}
.steps{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1.25rem}
.step{display:flex;gap:1rem;align-items:flex-start}
.sn{min-width:36px;height:36px;border-radius:50%;background:rgba(0,112,243,.1);color:var(--primary);font-weight:700;font-size:.85rem;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.sc h4{font-family:var(--font-heading);font-size:.95rem;font-weight:600;margin-bottom:.3rem}
.sc p{font-size:.845rem;color:var(--muted);line-height:1.6}
.results{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem}
@media(max-width:768px){.results{grid-template-columns:repeat(2,1fr)}}
.result-card{background:var(--bg-soft);border:1px solid rgba(0,112,243,.08);border-radius:var(--radius);padding:1.5rem;text-align:center}
.result-card strong{display:block;font-family:var(--font-heading);font-size:2rem;font-weight:700;color:var(--primary);margin-bottom:.4rem}
.result-card span{font-size:.82rem;color:var(--muted)}
.faq-list{display:flex;flex-direction:column;gap:.75rem}
.faq-item{background:var(--bg-soft);border:1px solid rgba(0,112,243,.08);border-radius:var(--radius);overflow:hidden}
.faq-q{padding:1.1rem 1.25rem;font-family:var(--font-heading);font-weight:600;font-size:.95rem;cursor:pointer;display:flex;justify-content:space-between;align-items:center;user-select:none}
.faq-q::after{content:'+';font-size:1.1rem;color:var(--primary);transition:transform .25s}
.faq-item.open .faq-q::after{transform:rotate(45deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease,padding .25s}
.faq-item.open .faq-a{max-height:400px;padding:0 1.25rem 1.1rem}
.faq-a p{font-size:.9rem;color:var(--muted);line-height:1.7}
.cta-band{background:linear-gradient(135deg,var(--primary) 0%,var(--primary-dark) 100%);border-radius:16px;padding:3rem;text-align:center;margin:80px 0;color:#fff}
.cta-band h2{font-family:var(--font-heading);font-size:clamp(1.5rem,3vw,2rem);font-weight:700;margin-bottom:.75rem}
.cta-band p{color:rgba(255,255,255,.85);margin-bottom:1.75rem}
.btn{display:inline-block;background:#fff;color:var(--primary);padding:.8rem 2rem;border-radius:8px;font-weight:700;font-size:.95rem;transition:opacity .2s}
.btn:hover{opacity:.92}
footer{background:#0a0a0a;color:#ccc;padding:4rem 5% 2rem}
.fi{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2rem;margin-bottom:3rem}
@media(max-width:860px){.fi{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.fi{grid-template-columns:1fr}}
.fb{font-family:var(--font-heading);font-weight:700;font-size:1.2rem;letter-spacing:-.02em;margin-bottom:.75rem;color:#fff}
.ft{font-size:.85rem;color:#999;line-height:1.7}
.ft-tag{font-weight:600;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;color:#fff;margin-bottom:.75rem}
.fl{list-style:none;display:flex;flex-direction:column;gap:.5rem}
.fl a{font-size:.85rem;color:#999;transition:color .2s}
.fl a:hover{color:var(--primary)}
.fc{font-size:.8rem;color:#666;text-align:center;padding-top:2rem;border-top:1px solid rgba(255,255,255,.08)}
.related-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:1rem}
@media(max-width:640px){.related-grid{grid-template-columns:1fr 1fr}}
</style>'''

NEW_NAV = '''<nav class="navbar" id="nb">
  <div class="nav-inner">
    <a href="../index.html" class="nav-logo">Vo<span>r</span>a</a>
    <div class="nav-links">
      <a href="../services.html">Services</a>
      <a href="../industries.html">Industries</a>
      <a href="../about.html">About</a>
      <a href="../contact.html">Contact</a>
    </div>
    <button class="nav-hamburger" id="hamburger" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <a href="../contact.html" class="nav-cta">Get a Proposal</a>
  </div>
  <div class="mobile-menu" id="mobile-menu" aria-hidden="true">
    <a href="../services.html">Services</a>
    <a href="../industries.html">Industries</a>
    <a href="../about.html">About</a>
    <a href="../contact.html">Contact</a>
    <a href="../contact.html">Get a Proposal</a>
  </div>
</nav>'''

NEW_SCRIPT = '''<script>
const nb=document.getElementById('nb');
window.addEventListener('scroll',()=>{nb.classList.toggle('scrolled',window.scrollY>40)});
const hamburger=document.getElementById('hamburger');
const mobileMenu=document.getElementById('mobile-menu');
if(hamburger&&mobileMenu){hamburger.addEventListener('click',()=>{const open=mobileMenu.classList.toggle('open');hamburger.setAttribute('aria-expanded',String(open));mobileMenu.setAttribute('aria-hidden',String(!open))});}
document.querySelectorAll('.faq-q').forEach(q=>{q.addEventListener('click',()=>{const i=q.parentElement,o=i.classList.contains('open');document.querySelectorAll('.faq-item').forEach(x=>x.classList.remove('open'));if(!o)i.classList.add('open')})});
</script>'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. Replace font loading (Inter only → Space Grotesk + Inter)
    content = re.sub(
        r'<link rel="preload"[^>]*Inter[^>]*/>\s*<noscript><link rel="stylesheet"[^>]*Inter[^>]*/></noscript>',
        NEW_FONTS,
        content,
        flags=re.DOTALL
    )

    # 2. Replace <style> block
    content = re.sub(
        r'<style>.*?</style>',
        NEW_CSS,
        content,
        count=1,
        flags=re.DOTALL
    )

    # 3. Replace <nav class="navbar"...> block
    content = re.sub(
        r'<nav class="navbar"[^>]*>.*?</nav>',
        NEW_NAV,
        content,
        count=1,
        flags=re.DOTALL
    )

    # 4. Fix dark inline styles in "Related Industries" section
    content = content.replace('background:rgba(255,255,255,.04)', 'background:#F7F9FC')
    content = content.replace('border:1px solid rgba(255,255,255,.1)', 'border:1px solid rgba(0,112,243,0.1)')
    # Fix 3-col grid → responsive class
    content = content.replace(
        'style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:1rem"',
        'class="related-grid"'
    )

    # 5. Fix var(--accent) → var(--primary) in footer logo
    content = content.replace('color:var(--accent)', 'color:var(--primary)')

    # 6. Replace script block at bottom
    content = re.sub(
        r'<script>\s*const nb=document\.getElementById\(\'nb\'\).*?</script>',
        NEW_SCRIPT,
        content,
        count=1,
        flags=re.DOTALL
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated = []
skipped = []

for fname in sorted(os.listdir(INDUSTRIES_DIR)):
    if fname.endswith('.html') and fname != 'index.html':
        fpath = os.path.join(INDUSTRIES_DIR, fname)
        if process_file(fpath):
            updated.append(fname)
        else:
            skipped.append(fname)

print(f"Updated: {len(updated)} files")
if skipped:
    print(f"No match (check manually): {skipped}")
