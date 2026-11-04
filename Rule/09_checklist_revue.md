# 09 — Checklist avant commit / PR (contenu du mod)

Cocher chaque case dans la description de la PR. Une case non vérifiée n'est **pas** cochée : on écrit pourquoi.

Cette liste couvre le contenu HOI4. Elle s'ajoute à la [définition de « terminé »](10_definition_de_termine.md), qui s'applique à toute tâche.

## Mécanique
- [ ] `python3 Rule/outils/verifier_mod.py` passe sans erreur.
- [ ] Le jeu a été lancé avec `-debug` et `error.log` ne contient aucune nouvelle erreur liée aux fichiers modifiés.
- [ ] Chaque élément ajouté a été déclenché en jeu (événement, priorité, technologie) et ses infobulles relues.
- [ ] Tous les effets et triggers utilisés existent (vérifiés dans le vanilla ou le wiki).
- [ ] Aucun élément orphelin : tout événement est appelé, toute technologie mène quelque part ou termine une branche voulue.

## Contenu
- [ ] Aucun `TODO`, `PLACEHOLDER`, texte de remplissage ou formule générique (voir `03_localisation.md`).
- [ ] Toutes les clés de localisation existent en français **et** en anglais.
- [ ] Faits réels vérifiés, divergences uchroniques marquées `# UCHRONIE`.
- [ ] Équilibrage comparé au vanilla, valeurs inhabituelles justifiées.
- [ ] `ai_will_do` / `ai_chance` renseignés et cohérents.

## Graphismes
- [ ] Formats et dimensions conformes à `08_graphismes.md`.
- [ ] Sprites déclarés dans un `.gfx`, images vérifiées en jeu.
- [ ] Origine de chaque image notée dans `gfx/CREDITS.md`.

## PR
- [ ] La PR reste dans le périmètre demandé.
- [ ] Le compte rendu obligatoire (fichiers, fonctionnalités, tests, limites, décisions) est rempli.
