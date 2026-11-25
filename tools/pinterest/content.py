# Cupidon Passion : série Pinterest 1 (27/11 au 25/12)
# fenêtre = (premier jour, dernier jour), jour 0 = vendredi 27 novembre
RDV = "Idées de rendez-vous en couple"
QJ = "Questions et jeux à deux"
CAD = "Idées cadeaux pour couple"
SOI = "Soirées en amoureux"
RAV = "Raviver son couple"
CEL = "En route vers l'amour (célibataires)"
QUIZ = "Quiz et tests de couple"
NOEL = "Cadeaux et Idées Noël, fêtes, moment à deux"
CONS = "Conseils & Rituels de couple"
CIT = "Citations d'amour et de complicité"

ALL = (0, 28)
AVENT = (0, 6)
NOELW = (0, 20)
FETES = (6, 28)
SV = (15, 28)

PINS = []


def P(tpl, board, page, win, kicker, vtitle, ptitle, desc, kw, sub=None, items=None, cta=None, photo=None):
    PINS.append(dict(tpl=tpl, board=board, page=page, win=win, kicker=kicker, title=vtitle, ptitle=ptitle,
                     desc=desc, kw=kw, sub=sub, items=items, cta=cta, photo=photo))


# ------------------------------------------------ Calendrier de l'avent (début de série)
P("photo", NOEL, "calendrier-avent-couple.html", AVENT, "Avant le 1er décembre", "Calendrier de l'avent pour couple",
  "Calendrier de l'avent pour couple : 24 idées à faire soi-même",
  "Un calendrier de l'avent pour couple fait maison : 24 petites attentions à glisser dans des enveloppes, une boîte ou un bocal. Mots doux, défis, souvenirs, soirées sans écran. Toutes les idées case par case pour préparer décembre à deux, avec un tout petit budget.",
  "calendrier de l'avent couple, calendrier de l'avent fait maison, idée calendrier avent amoureux, avent à deux",
  sub="24 petites attentions à préparer à la maison", cta="Voir les 24 idées", photo="calendrier-avent-couple-1.jpg")
P("liste", NOEL, "calendrier-avent-couple.html", AVENT, "Que mettre dans les cases ?", "Calendrier de l'avent en amoureux",
  "Que mettre dans un calendrier de l'avent pour son amoureux ?",
  "Besoin d'idées pour remplir un calendrier de l'avent pour votre amoureux ou amoureuse ? Mot doux sous l'oreiller, chocolat chaud maison, compliment précis, séance photo à la maison : 24 idées simples qui ne coûtent presque rien et créent un vrai rendez-vous chaque jour de décembre.",
  "que mettre dans un calendrier de l'avent couple, idée case calendrier avent, calendrier avent amoureux pas cher",
  items=["Un mot doux sous l'oreiller", "Le chocolat chaud maison", "Une soirée sans écran", "La séance photo maison"], cta="Les 24 idées")
P("photohaut", NOEL, "calendrier-avent-couple.html", AVENT, "Fait maison", "Un calendrier de l'avent qui rapproche",
  "Calendrier de l'avent DIY pour couple, petit budget",
  "Pas besoin de chocolats industriels : un calendrier de l'avent pour couple se fabrique en une soirée avec 24 enveloppes et des idées à vivre à deux. On vous explique comment le préparer, quoi mettre dans chaque case et comment éviter qu'il s'essouffle avant Noël.",
  "calendrier de l'avent DIY couple, calendrier avent enveloppes, idée cadeau avent pas cher, calendrier avent à deux",
  sub="Enveloppes, bocal ou petites boîtes", cta="Le fabriquer", photo="calendrier-avent-couple-2.jpg")
P("bulle", NOEL, "calendrier-avent-couple.html", AVENT, "Idée pour la case n°1", "Ce soir, on boit un chocolat chaud maison et on parle de nos plus beaux Noëls.",
  "Idée de case pour un calendrier de l'avent en couple",
  "Une idée toute simple pour ouvrir votre calendrier de l'avent en couple : un chocolat chaud maison et vos plus beaux souvenirs de Noël. Retrouvez les 23 autres idées, à glisser dans des enveloppes, pour faire de décembre un vrai mois à deux.",
  "calendrier de l'avent couple, idée case avent, soirée cocooning décembre, avent amoureux",
  sub="Et 23 autres idées pour décembre", cta="Voir le calendrier")

# ------------------------------------------------ Cadeaux de Noël (affiliation)
P("nuit", NOEL, "idees-cadeaux-noel-couple.html", (0, 3), "Noël à deux", "Idées cadeaux de Noël pour un couple",
  "Idées cadeaux de Noël pour un couple : offrir du temps plutôt qu'un objet",
  "Quel cadeau de Noël offrir à un couple ? Plutôt qu'un objet de plus, offrez un moment à vivre à deux : jeux de couple, coffrets expérience, carnet de souvenirs, bocal de rendez-vous. Des idées pour tous les budgets, faites maison ou à commander, avec nos coups de cœur.",
  "cadeau noël couple, idée cadeau noël pour un couple, cadeau à offrir à deux, cadeau noël original couple",
  sub="Offrir du temps plutôt qu'un objet de plus", cta="Voir les idées cadeaux")
P("photo", NOEL, "idees-cadeaux-noel-couple.html", (3, 12), "Sous le sapin", "Le cadeau de Noël qui se vit à deux",
  "Cadeau de Noël original pour un couple : des moments à vivre ensemble",
  "Vous cherchez un cadeau de Noël original pour votre couple ou pour des amis en couple ? Nos idées misent sur les moments partagés : une expérience à vivre, un jeu pour se parler, un souvenir à garder. Des cadeaux qui durent bien après le 25 décembre.",
  "cadeau noël original couple, cadeau expérience couple, cadeau noël amoureux, idée cadeau noël",
  sub="Expériences, jeux et souvenirs à partager", cta="Trouver le cadeau", photo="idees-cadeaux-noel-couple-1.jpg")
P("liste", NOEL, "idees-cadeaux-noel-couple.html", NOELW, "Petit budget", "Cadeaux de Noël à deux qui font plaisir",
  "Cadeau de Noël pour un couple à petit budget : nos idées",
  "Un cadeau de Noël pour un couple sans se ruiner, c'est possible. Bocal de rendez-vous à tirer au sort, carnet de vos souvenirs de l'année, jeu de questions, soirée préparée à l'avance : des idées faites maison ou à petit prix qui touchent vraiment.",
  "cadeau noël couple pas cher, cadeau noël fait maison couple, idée cadeau noël petit budget, cadeau à deux",
  items=["Un bocal de rendez-vous à tirer au sort", "Le carnet de vos souvenirs de l'année", "Un jeu de questions à deux"], cta="Toutes les idées")
P("bulle", NOEL, "idees-cadeaux-noel-couple.html", (13, 24), "Dernière minute", "Pas encore de cadeau de Noël pour votre moitié ?",
  "Cadeau de Noël de dernière minute pour son couple",
  "Pas encore trouvé de cadeau de Noël pour votre moitié ? Pas de panique : voici des idées de dernière minute qui ont du sens, à imprimer, à préparer en une soirée ou à recevoir vite. Le plus important, c'est le temps que vous offrez.",
  "cadeau noël dernière minute, cadeau noël couple rapide, idée cadeau noël amoureux, cadeau noël urgent",
  sub="Des idées qui ont du sens, même au dernier moment", cta="Vite, une idée")
P("nuit", NOEL, "idees-cadeaux-noel-couple.html", NOELW, "Un cadeau qui dure toute l'année", "Offrez une année de complicité",
  "Cadeau de Noël couple : un cadeau qui dure toute l'année",
  "Et si votre cadeau de Noël ne s'arrêtait pas au 25 décembre ? Un jeu de couple à vivre semaine après semaine, un bocal de rendez-vous, un abonnement à des moments à deux : nos idées de cadeaux qui font durer la magie toute l'année.",
  "cadeau couple toute l'année, cadeau noël durable couple, jeu de couple cadeau, idée cadeau original amoureux",
  sub="Des idées qui ne s'arrêtent pas au 25 décembre", cta="Voir les idées")
P("photohaut", CAD, "idee-cadeau-couple.html", NOELW, "30 idées", "Idée cadeau pour un couple",
  "Idée cadeau pour un couple : 30 idées originales à offrir",
  "Trouver un cadeau pour un couple n'est pas toujours simple. Voici 30 idées originales classées par envie : des cadeaux à vivre à deux, des cadeaux qui rapprochent et des petits prix qui font mouche. Pour Noël, un anniversaire, une pendaison de crémaillère ou un mariage.",
  "idée cadeau couple, cadeau pour un couple, cadeau original à deux, cadeau couple amis",
  sub="À vivre, à partager ou à petit prix", cta="Les 30 idées", photo="idees-cadeaux-noel-couple-1.jpg")
P("liste", CAD, "idee-cadeau-couple.html", NOELW, "Ça fait toujours plaisir", "Cadeaux pour un couple d'amis",
  "Quel cadeau offrir à un couple d'amis ?",
  "Un couple d'amis à gâter ? Jeu de société à deux, cadre avec un souvenir marquant, mugs assortis, jeu de questions ou de dilemmes, bougie pour les soirées cocooning : nos idées de cadeaux qui plaisent aux deux à la fois.",
  "cadeau couple d'amis, cadeau pour deux personnes, idée cadeau couple ami, cadeau commun couple",
  items=["Un jeu de société à deux", "Des mugs assortis", "Un jeu de dilemmes en amoureux", "Une bougie pour les soirs cocooning"], cta="Voir les 30 idées")
P("nuit", CAD, "idee-cadeau-couple.html", ALL, "Comment bien choisir ?", "Le bon cadeau pour un couple",
  "Comment choisir un cadeau pour un couple : nos conseils",
  "Comment choisir un cadeau qui plaira aux deux ? Pensez à ce qui manque au couple, au moment où il sera utilisé et à votre budget. Nos conseils et 30 idées originales pour ne plus offrir un cadeau qui finit dans un placard.",
  "choisir cadeau couple, cadeau qui plaît à deux, idée cadeau couple original, conseils cadeau",
  sub="Celui qui ne finit pas au fond d'un placard", cta="Nos conseils")
P("liste", CAD, "cadeau-couple-pas-cher.html", ALL, "Moins de 20 euros", "Cadeau de couple à petit prix",
  "Cadeau de couple à petit prix : 20 idées qui font plaisir",
  "Un joli cadeau de couple sans exploser le budget : boîte de bons pour à s'offrir au fil de l'année, cadre avec une photo marquante, mugs assortis, bougie parfumée, petit album de vos meilleurs souvenirs. 20 idées tendres et personnelles à petit prix.",
  "cadeau couple pas cher, cadeau petit prix amoureux, idée cadeau couple petit budget, cadeau moins de 20 euros",
  items=["Une boîte de bons pour", "Un cadre avec votre plus belle photo", "Deux mugs assortis", "Un petit album de souvenirs"], cta="Les 20 idées")
P("bulle", CAD, "cadeau-couple-pas-cher.html", ALL, "Le cadeau qui ne coûte rien", "Bon pour : un petit-déjeuner au lit, sans réveil, sans téléphone.",
  "Idée cadeau couple gratuite : la boîte de bons pour",
  "Le cadeau de couple qui ne coûte presque rien mais vaut tout : une boîte de bons pour à s'offrir au fil de l'année. Petit-déjeuner au lit, massage, soirée choisie par l'autre. Retrouvez cette idée et 19 autres cadeaux à petit prix.",
  "bon pour couple, cadeau couple gratuit, idée cadeau fait maison amoureux, cadeau pas cher",
  sub="Et 19 autres cadeaux à petit prix", cta="Voir les idées")
P("photo", CAD, "cadeau-1-an-couple.html", ALL, "Premier anniversaire", "Quel cadeau pour 1 an de couple ?",
  "Quel cadeau offrir pour 1 an de couple ? Nos idées",
  "Un an ensemble, ça se fête ! Cadre avec votre toute première photo, bucket list de couple pour l'année qui vient, souvenir de votre histoire : nos idées de cadeaux pour célébrer ce premier anniversaire et construire la suite à deux.",
  "cadeau 1 an de couple, cadeau anniversaire de couple, idée cadeau 1 an ensemble, premier anniversaire couple",
  sub="Célébrer votre histoire et construire la suite", cta="Les idées cadeaux", photo="retrouver-complicite-couple-1.jpg")
P("liste", CAD, "cadeau-1-an-couple.html", ALL, "Anniversaire de couple", "Cadeaux pour fêter 1 an ensemble",
  "Idées cadeaux pour fêter un an ensemble",
  "Vous fêtez votre premier anniversaire de couple ? Voici des idées de cadeaux qui racontent votre histoire et préparent la suite : la première photo de vous deux encadrée, une bucket list à réaliser ensemble, un souvenir à garder.",
  "cadeau 1 an couple, anniversaire de rencontre cadeau, cadeau anniversaire amoureux, idée cadeau copine copain",
  items=["Votre première photo encadrée", "Une bucket list pour l'année qui vient", "Un souvenir de votre histoire"], cta="Voir les idées")

# ------------------------------------------------ Le jeu Nous Deux (produit)
P("nuit", QJ, "nous-deux-le-jeu.html", ALL, "Le jeu de couple en ligne", "Nous Deux, le jeu qui rapproche",
  "Nous Deux, le jeu de couple en ligne qui rapproche",
  "Nous Deux, c'est un jeu de couple en ligne à vivre une étape à la fois : 52 étapes, des défis, des questions et des jeux pour une année de complicité. Il se joue sur le téléphone, à la maison comme à distance. Une idée cadeau parfaite pour un couple.",
  "jeu de couple, jeu de couple en ligne, jeu pour couple, cadeau couple original, jeu à deux",
  sub="52 étapes pour une année de complicité", cta="Découvrir le jeu")
P("bulle", NOEL, "nous-deux-le-jeu.html", (1, 9), "Idée cadeau de Noël", "Et si cette année, vous offriez une année de complicité ?",
  "Cadeau de Noël couple : Nous Deux, le jeu",
  "Un cadeau de Noël qui se vit plutôt qu'il ne se range : Nous Deux, le jeu de couple en ligne. Une étape par semaine, des défis, des questions et des souvenirs gardés. Parfait à glisser sous le sapin pour votre moitié ou pour un couple que vous aimez.",
  "cadeau noël couple, jeu de couple cadeau, idée cadeau noël amoureux, cadeau à vivre à deux",
  sub="Nous Deux, le jeu de couple à vivre une étape à la fois", cta="Voir le jeu")
P("liste", QJ, "nous-deux-le-jeu.html", ALL, "Ce que vous allez vivre", "Nous Deux, le jeu de couple",
  "Jeu de couple à faire à deux : défis, questions et badges",
  "Dans Nous Deux, le jeu, chaque étape vous propose un défi, une question ou un jeu à faire à deux. Vous débloquez des badges, vous gardez vos souvenirs et vous avancez à votre rythme. Le jeu se joue sur le téléphone, où que vous soyez.",
  "jeu de couple, défis couple, questions couple, jeu à deux téléphone, jeu couple à distance",
  items=["52 étapes originales", "Défis, questions et jeux", "Des badges à débloquer", "Vos souvenirs gardés"], cta="Découvrir le jeu")
P("photohaut", RAV, "nous-deux-le-jeu.html", ALL, "Une étape par semaine", "Retrouvez-vous, une étape à la fois",
  "Un jeu pour retrouver la complicité dans son couple",
  "La routine a pris le dessus ? Nous Deux, le jeu de couple en ligne, vous propose une petite étape à vivre ensemble chaque semaine : une question, un défi, un souvenir. Une façon douce et ludique de remettre de la complicité dans votre quotidien.",
  "retrouver la complicité couple, jeu de couple, sortir de la routine couple, raviver la flamme",
  sub="Questions, défis et souvenirs à deux", cta="Découvrir le jeu", photo="jeux-de-couple-a-deux-1.jpg")
P("nuit", CAD, "nous-deux-le-jeu.html", SV, "Saint-Valentin", "Un cadeau à vivre toute l'année",
  "Cadeau de Saint-Valentin original : un jeu de couple à vivre toute l'année",
  "Pour la Saint-Valentin, offrez plus qu'une soirée : Nous Deux, le jeu de couple en ligne, avec 52 étapes à vivre à deux au fil de l'année. Questions, défis, badges et souvenirs pour garder la complicité bien après le 14 février.",
  "cadeau saint valentin original, cadeau saint valentin couple, jeu de couple, idée saint valentin",
  sub="Nous Deux, le jeu : 52 étapes à deux", cta="Découvrir le jeu")

# ------------------------------------------------ Rendez-vous
P("nuit", RDV, "idees-rendez-vous-couple.html", ALL, "Une idée pour chaque envie", "60 idées de rendez-vous en couple",
  "60 idées de rendez-vous en couple : originales, pas chères, à la maison",
  "À court d'idées pour vos soirées à deux ? Voici 60 idées de rendez-vous en couple : à la maison, gratuites ou presque, pour sortir et bouger, ou franchement romantiques. De quoi casser la routine chaque semaine sans se ruiner.",
  "idée rendez-vous couple, idée date couple, activité à deux, sortie en amoureux, date pas cher",
  sub="À la maison, gratuites, à l'extérieur ou romantiques", cta="Voir les 60 idées")
P("liste", RDV, "idees-rendez-vous-couple.html", ALL, "Sans sortir de chez vous", "Rendez-vous en couple à la maison",
  "Idées de rendez-vous en couple à la maison",
  "Pas envie de sortir ? Installez un pique-nique dans le salon, créez une playlist de vos chansons et dansez, offrez-vous un massage à deux. Des idées de rendez-vous à la maison qui transforment une soirée ordinaire en vrai moment à deux.",
  "rendez-vous couple maison, date à la maison, idée soirée couple maison, activité couple intérieur",
  items=["Un pique-nique dans le salon", "Une playlist de vos chansons", "Un massage à deux, lumière tamisée"], cta="Plus d'idées")
P("liste", RDV, "idees-rendez-vous-couple.html", ALL, "Gratuites ou presque", "Rendez-vous en couple pas chers",
  "Idées de rendez-vous en couple gratuites ou pas chères",
  "Un beau rendez-vous n'a pas besoin de coûter cher. Point de vue en hauteur avec de quoi grignoter, quartier de votre ville jamais exploré, balade à vélo au hasard : nos idées de dates gratuites ou presque pour se retrouver.",
  "rendez-vous couple gratuit, date pas cher, sortie couple petit budget, idée activité à deux gratuite",
  items=["Un point de vue en hauteur", "Un quartier jamais exploré", "Une balade à vélo au hasard"], cta="Voir les idées")
P("photohaut", RDV, "idees-rendez-vous-couple.html", ALL, "Le rendez-vous de la semaine", "Et si vous instauriez un rendez-vous régulier ?",
  "Instaurer un rendez-vous régulier en couple",
  "Un soir par semaine rien qu'à vous deux : c'est l'un des rituels les plus simples pour garder le lien. Retrouvez 60 idées de rendez-vous pour ne jamais tomber à court, à la maison ou à l'extérieur.",
  "rituel de couple, rendez-vous hebdomadaire couple, date night, idée soirée à deux",
  sub="60 idées pour ne jamais être à court", cta="Trouver l'idée du jour", photo="retrouver-complicite-couple-1.jpg")
P("bulle", RDV, "idees-rendez-vous-couple.html", ALL, "Idée de date", "Ce week-end, on réserve un cours à deux : poterie, danse ou cuisine ?",
  "Idée de rendez-vous original : un cours à deux",
  "Une idée de rendez-vous qui change : réserver un cours à deux. Poterie, danse, cuisine ou escalade, apprendre ensemble crée des souvenirs et beaucoup de rires. Retrouvez 59 autres idées de dates originales.",
  "idée date originale, activité couple, cours à deux, sortie en amoureux originale",
  sub="Et 59 autres idées de rendez-vous", cta="Voir les idées")
P("liste", RDV, "idees-rendez-vous-couple.html", ALL, "Plutôt romantique", "Rendez-vous romantiques",
  "Idées de rendez-vous romantiques en couple",
  "Envie de romantisme ? Dîner aux chandelles, balade au coucher du soleil, lettre glissée dans une poche, soirée dansée dans le salon : nos idées de rendez-vous romantiques pour faire battre les cœurs, sans forcément dépenser beaucoup.",
  "rendez-vous romantique, idée romantique couple, soirée romantique, date romantique",
  items=["Une playlist pour danser au salon", "Un pique-nique aux bougies", "Un massage, lumière tamisée"], cta="Plus d'idées")
P("nuit", RDV, "idees-rendez-vous-couple.html", ALL, "Pour les couples fatigués", "Le rendez-vous qui demande zéro énergie",
  "Idée de rendez-vous en couple quand on est fatigués",
  "Fatigués mais envie de passer un vrai moment ensemble ? Il existe des rendez-vous en couple qui ne demandent presque aucune énergie : plaid, playlist, pique-nique dans le salon. Choisissez la bonne idée selon votre humeur du soir.",
  "rendez-vous couple simple, soirée couple fatigués, date facile, idée soirée à deux",
  sub="Choisissez l'idée selon votre humeur du soir", cta="Choisir l'idée")

# ------------------------------------------------ Questions et jeux
P("nuit", QJ, "questions-a-poser-en-couple.html", ALL, "Pour se redécouvrir", "100 questions à poser en couple",
  "100 questions à poser en couple pour se redécouvrir et rire ensemble",
  "Envie de vous rapprocher ? Ces 100 questions à poser en couple relancent la conversation, même après des années ensemble. Drôles, tendres ou profondes, parfaites pour une soirée à deux, un trajet en voiture ou avant de dormir.",
  "questions à poser en couple, questions couple, question à poser à son copain, question à poser à sa copine",
  sub="Drôles, tendres ou profondes", cta="Voir les questions")
P("bulle", QJ, "questions-a-poser-en-couple.html", ALL, "Question du soir", "Quel moment de notre histoire aimerais-tu revivre ?",
  "Question à poser à son conjoint ce soir",
  "Une question à poser à votre conjoint ce soir, et 99 autres pour vous redécouvrir. Des questions drôles, tendres ou plus profondes qui relancent la conversation et font naître de jolis souvenirs.",
  "question à poser à son conjoint, question couple profonde, questions pour se connaître, conversation couple",
  sub="Et 99 autres questions à vous poser", cta="Voir les questions")
P("bulle", QJ, "questions-a-poser-en-couple.html", ALL, "Question pour rire", "Si on partait demain, sans bagage, on irait où ?",
  "Questions drôles à poser en couple",
  "Des questions drôles à poser en couple pour rire ensemble et apprendre des choses étonnantes sur l'autre. À sortir pendant un dîner, un trajet en voiture ou une soirée canapé. 100 questions au total, des plus légères aux plus tendres.",
  "questions drôles couple, question marrante couple, jeu de questions couple, soirée fun à deux",
  sub="100 questions pour rire et se redécouvrir", cta="Jouer à deux")
P("liste", QJ, "questions-a-poser-en-couple.html", ALL, "Après des années ensemble", "Questions pour se redécouvrir",
  "Questions à poser en couple après des années ensemble",
  "On croit tout savoir de l'autre, et pourtant. Ces questions à poser en couple vous font redécouvrir votre partenaire, même après des années : ses rêves, ses souvenirs, ce qui le fait vibrer aujourd'hui. À tester ce soir.",
  "questions couple longue date, se redécouvrir en couple, question intime couple, communication couple",
  items=["Quel rêve n'as-tu jamais osé me dire ?", "Quel souvenir de nous te fait sourire ?", "Qu'est-ce qui te fait vibrer en ce moment ?"], cta="Les 100 questions")
P("bulle", QJ, "tu-preferes-couple.html", ALL, "Tu préfères, version couple", "Tu préfères un week-end surprise ou une soirée plaid et film ?",
  "Tu préfères : 40 questions pour couple",
  "Le jeu Tu préfères version couple : 40 dilemmes drôles ou tendres à trancher à deux. Parfait pour une soirée, un apéro ou un long trajet. Fous rires garantis et quelques révélations au passage.",
  "tu préfères couple, jeu tu préfères, questions tu préfères amoureux, jeu couple soirée",
  sub="40 dilemmes drôles à jouer à deux", cta="Jouer maintenant")
P("bulle", QJ, "tu-preferes-couple.html", ALL, "Dilemme du jour", "Tu préfères qu'on cuisine ensemble ou qu'on commande et qu'on danse ?",
  "Jeu Tu préfères pour couple : questions drôles",
  "Un dilemme pour ce soir, et 39 autres à trancher en amoureux. Le jeu Tu préfères en couple, c'est simple, ça se joue partout et ça révèle souvent des choses inattendues sur l'autre.",
  "tu préfères amoureux, question tu préfères drôle, jeu à deux sans matériel, jeu couple",
  sub="39 autres dilemmes à trancher", cta="Jouer à deux")
P("nuit", QJ, "tu-preferes-couple.html", ALL, "Jeu sans matériel", "Tu préfères : 40 questions pour couple",
  "Jeu Tu préfères couple : 40 questions à jouer à deux",
  "Pas de matériel, pas de préparation : le jeu Tu préfères version couple se joue en deux minutes, au restaurant, en voiture ou au lit. 40 questions drôles ou tendres pour rire et mieux vous connaître.",
  "tu préfères couple, jeu sans matériel couple, jeu à deux rapide, questions couple fun",
  sub="Au resto, en voiture ou sous la couette", cta="Voir les 40 questions")
P("photo", QJ, "jeux-de-couple-a-deux.html", ALL, "Gratuits ou à acheter", "Jeux de couple à faire à deux",
  "Jeux de couple à faire à deux : gratuits ou à acheter",
  "Quels jeux de couple faire à deux ce soir ? Jeux gratuits sans rien acheter, jeux de société pour deux, jeux en ligne : notre comparatif honnête pour choisir selon votre couple, et nos conseils pour réussir votre soirée jeu.",
  "jeux de couple, jeu à deux, jeu de société couple, jeux couple soirée, jeu couple gratuit",
  sub="Notre comparatif pour bien choisir", cta="Voir les jeux", photo="jeux-de-couple-a-deux-1.jpg")
P("liste", QJ, "jeux-de-couple-a-deux.html", ALL, "Sans rien acheter", "Jeux de couple gratuits pour ce soir",
  "Jeux de couple gratuits à faire à la maison",
  "Envie de jouer à deux sans rien acheter ? Questions, Tu préfères, défis, souvenirs à deviner : des jeux de couple gratuits à lancer ce soir, à la maison. Et si l'envie vous prend, nos idées de jeux à acheter.",
  "jeu couple gratuit, jeu à deux maison, jeu sans matériel, soirée jeu couple",
  items=["Le jeu des questions", "Tu préfères, version couple", "Le défi du compliment"], cta="Voir les jeux")
P("nuit", QJ, "jeux-de-couple-a-deux.html", ALL, "Il n'aime pas jouer ?", "Le jeu de couple pour ceux qui n'aiment pas jouer",
  "Comment faire jouer un conjoint qui n'aime pas les jeux",
  "Votre moitié n'aime pas les jeux ? Nos astuces pour proposer un jeu de couple sans pression, choisir le bon format et transformer ça en vrai moment de complicité. Plus un comparatif des jeux gratuits et à acheter.",
  "jeu de couple, conjoint n'aime pas jouer, jeu à deux, soirée jeu couple",
  sub="Nos astuces pour jouer sans pression", cta="Lire les astuces")

# ------------------------------------------------ Quiz
P("bulle", QUIZ, "quiz-type-de-couple.html", ALL, "Le quiz à faire à deux", "Quel type de couple êtes-vous ?",
  "Quel type de couple êtes-vous ? Le quiz à faire à deux",
  "Aventuriers, cocooners, complices ou bâtisseurs ? Faites le quiz Cupidon Passion à deux et découvrez votre profil de couple. Quelques questions, un résultat, et des idées adaptées à votre façon de vous aimer.",
  "quiz couple, test couple, quel type de couple, quiz à faire à deux, test amoureux",
  sub="Quelques questions, un profil, des idées pour vous", cta="Faire le quiz")
P("nuit", QUIZ, "quiz-type-de-couple.html", ALL, "Test couple gratuit", "Faites le test à deux",
  "Test de couple gratuit : découvrez votre profil",
  "Un test de couple gratuit et rapide à faire ensemble. Répondez chacun de votre côté ou côte à côte, et découvrez votre type de couple avec des idées de rendez-vous et de jeux qui vous ressemblent.",
  "test couple gratuit, quiz amour, test compatibilité couple, quiz couple drôle",
  sub="Découvrez votre profil de couple en quelques minutes", cta="Faire le test")
P("liste", QUIZ, "quiz-type-de-couple.html", ALL, "Et vous ?", "Quel couple êtes-vous ?",
  "Quiz couple : aventuriers, cocooners ou complices ?",
  "Plutôt soirées plaid ou week-ends improvisés ? Grandes discussions ou fous rires ? Le quiz Cupidon Passion vous aide à mettre des mots sur votre façon d'être en couple, avec des idées pensées pour votre profil.",
  "quiz couple, type de couple, test amour à deux, profil couple",
  items=["Plutôt plaid ou week-end improvisé ?", "Grandes discussions ou fous rires ?", "Routine douce ou surprises ?"], cta="Faire le quiz")
P("bulle", QUIZ, "quiz-type-de-couple.html", ALL, "Soirée quiz", "Ce soir, on fait le quiz et on compare nos réponses ?",
  "Quiz amoureux à faire en couple ce soir",
  "Une idée simple pour ce soir : faire le quiz de couple ensemble et comparer vos réponses. Ça fait rire, ça fait parler et ça donne des idées de rendez-vous adaptées à votre duo.",
  "quiz amoureux, quiz à faire en couple, soirée couple idée, test couple",
  sub="Ça fait rire, ça fait parler", cta="Lancer le quiz")

# ------------------------------------------------ Soirées en amoureux
P("photohaut", SOI, "soiree-amoureux-maison.html", ALL, "Cocooning", "Soirée en amoureux à la maison",
  "Idées de soirée en amoureux à la maison pour l'hiver",
  "L'hiver est la saison parfaite pour les soirées à deux à la maison. Ambiance tamisée, plaid, massage mutuel, dîner improvisé, jeu de questions : nos idées pour transformer un soir ordinaire en vraie soirée en amoureux, et en faire un rituel.",
  "soirée en amoureux maison, soirée cocooning couple, soirée romantique maison, idée soirée hiver couple",
  sub="Ambiance, idées et petits rituels", cta="Voir les idées", photo="idees-cadeaux-saint-valentin-couple-1.jpg")
P("liste", SOI, "soiree-amoureux-maison.html", ALL, "Ce soir à la maison", "Soirée à deux réussie",
  "Idées pour une soirée à deux réussie à la maison",
  "Réussir une soirée à deux chez soi, c'est d'abord poser l'ambiance : lumière douce, téléphones rangés, une playlist. Ensuite ? Massage mutuel, dîner à quatre mains, jeu de questions. Toutes nos idées de soirées en amoureux.",
  "soirée à deux maison, soirée romantique, idée soirée couple, soirée cocooning",
  items=["Téléphones rangés, lumière douce", "Un dîner à quatre mains", "Un massage mutuel", "Un jeu de questions"], cta="Toutes les idées")
P("bulle", SOI, "soiree-amoureux-maison.html", ALL, "Programme du soir", "Plaid, chocolat chaud et téléphones dans un tiroir.",
  "Soirée cocooning en couple : le programme parfait",
  "Le programme parfait pour une soirée cocooning en amoureux : plaid, chocolat chaud, téléphones rangés et une vraie conversation. Retrouvez nos idées pour réussir vos soirées à deux à la maison tout l'hiver.",
  "soirée cocooning couple, soirée plaid amoureux, soirée hiver à deux, idée soirée maison",
  sub="Nos idées pour des soirées à deux tout l'hiver", cta="Voir les idées")
P("nuit", SOI, "soiree-amoureux-maison.html", ALL, "Un rituel à installer", "Une soirée à deux par semaine",
  "Faire de la soirée en amoureux un rituel de couple",
  "Et si la soirée en amoureux devenait un rituel ? Un soir fixe par semaine, rien qu'à vous, avec une idée différente à chaque fois. Nos conseils pour l'installer et nos idées pour ne jamais s'ennuyer.",
  "rituel couple, soirée en amoureux, date night maison, habitude de couple",
  sub="Nos idées pour ne jamais s'ennuyer", cta="Commencer ce soir")
P("photo", SOI, "soiree-amoureux-maison.html", ALL, "Soirée romantique", "Transformer un soir ordinaire",
  "Soirée romantique à la maison : nos idées simples",
  "Pas besoin de réserver un restaurant pour une soirée romantique. Avec trois bougies, une playlist et une idée, votre salon devient le meilleur endroit pour un rendez-vous. Nos idées simples et pas chères.",
  "soirée romantique maison, idée romantique pas cher, soirée amoureux, rendez-vous maison",
  sub="Trois bougies, une playlist et une idée", cta="Voir les idées", photo="calendrier-avent-couple-2.jpg")

# ------------------------------------------------ Raviver son couple
P("photo", RAV, "retrouver-complicite-couple.html", ALL, "7 gestes simples", "Retrouver la complicité dans son couple",
  "Retrouver la complicité dans son couple : 7 gestes simples",
  "La routine, la fatigue ou les écrans ont éloigné votre couple ? 7 gestes simples pour retrouver la complicité au quotidien : se regarder, poser une vraie question, raconter un souvenir, dire merci. Des petites choses qui changent beaucoup.",
  "retrouver la complicité couple, raviver la flamme, couple routine, se rapprocher en couple",
  sub="Des petites choses qui changent beaucoup", cta="Lire les 7 gestes", photo="retrouver-complicite-couple-1.jpg")
P("liste", RAV, "retrouver-complicite-couple.html", ALL, "À tester cette semaine", "Gestes pour retrouver la complicité",
  "Gestes simples pour raviver la complicité de son couple",
  "Raviver la complicité commence souvent par des gestes minuscules : se regarder vraiment, poser une vraie question, glisser une petite attention, dire merci. Découvrez nos 7 gestes simples et comment en faire des habitudes.",
  "raviver la complicité, geste amoureux, couple routine solution, rapprocher son couple",
  items=["Reprendre l'habitude de se regarder", "Poser une vraie question", "Glisser une petite attention", "Dire merci"], cta="Les 7 gestes")
P("nuit", RAV, "retrouver-complicite-couple.html", ALL, "Couple et routine", "Pourquoi la complicité s'efface ?",
  "Pourquoi la complicité s'efface dans un couple",
  "Routine, fatigue, charge mentale, écrans, non-dits : la complicité s'efface souvent sans bruit. Comprendre pourquoi, c'est déjà commencer à la retrouver. Nos pistes concrètes pour remettre du lien et de la légèreté.",
  "complicité couple, couple qui s'éloigne, routine couple, charge mentale couple",
  sub="Comprendre pour mieux se retrouver", cta="Lire l'article")
P("bulle", RAV, "retrouver-complicite-couple.html", ALL, "Le geste du jour", "Raconte-moi un souvenir de nous que tu n'as jamais oublié.",
  "Une idée pour raviver la flamme ce soir",
  "Raconter un souvenir commun est l'un des gestes les plus simples pour se rapprocher. Essayez ce soir, puis découvrez nos 6 autres gestes pour retrouver la complicité dans votre couple.",
  "raviver la flamme, souvenir de couple, complicité amoureuse, idée couple",
  sub="Et 6 autres gestes pour se rapprocher", cta="Voir les gestes")
P("liste", RAV, "retrouver-complicite-couple.html", ALL, "Sans reproche", "En parler sans dispute",
  "Comment parler de la complicité perdue sans reproche",
  "Dire à l'autre qu'il vous manque sans que ça tourne au reproche : choisissez le bon moment, parlez en je, proposez plutôt que d'exiger et écoutez la réponse. Nos conseils pour une conversation qui rapproche.",
  "communication couple, parler à son conjoint, dispute couple, conseil couple",
  items=["Choisir le bon moment", "Parler en « je »", "Proposer plutôt qu'exiger", "Écouter la réponse"], cta="Nos conseils")

# ------------------------------------------------ Conseils & rituels
P("liste", CONS, "retrouver-complicite-couple.html", ALL, "Rituels de couple", "Rituels qui font durer l'amour",
  "Rituels de couple simples pour durer",
  "Les couples complices ont souvent des rituels : un rendez-vous régulier, un moment sans écran, un petit bilan à deux de temps en temps, une soirée maison qui devient un rendez-vous. Nos idées pour installer les vôtres.",
  "rituel de couple, habitude de couple, conseil couple durable, complicité",
  items=["Un rendez-vous régulier", "Un moment sans écran", "Un bilan à deux de temps en temps"], cta="Lire les conseils")
P("nuit", CONS, "conseils.html", ALL, "Le coin des conseils", "Conseils pour votre couple",
  "Conseils pour votre couple : complicité, jeux, cadeaux, soirées",
  "Tous les conseils Cupidon Passion pour nourrir votre couple : retrouver la complicité, jouer à deux, trouver le bon cadeau, réussir vos soirées à la maison. Des articles simples et bienveillants, à lire à deux.",
  "conseils couple, vie de couple, relation amoureuse conseils, blog couple",
  sub="Complicité, jeux, cadeaux et soirées à deux", cta="Lire les conseils")
P("bulle", CONS, "retrouver-complicite-couple.html", ALL, "Petit rituel", "Chaque dimanche soir : 10 minutes, sans téléphone, pour se raconter la semaine.",
  "Rituel de couple : le bilan du dimanche soir",
  "Un rituel de couple tout simple : dix minutes chaque dimanche soir, sans téléphone, pour se raconter la semaine. Retrouvez d'autres rituels et gestes pour garder la complicité au quotidien.",
  "rituel couple, communication couple, habitude amoureuse, conseil couple",
  sub="D'autres rituels pour garder le lien", cta="Voir les rituels")
P("photohaut", CONS, "jeux-de-couple-a-deux.html", ALL, "Un peu chaque semaine", "Jouer à deux, le rituel qui fait rire",
  "Jouer en couple chaque semaine : un rituel qui rapproche",
  "Jouer ensemble change l'ambiance d'un couple : on rit, on se parle autrement, on se découvre. Et si vous en faisiez un rituel ? Nos idées de jeux gratuits ou à acheter pour jouer un peu chaque semaine.",
  "jeu de couple, rituel couple, soirée jeu à deux, complicité",
  sub="Nos idées de jeux gratuits ou à acheter", cta="Voir les jeux", photo="jeux-de-couple-a-deux-1.jpg")

# ------------------------------------------------ Fêtes de fin d'année
P("nuit", NOEL, "que-faire-couple-fetes.html", FETES, "Pendant les fêtes", "Que faire à deux pendant les fêtes ?",
  "Que faire à deux pendant les fêtes de fin d'année",
  "Entre les repas de famille et les cadeaux, gardez du temps rien qu'à vous deux pendant les fêtes. Ambiance cosy, activités à faire ensemble, idées pour terminer l'année en beauté : notre petit guide des fêtes en amoureux.",
  "fêtes en couple, que faire à deux noël, activité couple fin d'année, noël en amoureux",
  sub="Garder du temps rien qu'à vous deux", cta="Voir les idées")
P("liste", NOEL, "que-faire-couple-fetes.html", FETES, "Fin d'année en amoureux", "Activités à deux pendant les fêtes",
  "Activités en couple pendant les vacances de Noël",
  "Les vacances de Noël sont parfaites pour se retrouver. Une soirée film de votre jeunesse, une balade dans les lumières, un chocolat chaud maison, trois rêves à écrire pour l'année prochaine : nos idées d'activités à deux.",
  "activité couple vacances noël, que faire en couple en décembre, noël à deux, idée sortie couple hiver",
  items=["Une balade dans les lumières", "Un film de votre jeunesse", "Trois rêves pour l'année prochaine"], cta="Plus d'idées")
P("bulle", NOEL, "que-faire-couple-fetes.html", FETES, "Avant la nouvelle année", "Écrivons trois rêves à réaliser ensemble l'année prochaine.",
  "Rituel de fin d'année en couple : trois rêves à réaliser",
  "Un joli rituel pour finir l'année à deux : écrire sur papier trois rêves à réaliser ensemble l'année prochaine. Retrouvez nos autres idées pour vivre les fêtes de fin d'année en amoureux.",
  "rituel fin d'année couple, projets de couple, nouvel an à deux, bilan couple",
  sub="Nos idées pour les fêtes à deux", cta="Voir les idées")
P("photo", NOEL, "que-faire-couple-fetes.html", FETES, "Noël cosy", "Créer une ambiance rien qu'à vous",
  "Noël en amoureux : créer une ambiance cosy à deux",
  "Un Noël en amoureux commence par une ambiance : lumières douces, déco faite ensemble, playlist de fêtes, plaid. Nos idées pour créer un cocon rien qu'à vous pendant les fêtes de fin d'année.",
  "noël en amoureux, ambiance cosy noël, déco noël couple, fêtes à deux",
  sub="Lumières douces, playlist et plaid", cta="Voir les idées", photo="calendrier-avent-couple-1.jpg")
P("nuit", NOEL, "que-faire-couple-fetes.html", FETES, "Réveillon à deux", "Un réveillon rien qu'à vous",
  "Idées pour un réveillon en amoureux",
  "Vous fêtez le réveillon en tête à tête ? Dîner à quatre mains, souvenirs de l'année, projets pour la suite, petite danse au salon : nos idées pour un réveillon en amoureux simple et mémorable.",
  "réveillon en amoureux, nouvel an à deux, soirée réveillon couple, idée réveillon",
  sub="Simple, tendre et mémorable", cta="Voir les idées")

# ------------------------------------------------ Saint-Valentin (démarrage)
P("photohaut", CAD, "idees-cadeaux-saint-valentin-couple.html", SV, "Saint-Valentin", "Sortir de la routine pour la Saint-Valentin",
  "Idées cadeaux de Saint-Valentin pour sortir de la routine",
  "Marre des fleurs et des chocolats ? Pour la Saint-Valentin, offrez quelque chose à vivre à deux : une expérience, un jeu pour se parler et rire, un souvenir de votre histoire. Nos idées de cadeaux qui sortent de la routine, même à petit budget.",
  "cadeau saint valentin, idée cadeau saint valentin original, saint valentin couple, cadeau amoureux",
  sub="Des cadeaux qui créent des souvenirs", cta="Lire l'article", photo="idees-cadeaux-saint-valentin-couple-1.jpg")
P("liste", CAD, "idees-cadeaux-saint-valentin-couple.html", SV, "14 février", "Cadeaux de Saint-Valentin à vivre",
  "Cadeau de Saint-Valentin original : à vivre plutôt qu'à ranger",
  "Un cadeau de Saint-Valentin original, c'est souvent un moment plutôt qu'un objet. Une sortie à deux, un jeu pour se parler, un souvenir qui raconte votre histoire, une idée faite maison : nos pistes pour un 14 février différent.",
  "cadeau saint valentin original, saint valentin idée, cadeau saint valentin lui, cadeau saint valentin elle",
  items=["Une expérience à vivre à deux", "Un jeu pour se parler et rire", "Un souvenir de votre histoire"], cta="Toutes les idées")
P("bulle", CAD, "idees-cadeaux-saint-valentin-couple.html", SV, "Saint-Valentin", "Faut-il absolument offrir un cadeau le 14 février ?",
  "Faut-il offrir un cadeau pour la Saint-Valentin ?",
  "Faut-il absolument offrir un cadeau pour la Saint-Valentin ? Notre réponse, les erreurs à éviter et des idées pour un 14 février réussi, même avec un petit budget ou après des années ensemble.",
  "saint valentin cadeau, saint valentin petit budget, saint valentin couple, idée 14 février",
  sub="Notre réponse et nos idées", cta="Lire l'article")
P("nuit", RDV, "idees-cadeaux-saint-valentin-couple.html", SV, "Petit budget", "Une Saint-Valentin réussie sans se ruiner",
  "Saint-Valentin petit budget : nos idées",
  "Une Saint-Valentin réussie ne dépend pas du prix du cadeau. Idées faites maison, gratuites ou à petit budget, erreurs à éviter : notre guide pour un 14 février qui vous ressemble.",
  "saint valentin pas cher, idée saint valentin petit budget, saint valentin fait maison, soirée saint valentin",
  sub="Idées faites maison ou à petit prix", cta="Voir les idées")

# ------------------------------------------------ Célibataires
P("nuit", CEL, "questions-a-poser-en-couple.html", ALL, "Premier rendez-vous", "Des questions pour briser la glace",
  "Questions à poser lors d'un premier rendez-vous",
  "Peur des blancs au premier rendez-vous ? Des questions légères, drôles ou plus profondes pour apprendre à se connaître et faire naître une vraie conversation. À piocher dans notre liste de 100 questions.",
  "questions premier rendez-vous, premier date questions, apprendre à se connaître, célibataire",
  sub="Pour faire naître une vraie conversation", cta="Voir les questions")
P("bulle", CEL, "tu-preferes-couple.html", ALL, "Pour un date", "Tu préfères un premier rendez-vous au musée ou au bowling ?",
  "Tu préfères : questions pour un premier rendez-vous",
  "Le Tu préfères marche aussi en date ! Des dilemmes légers pour rire, détendre l'atmosphère et découvrir les goûts de l'autre dès le premier rendez-vous. 40 questions à piocher.",
  "tu préfères date, premier rendez-vous idée, jeu pour faire connaissance, célibataire",
  sub="Pour rire et faire connaissance", cta="Voir les questions")
P("liste", CEL, "idees-rendez-vous-couple.html", ALL, "Idées de premier date", "Premier rendez-vous original",
  "Idées de premier rendez-vous originales",
  "Envie d'un premier rendez-vous qui sort du sempiternel verre en terrasse ? Point de vue en hauteur, quartier à explorer, cours à deux : des idées de dates originales qui facilitent la conversation.",
  "idée premier rendez-vous, premier date original, idée date, rencontre amoureuse",
  items=["Un point de vue en hauteur", "Un quartier à explorer", "Un cours de cuisine ou de danse"], cta="Plus d'idées")
P("bulle", CEL, "quiz-type-de-couple.html", ALL, "Et si c'était vous ?", "Quel couple formeriez-vous ?",
  "Quiz amoureux : quel type de couple formeriez-vous ?",
  "Célibataire ou en début d'histoire ? Faites notre quiz pour découvrir quel type de couple vous aimez former : aventurier, cocooner ou complice. Une façon ludique de mieux savoir ce que vous cherchez.",
  "quiz amoureux, test amour célibataire, quel couple suis-je, quiz relation",
  sub="Aventurier, cocooner ou complice ?", cta="Faire le quiz")

# ------------------------------------------------ Citations (textes originaux Cupidon Passion)
CITS = [
    ("L'amour, ce n'est pas tout faire ensemble. C'est avoir envie de se raconter la journée.", "retrouver-complicite-couple.html"),
    ("Les plus beaux rendez-vous commencent souvent en pyjama.", "soiree-amoureux-maison.html"),
    ("Être complices, c'est rire de la même chose avant même d'avoir parlé.", "questions-a-poser-en-couple.html"),
    ("Le meilleur cadeau, c'est un moment que l'on n'oubliera pas.", "idee-cadeau-couple.html"),
    ("On ne retrouve pas la flamme. On la rallume, un petit geste à la fois.", "retrouver-complicite-couple.html"),
    ("Aimer, c'est aussi poser la question dont on ne connaît pas encore la réponse.", "questions-a-poser-en-couple.html"),
    ("Un plaid, deux chocolats chauds, et le monde peut bien attendre.", "soiree-amoureux-maison.html"),
    ("Chaque semaine mérite son petit rendez-vous à deux.", "idees-rendez-vous-couple.html"),
    ("Le temps passé ensemble, c'est le seul cadeau qui ne s'use pas.", "idees-cadeaux-noel-couple.html"),
    ("Une histoire d'amour, ça s'écrit aussi dans les petits riens.", "nous-deux-le-jeu.html"),
]
_win = {"idees-cadeaux-noel-couple.html": NOELW}
for i, (q, page) in enumerate(CITS):
    P("bulle", CIT, page, _win.get(page, ALL), "Citation d'amour", q,
      f"Citation couple : {q.rstrip('.')}"[:100],
      f"« {q} » Une citation d'amour à partager avec votre moitié ou à garder pour vous. Sur Cupidon Passion, retrouvez des idées, des jeux et des conseils pour nourrir la complicité de votre couple au quotidien.",
      "citation amour, citation couple, phrase d'amour, citation complicité, mots doux",
      sub="Partagez-la avec votre moitié", cta="Plus d'idées pour vous deux")

# ------------------------------------------------ Compléments (pages qui rapportent + liste e-mail)
P("photohaut", NOEL, "idees-cadeaux-noel-couple.html", NOELW, "Pour lui, pour elle, pour deux", "Le cadeau de Noël qui crée des souvenirs",
  "Cadeau de Noël pour son copain ou sa copine : des souvenirs à deux",
  "Vous cherchez un cadeau de Noël pour votre copain, votre copine ou votre conjoint ? Offrez un souvenir à créer ensemble plutôt qu'un objet de plus : expérience, jeu, carnet de l'année. Nos idées testées et approuvées, pour tous les budgets.",
  "cadeau noël copain, cadeau noël copine, cadeau noël conjoint, idée cadeau noël amoureux",
  sub="Expérience, jeu ou carnet de l'année", cta="Voir les idées", photo="idees-cadeaux-noel-couple-1.jpg")
P("liste", NOEL, "idees-cadeaux-noel-couple.html", NOELW, "Comment choisir ?", "Trois questions avant d'acheter",
  "Comment choisir un cadeau de Noël pour un couple",
  "Avant d'acheter un cadeau de Noël pour un couple, posez-vous trois questions : que manque-t-il au couple, quel est votre budget, quand le cadeau sera-t-il utilisé ? La méthode simple et nos idées pour viser juste.",
  "choisir cadeau noël, cadeau noël couple, idée cadeau noël utile, cadeau noël original",
  items=["Que manque-t-il au couple ?", "Quel est votre budget ?", "Quand sera-t-il utilisé ?"], cta="Nos idées")
P("nuit", CAD, "cadeau-couple-pas-cher.html", NOELW, "Petit prix, grand effet", "Des cadeaux tendres à petit prix",
  "Cadeau de couple pas cher mais personnel",
  "Un cadeau pas cher peut être le plus touchant : une photo encadrée, un album de vos meilleurs souvenirs, une boîte de bons pour. 20 idées de cadeaux de couple tendres et personnels, pour Noël ou un anniversaire.",
  "cadeau couple pas cher, cadeau personnalisé couple, cadeau noël petit prix, idée cadeau amoureux",
  sub="20 idées tendres et personnelles", cta="Voir les 20 idées")
P("photo", QJ, "nous-deux-le-jeu.html", ALL, "Partout, sur le téléphone", "Un jeu de couple, même à distance",
  "Jeu de couple à distance : Nous Deux, le jeu",
  "En couple à distance ou souvent séparés ? Nous Deux, le jeu se joue sur le téléphone, chacun de son côté ou ensemble. Une étape par semaine, des questions et des défis pour garder le lien, où que vous soyez.",
  "jeu couple à distance, relation à distance, jeu couple téléphone, garder le lien à distance",
  sub="Une étape par semaine pour garder le lien", cta="Découvrir le jeu", photo="jeux-de-couple-a-deux-1.jpg")
P("bulle", CAD, "idee-cadeau-couple.html", ALL, "Crémaillère, mariage, anniversaire", "Un cadeau qui plaît aux deux, ça existe ?",
  "Cadeau pour un couple : crémaillère, mariage, anniversaire",
  "Pendaison de crémaillère, mariage, anniversaire : trouver un cadeau qui plaît aux deux, c'est possible. Nos 30 idées originales, des cadeaux à vivre aux petits prix qui font mouche.",
  "cadeau crémaillère couple, cadeau mariage original, cadeau anniversaire couple, idée cadeau deux personnes",
  sub="Nos 30 idées originales", cta="Voir les idées")
P("nuit", RAV, "index.html#lettre", ALL, "Offert", "Le Kit des Amoureux, gratuit",
  "Le Kit des Amoureux : idées et défis de couple offerts",
  "Recevez gratuitement Le Kit des Amoureux de Cupidon Passion : des idées de rendez-vous, des questions et des petits défis pour raviver la complicité de votre couple. Et chaque semaine, une nouvelle idée par e-mail.",
  "kit couple gratuit, idées couple gratuites, défis de couple, newsletter couple",
  sub="Idées, questions et défis à recevoir par e-mail", cta="Recevoir le kit")
P("liste", CONS, "index.html#lettre", ALL, "Chaque semaine", "Une idée pour votre couple",
  "Une idée par semaine pour votre couple, gratuite",
  "Envie d'entretenir la complicité sans y penser ? Inscrivez-vous et recevez chaque semaine une idée pour votre couple, plus Le Kit des Amoureux offert : rendez-vous, questions, défis. C'est gratuit.",
  "idée couple semaine, newsletter couple, conseil couple gratuit, complicité",
  items=["Le Kit des Amoureux offert", "Une idée chaque semaine", "Rendez-vous, questions, défis"], cta="Je m'inscris")
P("bulle", QUIZ, "tu-preferes-couple.html", ALL, "Test express", "Tu préfères qu'on parle de nos rêves ou qu'on les réalise ?",
  "Test couple rapide : le jeu Tu préfères",
  "Un test de couple rapide et drôle : le jeu Tu préfères. 40 dilemmes à trancher à deux pour découvrir vos points communs et vos différences, en riant.",
  "test couple, tu préfères couple, quiz à deux, jeu questions couple",
  sub="40 dilemmes pour vous découvrir", cta="Jouer à deux")
