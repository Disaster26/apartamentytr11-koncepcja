import os, json, html
d = os.path.dirname(os.path.abspath(__file__))
r = lambda f: open(os.path.join(d, f), encoding='utf-8').read()

# nr, typ, zdjecia (plik, opis), cena tydzien, weekend, doplata, wyroznienie
AP = [
    (1, '1 pokój · 2 osoby', [('a1-1', 'Apartament nr 1: łóżka w tropikalne wzory i stolik przy oknach'), ('a1-2', 'Apartament nr 1: zielona ściana i żółte zagłówki')], '280 zł', '350 zł', '', 'Booking.com 9,6 · Traveller Review Awards 2026'),
    (2, '1 pokój · do 4 osób', [('a2-1', 'Apartament nr 2: aneks kuchenny i stół'), ('a2-2', 'Apartament nr 2: sypialnia z kanapą i stołem')], '280 zł', '350 zł', 'Kolejna osoba: 125 zł, w weekend 150 zł', ''),
    (3, '1 pokój · 2 osoby', [('a3-1', 'Apartament nr 3: granatowa ściana ze złotymi liniami'), ('a3-2', 'Apartament nr 3: łóżko i okna na Stare Miasto')], '280 zł', '350 zł', '', ''),
    (4, '2 pokoje · do 8 osób', [('a4-1', 'Apartament nr 4: salon z aneksem kuchennym'), ('a4-2', 'Apartament nr 4: sypialnia z łóżkami piętrowymi'), ('a4-3', 'Apartament nr 4: drugi pokój ze stołem'), ('a4-4', 'Apartament nr 4: łazienka z wanną')], '300 zł', '380 zł', 'Kolejna osoba: 125 zł, w weekend 150 zł', ''),
    (5, '1 pokój · 2 osoby', [('a5-1', 'Apartament nr 5: pokój na poddaszu ze stolikiem'), ('a5-2', 'Apartament nr 5: aneks kuchenny'), ('a5-3', 'Apartament nr 5: łóżko przy granatowej ścianie')], '280 zł', '350 zł', '', 'Booking.com 9,7 · Traveller Review Awards 2025'),
    (6, '2 pokoje · do 8 osób', [('a6-1', 'Apartament nr 6: salon na poddaszu z niebieską kanapą'), ('a6-2', 'Apartament nr 6: pokój z łóżkami piętrowymi'), ('a6-3', 'Apartament nr 6: drugi pokój ze stołem')], '300 zł', '380 zł', 'Kolejna osoba: 125 zł, w weekend 150 zł', ''),
]

def big(n):
    for w in (1600, 800):
        if os.path.exists(os.path.join(d, 'img', f'{n}-{w}.webp')):
            return f'img/{n}-{w}.webp'

karty = []
for nr, typ, fot, c1, c2, dop, wyr in AP:
    gal = html.escape(json.dumps([[big(n), a] for n, a in fot], ensure_ascii=False))
    n0, a0 = fot[0]
    w = f'<p class="wyr"><svg><use href="#fan"/></svg>{wyr}</p>' if wyr else ''
    dp = f'<p class="dop">{dop}</p>' if dop else ''
    karty.append(f'''<article class="ap">
   <button class="fot" type="button" data-gal="{gal}" aria-label="Zdjęcia: apartament nr {nr}"><img src="img/{n0}-480.webp" srcset="img/{n0}-480.webp 480w, img/{n0}-800.webp 800w" sizes="(min-width:700px) 430px, 84vw" width="800" height="533" alt="{a0}" loading="lazy" decoding="async"><span class="nr">Apartament <b>{nr}</b></span><span class="ile">{len(fot)} zdjęcia</span></button>
   <div class="in">
    <h3>Apartament nr {nr}</h3>
    <p class="typ">{typ} · aneks kuchenny · łazienka</p>
    {w}
    <dl><dt>Doba, 2 osoby</dt><dd><b>{c1}</b></dd><dt>Weekend</dt><dd>{c2}</dd>{dp}</dl>
   </div>
  </article>''')

s = r('src.html')
s = s.replace('{{KARTY}}', '\n  '.join(karty))
s = s.replace('{{LOGO}}', r('logo.path').strip())
s = s.replace('{{BADGE_STYLE}}', r('badge_style.part').replace('<style>', '').replace('</style>', '').strip())
s = s.replace('{{BADGE_LINK}}', r('badge_link.part').strip())
open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(s))
