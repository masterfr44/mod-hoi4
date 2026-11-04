# 08 — Graphismes : personnages, unités, pays

## Formats (à vérifier contre un fichier vanilla équivalent avant d'en créer un)

| Élément | Dossier | Format |
|---|---|---|
| Portrait de dirigeant / général | `gfx/leaders/<TAG>/` | `.dds` ou `.png`, 156×210 |
| Petit portrait (conseiller) | `gfx/interface/ideas/` ou `gfx/leaders/<TAG>/small/` | 65×67 |
| Drapeau grand / moyen / petit | `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/` | `.tga` 32 bits, 82×52 / 41×26 / 10×7 |
| Icône de priorité | `gfx/interface/goals/` | `.dds` ou `.png`, mêmes dimensions que les icônes vanilla |
| Image d'événement | `gfx/event_pictures/` | mêmes dimensions que les images vanilla du même type |

Un drapeau existe **par idéologie** si le pays peut changer de régime (`FRA.tga`, `FRA_fascism.tga`, `FRA_communism.tga`…).

Chaque image est déclarée dans un fichier `interface/*.gfx` (`spriteType = { name = GFX_... texturefile = "..." }`). Nom du sprite = convention de `02_script_hoi4.md`.

## Règles anti slop pour les visuels

1. **Originalité.** Pas d'images extraites d'*Iron Order 1919*, d'un autre jeu ou d'un autre mod. Photos d'archives : seulement si elles sont dans le domaine public, avec la source notée dans `gfx/CREDITS.md`.
2. **Images générées par IA : autorisées seulement si elles sont retravaillées et relues**, et signalées dans `gfx/CREDITS.md`. On rejette les défauts typiques : mains déformées, uniformes ou insignes inventés et incohérents, texte illisible, armes impossibles, visages lisses « plastique ».
3. **Exactitude d'époque.** Uniformes, casques (Adrian, Stahlhelm, Brodie…), décorations et grades conformes au pays et à 1918, sauf design uchronique assumé.
4. **Style uniforme.** Tous les portraits suivent le même style (cadrage, éclairage, traitement de couleur) pour ne pas mélanger photo, peinture et dessin. Le style choisi est décrit dans `docs/` avant de produire en série.
5. **Mechas et unités uchroniques.** Un design se justifie par la technologie du mod (moteur, blindage, armement d'époque). Pas de technologie futuriste (lasers, écrans holographiques) dans un univers dieselpunk 1918.
6. **Drapeaux et emblèmes.** Les drapeaux réels sont exacts pour 1918. Les drapeaux inventés suivent les codes héraldiques et vexillologiques de l'époque.
7. **Lisibilité en jeu.** Vérifier l'image à sa taille réelle dans l'interface : une icône de priorité doit rester compréhensible à 94 pixels de large.
