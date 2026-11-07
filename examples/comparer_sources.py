"""Comparer le GHI de quatre sources en une localité.

Moyenne 2005-2020 de NASA POWER, CAMS Radiation, PVGIS-SARAH3 et PVGIS-ERA5,
sur les mois que les quatre servent. Toutes sont en confiance B : l'écart
mesure leur désaccord, pas l'erreur de l'une d'elles.

    python examples/comparer_sources.py [code_localite]
    python examples/comparer_sources.py civ_dep_korhogo
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import mean

DATA = Path(__file__).resolve().parent.parent / "data"
SOURCES = {
    "NASA POWER": DATA / "nasa-power" / "mensuel_1991_2025.csv",
    "CAMS Radiation": DATA / "cams-radiation" / "mensuel_2005_2025.csv",
    "PVGIS-SARAH3": DATA / "pvgis-sarah3" / "mensuel_2005_2023.csv",
    "PVGIS-ERA5": DATA / "pvgis-era5" / "mensuel_2005_2023.csv",
}
# 2005 : début de CAMS et de PVGIS. 2020 : avant le saut d'ERA5 (voir CAVEATS.md).
ANNEE_MIN, ANNEE_MAX = 2005, 2020


def ghi_mensuel(chemin: Path, localite: str) -> dict[tuple[int, int], float]:
    serie: dict[tuple[int, int], float] = {}
    with chemin.open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier):
            annee = int(ligne["annee"])
            if ligne["localite"] == localite and ligne["ghi"] and ANNEE_MIN <= annee <= ANNEE_MAX:
                serie[annee, int(ligne["mois"])] = float(ligne["ghi"])
    return serie


def main() -> None:
    parseur = argparse.ArgumentParser(description="GHI moyen de quatre sources en une localité.")
    parseur.add_argument(
        "localite",
        nargs="?",
        default="civ_dep_abidjan",
        help="code de la localité (voir data/localites.csv)",
    )
    localite = parseur.parse_args().localite

    series = {nom: ghi_mensuel(chemin, localite) for nom, chemin in SOURCES.items()}
    mois = set.intersection(*(set(serie) for serie in series.values()))
    if not mois:
        raise SystemExit(f"Aucun mois commun pour '{localite}' (voir data/localites.csv).")

    periode = f"{ANNEE_MIN}-{ANNEE_MAX}"
    print(f"GHI moyen (kWh/m²/jour), {localite}, {len(mois)} mois communs ({periode})\n")
    moyennes = {nom: mean(serie[m] for m in mois) for nom, serie in series.items()}
    for nom, valeur in sorted(moyennes.items(), key=lambda paire: paire[1], reverse=True):
        print(f"  {nom:<15} {valeur:5.2f}")
    ecart = max(moyennes.values()) - min(moyennes.values())
    relatif = ecart / mean(moyennes.values())
    print(f"\nÉcart entre sources : {ecart:.2f} kWh/m²/jour ({relatif:.1%})")


if __name__ == "__main__":
    main()
