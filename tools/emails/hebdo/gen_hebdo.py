"""Génère les e-mails hebdo de Nous Deux (rappel de l'étape de la semaine) au format HTML Brevo."""
import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
E = [
 ("Votre aventure commence cette semaine 💘", "Première étape : un message qui fait du bien",
  "Bienvenue sur votre route à deux ! Votre première étape s'appelle « Le message inattendu ». Elle ne prend que quelques secondes, et pourtant elle peut illuminer une journée entière.",
  "n'attendez pas le moment parfait. Le plus beau message est souvent le plus simple, envoyé au milieu d'une journée ordinaire."),
 ("Vous souvenez-vous du déclic ? ✨", "Une question à se poser cette semaine",
  "Cette semaine, votre étape s'appelle « Le déclic ». Une question toute douce, à vous poser l'un à l'autre, pour revenir au tout début de votre histoire.",
  "quand l'autre raconte, ne l'interrompez pas, même pour compléter. Laissez-le aller au bout, puis dites-lui ce que vous avez préféré dans son récit."),
 ("Dix minutes rien qu'à vous ⏳", "Un petit rituel qui change tout",
  "Votre étape de la semaine est un rituel : « Dix minutes rien qu'à nous ». Pas besoin de sortir ni de préparer quoi que ce soit, juste de vous accorder ce temps-là.",
  "posez les téléphones dans une autre pièce. Ce n'est pas la durée qui compte, c'est d'être vraiment là, l'un pour l'autre."),
 ("Vous connaissez-vous vraiment ? 🎲", "Un jeu pour rire (et apprendre des choses)",
  "Cette semaine, place au jeu avec « Deviner l'autre ». Vous risquez d'être surpris, dans un sens comme dans l'autre.",
  "si vous vous trompez, c'est une bonne nouvelle. Ça veut dire qu'il reste des choses à découvrir chez la personne que vous aimez. Demandez-lui de vous expliquer."),
 ("Ce que vous n'avez jamais dit à voix haute 💬", "Un défi tout en douceur",
  "Votre étape s'appelle « Le compliment sincère ». Un défi simple sur le papier, mais qui demande un peu de courage, et qui fait un bien fou.",
  "soyez précis. « Tu es génial » fait plaisir, mais « j'admire ta patience avec ta sœur » touche en plein cœur."),
 ("Et si demain matin commençait autrement ? ☀️", "Un rituel de trente secondes",
  "Cette semaine, votre étape est « Le réveil complice ». Trente petites secondes au réveil, qui peuvent donner le ton de toute la journée.",
  "les petits gestes répétés comptent plus que les grandes déclarations rares. C'est dans le quotidien que la complicité se construit."),
 ("Qu'est-ce qui vous a plu, au tout début ? 💞", "Une question pour retomber amoureux",
  "Votre étape de la semaine est une question : « Ce qui m'a séduit ». Un joli retour en arrière, pour vous rappeler pourquoi vous vous êtes choisis.",
  "après avoir écouté l'autre, reformulez ce que vous avez entendu (« si je comprends bien, tu as aimé... »). C'est la meilleure façon de montrer qu'on écoute vraiment."),
 ("Une photo pour votre album 📸", "Le défi de la semaine",
  "Cette semaine, votre étape s'appelle « La photo souvenir ». Spontanée, pas forcément parfaite : c'est le moment qu'elle capture qui compte.",
  "créez un album rien qu'à vous sur votre téléphone. Dans un an, vous serez heureux de le feuilleter ensemble."),
 ("Saurez-vous trouver le mensonge ? 🕵️", "Un jeu pour vous redécouvrir",
  "Votre étape de la semaine est un jeu : « Trois vérités, un mensonge ». Fous rires garantis, et vous allez sûrement apprendre quelque chose de nouveau.",
  "posez des questions sur les vérités aussi, pas seulement sur le mensonge. Derrière chaque anecdote, il y a une histoire à écouter."),
 ("Un dernier mot avant de dormir 🌙", "Un rituel tout simple pour bien finir la journée",
  "Cette semaine, votre étape est « Le bonsoir attentionné ». Un tout petit rituel du soir, qui laisse une belle trace avant de s'endormir.",
  "même après une journée difficile, cherchez un moment positif à partager. Terminer sur une note douce aide à se retrouver le lendemain."),
 ("Quelle est votre chanson ? 🎶", "Le défi musical de la semaine",
  "Votre étape s'appelle « La chanson de nous ». Choisir ensemble une chanson qui vous ressemble aujourd'hui, et prendre le temps de l'écouter.",
  "si vous n'êtes pas d'accord sur la chanson, tant mieux. Racontez-vous pourquoi chacun a choisi la sienne, c'est là que la conversation devient belle."),
 ("Votre endroit préféré au monde 🗺️", "Une question qui fait voyager",
  "Cette semaine, votre étape est une question : « Mon endroit préféré ». Un lieu, un souvenir, et sûrement une envie d'y retourner.",
  "et si vous y retourniez vraiment ? Notez la date quelque part. Bravo aussi pour ces 12 semaines : vous approchez de la fin du premier niveau 🎉"),
]
T = """<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Nous Deux, le jeu</title></head>
<body style="margin:0;padding:0;background:#f7f2ea;font-family:Arial,Helvetica,sans-serif;color:#1d1a3a">
<div style="display:none;max-height:0;overflow:hidden">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f7f2ea"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#ffffff;border-radius:16px;overflow:hidden">
<tr><td align="center" style="background:#1a1966;padding:24px 20px 18px"><img src="https://cupidonpassion.com/assets/cupidon.png" width="90" height="90" alt="Cupidon" style="display:block;border:0"><p style="margin:8px 0 0;color:#e5b567;font-size:13px;letter-spacing:3px;font-weight:bold">NOUS DEUX, LE JEU · SEMAINE {n}</p></td></tr>
<tr><td style="padding:28px 28px 8px;font-size:16px;line-height:1.6"><p style="margin:0 0 14px">Bonjour,</p>
<p style="margin:0 0 14px">{intro}</p>
<p style="margin:0 0 14px;background:#fbf1f3;border-left:4px solid #e8455a;padding:12px 14px;border-radius:8px"><b>Le conseil de Cupidon :</b> {tip}</p></td></tr>
<tr><td align="center" style="padding:8px 28px 24px"><a href="https://jeu.cupidonpassion.com" style="display:inline-block;background:#e8455a;color:#ffffff;text-decoration:none;font-weight:bold;font-size:16px;padding:14px 28px;border-radius:999px">Ouvrir le jeu</a></td></tr>
<tr><td style="padding:0 28px 28px;font-size:14px;line-height:1.6;color:#4a4566"><p style="margin:0 0 14px">Vous avez pris un peu d'avance ou de retard ? Aucun souci, le jeu reprend exactement là où vous vous êtes arrêtés.</p>
<p style="margin:0;font-size:16px;color:#1d1a3a">À la semaine prochaine,<br>Cupidon 💘</p></td></tr>
<tr><td align="center" style="background:#f7f2ea;padding:16px;font-size:12px;color:#8a84a3"><a href="https://cupidonpassion.com" style="color:#8a84a3">cupidonpassion.com</a> · <a href="{{{{ unsubscribe }}}}" style="color:#8a84a3">Ne plus recevoir les rappels</a></td></tr>
</table></td></tr></table></body></html>"""
meta = []
for i, (subj, pre, intro, tip) in enumerate(E, 1):
    h = T.format(n=i, pre=html.escape(pre), intro=intro, tip=tip)
    open(os.path.join(HERE, f"s{i:02d}.html"), "w", encoding="utf-8").write(h)
    meta.append({"n": i, "subject": subj, "preview": pre})
json.dump(meta, open(os.path.join(HERE, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(meta))
