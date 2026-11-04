# Journal des décisions de conception

Ce fichier garde les décisions qui changent la situation de départ du mod (voir `Rule/07_histoire_1918.md`). Une décision n'y est écrite qu'une fois validée par masterfr.

## Version du jeu visée

HOI4 1.19 (dernier correctif : 1.19.4.1, 29 octobre 2026, d'après la page *Patches* du wiki officiel). `descriptor.mod` déclare `supported_version="1.19.*"`.

## Date de départ

Décision en attente. Options présentées :

| Date | Situation |
|---|---|
| 11 novembre 1918 | Armistice de Rethondes ; révolution en Allemagne ; guerre civile russe |
| 1er janvier 1918 | Guerre en cours ; Brest-Litovsk pas encore signé |
| 3 mars 1918 | Traité de Brest-Litovsk ; la Russie sort de la guerre |

Tant que la date n'est pas fixée, le signet (`common/bookmarks/`) et l'override de `NDefines.NGame.START_DATE` (`common/defines/`) ne sont pas écrits.

## Historique de départ

Les fichiers `history/` vanilla décrivent 1936. Changer seulement la date de départ ferait démarrer le monde de 1936 en 1918. Ils seront réécrits pays par pays après le choix de la date.
