"""Classer des localités par GHI annuel moyen.

Moyenne CAMS Radiation 2005-2024, calculée au point de chaque localité. Sert à
hiérarchiser des sites avant une étude de faisabilité.

    python examples/comparer_sites.py [code_localite ...]
    python examples/comparer_sites.py civ_dep_korhogo civ_dep_man
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

DATA = Path(__file__).resolve().parent.parent / "data"
DONNEES = DATA / "cams-radiation" / "mensuel_2005_2025.csv"
ANNEE_MIN, ANNEE_MAX = 2005, 2024  # vingt années complètes
VILLES = [
    "civ_dep_abidjan",
    "civ_dep_yamoussoukro",
    "civ_dep_bouake",
    "civ_dep_daloa",
    "civ_dep_korhogo",
    "civ_dep_man",
    "civ_dep_odienne",
    "civ_dep_san_pedro",
]


def ghi_annuel_moyen(localites: set[str]) -> dict[str, float]:
    valeurs: dict[str, list[float]] = defaultdict(list)
    with DONNEES.open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier):
            if not (ANNEE_MIN <= int(ligne["annee"]) <= ANNEE_MAX):
                continue
            if ligne["localite"] in localites and ligne["ghi"]:
                valeurs[ligne["localite"]].append(float(ligne["ghi"]))
    return {localite: mean(serie) for localite, serie in valeurs.items()}


def main() -> None:
    parseur = argparse.ArgumentParser(description="Classement de localités par GHI annuel moyen.")
    parseur.add_argument(
        "localites",
        nargs="*",
        default=VILLES,
        help="codes de localités (défaut : huit villes)",
    )
    localites = parseur.parse_args().localites

    moyennes = ghi_annuel_moyen(set(localites))
    if not moyennes:
        raise SystemExit("Aucune donnée pour ces localités (voir data/localites.csv).")

    print(f"GHI annuel moyen (kWh/m²/jour), CAMS Radiation {ANNEE_MIN}-{ANNEE_MAX}\n")
    classement = sorted(moyennes.items(), key=lambda paire: paire[1], reverse=True)
    for rang, (localite, valeur) in enumerate(classement, 1):
        print(f"  {rang}. {localite:<24} {valeur:5.2f}")


if __name__ == "__main__":
    main()
