import json,os
BASE="/boyle-heights-family-dentistry/"
ORIGIN="https://answerfirstai-ai.github.io"
NAME="Boyle Heights Family Dentistry"
TEL="+13232688308"; PH="(323) 268-8308"
ADDR="482 N St Louis St, Los Angeles, CA 90033"
MAPS="https://www.google.com/maps?ftid=0x80c2c60928d2bdad:0x53dfda274f12f146"
DIR="https://www.google.com/maps/dir/?api=1&amp;destination=482+N+St+Louis+St%2C+Los+Angeles%2C+CA+90033"
EMBED="https://www.google.com/maps?q=482+N+St+Louis+St,+Los+Angeles,+CA+90033&amp;output=embed"
TILES=open('hero_tiles.svgfrag').read()
N=lambda s:f'<span class="need">[NEED: {s}]</span>'
PHONE='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
def call(label=None,cls="btn big"): return f'<a class="{cls}" href="tel:{TEL}">{PHONE}<span>{label or "Call "+PH}</span></a>'
schema={"@context":"https://schema.org","@type":"Dentist","@id":ORIGIN+BASE+"#practice","name":NAME,"url":ORIGIN+BASE,"telephone":"+1-323-268-8308",
 "image":ORIGIN+BASE+"img/og.png","logo":ORIGIN+BASE+"img/apple-touch-icon.png",
 "address":{"@type":"PostalAddress","streetAddress":"482 N St Louis St","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90033","addressCountry":"US"},
 "areaServed":["Boyle Heights","East Los Angeles","Lincoln Heights"],"hasMap":MAPS,
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"09:00","closes":"18:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"15:00"}]}
HOURS=[(1,"Monday","9 AM – 6 PM"),(2,"Tuesday","9 AM – 6 PM"),(3,"Wednesday","9 AM – 6 PM"),(4,"Thursday","9 AM – 6 PM"),(5,"Friday","Closed"),(6,"Saturday","9 AM – 3 PM"),(0,"Sunday","Closed")]
def hours():
    li="".join(f'<li data-day="{d}"{" class=closed" if v=="Closed" else ""}><span>{n}</span><span>{v}</span></li>' for d,n,v in HOURS)
    return f'<p class="status" aria-live="polite"><i></i><b>Hours from our Google listing</b></p><ul class="hours">{li}</ul><p class="small">Hours from our Google listing (Friday shown closed); please call {PH} to confirm. {N("confirm hours with the office — an older directory lists Mon–Fri 9–5")}</p>'
PRE=f'<link rel="preload" as="image" type="image/avif" imagesrcset="{BASE}img/hero-1440.avif 1440w, {BASE}img/hero-2880.avif 2880w" imagesizes="100vw" media="(min-width:701px)" fetchpriority="high"><link rel="preload" as="image" type="image/avif" imagesrcset="{BASE}img/hero-m-800.avif 800w, {BASE}img/hero-m-1600.avif 1600w" imagesizes="100vw" media="(max-width:700px)" fetchpriority="high">'
def page(path,title,desc,body,cur,noindex=False):
    url=ORIGIN+BASE+path
    nav="".join(f'<li><a href="{BASE}{p}"{" aria-current=page" if p==cur else ""}>{l}</a></li>' for p,l in (("","Home"),("services/","Services"),("visit/","Visit")))
    ld='' if noindex else f'<script type="application/ld+json">{json.dumps(schema)}</script>'
    head_seo='<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">{head_seo}
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{ORIGIN+BASE}img/og.png"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2F6B4F"><link rel="icon" href="{BASE}img/favicon.svg" type="image/svg+xml"><link rel="icon" href="{BASE}favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="{BASE}img/apple-touch-icon.png">
<link rel="preload" href="{BASE}fonts/Figtree-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{BASE}fonts/YoungSerif-400.woff2" as="font" type="font/woff2" crossorigin>
{PRE if path=="" else ""}<link rel="stylesheet" href="{BASE}css/site.css">{ld}</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="hdr"><a class="mark" href="{BASE}"><img src="{BASE}img/favicon.svg" width="34" height="34" alt=""><span>Boyle Heights<br>Family Dentistry</span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="mainnav">Menu</button><nav class="main" id="mainnav" aria-label="Main"><ul>{nav}</ul></nav><a class="btn hdr-call" href="tel:{TEL}" aria-label="Call {PH}">{PHONE}<span class="l-full">{PH}</span><span class="l-short">Call</span></a></div><div class="band" aria-hidden="true"></div></header>
<main id="main">{body}</main>
<div class="band" aria-hidden="true"></div>
<footer class="site plaque-band"><div class="wrap">
<div class="plaque"><p class="pl-name">{NAME}</p><p class="pl-call"><a href="tel:{TEL}">Call {PH}.</a></p><p class="pl-addr">{ADDR} {N("confirm address")}</p></div>
<div class="cols">
<div><h2>Hours</h2><p>Mon-Thu 9 AM-6 PM<br>Saturday 9 AM-3 PM<br>Closed Friday &amp; Sunday (per Google)</p><p class="small fn">Our Google listing shows Fridays closed; please call {PH} to confirm hours.</p></div>
<div><h2>Pages</h2><p><a href="{BASE}">Home</a><br><a href="{BASE}services/">Services</a><br><a href="{BASE}visit/">Visit &amp; directions</a></p></div>
<div><h2>Directions</h2><p><a href="{DIR}" rel="noopener">Get directions</a><br><a href="{MAPS}" rel="noopener">Google listing</a></p></div>
</div><p class="small fn" style="margin-top:2rem">© 2026 {NAME}. The tile is an original illustration. Hero tile wall is an illustrative scene, not a photo of the office.</p></div></footer>
<div class="sticky-call"><a class="btn big" href="tel:{TEL}">{PHONE}<span>Call {PH}</span></a></div>
<script src="{BASE}js/gsap.min.js" defer></script><script src="{BASE}js/ScrollTrigger.min.js" defer></script><script src="{BASE}js/site.js" defer></script>
</body></html>'''
def hero(h1,sub,extra=""): return f'<section class="hero page-hero">{extra}<h1>{h1}</h1><p class="sub">{sub}</p><div>{call()}</div></section>'
SMS='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M4 3h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H8l-5 4V4a1 1 0 0 1 1-1z"/></svg>'
PIN='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a7 7 0 0 1 7 7c0 5-7 13-7 13S5 14 5 9a7 7 0 0 1 7-7zm0 4.5A2.5 2.5 0 1 0 12 11.5 2.5 2.5 0 0 0 12 6.5z"/></svg>'
FORM=f'''<h2>Two ways to reach us</h2><p>Tap one. Call {PH}, or get directions to {ADDR}.</p>
<div class="reach"><a class="btn big" href="tel:{TEL}">{PHONE}<span>Call {PH}</span></a>
<a class="btn big ghost" href="{DIR}" rel="noopener">{PIN}<span>Get directions</span></a></div>
'''
MAP=f'<div class="map"><iframe title="Map to {NAME}" src="{EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>'
TRUST=f'<ul class="trust"><li>Mon–Thu 9–6 · Sat 9–3 {N("confirm hours")}</li><li>Wheelchair accessible {N("confirm, directory-sourced")}</li><li><a href="{MAPS}" rel="noopener">See our reviews on Google</a></li></ul>'
HERO_IMG=f'<picture class="hero-media"><source media="(max-width:700px)" type="image/avif" srcset="{BASE}img/hero-m-800.avif 800w, {BASE}img/hero-m-1600.avif 1600w" sizes="100vw"><source media="(max-width:700px)" type="image/webp" srcset="{BASE}img/hero-m-800.webp 800w, {BASE}img/hero-m-1600.webp 1600w" sizes="100vw"><source type="image/avif" srcset="{BASE}img/hero-1440.avif 1440w, {BASE}img/hero-2880.avif 2880w" sizes="100vw"><source type="image/webp" srcset="{BASE}img/hero-1440.webp 1440w, {BASE}img/hero-2880.webp 2880w" sizes="100vw"><img src="{BASE}img/hero-1440.webp" width="1440" height="810" fetchpriority="high" decoding="async" alt="Illustrative: a wall of hand-glazed tiles in green and rose with an original pattern, set in limewash, in raking afternoon light. Not a photo of the office."></picture><span class="hero-label">Illustrative scene</span>'
DAYS=[(1,"Mon","9-6"),(2,"Tue","9-6"),(3,"Wed","9-6"),(4,"Thu","9-6"),(5,"Fri","Closed"),(6,"Sat","9-3"),(0,"Sun","Closed")]
TILEROW='<ul class="hours tilerow" role="list">'+"".join(f'<li data-day="{d}" class="ht{" closed" if v=="Closed" else ""}"><b>{n}</b><span>{v}</span></li>' for d,n,v in DAYS)+'</ul>'
home=f'''<section class="hero photo-hero">{HERO_IMG}<div class="hero-in"><span class="eyebrow">Family dentist · Boyle Heights, LA 90033</span>
<h1>Your family dentist on St Louis Street.</h1><p class="sub">A small practice near the corner of Cesar Chavez.</p><div class="cta-line">{call()}<a class="tlink" href="#hours">Hours</a></div></div></section>
<section class="grout" id="hours" aria-labelledby="hh"><div class="wrap"><h2 id="hh">Hours</h2><p class="status" aria-live="polite"><i></i><b>Hours from our Google listing</b></p>{TILEROW}<p>Google lists Mon-Thu 9-6, Sat 9-3, closed Fri. Call to confirm. {N("confirm hours with the office; an older directory lists Mon-Fri 9-5")}</p></div></section>
<div class="band" aria-hidden="true"></div>
<section class="green-wall" aria-labelledby="wd"><div class="wrap wd-grid"><div class="feature-tile"><span>General dentistry</span></div><div><h2 id="wd">What we do</h2><p>General dentistry for the whole family. Call to ask about anything else. {N("services")}</p><div class="cta-line">{call("Call "+PH,"btn light")}<a class="tlink light" href="{BASE}services/">About our services</a></div></div></div></section>
<div class="band" aria-hidden="true"></div>
<section class="grout" aria-labelledby="bf"><div class="wrap"><h2 id="bf">Before your first visit</h2>
<dl class="rows"><div><dt>Insurance</dt><dd>Call and we'll check your plan. {N("accepted plans")}</dd></div><div><dt>Friday</dt><dd>Closed Fridays, per Google. Call <a href="tel:{TEL}">{PH}</a> to confirm.</dd></div><div><dt>Parking</dt><dd>{N("parking info")}</dd></div><div><dt>Accessibility</dt><dd>A directory lists the office as wheelchair accessible. {N("confirm")}</dd></div></dl></div></section>
<section class="grout limewash" aria-labelledby="vs"><div class="wrap split"><div><h2 id="vs">St Louis St, Boyle Heights</h2><p>482 N St Louis St (some directories list 2110 E Cesar E Chavez Ave, likely the same corner). {N("confirm address and entrance")}</p>
<div class="cta-line"><a class="btn" href="{DIR}" rel="noopener">{PIN}<span>Get directions</span></a><a class="btn ghost" href="tel:{TEL}">Call {PH}</a></div></div>
<div class="tile-frame"><div class="map-ph" data-map="{EMBED}"><p><b>482 N St Louis St</b><br>near Cesar E Chavez Ave</p><button class="btn ghost" type="button" data-load-map>Load map</button><p class="small">The map loads from Google when you ask.</p></div></div></div></section>'''
services=hero("Services","Everyday dental care for every age.")+f'''
<section><div class="wrap prose"><h2>General dentistry</h2><p>Checkups and family dental care for kids, parents and grandparents. Call to ask about the care you need.</p>
<h3>More services</h3><p>We only list services the office has confirmed. {N("confirm services, e.g. cleanings, fillings, extractions, crowns")}</p>
<h3>Tooth pain</h3><p>Call and we'll find you a time. {N("confirm same-day/urgent availability")}</p>
<h3>Insurance</h3><p>Ask about your insurance when you call. {N("accepted plans")}</p>
<div class="cta-line">{call("Call "+PH,"btn")}<a class="btn ghost" href="{BASE}visit/">Hours &amp; directions</a></div></div></section>'''
visit=hero("Visit us",ADDR)+f'''
<section><div class="wrap split"><div><h2>Hours</h2>{hours()}</div>{MAP}</div></section>
<section class="alt"><div class="wrap split"><div class="prose"><h2>Getting here</h2><p>On St Louis St near Cesar E Chavez Ave, Boyle Heights. {N("confirm entrance")}</p>
<h3>Parking</h3><p>{N("parking info")}</p><h3>Accessibility</h3><p>A directory lists the office as wheelchair accessible. {N("confirm")}</p>
<div class="cta-line"><a class="btn" href="{DIR}" rel="noopener">Get directions</a></div></div><div>{FORM}</div></div></section>'''
nf=f'<section class="hero page-hero"><h1>This page isn\'t here.</h1><p class="sub">Let\'s get you back.</p><div class="cta-line" style="justify-content:center"><a class="btn ghost" href="{BASE}">Home</a>{call("Call "+PH,"btn")}</div></section>'
os.makedirs('services',exist_ok=True);os.makedirs('visit',exist_ok=True)
open('index.html','w').write(page("","Boyle Heights Family Dentistry | Family Dentist in Boyle Heights, LA","Neighborhood family dentist on St Louis St in Boyle Heights, LA 90033. Call (323) 268-8308 to book.",home,""))
open('services/index.html','w').write(page("services/","Dental Services | Boyle Heights Family Dentistry, LA 90033","General and family dentistry in Boyle Heights, Los Angeles. Ask about your insurance: call (323) 268-8308.",services,"services/"))
open('visit/index.html','w').write(page("visit/","Hours & Directions | Boyle Heights Family Dentistry","Find Boyle Heights Family Dentistry at 482 N St Louis St, Los Angeles 90033. Hours, map and directions.",visit,"visit/"))
open('404.html','w').write(page("404.html","Page not found | Boyle Heights Family Dentistry","Page not found.",nf,"",noindex=True))
sm="".join(f"<url><loc>{ORIGIN+BASE+p}</loc><lastmod>2026-10-22</lastmod></url>" for p in ("","services/","visit/"))
open('sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
open('robots.txt','w').write(f"User-agent: *\nAllow: /\nSitemap: {ORIGIN+BASE}sitemap.xml\n")
open('.nojekyll','w').write('')
