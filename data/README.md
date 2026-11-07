# Données

Un dossier par source, avec son `ATTRIBUTION.txt`. Les localités sont décrites
dans `localites.csv`.

| Dossier | Grandeurs | Mensuel | Journalier |
|---|---|---|---|
| `nasa-power/` | `ghi`, `t2m`, `rh2m`, `vent_2m`, `vent_10m`, `precipitation` | 1991-2025 | 1991-2025 |
| | `dni`, `dhi`, `albedo_surface` | 2001-2025 | 2001-2025 |
| `era5/` | `t2m`, `rh2m`, `vent_10m`, `precipitation` | 1991-2025 | 1991-2025 |
| `cams-radiation/` | `ghi`, `dni`, `dhi`, `ghi_ciel_clair`, `dni_ciel_clair`, `dhi_ciel_clair`, `irradiation_extraterrestre`, `fiabilite_satellite` | 2005-2025 | 2005-2025 |
| `cams-eac4/` | `pm2_5`, `pm10` | 2003-2025 | 2003-2025 |
| `pvgis-sarah3/` | `ghi`, `dni` | 2005-2023 | — |
| `pvgis-era5/` | `ghi`, `dni` | 2005-2023 | — |
| `gpm-imerg/` | `precipitation` | — | 1998-2025 |
| `chirps/` | `precipitation` | — | 1991-2025 |

Le journalier est découpé par décennie : 1991-2000, 2001-2010, 2011-2020,
2021-2025, bornées à la période de la source.

## Colonnes

| Colonne | Contenu | Unité |
|---|---|---|
| `localite` | code de la localité (`localites.csv`) | |
| `annee`, `mois` | période d'une ligne mensuelle | |
| `date` | jour d'une ligne journalière (AAAA-MM-JJ, jour UTC, qui est le jour civil local) | |
| `ghi` | irradiation globale horizontale | kWh/m²/jour |
| `dni` | irradiation normale directe | kWh/m²/jour |
| `dhi` | irradiation diffuse horizontale | kWh/m²/jour |
| `ghi_ciel_clair`, `dni_ciel_clair`, `dhi_ciel_clair` | les mêmes, sans nuage (modèle McClear) | kWh/m²/jour |
| `irradiation_extraterrestre` | irradiation sur plan horizontal au sommet de l'atmosphère | kWh/m²/jour |
| `fiabilite_satellite` | part des pas de 15 minutes couverts par des images satellite fiables | 0 à 1 |
| `albedo_surface` | albédo de surface | sans dimension |
| `t2m` | température de l'air à 2 m | °C |
| `rh2m` | humidité relative à 2 m | % |
| `vent_2m`, `vent_10m` | vitesse du vent à 2 m et à 10 m | m/s |
| `precipitation` | précipitation | mm/jour |
| `pm2_5`, `pm10` | particules de moins de 2,5 µm et de 10 µm | µg/m³ |

En mensuel, chaque valeur est la moyenne journalière du mois, dans la même unité
que le journalier.

Une **cellule vide** veut dire que la source ne sert pas de valeur : un jour
sans images satellite pour CAMS, ou une grandeur que la source ne sert pas
encore à cette date (DNI, DHI et albédo NASA avant 2001). Aucune valeur n'est
bouchée ni interpolée.

## `localites.csv`

| Colonne | Contenu |
|---|---|
| `code` | code de la localité |
| `nom` | nom |
| `niveau` | `region` ou `departement` |
| `region` | région de rattachement (vide pour les 3 départements des districts autonomes) |
| `district` | district de rattachement |
| `latitude`, `longitude` | point représentatif, en degrés (Wikidata) |
| `population_2021` | population au RGPH 2021 (INS Côte d'Ivoire) |

Les séries sont calculées au point de la localité, ou à la maille de la source
qui le contient. Seize régions ont les coordonnées de leur département chef-lieu
et portent donc les mêmes séries que lui.
