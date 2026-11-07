# Limites connues

À lire avant tout usage. Chaque limite vient d'un constat publié dans les
décisions du moteur
([docs/decisions/](https://github.com/siba-IEE/kuma-data-core-civ/tree/main/docs/decisions)),
dont le numéro est donné entre parenthèses.

## Confiance

Tout le référentiel est en confiance B : satellite et réanalyse, sans mesure au
sol. Aucune valeur n'est une mesure de terrain. Un écart entre deux sources
mesure leur désaccord, pas leur erreur. Une source n'est pas une vérité : NASA
POWER, ERA5 et CAMS sont des modèles différents.

## Mailles partagées

Les localités voisines tombent souvent dans la même maille d'une source, et y
portent la même série. Ces séries ne sont pas des mesures indépendantes
(ADR-0027).

| Source | Points distincts pour 142 localités |
|---|---:|
| NASA POWER, rayonnement et albédo (CERES, 1°) | 35 |
| CAMS EAC4 (0,75°) | 49 |
| NASA POWER, météo et pluie (MERRA-2, 0,5° × 0,625°) | 77 |
| ERA5 (0,25°) | 110 |
| GPM IMERG (0,1°) | 120 |
| CHIRPS (0,05°) | 121 |
| CAMS Radiation, PVGIS (au point) | 126 |

Seize régions ont les coordonnées de leur département chef-lieu : même au point,
elles portent les mêmes séries que lui. C'est ce qui ramène les 142 localités à
126 points.

## Rayonnement

- **DNI NASA POWER** : il est en dessous des trois autres sources dans les 142
  localités. Il ne sert pas de référence pour le direct (ADR-0012, ADR-0017).
- **DNI, DHI et albédo NASA avant 2001** : NASA POWER ne sert le DNI et
  l'albédo qu'à partir de 2001. Le DHI est servi dès 1991, mais il saute
  d'environ un tiers entre 2000 et 2001 : il n'est publié qu'à partir de 2001
  (ADR-0007, ADR-0013, ADR-0019).
- **ERA5 via PVGIS, 2021-2023** : le GHI fait un saut de +3,6 % et le DNI de
  +7,7 %, environ trois fois la variabilité d'une année sur l'autre. Le
  rayonnement ERA5 servi directement par Copernicus fait le même saut : c'est
  probablement la réanalyse ERA5 elle-même. Les valeurs ne sont pas corrigées
  (ADR-0018, ADR-0021).
- **PVGIS** (SARAH-3 et ERA5) s'arrête en 2023, dernière année servie.
- **CAMS, jours sans images Meteosat** : le tous ciels n'est pas servi le
  2005-01-11, le 2005-01-12, le 2006-01-10 et le 2006-01-11 partout, ni le
  2006-09-23 dans 54 localités. La cellule est vide. Le ciel clair et
  l'irradiation extraterrestre, qui ne dépendent pas des images, sont servis
  (ADR-0035, ADR-0039).
- **CAMS, révision de 2021-2025** : CAMS a révisé ces années après une première
  capture. Le référentiel publie les valeurs révisées. Le GHI y est plus élevé
  de 0,018 kWh/m²/jour en moyenne, et de 0,118 au plus (ADR-0037).
- **Fiabilité satellite** : elle qualifie le tous ciels CAMS d'un jour ou d'un
  mois, pas le ciel clair. Elle vaut environ 0,52 les jours sans images
  (ADR-0039).

## Pluie

- **Pluie journalière NASA POWER** : ne pas l'utiliser pour les extrêmes, les
  tendances ou les épisodes de pluie.
  - Elle sert des jours improbables : 726,74 mm à San-Pédro le 2022-09-16, et
    321,59 mm à Ouangolodougou le 2025-12-02, en saison sèche.
  - Elle rompt vers 2016-2017 : les jours au-delà de 50 mm sont près de 12 fois
    plus fréquents après, sans hausse du nombre de jours de pluie.
  - Son cumul mensuel reste utilisable avec prudence avant 2016 (ADR-0032).
- **CHIRPS journalier** : ce n'est pas une estimation jour par jour. CHIRPS
  répartit le cumul de chaque pentade (5 jours) entre ses jours selon ERA5, ce
  qui peut créer de faux épisodes pluvieux. Il faut l'utiliser en cumul de
  pentade ou de mois. En février 2000, cinq mailles ne redonnent pas le CHIRPS
  mensuel (ADR-0036).
- **GPM IMERG** : la pluie commence en 1998. Selon les notes de la version V07,
  l'étalonnage passe de TRMM à GPM en 2014, et l'habileté est moindre en zone
  côtière (ADR-0033).

## Météo

- **Vent ERA5 journalier** : il est recalculé depuis les composantes du vent.
  La moyenne des jours reste sous le vent mensuel ERA5, de 0,021 m/s en
  moyenne et de 0,110 au plus (ADR-0034).
- **Humidité ERA5** : ERA5 ne sert pas d'humidité relative. Elle est calculée
  heure par heure depuis la température et le point de rosée, puis moyennée.
  Elle est plus humide que NASA POWER de 1,52 point en moyenne, et de 5,03 de
  décembre à février (ADR-0038).

## Particules

CAMS EAC4 est une réanalyse sur une maille de 0,75°, environ 83 km. Les 142
localités n'y font que 49 points (ADR-0022).
