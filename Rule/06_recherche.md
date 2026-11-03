# 06 — Arbre de recherche logique et réaliste

Le mod commence en **1918** : l'arbre vanilla (qui part de 1936) est remplacé ou reconstruit à partir des technologies réellement disponibles à la fin de la Grande Guerre, avec une branche uchronique pour les mechas.

## Structure d'une technologie

```
technologies = {
	iro_char_lourd_1918 = {
		research_cost = 1.5
		start_year = 1918
		folder = {
			name = armour_folder
			position = { x = 2 y = @1918 }
		}
		path = {
			leads_to_tech = iro_char_lourd_1922
			research_cost_coeff = 1
		}
		categories = { armor }
		ai_will_do = { factor = 1 }
	}
}
```

Les positions `y` utilisent des variables d'année (`@1918`, `@1920`…) définies en haut du fichier, comme en vanilla, pour que les lignes de l'arbre correspondent aux années.

## Règles de réalisme

1. **Chaque technologie s'appuie sur un équipement ou une doctrine réels**, ou sur une extrapolation uchronique assumée et documentée. Exemple réel : Renault FT (1917), Mark V (1918), mitrailleuse Hotchkiss, avion Fokker D.VII, sous-marin type U-151.
2. **`start_year` cohérent** avec la date de mise en service réelle. Rechercher avant la date entraîne une pénalité « en avance » : c'est voulu.
3. **Progression plausible.** Pas de char moyen de 1936 disponible en 1920. Les sauts technologiques (moteur diesel fiable, radio embarquée, blindage soudé) sont des étapes de l'arbre, pas des bonus gratuits.
4. **Branche mécha (uchronie du mod).** Elle a ses propres prérequis industriels et technologiques (moteurs, métallurgie, électricité) et n'est pas plus rentable qu'une branche conventionnelle sans contrepartie (coût, carburant, fiabilité).
5. **Prérequis lisibles.** Une technologie a au plus 2 ou 3 prérequis ; pas de croisements de flèches inutiles dans l'interface.
6. **Statistiques comparées au vanilla.** Les valeurs d'équipement (attaque douce/dure, blindage, vitesse) sont calibrées en comparaison avec les équipements vanilla de même rôle. Indiquer dans la PR la référence utilisée.
7. **Doctrines d'époque.** Les doctrines de 1918 sont celles de la fin de la guerre : infiltration (Stoßtrupp), bataille conduite, guerre de position. Les doctrines de 1936+ arrivent plus tard dans l'arbre.
8. **Localisation complète** : nom de la technologie, `_desc` avec une phrase de contexte historique, nom de chaque équipement débloqué.

## Sources acceptées

Ouvrages d'histoire militaire, wiki officiel HOI4 pour la mécanique, fichiers vanilla pour les ordres de grandeur. Une IA ne cite pas de source qu'elle n'a pas réellement consultée.
