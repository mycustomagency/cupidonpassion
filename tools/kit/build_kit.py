"""Le Kit des Amoureux : génère le PDF A4 (HTML + Chromium)."""
import json, html, re
from playwright.sync_api import sync_playwright

D = json.load(open("/home/claude/kit/kit.json"))
D["rdv"][1]["items"][0] = D["rdv"][1]["items"][0].replace("le film de votre première fois ensemble", "le film de votre premier rendez-vous")
M = "file:///home/claude/cupidonpassion/tools/pinterest/cupidon-hd.png"
e = html.escape


def head(kicker, title, intro, n=None):
    num = f'<span class="secnum">{n}</span>' if n else ""
    return f'''<div class="sechead">
  <div class="medal"><img src="{M}" alt=""></div>
  <div><p class="kicker">{num}{e(kicker)}</p><h2>{e(title)}</h2><p class="intro">{e(intro)}</p></div>
</div>'''


css = r'''
@font-face{font-family:"Dancing";src:url("file:///home/claude/fonts/DancingScript.ttf")}
@font-face{font-family:"Inter";font-weight:400;src:url("file:///usr/share/fonts/opentype/inter/Inter-Regular.otf")}
@font-face{font-family:"Inter";font-weight:500;src:url("file:///usr/share/fonts/opentype/inter/Inter-Medium.otf")}
@font-face{font-family:"Inter";font-weight:700;src:url("file:///usr/share/fonts/opentype/inter/Inter-Bold.otf")}
@font-face{font-family:"Inter";font-weight:800;src:url("file:///usr/share/fonts/opentype/inter/Inter-ExtraBold.otf")}
@page{size:A4;margin:13mm 14mm 14mm}
@page full{size:A4;margin:0}
.cover,.end{page:full}
*{box-sizing:border-box}
body{margin:0;background:#fff;font-family:Inter,sans-serif;color:#1d1a3a;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;page-break-after:always}
.cover,.end{width:210mm;height:297mm;overflow:hidden;position:relative}

.foot{margin-top:8mm;text-align:center;font-size:8.5pt;color:#9a93b5;letter-spacing:.08em}
.bgh{position:absolute;color:#e8455a;opacity:.07;font-size:40pt}
/* cover */
.cover{background:radial-gradient(120% 80% at 80% 0%,#3432ca 0%,#1a1966 45%,#0d0b2e 100%);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.cover .brand{letter-spacing:.45em;font-size:10pt;color:#e5b567;font-weight:700;margin:0 0 8mm}
.cover .halo{width:110mm;height:110mm;border-radius:50%;background:radial-gradient(circle,rgba(255,143,163,.35) 0%,rgba(52,50,202,.0) 70%);display:flex;align-items:center;justify-content:center}
.cover .halo img{width:92mm}
.cover h1{font-family:Dancing;font-size:58pt;margin:4mm 0 2mm;font-weight:700;color:#fff}
.cover .sub{font-size:13pt;color:#e7e2f5;line-height:1.5;margin:0 0 10mm}
.cover .pill{background:#e8455a;color:#fff;border-radius:99px;padding:3mm 8mm;font-weight:700;font-size:11pt}
.cover .site{position:absolute;bottom:14mm;font-size:10pt;color:#c9c3da;letter-spacing:.1em}
/* section header */
.sechead{display:flex;gap:6mm;align-items:center;margin:0 0 7mm}
.medal{width:30mm;height:30mm;flex-shrink:0;border-radius:50%;background:radial-gradient(circle at 35% 30%,#3432ca 0%,#1a1966 60%,#0d0b2e 100%);border:1.2mm solid #e5b567;overflow:hidden;display:flex;align-items:center;justify-content:center;margin:1mm}
.medal img{width:23mm;display:block}
.kicker{margin:0;font-family:Dancing;font-size:20pt;color:#e8455a}
.secnum{font-family:Inter;font-weight:800;font-size:10pt;background:#e5b567;color:#0d0b2e;border-radius:99px;padding:.6mm 3mm;margin-right:3mm;vertical-align:middle}
h2{margin:1mm 0 2mm;font-size:24pt;line-height:1.1;color:#0d0b2e;font-weight:800}
.intro{margin:0;font-size:11pt;color:#4a4566;line-height:1.5}
h3{font-size:13pt;color:#fff;background:#1a1966;display:block;width:fit-content;page-break-after:avoid;padding:2mm 5mm;border-radius:99px;margin:5mm 0 4mm;break-after:avoid}
h3.c2{background:#e8455a}h3.c3{background:#c98a2e}h3.c4{background:#3432ca}h3.c5{background:#0d0b2e}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:3.2mm}
.card{background:#fbf7f1;border-radius:4mm;padding:3.6mm 4mm;display:flex;gap:3mm;align-items:flex-start;break-inside:avoid;box-shadow:0 .4mm 1.6mm rgba(13,11,46,.08);border:.3mm solid #efe7dc}
.box{width:4.6mm;height:4.6mm;border:.45mm solid #e8455a;border-radius:1.2mm;flex-shrink:0;margin-top:.4mm}
.num{font-weight:800;color:#e8455a;font-size:10pt;min-width:6mm;flex-shrink:0}
.card p{margin:0;font-size:10.2pt;line-height:1.45}
.q .card p{font-size:10.6pt}
.tp{display:grid;grid-template-columns:1fr;gap:3mm}
.tpc{background:#fbf7f1;border-radius:4mm;padding:3.2mm 4mm;display:grid;grid-template-columns:7mm 1fr 10mm 1fr;align-items:center;gap:3mm;break-inside:avoid;border:.3mm solid #efe7dc}
.tpc .a,.tpc .b{font-size:10pt;line-height:1.4;background:#fbf1f3;border-radius:3mm;padding:2.2mm 3mm;height:100%;display:flex;align-items:center}
.tpc .b{background:#eeedfb}
.ou{font-family:Dancing;font-size:16pt;color:#e8455a;text-align:center}
.bl{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm 6mm}
.bl .it{display:flex;gap:3mm;align-items:flex-start;font-size:10.4pt;line-height:1.4;padding:1.6mm 0;border-bottom:.3mm dashed #e3d9cc;break-inside:avoid}
.lines .ln{display:flex;gap:3mm;align-items:center;height:9.5mm;border-bottom:.35mm solid #d8cfc2}
.defis{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm}
.defi{background:#fbf7f1;border-radius:4mm;padding:4mm;border-top:2.2mm solid #e8455a;break-inside:avoid;box-shadow:0 .4mm 1.6mm rgba(13,11,46,.08)}
.defi:nth-child(3n+2){border-top-color:#3432ca}.defi:nth-child(3n){border-top-color:#e5b567}
.defi .m{font-size:8.5pt;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#9a93b5;margin:0}
.defi h4{margin:1mm 0 2mm;font-size:11.5pt;color:#0d0b2e}
.defi p{margin:0;font-size:9.8pt;line-height:1.45;color:#3b3658}
.defi .done{margin-top:3mm;font-size:8.5pt;color:#9a93b5;display:flex;gap:2mm;align-items:center}
.bons{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.bon{border:.6mm dashed #e8455a;border-radius:5mm;padding:4.5mm 5mm;background:#fff;position:relative;min-height:30mm;display:flex;gap:4mm;align-items:center;break-inside:avoid}
.bon img{width:17mm;flex-shrink:0}
.bon .t{font-size:8pt;letter-spacing:.3em;color:#c98a2e;font-weight:800;margin:0 0 1.5mm}
.bon .x{font-size:11.5pt;font-weight:700;line-height:1.35;margin:0;color:#0d0b2e}
.bon .s{position:absolute;right:4mm;bottom:2.5mm;font-family:Dancing;font-size:11pt;color:#e8455a}
.panel{background:#fbf7f1;border-radius:5mm;padding:6mm 7mm;margin:6mm 0;border:.3mm solid #efe7dc}
.panel h4{margin:0 0 3mm;font-size:12pt;color:#e8455a}
.panel p{margin:0 0 2.6mm;font-size:10.8pt;line-height:1.55}
.lead{font-size:12pt;line-height:1.65;margin:0 0 4mm}
.sign{font-family:Dancing;font-size:22pt;color:#e8455a;margin:6mm 0 0}
.toc{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.toc div{background:#fbf7f1;border-radius:4mm;padding:3.4mm 4mm;font-size:10.5pt;border:.3mm solid #efe7dc}
.toc b{color:#e8455a;margin-right:2mm}
.end{background:radial-gradient(120% 80% at 20% 100%,#3432ca 0%,#1a1966 45%,#0d0b2e 100%);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.end h2{color:#fff;font-family:Dancing;font-size:44pt;font-weight:700}
.end p{font-size:12.5pt;line-height:1.7;color:#e7e2f5;max-width:140mm}
.end img{width:60mm;margin-bottom:4mm}
'''

P = []
P.append(f'''<section class="page cover">
<p class="brand">CUPIDON PASSION</p>
<div class="halo"><img src="{M}" alt=""></div>
<h1>Le Kit des Amoureux</h1>
<p class="sub">52 rendez-vous, 80 questions, 40 dilemmes, 12 défis<br>et des bons à offrir pour raviver votre complicité toute l'année</p>
<span class="pill">Un cadeau qui rapproche</span>
<p class="site">cupidonpassion.com</p>
</section>''')

P.append(f'''<section class="page">
{head("Avant de commencer", "Bienvenue sur votre route à deux", "Un carnet à piocher, à cocher et à partager, au fil des saisons.")}
<p class="lead">Il paraît qu'on ne tombe amoureux qu'une fois. C'est faux. On peut retomber amoureux mille fois de la même personne, à condition de s'en donner les moyens. Ce kit est fait pour ça.</p>
<p class="lead">Vous ne trouverez ici ni grandes théories ni leçons sur le couple. Juste de quoi passer du bon temps ensemble, vous redécouvrir, rire, vous confier et rêver plus loin. Des idées à piocher un soir de semaine comme un dimanche pluvieux, à deux, sans écran et sans pression.</p>
<div class="toc">
<div><b>1</b>52 rendez-vous, un par semaine</div>
<div><b>2</b>80 questions pour se retrouver</div>
<div><b>3</b>Tu préfères : 40 dilemmes</div>
<div><b>4</b>Notre bucket list à deux</div>
<div><b>5</b>12 défis, un par mois</div>
<div><b>6</b>12 bons à offrir</div>
</div>
<div class="panel">
<h4>Comment en profiter</h4>
<p><b>Les rendez-vous</b> vous donnent une idée par semaine, classée par saison. Cochez celles que vous réalisez : le carnet devient le journal de votre année.</p>
<p><b>Les questions</b> se glissent partout : au dîner, en voiture, avant de dormir. Écoutez vraiment la réponse.</p>
<p><b>Le Tu préfères</b> se joue à deux : l'un lit, l'autre choisit et explique pourquoi, puis on inverse.</p>
<p><b>La bucket list, les défis et les bons</b> transforment vos envies en vrais moments à vivre.</p>
</div>
<p class="sign">Belle route à deux, Cupidon</p>
<p class="foot">Usage personnel. Merci de ne pas revendre ni diffuser ce kit : partagez plutôt le lien cupidonpassion.com</p>
</section>''')

# rendez-vous
cols = ["", "c2", "c3", "c4", "c5"]
body = head("52 rendez-vous à vivre", "Une idée par semaine", "Classées par saison. Cochez celles que vous réalisez.", 1)
n = 0
for i, s in enumerate(D["rdv"]):
    body += f'<h3 class="{cols[i]}">{e(s["title"])}</h3><div class="grid">'
    for it in s["items"]:
        n += 1
        body += f'<div class="card"><span class="box"></span><span class="num">{n:02d}</span><p>{e(it)}</p></div>'
    body += '</div>'
P.append(f'<section class="page flow">{body}</section>')

body = head("80 questions", "Pour se retrouver", "À poser un soir, une par une. Le secret : écouter la réponse sans préparer la sienne.", 2)
n = 0
for i, s in enumerate(D["qs"]):
    body += f'<h3 class="{cols[i % 5]}">{e(s["title"])}</h3><div class="grid q">'
    for it in s["items"]:
        n += 1
        body += f'<div class="card"><span class="num">{n:02d}</span><p>{e(it)}</p></div>'
    body += '</div>'
P.append(f'<section class="page flow">{body}</section>')

body = head("Le jeu à deux", "Tu préfères ?", "40 dilemmes à trancher. On lit, on choisit, on explique : vous allez apprendre des choses l'un sur l'autre.", 3)
body += '<div class="tp">'
for i, it in enumerate(D["tp"], 1):
    t = re.sub(r"^Tu préfères\s+", "", it).rstrip(" ?")
    parts = t.split(" ou ", 1)
    a, b = (parts + [""])[:2]
    body += f'<div class="tpc"><span class="num">{i:02d}</span><div class="a">{e(a[0].upper() + a[1:])}</div><div class="ou">ou</div><div class="b">{e(b[0].upper() + b[1:] if b else "")}</div></div>'
body += '</div>'
P.append(f'<section class="page flow">{body}</section>')

body = head("Nos rêves", "Notre bucket list à deux", "40 rêves à réaliser ensemble : un jour, bientôt, ou cette année. Cochez au fur et à mesure.", 4)
body += '<div class="bl">' + "".join(f'<div class="it"><span class="box"></span><span>{e(x)}</span></div>' for x in D["bl"]) + '</div>'
body += '<h3 class="c2" style="margin-top:8mm">Nos rêves à nous</h3><div class="lines">' + '<div class="ln"><span class="box"></span></div>' * 8 + '</div>'
P.append(f'<section class="page flow">{body}</section>')

body = head("Un fil rouge", "12 défis, un par mois", "Chaque mois, un petit engagement à tenir à deux, sans se prendre au sérieux.", 5)
body += '<div class="defis">' + "".join(f'<div class="defi"><p class="m">{d["month"]}</p><h4>{e(d["title"])}</h4><p>{e(d["text"])}</p><p class="done"><span class="box"></span>Défi relevé</p></div>' for d in D["defis"]) + '</div>'
P.append(f'<section class="page">{body}</section>')

body = head("À découper", "Vos bons pour l'autre", "À offrir ou à glisser dans une poche. Douze promesses toutes simples qui font toujours leur effet.", 6)
body += '<div class="bons">' + "".join(f'<div class="bon"><img src="{M}" alt=""><div><p class="t">BON POUR</p><p class="x">{e(b)}</p></div><span class="s">Cupidon Passion</span></div>' for b in D["bons"]) + '</div>'
P.append(f'<section class="page">{body}</section>')

P.append(f'''<section class="page end">
<img src="{M}" alt="">
<h2>À vous d'écrire la suite</h2>
<p>L'amour, ce sont mille petits moments choisis. Vous avez désormais de quoi en créer toute une année, à votre rythme, à votre façon.</p>
<p>Piochez une idée quand l'envie vient, cochez vos rêves un à un, offrez vos bons quand le cœur vous en dit. L'important n'est pas de tout faire, mais de continuer à se choisir.</p>
<p style="margin-top:8mm;font-family:Dancing;font-size:22pt;color:#ff8fa3">Belle route à deux</p>
<p style="font-size:10pt;letter-spacing:.12em;color:#c9c3da">CUPIDONPASSION.COM</p>
</section>''')

doc = f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(P)}</body></html>'
open("/home/claude/kit/kit.html", "w").write(doc)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto("file:///home/claude/kit/kit.html")
    pg.wait_for_timeout(800)
    pg.pdf(path="/home/claude/kit/Le-Kit-des-Amoureux.pdf", format="A4", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("ok")
