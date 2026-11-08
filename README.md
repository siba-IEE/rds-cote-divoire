# RDS Côte d'Ivoire

Référentiel de Données Solaires de la Côte d'Ivoire : rayonnement, météo et
particules pour 142 localités (31 régions, 111 départements), de 1991 à 2025
selon la source, en mensuel et en journalier. Licence CC BY 4.0.

| | |
|---|---|
| Valeurs publiées | 37,6 millions |
| Localités | 142 : les 31 régions et les 111 départements |
| Profondeur | 1991-2025 (rayonnement satellite : 2005-2025) |
| Sources | NASA POWER, ERA5, CAMS Radiation, CAMS EAC4, PVGIS (SARAH-3 et ERA5), GPM IMERG, CHIRPS |
| Confiance | B partout : satellite et réanalyse, aucune mesure au sol pour l'instant |
| DOI | [10.5281/zenodo.24051870](https://doi.org/10.5281/zenodo.24051870) |

Inventaire des fichiers, périodes et sommes de contrôle : [MANIFEST.csv](MANIFEST.csv),
vérifiable par `python examples/verifier_manifeste.py`.

## Les données

[`data/`](data/) contient un dossier par source. Le mensuel tient en un fichier
par source, et le journalier en un fichier par décennie. Une ligne correspond à
une localité et une période, avec une colonne par grandeur. Le dictionnaire des
colonnes et des unités est dans [`data/README.md`](data/README.md).

| Grandeur | Sources |
|---|---|
| GHI, DNI, DHI | NASA POWER, CAMS Radiation ; GHI et DNI aussi SARAH-3 et ERA5 (PVGIS) |
| Ciel clair, irradiation extraterrestre, fiabilité satellite | CAMS Radiation |
| Température, humidité, vent à 10 m | NASA POWER, ERA5 |
| Vent à 2 m, albédo | NASA POWER |
| Pluie | NASA POWER, ERA5, GPM IMERG, CHIRPS |
| Particules PM2.5, PM10 | CAMS EAC4 |

Lire [CAVEATS.md](CAVEATS.md) avant usage : plusieurs séries ont des limites
connues. Par exemple, la pluie journalière NASA est inutilisable pour les
épisodes, et les localités voisines partagent souvent la même maille.

## D'où viennent les valeurs

Les séries sont gravées par
[Kuma Data Core (Côte d'Ivoire)](https://github.com/siba-IEE/kuma-data-core-civ),
puis exportées telles quelles par `scripts/exporter_rds.py`. Seules les valeurs
courantes sont exportées : quand une source révise ses valeurs, l'ancienne
version reste dans le moteur. Chaque lot a une décision publiée, qui fixe la
requête, la conversion, les contrôles et les constats
([docs/decisions/](https://github.com/siba-IEE/kuma-data-core-civ/tree/main/docs/decisions)).

## Citer

> Kalivogui, S. (2026). Référentiel de Données Solaires de la Côte d'Ivoire (RDS Côte d'Ivoire). Kuma Science. https://doi.org/10.5281/zenodo.24051870

Ce DOI renvoie toujours à la dernière version. La 1.0.0 a aussi son propre
DOI : 10.5281/zenodo.24051871. Voir [CITATION.cff](CITATION.cff).

## Sources, limites, licence

- Sources, licences et attributions : [SOURCES.md](SOURCES.md), et un
  `ATTRIBUTION.txt` par dossier de `data/`.
- Limites connues : [CAVEATS.md](CAVEATS.md).
- Confiance, passeport et révisions : [GOVERNANCE.md](GOVERNANCE.md).
- Exemples sans dépendance : [examples/](examples/).
- Licence : CC BY 4.0 ([LICENSE](LICENSE)). Les sources tierces gardent leur
  propre attribution.
- Contribuer, signaler une erreur : [CONTRIBUTING.md](CONTRIBUTING.md), ou
  écrire à contact@kumascience.com.
