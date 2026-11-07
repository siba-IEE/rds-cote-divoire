"""Climatologie mensuelle du GHI d'une localité, d'après NASA POWER.

Moyenne 1991-2020 de chaque mois, puis moyenne annuelle.

    python examples/resume_site.py [code_localite]
    python examples/resume_site.py civ_dep_korhogo
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

DONNEES = Path(__file__).resolve().parent.parent / "data" / "nasa-power" / "mensuel_1991_2025.csv"
ANNEE_MIN, ANNEE_MAX = 1991, 2020  # fenêtre climatologique de référence
MOIS = ["jan", "fév", "mar", "avr", "mai", "juin", "juil", "août", "sep", "oct", "nov", "déc"]


def ghi_par_mois(localite: str) -> dict[int, list[float]]:
    valeurs: dict[int, list[float]] = defaultdict(list)
    with DONNEES.open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier):
            if not (ANNEE_MIN <= int(ligne["annee"]) <= ANNEE_MAX):
                continue
            if ligne["localite"] == localite and ligne["ghi"]:
                valeurs[int(ligne["mois"])].append(float(ligne["ghi"]))
    return valeurs


def main() -> None:
    parseur = argparse.ArgumentParser(description="Climatologie mensuelle du GHI d'une localité.")
    parseur.add_argument(
        "localite",
        nargs="?",
        default="civ_dep_abidjan",
        help="code de la localité (voir data/localites.csv)",
    )
    localite = parseur.parse_args().localite

    valeurs = ghi_par_mois(localite)
    if not valeurs:
        raise SystemExit(f"Aucune donnée pour '{localite}' (voir data/localites.csv).")

    print(f"GHI mensuel moyen (kWh/m²/jour), {localite}, NASA POWER 1991-2020\n")
    moyennes = [mean(valeurs[mois]) for mois in range(1, 13)]
    for nom, valeur in zip(MOIS, moyennes, strict=True):
        print(f"  {nom:<5} {valeur:5.2f}")
    print(f"\nMoyenne annuelle : {mean(moyennes):.2f} kWh/m²/jour")


if __name__ == "__main__":
    main()
