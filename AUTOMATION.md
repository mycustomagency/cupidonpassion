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

## Prompts d'images (pour Gemini ou autre)
Dans la PR, fournir pour chaque image un prompt prêt à coller : photographie réaliste, lumière naturelle chaude, ambiance cosy, aucune personne ni visage, aucun texte lisible, style éditorial naturel, format paysage 3:2, haute résolution, avec le sujet précis de l'image. Rappeler : redimensionner en 1200x800, JPG, nom de fichier exact.

## Règles d'écriture
- Vouvoiement, ton chaleureux et concret. Aucun tiret cadratin ni demi-cadratin (le script refuse de générer la page s'il en trouve), car cela trahit une rédaction par IA.
- 1 200 à 1 800 mots, H2 sous forme de questions ou de listes, FAQ de 3 questions.
- Title 60 caractères max, meta description 155 max (le script bloque sinon).
- Au moins 3 liens internes, un seul appel à l'action principal (jeu ou quiz).
- Aucune statistique ni étude inventée, aucun chiffre sur le site susceptible de changer.
- Articles intemporels : aucune date visible ni dans les données, pas d'année dans le texte (écrire « l'année suivante », « cette saison »).
- Signature : « L'équipe Cupidon Passion ».
- Liens d'affiliation Amazon : seulement si utiles, avec `rel="sponsored nofollow noopener"` et la mention partenaire.
