# Journal des décisions de conception

Ce fichier garde les décisions qui changent la situation de départ du mod (voir `Rule/07_histoire_1918.md`). Une décision n'y est écrite qu'une fois validée par masterfr.

## Version du jeu visée

HOI4 1.19 (dernier correctif : 1.19.4.1, 29 octobre 2026, d'après la page *Patches* du wiki officiel). `descriptor.mod` déclare `supported_version="1.19.*"`.

## Date de départ

**1er janvier 1919**, choisie par masterfr le 4 novembre 2026 (« ça permettra de commencer tranquillement une partie »). Le mois a été donné sans jour ; le 1er janvier est retenu par défaut.

Situation réelle à cette date : armistice du 11 novembre 1918 en vigueur, paix non signée (conférence de Paris ouverte le 18 janvier 1919), république allemande dirigée par le Conseil des commissaires du peuple d'Ebert, guerre civile russe, guerre polono-ukrainienne autour de Lwów.

Mise en œuvre :
- `common/defines/iro_defines.lua` : `NDefines.NGame.START_DATE` et `NDefines.NDiplomacy.TENSION_TIME_SCALE_START_DATE` à `"1919.1.1.12"`.
- `common/bookmarks/iro_1919.txt` : signet unique, les signets vanilla étant retirés par `replace_path="common/bookmarks"`.
- `NDefines.NGame.END_DATE` reste à sa valeur vanilla (`"1949.1.1.1"`, date du tableau des scores final) : à décider.

## Historique de départ

Les fichiers `history/` vanilla décrivent 1936. Changer seulement la date de départ ferait démarrer le monde de 1936 en 1918. Ils seront réécrits pays par pays après le choix de la date.
