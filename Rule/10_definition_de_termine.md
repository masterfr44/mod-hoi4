# 10 — Définition de « terminé » et compte rendu obligatoire

Avant de déclarer une tâche terminée, vérifier les points suivants.

> Note d'application au mod : la plupart des points concernent l'interface du jeu (écrans `.gui`, décisions, infobulles) et tout outil annexe (scripts, page web, etc.). Pour HOI4, un « bouton » est aussi une option d'événement, une décision ou une priorité ; un « chargement » ou un « résultat vide » correspond aux cas où une condition n'est pas remplie (décision indisponible, liste vide). Les points qui ne s'appliquent pas à la tâche sont marqués « non concerné », jamais cochés d'office.

## Fonctionnalité

- [ ] Chaque bouton et lien a un comportement défini.
- [ ] Les formulaires gèrent les erreurs et les entrées invalides.
- [ ] Les états de chargement et les résultats vides sont traités lorsque nécessaire.
- [ ] Aucune fonctionnalité n'est annoncée comme opérationnelle sans l'être.
- [ ] Les données de démonstration sont clairement identifiées.

## Qualité du code

- [ ] Aucun code dupliqué inutilement.
- [ ] Aucune dépendance ajoutée sans justification.
- [ ] Aucune erreur connue dissimulée.
- [ ] Les modifications restent limitées au périmètre demandé.
- [ ] Les conventions existantes sont respectées.

## Qualité visuelle

- [ ] L'interface possède une hiérarchie visuelle claire.
- [ ] Aucun élément décoratif n'encombre inutilement l'interface.
- [ ] Les espacements, couleurs et typographies sont cohérents.
- [ ] Le rendu est vérifié lorsque possible.
- [ ] Les éléments interactifs sont identifiables et utilisables.

## Accessibilité et sécurité

- [ ] La navigation au clavier est vérifiée lorsque pertinente.
- [ ] Les éléments interactifs possèdent des libellés compréhensibles.
- [ ] Les entrées utilisateur sont validées selon leur usage.
- [ ] Aucune clé secrète ou donnée sensible n'est exposée.
- [ ] Les erreurs ne révèlent pas inutilement d'informations internes.

## Compte rendu obligatoire

À la fin de chaque tâche, l'agent doit indiquer :

1. Les fichiers modifiés.
2. Les fonctionnalités créées ou corrigées.
3. Les tests réellement exécutés et leurs résultats.
4. Les problèmes ou limitations restants.
5. Les éventuelles décisions nécessitant une validation humaine.

**Une case non vérifiée ne doit pas être considérée comme validée. Si un contrôle n'a pas pu être effectué, l'agent doit le signaler explicitement.**
