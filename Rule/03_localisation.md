# 03 — Localisation et écriture

## Format technique

- Fichier : `localisation/french/iro_<sujet>_l_french.yml` (et `localisation/english/..._l_english.yml`). Le nom **doit** finir par `_l_<langue>.yml`.
- Encodage UTF-8 **avec BOM**.
- Première ligne : `l_french:` (ou `l_english:`).
- Chaque entrée : un espace d'indentation, la clé, `:0`, puis le texte entre guillemets :

```yaml
l_french:
 fra_politique.1.t:0 "La Chambre bleu horizon"
 fra_politique.1.d:0 "Les élections de novembre ont envoyé à la Chambre une majorité d'anciens combattants..."
```

- Saut de ligne dans un texte : `\n`. Guillemet dans un texte : `\"`.
- Couleurs et icônes : utiliser la syntaxe du jeu (`§Y...§!`, `£pol_power`), pas de Markdown.

## Toutes les langues, toutes les clés

- Chaque clé utilisée dans un script (`title`, `desc`, `name`, nom de priorité, `_desc` de priorité, nom de technologie…) **existe** dans la localisation.
- Le français est la langue de référence. L'anglais doit avoir les mêmes clés ; s'il n'est pas encore traduit, on copie le texte français plutôt que de laisser la clé vide (le jeu afficherait la clé brute).

## Style d'écriture — anti slop

Un bon texte d'événement HOI4 fait 3 à 8 phrases et ressemble à une dépêche, un rapport ou une chronique de l'époque.

**À faire**
- Citer des noms, lieux, dates, chiffres précis (« 1 400 000 morts », « le 11 novembre », « les mines de Lens »).
- Donner le point de vue de l'époque : vocabulaire de 1918, pas de concepts modernes.
- Rendre chaque option différente par son ton et ses conséquences.

**À bannir** (marqueurs typiques de texte généré)
- « Dans un monde en pleine mutation… », « Une nouvelle ère s'ouvre… », « Le destin de la nation est en jeu… »
- Les listes de trois adjectifs (« audacieux, visionnaire et déterminé »).
- « crucial », « pivot », « tapisserie », « témoignage de », « naviguer les défis », « paysage politique » à toutes les phrases.
- Les conclusions morales (« Seul l'avenir dira si ce choix était le bon. »).
- Les options du type « Nous devons agir ! » / « Attendons. » sans contenu.
- Les anachronismes : « soft power », « fake news », « géopolitique » au sens moderne, etc.

Si on ne sait pas quoi écrire de précis, c'est que l'événement n'a pas encore de raison d'être (voir `01_principes.md` §3).
