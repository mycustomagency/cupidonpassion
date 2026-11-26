"""Applique la mise en page V2 aux articles (couverture, corps crème, mot de Cupidon, carte à tirer, À lire aussi, Pinterest)."""
import re, os, html, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://cupidonpassion.com/"
A = {
 "idees-rendez-vous-couple": ("Rendez-vous", "60 idées de rendez-vous en couple", None, None, "rdv"),
 "questions-a-poser-en-couple": ("Complicité", "100 questions à poser en couple", None, None, "qs"),
 "tu-preferes-couple": ("Jeux", "Tu préfères : le jeu en 40 questions", None, None, "tp"),
 "jeux-de-couple-a-deux": ("Jeux", "Jeux de couple à faire à deux", None, None, "tp"),
 "retrouver-complicite-couple": ("Complicité", "Retrouver la complicité : 7 gestes simples", None, None, "qs"),
 "soiree-amoureux-maison": ("À la maison", "Soirée en amoureux à la maison", None, None, "rdv"),
 "que-faire-couple-fetes": ("Fêtes", "Que faire à deux pendant les fêtes ?", None, None, "rdv"),
 "calendrier-avent-couple": ("Noël", "Calendrier de l'Avent pour couple", None, None, "rdv"),
 "resolutions-de-couple": ("Nouvel an", "Résolutions de couple qui tiennent", None, None, "qs"),
 "idees-cadeaux-noel-couple": ("Noël", "Idées cadeaux de Noël pour un couple", None, None, "rdv"),
 "idees-cadeaux-saint-valentin-couple": ("Saint-Valentin", "Cadeaux de Saint-Valentin originaux", None, None, "rdv"),
 "idee-cadeau-couple": ("Cadeaux", "30 idées cadeaux pour un couple", None, None, "rdv"),
 "cadeau-couple-pas-cher": ("Budget", "Cadeau de couple à petit prix", None, None, "rdv"),
 "cadeau-1-an-couple": ("Anniversaire", "Quel cadeau pour 1 an de couple ?", None, None, "rdv"),
}
REL = {
 "idees-rendez-vous-couple": ["soiree-amoureux-maison", "jeux-de-couple-a-deux", "questions-a-poser-en-couple"],
 "questions-a-poser-en-couple": ["tu-preferes-couple", "retrouver-complicite-couple", "idees-rendez-vous-couple"],
 "tu-preferes-couple": ["questions-a-poser-en-couple", "jeux-de-couple-a-deux", "soiree-amoureux-maison"],
 "jeux-de-couple-a-deux": ["tu-preferes-couple", "questions-a-poser-en-couple", "soiree-amoureux-maison"],
 "retrouver-complicite-couple": ["questions-a-poser-en-couple", "idees-rendez-vous-couple", "resolutions-de-couple"],
 "soiree-amoureux-maison": ["idees-rendez-vous-couple", "jeux-de-couple-a-deux", "que-faire-couple-fetes"],
 "que-faire-couple-fetes": ["calendrier-avent-couple", "idees-cadeaux-noel-couple", "soiree-amoureux-maison"],
 "calendrier-avent-couple": ["idees-cadeaux-noel-couple", "que-faire-couple-fetes", "cadeau-couple-pas-cher"],
 "resolutions-de-couple": ["retrouver-complicite-couple", "idees-rendez-vous-couple", "questions-a-poser-en-couple"],
 "idees-cadeaux-noel-couple": ["calendrier-avent-couple", "cadeau-couple-pas-cher", "idee-cadeau-couple"],
 "idees-cadeaux-saint-valentin-couple": ["idee-cadeau-couple", "cadeau-1-an-couple", "soiree-amoureux-maison"],
 "idee-cadeau-couple": ["cadeau-couple-pas-cher", "idees-cadeaux-noel-couple", "cadeau-1-an-couple"],
 "cadeau-couple-pas-cher": ["idee-cadeau-couple", "idees-cadeaux-noel-couple", "calendrier-avent-couple"],
 "cadeau-1-an-couple": ["idee-cadeau-couple", "idees-cadeaux-saint-valentin-couple", "idees-rendez-vous-couple"],
}
PIN_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 17v5"/><path d="M9 3h6l-1 6 3 4H7l3-4z"/></svg>'

def cover(s):
    c = A[s][2] or f"{s}-1.jpg"
    return c
def thumb(s):
    t = A[s][3] or f"{s}.jpg"
    return "assets/img/blog/cards/" + t
def pin_url(s, title):
    q = urllib.parse.urlencode({"url": SITE + s + ".html", "media": SITE + "assets/img/blog/" + cover(s), "description": title + " | Cupidon Passion"})
    return "https://www.pinterest.com/pin/create/button/?" + q

for s, (tag, short, _, _, deck) in A.items():
    p = os.path.join(ROOT, s + ".html"); t = open(p, encoding="utf-8").read()
    if "art-v2" in t:
        print("déjà fait", s); continue
    h1 = re.search(r"<h1>(.*?)</h1>", t, re.S).group(1)
    title = html.unescape(re.sub("<[^>]+>", "", h1)).replace("\xa0", " ")
    t = t.replace('<article class="article wrap">', '<article class="article wrap art-v2">', 1)
    # étiquette avant le titre
    t = t.replace("<h1>", f'<span class="art-tag">{tag}</span>\n  <h1>', 1)
    # meta lecture
    metas = list(re.finditer(r'<p class="meta">([^<]*Lecture[^<]*)</p>', t))
    m = metas[0]
    t = t[:m.start()] + f'<p class="meta">{m.group(1)} · Par Cupidon</p>' + t[m.end():]
    m = re.search(r'<p class="meta">[^<]*Lecture[^<]*</p>', t)
    # retirer page-hero svg
    t = re.sub(r'\s*<div class="page-hero">.*?</div>', "", t, count=1, flags=re.S)
    # retirer la figure du corps qui reprend la couverture
    c = cover(s)
    t = re.sub(r'\s*<figure class="art-img"><img src="assets/img/blog/' + re.escape(c) + r'".*?</figure>', "", t, count=1, flags=re.S)
    alt = html.escape(title, quote=True)
    head = (f'\n  <figure class="art-cover"><img src="assets/img/blog/{c}" alt="{alt}" width="1200" height="800" fetchpriority="high">'
            f'<a class="pin-save" href="{html.escape(pin_url(s, title))}" target="_blank" rel="noopener">{PIN_SVG} Enregistrer</a></figure>'
            f'\n  <div class="art-body">')
    m = re.search(r'<p class="meta">[^<]*Lecture[^<]*</p>', t)
    t = t[:m.end()] + head + t[m.end():]
    # astuces -> le mot de Cupidon
    def tip(mm):
        inner = re.sub(r"^\s*<strong>[^<]*Astuce[^<]*</strong>\s*", "", mm.group(1))
        inner = inner[:1].upper() + inner[1:]
        return ('<div class="cupidon-says"><div class="medal"><img src="assets/cupidon.png" alt="" width="68" height="68"></div>'
                f'<div><p class="cs-title">Le mot de Cupidon 💘</p><p>{inner}</p></div></div>')
    t = re.sub(r'<div class="tip">(.*?)</div>', tip, t, flags=re.S)
    # carte à tirer au milieu
    h2s = [x.start() for x in re.finditer(r'\n\s*<h2 id=', t)]
    if len(h2s) >= 2:
        i = h2s[len(h2s) // 2]
        box = ('\n  <div class="draw-box" data-draw data-deck="' + deck + '"><p class="draw-kind">Pas d\'idée ce soir ? 🎲</p>'
               '<p class="draw-text">Laissez Cupidon tirer une carte pour vous.</p>'
               '<button type="button" class="draw-btn">Tirer une carte</button></div>')
        t = t[:i] + box + t[i:]
    # emojis offre et lettre
    t = t.replace('<p class="eyebrow">Notre cadeau à vous</p>', '<p class="eyebrow">💘 Cadeau de bienvenue</p>')
    t = t.replace('<h2>Le Kit des Amoureux, offert</h2>', '<h2>Le Kit des Amoureux, offert 🎁</h2>')
    t = t.replace('<p class="eyebrow">La lettre de Cupidon</p>', '<p class="eyebrow">💌 La lettre de Cupidon</p>')
    # fin d'article + à lire aussi + bandeau pinterest
    cards = "".join(
        f'<a class="rel-card" href="{r}.html"><div class="ri"><img src="{thumb(r)}" alt="" width="720" height="480" loading="lazy"></div>'
        f'<div class="rt"><span>{A[r][0]}</span><p>{A[r][1]}</p></div></a>' for r in REL[s])
    tail = ('\n  </div>\n</article>\n<section class="related"><p class="eyebrow-script">À lire aussi</p>'
            '<h2>Encore plus d\'idées à vivre à deux</h2><div class="rel-grid">' + cards + '</div></section>'
            '\n<section class="pin-band"><div><p>📌 Gardez ces idées sous la main pour plus tard.</p>'
            f'<a class="pin-save" href="{html.escape(pin_url(s, title))}" target="_blank" rel="noopener">{PIN_SVG} Enregistrer sur Pinterest</a></div></section>')
    t = t.replace("\n</article>", tail, 1)
    t = t.replace("</body>", '<script src="assets/cupidon-cards.js" defer></script>\n</body>', 1)
    open(p, "w", encoding="utf-8").write(t)
    print("ok", s)
