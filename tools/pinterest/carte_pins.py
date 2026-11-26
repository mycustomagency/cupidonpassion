"""Épingles Pinterest de la carte cadeau Nous Deux (série cadeau, 28/11 au 22/12)."""
import csv, datetime as dt, os, sys
from PIL import Image, ImageDraw, ImageFilter
from pins import (F, wrap, fit_title, text_block, gradient, glow, hearts, pill, footer, mascot,
                  NUIT, INDIGO, ROI, CORAIL, ROSE, OR, CREME, BLANC)

CARTE = "/home/claude/carte"
OUT = "/home/claude/cp/carte"
os.makedirs(OUT, exist_ok=True)
FRONT = Image.open(f"{CARTE}/front.png").convert("RGB")
INSIDE = Image.open(f"{CARTE}/inside.png").convert("RGB")  # face "Pour toi, pour nous" (sans le code)


def card(img, w, rot):
    h = int(img.height * w / img.width)
    c = img.resize((w, h), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", c.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w, h], 18, fill=255)
    ImageDraw.Draw(c).rounded_rectangle([1, 1, w - 2, h - 2], 18, outline=OR + (255,), width=3)
    c.putalpha(m)
    return c.rotate(rot, resample=Image.BICUBIC, expand=True)


def drop(im, c, x, y, blur=24):
    a = c.split()[3]
    sh = Image.new("RGBA", c.size, (0, 0, 0, 150))
    sh.putalpha(a.point(lambda v: v * 150 // 255))
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    layer.paste(sh, (x + 10, y + 22), sh)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    im.alpha_composite(layer)
    im.alpha_composite(c, (x, y))


def render(p, W=1000, H=1500):
    dark = p["theme"] == "nuit"
    if dark:
        im = gradient(W, H, INDIGO, NUIT).convert("RGBA")
        glow(im, int(W * .85), int(H * .12), 380, ROI, 120)
        glow(im, int(W * .1), int(H * .8), 320, CORAIL, 60)
        hearts(im, 14, p["title"], ROSE, alpha=55)
        tcol, kcol, scol = BLANC, OR, (217, 212, 228)
    else:
        im = Image.new("RGBA", (W, H), CREME + (255,))
        glow(im, int(W * .5), int(H * .6), 420, (255, 214, 222), 120)
        hearts(im, 12, p["title"], CORAIL, alpha=40)
        tcol, kcol, scol = NUIT, CORAIL, (80, 74, 110)
    d = ImageDraw.Draw(im)
    y = 80
    fk = F("lora", 44)
    kw = d.textlength(p["kicker"], font=fk)
    d.text(((W - kw) / 2, y), p["kicker"], font=fk, fill=kcol)
    y += 74
    f, lines, s = fit_title(d, p["title"].upper(), "Inter-Black", W - 140, 300, 92)
    y = text_block(d, lines, f, s, 0, y, W, tcol)
    if p.get("sub"):
        fs = F("lora", 40)
        y += 18
        y = text_block(d, wrap(d, p["sub"], fs, W - 180), fs, 40, 0, y, W, scol, 1.3)
    # les deux faces de la carte
    top = int(y) + 40
    back = card(INSIDE, 420, 8)
    front = card(FRONT, 450, -6)
    drop(im, back, 95, top + 30)
    drop(im, front, W - front.width - 85, top)
    pill(d, W / 2, H - 230, p["cta"], F("Inter-ExtraBold", 34), CORAIL, BLANC, h=80)
    footer(im, d, W, H, dark, 1.0)
    return im.convert("RGB")


CAD = "Idées cadeaux pour couple"
NOEL = "Cadeaux et Idées Noël, fêtes, moment à deux"
QJ = "Questions et jeux à deux"
PAGE = "nous-deux-le-jeu.html"

PINS = [
    dict(theme="nuit", board=NOEL, kicker="Idée cadeau de Noël", title="Une carte cadeau à glisser sous le sapin",
         sub="Nous Deux, le jeu de couple : 52 étapes à vivre ensemble", cta="Offrir le jeu",
         ptitle="Carte cadeau de Noël pour couple : offrez Nous Deux, le jeu",
         desc="Une idée cadeau de Noël pour un couple qui se vit au lieu de se ranger : Nous Deux, le jeu de couple en ligne, livré avec une jolie carte cadeau à imprimer. Vous l'écrivez, vous la glissez sous le sapin, et l'aventure commence : 52 étapes, une par semaine, avec défis, questions et rituels à deux.",
         kw="carte cadeau couple, cadeau noël couple, idée cadeau noël amoureux, cadeau à imprimer, jeu de couple cadeau"),
    dict(theme="creme", board=CAD, kicker="Cadeau de dernière minute", title="Un cadeau prêt en 5 minutes",
         sub="Vous imprimez la carte, vous écrivez votre petit mot, c'est prêt", cta="Voir la carte cadeau",
         ptitle="Cadeau de dernière minute pour couple : une carte à imprimer",
         desc="Besoin d'un cadeau de dernière minute qui fait vraiment plaisir ? Avec Nous Deux, le jeu de couple en ligne, vous recevez une carte cadeau à imprimer chez vous. Un petit mot à écrire, et vous offrez une année de complicité à vivre à deux. Pas de livraison à attendre.",
         kw="cadeau dernière minute, cadeau de dernière minute couple, carte cadeau à imprimer, cadeau couple original"),
    dict(theme="nuit", board=CAD, kicker="Pour lui, pour elle, pour vous deux", title="Offrez une année de complicité",
         sub="52 étapes, une par semaine, sur le téléphone", cta="Découvrir le jeu", bow=True,
         ptitle="Idée cadeau couple original : une année de complicité à offrir",
         desc="Un cadeau original pour son amoureux ou son amoureuse : Nous Deux, le jeu de couple, avec sa carte cadeau à imprimer. Chaque semaine, une étape à vivre ensemble (un défi, une question, un rituel, un jeu) pour retomber amoureux pas à pas. Accès sans limite de durée.",
         kw="idée cadeau couple, cadeau original amoureux, cadeau pour lui, cadeau pour elle, jeu de couple"),
    dict(theme="creme", board=NOEL, kicker="Le cadeau qui se vit", title="Moins d'objets, plus de moments à deux",
         sub="Une carte cadeau pour commencer l'aventure Nous Deux", cta="Offrir le jeu",
         ptitle="Cadeau de Noël expérience pour couple : des moments à deux",
         desc="Cette année, offrez des moments plutôt qu'un objet de plus. Nous Deux, le jeu de couple en ligne, arrive avec une carte cadeau à imprimer et propose 52 étapes à vivre ensemble : questions, défis, rituels et petits jeux. Un cadeau expérience simple et plein de sens.",
         kw="cadeau expérience couple, cadeau noël expérience, offrir un moment à deux, cadeau couple noël"),
    dict(theme="nuit", board=QJ, kicker="Jeu de couple à offrir", title="Le jeu de couple qui s'offre",
         sub="Avec sa carte cadeau à imprimer et à écrire", cta="Voir le jeu",
         ptitle="Jeu de couple à offrir, avec carte cadeau à imprimer",
         desc="Nous Deux, le jeu de couple en ligne, se joue sur le téléphone et s'offre avec une carte cadeau à imprimer. 52 étapes, 4 niveaux et des badges à débloquer pour se retrouver chaque semaine. Une jolie idée pour Noël, un anniversaire ou la Saint-Valentin.",
         kw="jeu de couple à offrir, jeu couple cadeau, jeu de couple en ligne, cadeau jeu à deux"),
    dict(theme="creme", board=CAD, kicker="Pour un couple que vous aimez", title="Un cadeau pour vos amis amoureux",
         sub="Parents, amis, jeunes mariés : une année de complicité", cta="Offrir le jeu",
         ptitle="Cadeau pour un couple d'amis ou des parents : idée originale",
         desc="Vous cherchez un cadeau pour un couple d'amis, vos parents ou des jeunes mariés ? Offrez-leur Nous Deux, le jeu de couple en ligne, avec sa carte cadeau à imprimer et à personnaliser. 52 étapes à vivre à deux, pour toutes les générations de couples.",
         kw="cadeau pour un couple, cadeau couple d'amis, cadeau parents couple, cadeau jeunes mariés, cadeau à deux"),
    dict(theme="nuit", board=NOEL, kicker="Sous le sapin cette année", title="Retombons amoureux, une étape à la fois",
         sub="La carte cadeau Nous Deux, prête à imprimer", cta="Découvrir le jeu", bow=True,
         ptitle="Cadeau romantique de Noël : Nous Deux, le jeu de couple",
         desc="Un cadeau romantique pour Noël, à offrir à votre moitié : la carte cadeau Nous Deux. Elle ouvre l'accès à un jeu de couple en ligne de 52 étapes, une par semaine, pour se dire des choses, rire ensemble et créer des souvenirs. À imprimer chez vous en quelques minutes.",
         kw="cadeau romantique noël, cadeau noël pour sa copine, cadeau noël pour son copain, carte cadeau couple"),
    dict(theme="creme", board=QJ, kicker="Même à distance", title="Un cadeau pour un couple à distance",
         sub="Le jeu se joue sur le téléphone, où que vous soyez", cta="Voir le jeu",
         ptitle="Cadeau pour couple à distance : un jeu à vivre ensemble",
         desc="Vous vivez une relation à distance ? Nous Deux, le jeu de couple en ligne, se joue sur le téléphone, en appel vidéo ou par messages. Offrez-le avec sa carte cadeau à imprimer (ou à envoyer en photo) : une étape par semaine pour rester proches malgré les kilomètres.",
         kw="cadeau couple à distance, relation à distance cadeau, jeu couple à distance, idée cadeau loin de lui"),
]

# planning : 1 épingle tous les 3 jours à 10h15 (Paris) = 09:15 UTC, du 28/11 au 19/12
START = dt.date(2026, 11, 28)
if __name__ == "__main__":
    rows = []
    for i, p in enumerate(PINS):
        fn = f"cp-carte-{i + 1:02d}.jpg"
        render(p).save(f"{OUT}/{fn}", quality=80, optimize=True, progressive=True)
        day = START + dt.timedelta(days=3 * i)
        rows.append({"Title": p["ptitle"][:100], "Media URL": "https://cupidonpassion.com/img/pins/" + fn,
                     "Pinterest board": p["board"], "Thumbnail": "", "Description": p["desc"][:500],
                     "Link": "https://cupidonpassion.com/" + PAGE,
                     "Publish date": f"{day.isoformat()}T09:15:00", "Keywords": p["kw"]})
        assert len(p["desc"]) <= 500 and "—" not in p["desc"] + p["title"] + p["sub"]
    with open(f"{OUT}/pinterest-cupidon-carte-cadeau-du-28-11-au-19-12.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("ok", len(rows))
