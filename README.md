# Vuokranseuranta sovellus
Vuokranseuranta sovelluksen avulla käyttäjä voi pitää kirjaa vuokra asuntojen tuloista ja menoista. Käyttäjä näkee myös yhteemvedon kaikista menoista ja tuloista

## Asennus
1. Riippuvuuksien asennus komennolla
```
poetry install
```
2. Alustustoiminpiteet komennolla
```
poetry run invoke build
```
3. Käynnistä sovellus komennolla
```
poetry run python3 src/index.py
```

(komennolla "poetry run invoke start" komentorivin syöte ei toimi kunnolla)

## Muita toimintoja

Testaus
```
poetry run invoke test
```

Testikattavuus
```
poetry run invoke coverage-report
```

Pylint
```
poetry run invoke lint
```