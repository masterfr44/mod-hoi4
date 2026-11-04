#!/usr/bin/env python3
"""Vérifications mécaniques du mod (voir Rule/README.md).

Usage : python3 Rule/outils/verifier_mod.py [racine_du_mod]

Code de sortie 1 s'il y a au moins une ERREUR. Les AVERTISSEMENTS ne bloquent pas
mais doivent être lus. Ce script ne remplace pas un test en jeu.
"""
import re
import sys
from pathlib import Path

BOM = b"\xef\xbb\xbf"
DOSSIERS_IGNORES = {".git", "Rule", "docs"}
EXT_SCRIPT = {".txt", ".gfx", ".gui", ".mod"}

REMPLISSAGE = re.compile(r"\b(TODO|FIXME|XXX|PLACEHOLDER|lorem ipsum|TBD)\b", re.IGNORECASE)
# Formules typiques de texte généré (voir 03_localisation.md). Avertissement seulement.
FORMULES_SLOP = [
    "dans un monde en pleine mutation", "une nouvelle ère", "le destin de la nation",
    "seul l'avenir dira", "tapisserie", "témoignage de", "naviguer les défis",
    "a new era", "testament to", "tapestry", "only time will tell", "navigate the challenges",
]
# Clés de localisation référencées par un script : title = xxx, desc = xxx, name = xxx
REF_LOC = re.compile(r"^\s*(?:title|desc|name)\s*=\s*([A-Za-z0-9_.]+)\s*$")
ID_FOCUS = re.compile(r"^\s*id\s*=\s*([A-Za-z0-9_]+)")
ENTREE_LOC = re.compile(r'^ ([A-Za-z0-9_.\-]+):\d*\s+"(.*)"\s*$')


class Rapport:
    def __init__(self):
        self.erreurs, self.avertissements = [], []

    def err(self, f, ligne, msg):
        self.erreurs.append(f"{f}:{ligne}: {msg}")

    def avert(self, f, ligne, msg):
        self.avertissements.append(f"{f}:{ligne}: {msg}")


def fichiers(racine):
    for p in sorted(racine.rglob("*")):
        if p.is_file() and not DOSSIERS_IGNORES.intersection(p.relative_to(racine).parts):
            yield p


def sans_commentaire(ligne):
    """Retire un commentaire # qui n'est pas dans une chaîne."""
    dans_chaine = False
    for i, c in enumerate(ligne):
        if c == '"':
            dans_chaine = not dans_chaine
        elif c == "#" and not dans_chaine:
            return ligne[:i]
    return ligne


def verifier_script(p, rel, r, refs):
    brut = p.read_bytes()
    if brut.startswith(BOM):
        r.err(rel, 1, "fichier de script encodé avec BOM (doit être UTF-8 sans BOM)")
    try:
        texte = brut.decode("utf-8-sig")
    except UnicodeDecodeError:
        r.err(rel, 1, "fichier non UTF-8")
        return
    profondeur = 0
    dans_focus = False
    for n, ligne in enumerate(texte.splitlines(), 1):
        code = sans_commentaire(ligne)
        if "“" in code or "”" in code:
            r.err(rel, n, "guillemets typographiques “ ” dans le script (utiliser \")")
        if REMPLISSAGE.search(ligne):
            r.err(rel, n, f"texte de remplissage : {ligne.strip()}")
        m = REF_LOC.match(code)
        if m and ("." in m.group(1) or p.parent.name == "national_focus"):
            refs.append((rel, n, m.group(1)))
        if re.match(r"^\s*focus\s*=\s*\{", code):
            dans_focus = True
        elif dans_focus:
            m = ID_FOCUS.match(code)
            if m:
                refs.append((rel, n, m.group(1)))
                refs.append((rel, n, m.group(1) + "_desc"))
                dans_focus = False
        for c in re.sub(r'"[^"]*"', "", code):
            if c == "{":
                profondeur += 1
            elif c == "}":
                profondeur -= 1
                if profondeur < 0:
                    r.err(rel, n, "accolade fermante en trop")
                    profondeur = 0
    if profondeur > 0:
        r.err(rel, "fin", f"{profondeur} accolade(s) non fermée(s)")


def verifier_loc(p, rel, r, cles):
    m = re.search(r"_l_([a-z_]+)\.yml$", p.name)
    if not m:
        r.err(rel, 1, "nom de fichier de localisation invalide (doit finir par _l_<langue>.yml)")
        return
    langue = m.group(1)
    brut = p.read_bytes()
    if not brut.startswith(BOM):
        r.err(rel, 1, "localisation sans BOM (UTF-8 avec BOM obligatoire)")
    try:
        lignes = brut.decode("utf-8-sig").splitlines()
    except UnicodeDecodeError:
        r.err(rel, 1, "fichier non UTF-8")
        return
    if not lignes or lignes[0].strip() != f"l_{langue}:":
        r.err(rel, 1, f"la première ligne doit être 'l_{langue}:'")
    for n, ligne in enumerate(lignes[1:], 2):
        if not ligne.strip() or ligne.lstrip().startswith("#"):
            continue
        e = ENTREE_LOC.match(ligne)
        if not e:
            r.err(rel, n, "entrée mal formée (attendu : ' cle:0 \"texte\"')")
            continue
        cle, texte = e.groups()
        cles.setdefault(langue, {})[cle] = (rel, n)
        if not texte.strip():
            r.err(rel, n, f"texte vide pour '{cle}'")
        if REMPLISSAGE.search(texte):
            r.err(rel, n, f"texte de remplissage dans '{cle}'")
        bas = texte.lower()
        for f in FORMULES_SLOP:
            if f in bas:
                r.avert(rel, n, f"formule générique « {f} » dans '{cle}' (voir 03_localisation.md)")


def main():
    racine = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2])
    r = Rapport()
    refs, cles = [], {}
    nb = 0
    for p in fichiers(racine):
        rel = p.relative_to(racine).as_posix()
        if p.suffix in EXT_SCRIPT:
            verifier_script(p, rel, r, refs)
            nb += 1
        elif p.suffix == ".yml" and "localisation" in p.parts:
            verifier_loc(p, rel, r, cles)
            nb += 1

    toutes = set().union(*[set(d) for d in cles.values()]) if cles else set()
    for rel, n, cle in refs:
        if cle not in toutes:
            r.err(rel, n, f"clé de localisation absente : {cle}")
    for langue in ("french", "english"):
        absentes = toutes - set(cles.get(langue, {}))
        for cle in sorted(absentes):
            r.err(f"localisation/{langue}", "-", f"clé '{cle}' absente en {langue}")

    for a in r.avertissements:
        print("AVERTISSEMENT", a)
    for e in r.erreurs:
        print("ERREUR", e)
    print(f"\n{nb} fichier(s) vérifié(s) : {len(r.erreurs)} erreur(s), "
          f"{len(r.avertissements)} avertissement(s).")
    if nb == 0:
        print("Aucun fichier de mod trouvé : rien n'a été vérifié.")
    return 1 if r.erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
