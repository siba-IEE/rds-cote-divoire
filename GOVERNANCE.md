# Gouvernance

Kuma Science opère le référentiel et valide ce qui y entre.

## Confiance

Le niveau de confiance découle de la nature de la donnée, selon une règle fixe :

- **A** : mesure au sol validée ;
- **B** : satellite ou réanalyse ;
- **C** : estimation tirée de la littérature.

La version 1.0.0 est entièrement en B. Aucune valeur ne passe en A sans mesure
au sol. Une valeur calée sur une station s'ajoute à la valeur B, qui reste
publiée.

## Passeport

Chaque série publiée a une source, une méthode, une période, un niveau de
confiance et ses limites connues. On les trouve dans l'`ATTRIBUTION.txt` du
dossier, dans `CAVEATS.md` et dans la décision du moteur qui a gravé la série.

## Révisions

Le moteur n'écrase aucune valeur : une valeur révisée par sa source ouvre une
nouvelle version, l'ancienne reste dans le moteur. Le référentiel publie la
valeur courante. Une révision entre deux versions publiées est notée dans
`CHANGELOG.md`, et la somme de contrôle du fichier change dans `MANIFEST.csv`.

## Contributions tierces

Une donnée tierce suit le même chemin que la donnée interne : passeport,
contrôles, décision publiée. Elle garde son attribution.
