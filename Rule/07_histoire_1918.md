# 07 — Départ en 1918 et cohérence historique

## Mise en place technique

- Date de départ : `NDefines.NGame.START_DATE` dans `common/defines/` (format `"1918.1.1.12"`), et un signet (`common/bookmarks/`) à la même date.
- Les fichiers vanilla `history/countries`, `history/states` et `history/units` décrivent 1936 : ils doivent être **réécrits** pour 1918 (frontières, propriétaires, bâtiments, dirigeants, ordres de bataille), pas seulement décalés de date.
- Pays qui n'existent pas encore en 1918 (ou plus) : gérer avec `replace_path` ou en vidant leurs états, jamais en laissant des fichiers 1936 contradictoires.

## Choisir la date exacte

Le premier jalon du mod est **1918**. La date précise (par ex. 1er janvier 1918 en pleine guerre, ou 11 novembre 1918 à l'armistice) est une décision de conception : elle change toute la situation de départ. Elle est écrite dans `docs/` ou dans le README avant de remplir l'historique. Tant qu'elle n'est pas fixée, une IA ne la choisit pas seule.

## Réel ou uchronie : toujours le dire

Le mod mélange l'histoire réelle et l'univers dieselpunk inspiré d'*Iron Order 1919*. Chaque contenu doit savoir de quel côté il est :

- **Fait réel** (dirigeants, frontières, traités, batailles avant le point de divergence) → doit être **exact**. Noms complets, dates, titres corrects. Exemple : Georges Clemenceau, président du Conseil depuis novembre 1917.
- **Divergence uchronique** → doit être **cohérente** avec le reste de l'univers du mod et notée comme telle (commentaire `# UCHRONIE : ...` dans le script).

Ce qui est interdit, c'est l'erreur involontaire présentée comme un fait : un dirigeant au mauvais poste, une ville dans le mauvais pays, une unité qui n'existait pas.

## Personnages

- Nom, prénom, rôle et idéologie conformes à l'époque. Vérifier qu'il était vivant et actif en 1918.
- Les traits correspondent à sa carrière réelle (un général d'artillerie n'a pas un trait de cavalerie sans raison).
- Personnage inventé : marqué comme tel dans un commentaire et dans `docs/`.

## Vérification

Pour chaque pays ajouté, la PR contient une courte liste des faits utilisés (chef d'État, chef de gouvernement, partis, situation militaire au départ) et la source.
