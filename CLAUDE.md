# Instructions pour les IA travaillant sur ce dépôt

Mod Hearts of Iron IV inspiré d'*Iron Order 1919*, départ en 1918. Langue de travail : français.

**Avant d'écrire ou de modifier du contenu, lire le dossier [`Rule/`](Rule/README.md).** Ses règles sont obligatoires.

En résumé :

1. Ne jamais inventer un effet, un trigger ou un modificateur : le vérifier dans les fichiers vanilla ou le wiki officiel. En cas de doute, le dire.
2. Pas de texte de remplissage ni de formules génériques ; chaque texte est précis et propre à son pays et à son époque.
3. Faits réels exacts ; divergences uchroniques marquées `# UCHRONIE`.
4. Produire peu, mais du contenu relisible et testé.
5. Lancer `python3 Rule/outils/verifier_mod.py` avant chaque commit.
6. Terminer chaque tâche par le compte rendu obligatoire de [`Rule/10_definition_de_termine.md`](Rule/10_definition_de_termine.md) : fichiers modifiés, fonctionnalités, tests réellement exécutés, limites restantes, décisions à valider. Ne jamais présenter un contrôle non effectué comme validé.
