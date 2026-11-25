"""Cupidon Passion : générateur de visuels d'épingles (1000x1500, 1080x1350, 1080x1920)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, random

SITE = "/home/claude/mycustomagency/cupidonpassion"
MASCOT = Image.open(f"{SITE}/assets/cupidon.png").convert("RGBA")
PHOTOS = f"{SITE}/assets/img/blog"

NUIT, NUIT2, INDIGO, ROI = (13, 11, 46), (20, 18, 56), (26, 25, 102), (52, 50, 202)
CORAIL, ROSE, OR, CREME = (232, 69, 90), (255, 143, 163), (229, 181, 103), (247, 242, 234)
BLANC = (255, 255, 255)

IN = "/usr/share/fonts/opentype/inter/"
LORA_I = "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"


def F(name, size):
    if name == "lora":
        f = ImageFont.truetype(LORA_I, size)
        try:
            f.set_variation_by_name("SemiBold Italic")
        except Exception:
            pass
        return f
    return ImageFont.truetype(IN + name + ".otf", size)


def wrap(draw, text, font, maxw):
    for pct in ("?", "!", ":", ";", "»"):
        text = text.replace(" " + pct, "\u00a0" + pct)
    text = text.replace("« ", "«\u00a0")
    words, lines, cur = [w for w in text.split(" ") if w], [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, text, fname, maxw, maxh, start, minsize=40, lh=1.08):
    size = start
    while size >= minsize:
        f = F(fname, size)
        lines = wrap(draw, text, f, maxw)
        h = len(lines) * size * lh
        if h <= maxh and all(draw.textlength(l, font=f) <= maxw for l in lines):
            return f, lines, size
        size -= 4
    f = F(fname, minsize)
    return f, wrap(draw, text, f, maxw), minsize


def text_block(draw, lines, font, size, x, y, w, fill, lh=1.08, align="center"):
    for l in lines:
        tw = draw.textlength(l, font=font)
        tx = x + (w - tw) / 2 if align == "center" else x
        draw.text((tx, y), l, font=font, fill=fill)
        y += size * lh
    return y


def gradient(W, H, top, bottom):
    im = Image.new("RGB", (W, H), top)
    d = ImageDraw.Draw(im)
    for yy in range(H):
        t = yy / H
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, yy), (W, yy)], fill=c)
    return im


def glow(im, cx, cy, r, color, alpha=110):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(r // 2))
    im.paste(layer, (0, 0), layer)


def hearts(im, n, seed, color, area=None, smin=14, smax=34, alpha=90):
    rnd = random.Random(seed)
    W, H = im.size
    x0, y0, x1, y1 = area or (0, 0, W, H)
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for _ in range(n):
        s = rnd.randint(smin, smax)
        x, y = rnd.randint(x0, x1 - s), rnd.randint(y0, y1 - s)
        heart(d, x, y, s, color + (alpha,))
    im.paste(layer, (0, 0), layer)


def heart(d, x, y, s, fill):
    r = s / 4
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=fill)
    d.ellipse([x + 2 * r, y, x + 4 * r, y + 2 * r], fill=fill)
    d.polygon([(x + 0.15 * r, y + 1.35 * r), (x + 3.85 * r, y + 1.35 * r), (x + 2 * r, y + 4 * r)], fill=fill)


def mascot(im, x, y, size, flip=False):
    m = MASCOT.resize((size, size), Image.LANCZOS)
    if flip:
        m = m.transpose(Image.FLIP_LEFT_RIGHT)
    im.paste(m, (x, y), m)


def photo(name, w, h):
    p = Image.open(os.path.join(PHOTOS, name)).convert("RGB")
    r = max(w / p.width, h / p.height)
    p = p.resize((int(p.width * r) + 1, int(p.height * r) + 1), Image.LANCZOS)
    l, t = (p.width - w) // 2, (p.height - h) // 2
    return p.crop((l, t, l + w, t + h))


def rounded(img, rad):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, img.width, img.height], rad, fill=255)
    out = img.convert("RGBA")
    out.putalpha(mask)
    return out


def shadow_paste(im, card, x, y, rad=28, blur=22, off=14):
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x + off // 2, y + off, x + card.width + off // 2, y + card.height + off], rad, fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    im.paste(sh, (0, 0), sh)
    im.paste(card, (x, y), card)


def pill(draw, cx, y, text, font, bg, fg, padx=34, h=74):
    tw = draw.textlength(text, font=font)
    w = tw + 2 * padx
    draw.rounded_rectangle([cx - w / 2, y, cx + w / 2, y + h], h // 2, fill=bg)
    bb = font.getbbox(text)
    draw.text((cx - tw / 2, y + (h - (bb[3] - bb[1])) / 2 - bb[1]), text, font=font, fill=fg)


def footer(im, d, W, H, dark=True, k=1.0):
    col = CREME if dark else NUIT
    f = F("Inter-Bold", int(30 * k))
    t = "cupidonpassion.com"
    tw = d.textlength(t, font=f)
    y = H - int(78 * k)
    d.line([(W / 2 - 160 * k, y - 22 * k), (W / 2 + 160 * k, y - 22 * k)], fill=OR, width=2)
    d.text(((W - tw) / 2, y), t, font=f, fill=col)


# ---------------------------------------------------------------- modèles
# p : dict(kicker, title, sub, cta, photo, items, theme)

def t_nuit(W, H, p):
    """Fond nuit étoilé, mascotte, grand titre, bouton corail."""
    k = W / 1000
    im = gradient(W, H, INDIGO, NUIT).convert("RGBA")
    glow(im, int(W * .85), int(H * .1), int(380 * k), ROI, 120)
    glow(im, int(W * .1), int(H * .85), int(320 * k), CORAIL, 60)
    hearts(im, 16, p["title"], ROSE, alpha=55)
    d = ImageDraw.Draw(im)
    ms = int(400 * k)
    mascot(im, (W - ms) // 2, int(H * .09), ms)
    y = int(H * .09) + ms + int(30 * k)
    fk = F("lora", int(46 * k))
    kw = d.textlength(p["kicker"], font=fk)
    d.text(((W - kw) / 2, y), p["kicker"], font=fk, fill=OR)
    y += int(80 * k)
    f, lines, s = fit_title(d, p["title"].upper(), "Inter-Black", W - int(140 * k), int(H * .34), int(104 * k))
    y = text_block(d, lines, f, s, 0, y, W, BLANC)
    if p.get("sub"):
        fs = F("lora", int(46 * k))
        y += int(30 * k)
        y = text_block(d, wrap(d, p["sub"], fs, W - int(200 * k)), fs, int(46 * k), 0, y, W, (217, 212, 228), 1.35)
    pill(d, W / 2, H - int(230 * k), p.get("cta", "Découvrir"), F("Inter-ExtraBold", int(34 * k)), CORAIL, BLANC, h=int(80 * k))
    footer(im, d, W, H, True, k)
    return im


def t_photo_creme(W, H, p):
    """Crème, photo encadrée avec ombre, titre nuit, accroche dorée."""
    k = W / 1000
    im = Image.new("RGBA", (W, H), CREME + (255,))
    hearts(im, 22, p["title"], CORAIL, alpha=28)
    d = ImageDraw.Draw(im)
    y = int(80 * k)
    fk = F("Inter-ExtraBold", int(28 * k))
    kt = p["kicker"].upper()
    kw = d.textlength(kt, font=fk) + 8 * len(kt) * 0
    d.text(((W - d.textlength(kt, font=fk)) / 2, y), kt, font=fk, fill=CORAIL)
    y += int(60 * k)
    f, lines, s = fit_title(d, p["title"], "Inter-Black", W - int(130 * k), int(H * .25), int(92 * k))
    y = text_block(d, lines, f, s, 0, y, W, NUIT)
    if p.get("sub"):
        fs = F("lora", int(40 * k))
        y += int(10 * k)
        y = text_block(d, wrap(d, p["sub"], fs, W - int(180 * k)), fs, int(40 * k), 0, y, W, INDIGO, 1.3)
    y = int(y + 34 * k)
    pw = W - int(150 * k)
    ph = H - y - int(260 * k)
    card = rounded(photo(p["photo"], pw, ph), int(30 * k))
    bord = Image.new("RGBA", (pw + int(24 * k), ph + int(24 * k)), (0, 0, 0, 0))
    ImageDraw.Draw(bord).rounded_rectangle([0, 0, bord.width, bord.height], int(38 * k), fill=BLANC)
    bord.paste(card, (int(12 * k), int(12 * k)), card)
    shadow_paste(im, bord, (W - bord.width) // 2, y)
    ms = int(190 * k)
    mascot(im, W - ms - int(30 * k), y + bord.height - int(140 * k), ms)
    d = ImageDraw.Draw(im)
    pill(d, W / 2, H - int(200 * k), p.get("cta", "Lire l'article"), F("Inter-ExtraBold", int(32 * k)), NUIT, CREME, h=int(76 * k))
    footer(im, d, W, H, False, k)
    return im


def t_liste(W, H, p):
    """Corail, liste numérotée dans une carte crème."""
    k = W / 1000
    im = gradient(W, H, (240, 92, 110), (200, 50, 78)).convert("RGBA")
    hearts(im, 18, p["title"], BLANC, alpha=40)
    d = ImageDraw.Draw(im)
    y = int(70 * k)
    fk = F("lora", int(48 * k))
    d.text(((W - d.textlength(p["kicker"], font=fk)) / 2, y), p["kicker"], font=fk, fill=CREME)
    y += int(80 * k)
    f, lines, s = fit_title(d, p["title"].upper(), "Inter-Black", W - int(120 * k), int(H * .22), int(96 * k))
    y = text_block(d, lines, f, s, 0, y, W, BLANC)
    y = int(y + 36 * k)
    cx0, cx1 = int(70 * k), W - int(70 * k)
    items = p["items"]
    fi = F("Inter-Bold", int(46 * k))
    rows = [wrap(d, it, fi, cx1 - cx0 - int(150 * k)) for it in items]
    ch = sum(len(r) * int(58 * k) + int(50 * k) for r in rows) + int(70 * k)
    card = Image.new("RGBA", (cx1 - cx0, ch), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([0, 0, card.width, card.height], int(34 * k), fill=CREME)
    yy = int(34 * k)
    fn = F("Inter-Black", int(34 * k))
    for i, r in enumerate(rows):
        cd.ellipse([int(30 * k), yy - int(4 * k), int(30 * k) + int(62 * k), yy + int(58 * k)], fill=NUIT)
        n = str(i + 1)
        cd.text((int(61 * k) - cd.textlength(n, font=fn) / 2, yy + int(6 * k)), n, font=fn, fill=OR)
        for j, l in enumerate(r):
            cd.text((int(118 * k), yy + j * int(58 * k)), l, font=fi, fill=NUIT)
        yy += len(r) * int(58 * k) + int(50 * k)
    free = (H - int(260 * k)) - y - ch
    if free > 0:
        y += int(free * 0.45)
    shadow_paste(im, card, cx0, y)
    ms = int(200 * k)
    mascot(im, W - ms - int(10 * k), y + ch - int(90 * k), ms, flip=True)
    d = ImageDraw.Draw(im)
    pill(d, W / 2, H - int(215 * k), p.get("cta", "Toutes les idées"), F("Inter-ExtraBold", int(32 * k)), NUIT, BLANC, h=int(76 * k))
    footer(im, d, W, H, True, k)
    return im


def t_photo_haut(W, H, p):
    """Photo pleine largeur en haut, bandeau nuit avec titre en bas."""
    k = W / 1000
    im = Image.new("RGBA", (W, H), NUIT + (255,))
    ph = int(H * .5)
    im.paste(photo(p["photo"], W, ph), (0, 0))
    fade = Image.new("RGBA", (W, int(200 * k)), (0, 0, 0, 0))
    fd = ImageDraw.Draw(fade)
    for i in range(fade.height):
        fd.line([(0, i), (W, i)], fill=NUIT + (int(255 * i / fade.height),))
    im.paste(fade, (0, ph - fade.height), fade)
    glow(im, int(W * .9), int(H * .9), int(300 * k), ROI, 90)
    d = ImageDraw.Draw(im)
    fk = F("Inter-ExtraBold", int(28 * k))
    kt = p["kicker"].upper()
    tw = d.textlength(kt, font=fk) + int(40 * k)
    y = ph - int(30 * k)
    d.rounded_rectangle([(W - tw) / 2, y, (W + tw) / 2, y + int(56 * k)], int(28 * k), fill=OR)
    d.text(((W - d.textlength(kt, font=fk)) / 2, y + int(12 * k)), kt, font=fk, fill=NUIT)
    y += int(90 * k)
    f, lines, s = fit_title(d, p["title"], "Inter-Black", W - int(130 * k), int(H * .2), int(88 * k))
    y = text_block(d, lines, f, s, 0, y, W, BLANC)
    if p.get("sub"):
        fs = F("lora", int(40 * k))
        y += int(12 * k)
        text_block(d, wrap(d, p["sub"], fs, W - int(180 * k)), fs, int(40 * k), 0, y, W, ROSE, 1.3)
    pill(d, W / 2, H - int(215 * k), p.get("cta", "Lire l'article"), F("Inter-ExtraBold", int(32 * k)), CORAIL, BLANC, h=int(76 * k))
    footer(im, d, W, H, True, k)
    return im


def t_bulle(W, H, p):
    """Question ou phrase dans une bulle, mascotte qui la pose."""
    k = W / 1000
    im = gradient(W, H, (62, 58, 190), (24, 22, 90)).convert("RGBA")
    hearts(im, 26, p["title"], ROSE, alpha=50)
    d = ImageDraw.Draw(im)
    y = int(80 * k)
    fk = F("lora", int(50 * k))
    d.text(((W - d.textlength(p["kicker"], font=fk)) / 2, y), p["kicker"], font=fk, fill=OR)
    y = int(y + 110 * k)
    bx0, bx1 = int(80 * k), W - int(80 * k)
    f, lines, s = fit_title(d, p["title"], "Inter-ExtraBold", bx1 - bx0 - int(110 * k), int(H * .3), int(78 * k), lh=1.2)
    bh = int(len(lines) * s * 1.2 + 120 * k)
    d.rounded_rectangle([bx0, y, bx1, y + bh], int(48 * k), fill=CREME)
    d.polygon([(int(W * .28), y + bh - 2), (int(W * .4), y + bh - 2), (int(W * .25), y + bh + int(80 * k))], fill=CREME)
    text_block(d, lines, f, s, bx0, y + int(60 * k), bx1 - bx0, NUIT, 1.2)
    y = int(y + bh + 40 * k)
    ms = int(380 * k)
    mascot(im, int(W * .03), y, ms)
    if p.get("sub"):
        fs = F("lora", int(50 * k))
        sl = wrap(d, p["sub"], fs, int(W * .48))
        text_block(d, sl, fs, int(50 * k), int(W * .46), y + int(110 * k), int(W * .5), CREME, 1.3, align="left")
    pill(d, W / 2, H - int(215 * k), p.get("cta", "Jouer à deux"), F("Inter-ExtraBold", int(32 * k)), CORAIL, BLANC, h=int(76 * k))
    footer(im, d, W, H, True, k)
    return im


TEMPLATES = {"nuit": t_nuit, "photo": t_photo_creme, "liste": t_liste, "photohaut": t_photo_haut, "bulle": t_bulle}
FORMATS = {"pin": (1000, 1500), "fb": (1080, 1350), "story": (1080, 1920)}


def render(tpl, p, fmt="pin"):
    W, H = FORMATS[fmt]
    return TEMPLATES[tpl](W, H, p).convert("RGB")
