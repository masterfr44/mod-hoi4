# Rule — Règles de création du mod (anti « AI slop »)

Ce dossier définit les règles que **tout contenu ajouté au mod** doit respecter, qu'il soit écrit à la main ou généré par une IA (Claude, ChatGPT, etc.).

L'« AI slop », c'est du contenu qui *a l'air* correct mais qui est creux, inventé ou cassé : des événements au texte générique, des effets qui n'existent pas dans le moteur, des dates historiques fausses, des clés de localisation manquantes, des fichiers jamais testés en jeu. Ces règles sont là pour l'empêcher d'entrer dans le dépôt.

## Ordre de lecture

| Fichier | Sujet |
|---|---|
| [01_principes.md](01_principes.md) | Les règles d'or, valables partout |
| [02_script_hoi4.md](02_script_hoi4.md) | Syntaxe, encodage, nommage, arborescence du mod |
| [03_localisation.md](03_localisation.md) | Textes du jeu (`.yml`), style d'écriture |
| [04_evenements.md](04_evenements.md) | Événements |
| [05_priorites_nationales.md](05_priorites_nationales.md) | Arbres de priorités nationales (focus) |
| [06_recherche.md](06_recherche.md) | Arbre de recherche logique et réaliste |
| [07_histoire_1918.md](07_histoire_1918.md) | Départ en 1918, cohérence historique et uchronique |
| [08_graphismes.md](08_graphismes.md) | Portraits, drapeaux, icônes, unités |
| [09_checklist_revue.md](09_checklist_revue.md) | Liste à cocher pour le contenu HOI4 avant chaque commit / PR |
| [10_definition_de_termine.md](10_definition_de_termine.md) | Définition de « terminé » et compte rendu obligatoire, pour toute tâche |

## Outil de vérification

`Rule/outils/verifier_mod.py` détecte automatiquement une partie des erreurs (accolades déséquilibrées, texte de remplissage, clés de localisation manquantes, mauvais encodage). Lancez-le avant chaque commit :

```bash
python3 Rule/outils/verifier_mod.py
```

Il ne remplace pas un test en jeu : il attrape seulement les erreurs mécaniques.

## Pour les IA

Une IA qui travaille sur ce dépôt **doit lire ce dossier avant d'écrire du contenu** (voir `CLAUDE.md` à la racine). En cas de doute sur une syntaxe ou un fait historique, elle doit le dire au lieu d'inventer.
