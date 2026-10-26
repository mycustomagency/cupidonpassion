# Publication hebdomadaire d'un article (Cupidon Passion)

Chaque lundi, une tâche planifiée prépare **une branche et une pull request** avec un nouvel article.
Rien n'est publié tant que la PR n'est pas fusionnée (merge) par Vanessa.

## Étapes de la tâche
1. Lire `plan-editorial` (sujet de la semaine, mot-clé, page à lier). À défaut, proposer un sujet saisonnier cohérent.
2. Lire 2 articles existants pour garder le ton, vérifier qu'aucun doublon de sujet n'existe.
3. Écrire `articles-json/<slug>.json` (voir `articles-json/calendrier-avent-couple.json` comme modèle).
4. Lancer `python3 tools/build_article.py articles-json/<slug>.json` : crée la page, met à jour `sitemap.xml` et la grille de `conseils.html`.
5. Ajouter dans les anciens articles proches un lien vers le nouvel article (maillage interne).
6. Ouvrir une branche `blog/<slug>` et une PR dont la description contient : mot-clé visé, liste des images à ajouter (nom de fichier exact, sujet, texte alternatif, dimensions 1200x800), points à vérifier.

## Images
Les images sont à déposer par Vanessa dans `assets/img/blog/` avec le nom de fichier indiqué dans la PR.
Tant qu'un fichier est absent, la figure se masque automatiquement : la page ne montre jamais d'image cassée.

## Règles d'écriture
- Vouvoiement, ton chaleureux et concret. Aucun tiret cadratin.
- 1 200 à 1 800 mots, H2 sous forme de questions ou de listes, FAQ de 3 questions.
- Title 60 caractères max, meta description 155 max (le script bloque sinon).
- Au moins 3 liens internes, un seul appel à l'action principal (jeu ou quiz).
- Aucune statistique ni étude inventée, aucun chiffre sur le site susceptible de changer.
- Signature : « L'équipe Cupidon Passion ».
- Liens d'affiliation Amazon : seulement si utiles, avec `rel="sponsored nofollow noopener"` et la mention partenaire.
