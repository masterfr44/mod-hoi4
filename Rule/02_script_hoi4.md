# 02 — Script HOI4 : syntaxe, encodage, nommage

## Arborescence

On suit **exactement** l'arborescence du jeu vanilla. Un fichier mal placé est ignoré sans message clair.

```
descriptor.mod
common/
  national_focus/      arbres de priorités
  technologies/        arbre de recherche
  characters/          dirigeants, généraux, conseillers
  ideas/               esprits nationaux
  country_tags/        déclaration des tags
  countries/           couleurs, graphismes par pays
  bookmarks/           scénario de départ 1918
  defines/             NDefines (date de départ, etc.)
events/                un fichier par pays ou par thème
history/
  countries/           situation de départ de chaque pays
  states/              propriétaires, bâtiments, population
  units/               ordres de bataille (OOB)
localisation/
  english/  french/    fichiers .yml
gfx/
  flags/  leaders/  interface/goals/  event_pictures/
interface/             fichiers .gfx qui déclarent les sprites
```

Pour remplacer entièrement un dossier vanilla (par exemple tous les pays de 1936), utiliser `replace_path` dans `descriptor.mod` plutôt que de laisser des fichiers vides.

## Encodage

| Fichiers | Encodage |
|---|---|
| Scripts `.txt`, `.gfx`, `.gui` | UTF-8 **sans** BOM |
| Localisation `.yml` | UTF-8 **avec** BOM (obligatoire, sinon le texte ne s'affiche pas) |

Fins de ligne : indifférent pour le jeu, mais on garde le même style dans tout le dépôt (LF).

## Syntaxe

- Une accolade ouverte = une accolade fermée. Indentation par **tabulation**, une tabulation par niveau.
- Pas de guillemets « intelligents » (`“ ”`) dans les scripts : seulement `"`.
- Commentaires avec `#`. Un commentaire explique le **pourquoi** (« rééquilibre la France pour éviter l'effondrement de 1919 »), pas le quoi.
- Toujours vérifier qu'un bloc est dans le **bon scope** (pays, état, personnage). Un `add_building_construction` dans un scope pays ne fait rien.

## Nommage

- Tags de pays : 3 lettres majuscules. Pour un pays nouveau, vérifier que le tag n'existe pas déjà en vanilla (`common/country_tags/00_countries.txt`).
- Tout identifiant créé par le mod commence par le **tag du pays** ou par le préfixe du mod `iro_` pour ce qui est commun :
  - priorité : `FRA_reconstruction_du_nord`
  - événement : namespace `fra_politique`, id `fra_politique.1`
  - idée : `FRA_idea_saignee_de_verdun`
  - technologie : `iro_char_lourd_1918`
  - sprite : `GFX_goal_FRA_reconstruction_du_nord`
- Identifiants en minuscules (sauf le tag), mots séparés par `_`, sans accents ni espaces.
- Un nom décrit le contenu. Interdit : `FRA_focus_1`, `event_new`, `test2`.

## Réutiliser plutôt que dupliquer

- Un bloc d'effets utilisé plusieurs fois devient un `scripted_effect` (`common/scripted_effects/`).
- Une condition répétée devient un `scripted_trigger`.
- Les valeurs à régler (coûts, bonus) qui reviennent souvent peuvent être des variables `@nom = valeur` en haut du fichier.

## IA (`ai_will_do`, `ai_chance`)

Chaque priorité et chaque option d'événement a un poids pour l'IA, **justifié** : l'IA doit suivre le chemin historique ou uchronique voulu, sauf choix aléatoire délibéré. Pas de `ai_chance = { factor = 1 }` partout par défaut.
