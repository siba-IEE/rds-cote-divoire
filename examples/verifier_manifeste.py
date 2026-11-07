"""Vérifier les fichiers de data/ contre MANIFEST.csv.

Recalcule la somme SHA-256, le nombre de lignes et de localités de chaque
fichier listé, et signale les fichiers de données absents du manifeste.

    python examples/verifier_manifeste.py
"""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def empreinte(chemin: Path) -> tuple[str, int, int]:
    sha = hashlib.sha256(chemin.read_bytes()).hexdigest()
    with chemin.open(encoding="utf-8") as fichier:
        lignes = list(csv.DictReader(fichier))
    return sha, len(lignes), len({ligne["localite"] for ligne in lignes})


def main() -> None:
    with (RACINE / "MANIFEST.csv").open(encoding="utf-8") as fichier:
        manifeste = list(csv.DictReader(fichier))

    erreurs = []
    for entree in manifeste:
        chemin = RACINE / entree["chemin"]
        if not chemin.is_file():
            erreurs.append(f"absent : {entree['chemin']}")
            continue
        attendu = (entree["sha256"], int(entree["lignes"]), int(entree["localites"]))
        if empreinte(chemin) != attendu:
            erreurs.append(f"différent du manifeste : {entree['chemin']}")

    listes = {entree["chemin"] for entree in manifeste}
    for chemin in sorted((RACINE / "data").glob("*/*.csv")):
        if chemin.relative_to(RACINE).as_posix() not in listes:
            erreurs.append(f"hors manifeste : {chemin.relative_to(RACINE).as_posix()}")

    if erreurs:
        raise SystemExit("\n".join(erreurs))
    print(f"{len(manifeste)} fichiers conformes au manifeste.")


if __name__ == "__main__":
    main()
