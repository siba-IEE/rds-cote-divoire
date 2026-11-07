# Exemples

Scripts courts qui lisent les CSV de `data/`. Python 3 et sa bibliothèque
standard suffisent. Les lancer depuis la racine du dépôt.

| Script | Ce qu'il calcule |
|---|---|
| `resume_site.py` | climatologie mensuelle du GHI d'une localité (NASA POWER, 1991-2020) |
| `comparer_sites.py` | classement de localités par GHI annuel moyen (CAMS Radiation, 2005-2024) |
| `comparer_sources.py` | GHI moyen d'une localité selon quatre sources, sur les mêmes mois |
| `verifier_manifeste.py` | contrôle des fichiers de `data/` contre `MANIFEST.csv` |

Les trois premiers prennent des codes de localité en argument (voir
`data/localites.csv`). Sans argument : Abidjan, ou huit villes pour
`comparer_sites.py`.

```
$ python examples/comparer_sites.py
GHI annuel moyen (kWh/m²/jour), CAMS Radiation 2005-2024

  1. civ_dep_odienne           5.86
  2. civ_dep_korhogo           5.75
  3. civ_dep_man               5.52
  4. civ_dep_bouake            5.30
  5. civ_dep_yamoussoukro      5.26
  6. civ_dep_daloa             5.24
  7. civ_dep_san_pedro         4.92
  8. civ_dep_abidjan           4.62
```

```
$ python examples/comparer_sources.py civ_dep_korhogo
GHI moyen (kWh/m²/jour), civ_dep_korhogo, 192 mois communs (2005-2020)

  PVGIS-SARAH3     5.88
  CAMS Radiation   5.74
  PVGIS-ERA5       5.55
  NASA POWER       5.29

Écart entre sources : 0.59 kWh/m²/jour (10.5%)
```

Avec pandas, la climatologie d'une localité tient en une ligne :

```python
import pandas as pd
df = pd.read_csv("data/nasa-power/mensuel_1991_2025.csv")
df[(df.localite == "civ_dep_abidjan") & df.annee.between(1991, 2020)].groupby("mois")["ghi"].mean()
```
