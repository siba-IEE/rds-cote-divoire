# Contribuer

## Signaler une erreur

Ouvrir une issue « Signaler une erreur de donnée » avec le fichier, la
localité, la date et la valeur en cause. La valeur est comparée à celle que
sert la source :

- si l'export la déforme, le fichier est corrigé et la version suivante le
  note dans `CHANGELOG.md` ;
- si la source sert bien cette valeur, elle reste telle quelle et la limite
  est ajoutée à `CAVEATS.md`.

## Proposer une donnée

Ouvrir une issue « Proposer une donnée ». Une série n'entre qu'avec :

- une source citable ;
- la méthode de production ou de collecte (instrument, modèle, contrôles) ;
- la période couverte ;
- l'incertitude connue ;
- une licence qui permet de la redistribuer en CC BY 4.0.

Ce qui manque le plus : des mesures au sol en Côte d'Ivoire (pyranomètre,
station météo). Elles seules permettront la confiance A.

## Fichiers de `data/`

Ils sont produits par l'exporteur de
[Kuma Data Core CIV](https://github.com/siba-IEE/kuma-data-core-civ) et ne
sont pas édités à la main. Une donnée nouvelle ou corrigée entre d'abord dans
le moteur, avec sa décision publiée, puis dans un nouvel export.

La documentation et les exemples se corrigent par pull request directe.

## Licence

En contribuant, vous acceptez que votre apport soit publié sous CC BY 4.0, avec
attribution.
