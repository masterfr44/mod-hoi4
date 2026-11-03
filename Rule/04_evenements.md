# 04 — Événements

## Structure minimale

```
add_namespace = fra_politique

country_event = {
	id = fra_politique.1
	title = fra_politique.1.t
	desc = fra_politique.1.d
	picture = GFX_report_event_fra_chambre

	is_triggered_only = yes

	option = {
		name = fra_politique.1.a
		ai_chance = { factor = 70 }
		# effets réels
	}
	option = {
		name = fra_politique.1.b
		ai_chance = { factor = 30 }
		# effets réels, différents de l'option a
	}
}
```

## Règles

1. **Un namespace par thème ou par pays** (`fra_politique`, `iro_mechas`), déclaré une seule fois en haut du fichier. Les ids se suivent sans trou (`.1`, `.2`, `.3`).
2. **Déclenchement explicite.** Chaque événement est soit `is_triggered_only = yes` et appelé ailleurs (priorité, autre événement, `on_action`, décision), soit déclenché par `trigger` + `mean_time_to_happen`. Noter en commentaire au-dessus de l'événement **d'où il est appelé**.
3. **Pas d'événement en boucle.** Un événement à `mean_time_to_happen` a un `fire_only_once = yes` ou une condition qui devient fausse après coup.
4. **Au moins deux options qui diffèrent vraiment**, sauf pour un événement purement informatif (une seule option « Compris »/« Intéressant », clairement assumée).
5. **Effets équilibrés.** Ordres de grandeur vanilla : un événement courant donne 25 à 100 de pouvoir politique, ±1 à 5 % de stabilité ou de soutien à la guerre. Au-delà, il faut une raison dans la PR.
6. **Infobulle claire.** Si un effet est caché (`hidden_effect`), l'option affiche un `custom_effect_tooltip` qui dit ce qui va se passer.
7. **Image adaptée.** Une image d'événement correspond au sujet. Pas de réutilisation d'une image vanilla de 1939 pour une scène de 1918 si elle est anachronique.
8. **Événements entre pays** : l'événement reçu par l'autre pays existe, a sa localisation, et ses options ont un effet en retour pour l'expéditeur (sinon le joueur ne sait pas que la réponse est arrivée).

## Test

Console : `event fra_politique.1 FRA`. Vérifier les infobulles de chaque option et `error.log`.
