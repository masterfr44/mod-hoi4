# 05 — Priorités nationales (arbres de focus)

## Structure

```
focus_tree = {
	id = iro_france_focus
	country = {
		factor = 0
		modifier = { add = 10 tag = FRA }
	}
	default = no

	focus = {
		id = FRA_reconstruction_du_nord
		icon = GFX_goal_FRA_reconstruction_du_nord
		x = 0
		y = 0
		cost = 10
		available = { }
		completion_reward = { }
		ai_will_do = { factor = 5 }
	}
}
```

`cost = 10` = 70 jours. Les priorités vanilla vont en général de 5 à 10 ; rarement plus.

## Règles de conception

1. **Un arbre raconte une histoire.** On commence par écrire en quelques lignes (dans la PR ou dans un fichier `docs/`) les branches de l'arbre : par exemple *Reconstruction*, *Armée*, *Politique (3 voies exclusives)*, *Diplomatie*, *Programme mécha*. Puis seulement on écrit le script.
2. **Branches politiques exclusives** avec `mutually_exclusive`, et des conditions d'accès (`available`) liées à l'état du pays (idéologie, stabilité, guerre en cours), pas seulement à la priorité précédente.
3. **Récompenses variées et adaptées.** Pas uniquement `add_political_power` et `add_research_slot`. Utiliser : esprits nationaux, bâtiments sur des états précis, bonus de recherche ciblés, décisions débloquées, personnages recrutés, revendications, événements.
4. **Coût en rapport avec l'effet.** Un emplacement de recherche ou une usine militaire gratuite coûte au moins 10. Pas plus de 2 à 3 emplacements de recherche dans tout l'arbre.
5. **Placement lisible.** Coordonnées `x`/`y` sans chevauchement, les prérequis vont du haut vers le bas, `relative_position_id` pour garder une branche groupée.
6. **Pas de copier-coller entre pays.** Deux pays peuvent partager une branche générique (via un arbre partagé ou `shared_focus`), mais les branches nationales sont propres à chaque pays.
7. **Chaque priorité a une icône et une description** (`<id>_desc` dans la localisation) qui dit le contexte, pas seulement l'effet.
8. **L'IA suit un chemin.** `ai_will_do` oriente l'IA vers la voie historique/uchronique du mod.

## Test

Console : `focus.autocomplete` puis compléter l'arbre, vérifier l'affichage (pas de lignes qui se croisent) et `error.log`.
