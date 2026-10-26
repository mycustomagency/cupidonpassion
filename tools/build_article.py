#!/usr/bin/env python3
"""Génère un article du blog Cupidon Passion à partir d'un fichier JSON.

Usage : python3 tools/build_article.py articles-json/<slug>.json

Le script :
  1. crée <slug>.html dans le gabarit du site (head, menu, pied de page, kit gratuit, lettre) ;
  2. ajoute l'URL dans sitemap.xml ;
  3. ajoute la carte de l'article en tête de la grille de conseils.html.
Il est relançable : une page déjà présente est remplacée, sitemap et grille ne sont pas dupliqués.
"""
import json, re, sys, os, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://cupidonpassion.com/"

def esc(s): return html.escape(s, quote=False).replace('"', "&quot;")

def main(path):
    d = json.load(open(path, encoding="utf-8"))
    slug = d["slug"]
    page = slug + ".html"
    head = open(os.path.join(ROOT, "tools/_head.html"), encoding="utf-8").read()
    foot = open(os.path.join(ROOT, "tools/_foot.html"), encoding="utf-8").read()
    tail = open(os.path.join(ROOT, "tools/_offer_letter.html"), encoding="utf-8").read()

    # --- head : remplacer title, description, canonical, og, JSON-LD
    def sub(pattern, repl, s):
        out, n = re.subn(pattern, lambda m: repl, s, count=1, flags=re.S)
        assert n == 1, pattern
        return out
    t, desc, url = d["title"], d["meta_description"], BASE + page
    assert len(t) <= 60, f"title trop long ({len(t)})"
    assert len(desc) <= 155, f"meta trop longue ({len(desc)})"
    head = sub(r"<title>.*?</title>", f"<title>{esc(t)}</title>", head)
    head = sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{esc(desc)}">', head)
    head = sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{url}">', head)
    head = sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{esc(t)}">', head)
    head = sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{esc(desc)}">', head)
    head = sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{url}">', head)
    og_img = d.get("og_image")
    if og_img:
        head = head.replace('<meta property="og:locale"', f'<meta property="og:image" content="{BASE}{og_img}">\n<meta property="og:locale"', 1)
    today = d.get("date") or datetime.date.today().isoformat()
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": t, "inLanguage": "fr-FR",
          "datePublished": today, "dateModified": today,
          "author": {"@type": "Organization", "name": "Cupidon Passion"},
          "publisher": {"@type": "Organization", "name": "Cupidon Passion"},
          "description": desc, "mainEntityOfPage": url}
    if og_img: ld["image"] = BASE + og_img
    blocks = [json.dumps(ld, ensure_ascii=False)]
    if d.get("faq"):
        faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
        blocks.append(json.dumps(faq, ensure_ascii=False))
    head = sub(r'<script type="application/ld\+json">.*?</script>',
               "".join(f'<script type="application/ld+json">\n{b}\n</script>\n' for b in blocks).rstrip("\n"), head)

    # --- corps
    parts = [f'<article class="article wrap">\n  <p class="meta"><a href="index.html">Accueil</a> › <a href="conseils.html">Conseils</a> › {esc(d["h1"])}</p>',
             f'  <h1>{esc(d["h1"])}</h1>',
             f'  <p class="meta">Mis à jour en {d["updated_label"]} · Lecture {d["minutes"]} min</p>']
    body = d["body_html"]
    # figures : {{img:clé}} dans le corps
    for key, im in d.get("images", {}).items():
        fig = (f'<figure class="art-img"><img src="assets/img/blog/{im["file"]}" alt="{esc(im["alt"])}" '
               f'width="{im.get("w",1200)}" height="{im.get("h",800)}" loading="lazy" '
               f'onerror="this.closest(\'figure\').hidden=true">'
               + (f'<figcaption>{esc(im["caption"])}</figcaption>' if im.get("caption") else "") + '</figure>')
        body = body.replace("{{img:%s}}" % key, fig)
    assert "{{" not in body, "placeholder image non résolu"
    parts.append(body)
    out = head + "\n".join(parts) + "\n  " + tail.strip("\n") + "\n" + foot
    open(os.path.join(ROOT, page), "w", encoding="utf-8").write(out)

    # --- sitemap
    sm_path = os.path.join(ROOT, "sitemap.xml")
    sm = open(sm_path, encoding="utf-8").read()
    if url not in sm:
        sm = sm.replace("</urlset>", f'  <url><loc>{url}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n</urlset>')
        open(sm_path, "w", encoding="utf-8").write(sm)

    # --- grille conseils
    cp = os.path.join(ROOT, "conseils.html")
    c = open(cp, encoding="utf-8").read()
    if f'href="{page}"' not in c:
        card = (f'    <a class="blog-card" href="{page}">\n      <span class="blog-tag">{esc(d["tag"])}</span>\n'
                f'      <h2>{esc(d["h1"])}</h2>\n      <p>{esc(d["card_excerpt"])}</p>\n'
                f'      <span class="blog-more">Lire l\'article →</span>\n    </a>\n\n')
        c = c.replace('<div class="blog-grid">\n\n', '<div class="blog-grid">\n\n' + card, 1)
        assert page in c
        open(cp, "w", encoding="utf-8").write(c)
    # --- contrôles
    text = re.sub(r"<[^>]+>", " ", body)
    words = len(text.split())
    print(f"OK {page} | {words} mots | title {len(t)} car. | meta {len(desc)} car.")
    if "—" in out.split("<article")[1]: print("ATTENTION : tiret cadratin présent")

if __name__ == "__main__":
    main(sys.argv[1])
