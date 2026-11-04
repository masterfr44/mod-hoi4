# 01 — Principes anti « AI slop »

Ces règles s'appliquent à tout : script, texte, graphisme.

## 1. Ne rien inventer qui doive exister dans le moteur

- Chaque effet, déclencheur (trigger), modificateur ou scope utilisé doit **exister dans la version de HOI4 ciblée**. Vérifier dans les fichiers vanilla (`Hearts of Iron IV/common`, `events`, `history`…) ou sur le wiki officiel (`hoi4.paradoxwikis.com`, pages *Effect*, *Triggers*, *Modifiers*).
- Si un effet n'a pas pu être vérifié, ne pas l'utiliser. Le signaler dans la PR.
- Pas de `add_super_army = yes` ou autre effet « qui sonne bien » sans source.

## 2. Pas de remplissage

Interdit dans un commit :

- `TODO`, `FIXME`, `PLACEHOLDER`, `lorem ipsum`, `...` laissés dans un texte affiché au joueur.
- Des textes génériques interchangeables (« Notre nation fait face à un choix crucial », « Une nouvelle ère commence »). Chaque texte doit contenir des éléments **propres à ce pays, ce moment, ces personnages**.
- Des options d'événement qui ne font rien ou font la même chose.
- Des priorités nationales recopiées d'un pays à l'autre en changeant seulement le tag.

Un fichier incomplet reste sur une branche de travail ; il n'est pas fusionné.

## 3. Chaque élément a une raison d'être

Avant d'ajouter un événement, une priorité ou une technologie, on doit pouvoir répondre :

- **Pourquoi** existe-t-il (fait historique, choix uchronique du mod, besoin de gameplay) ?
- **Qu'est-ce qu'il change** concrètement pour le joueur ?
- **À quoi il se relie** (quelle priorité le déclenche, quelle technologie il débloque) ?

Rien d'orphelin : un événement jamais déclenché ou une technologie qui ne mène nulle part est un bug.

## 4. Peu mais bien

Mieux vaut 10 événements écrits, équilibrés et testés que 100 générés en série. Une IA ne doit pas produire plus de contenu que ce qui peut être relu par une personne dans la même session.

## 5. Tester en jeu

Un contenu n'est « fini » que lorsqu'il a été chargé dans le jeu :

- lancer HOI4 avec `-debug` ;
- vérifier `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log` : **aucune nouvelle erreur** liée au fichier modifié ;
- déclencher l'élément (console : `event <id> <TAG>`, `focus.autocomplete`, `research <tech>`…) et regarder le résultat.

Si le test n'a pas été fait, l'écrire clairement dans la PR (« non testé en jeu »).

## 6. Être honnête sur l'incertitude

Une IA (ou un contributeur) qui ne connaît pas une date, un nom, une syntaxe, le dit. Une question vaut mieux qu'une erreur plausible.

## 7. Respect de l'œuvre d'origine

Le mod s'**inspire** de *Iron Order 1919* : on reprend l'esprit (uchronie dieselpunk, mechas dans l'après-guerre), **pas les fichiers**. Interdit de copier images, modèles 3D, musiques ou textes du jeu original ou d'un autre mod sans autorisation écrite. Les créations sont originales, et les sources d'inspiration sont créditées.
