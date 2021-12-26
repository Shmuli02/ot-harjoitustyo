# Vuokranseuranta sovellus
Vuokranseuranta sovelluksen avulla käyttäjä voi pitää kirjaa vuokra asuntojen tuloista ja menoista. Käyttäjä näkee myös yhteemvedon kaikista menoista ja tuloista

## Dokumentaatio
- [Käyttöohje](projekti/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](projekti/dokumentaatio/testaus.md)
- [Arkkitehtuurikuvaus](projekti/dokumentaatio/arkkitehtuuri.md)
- [Vaatimusmäärittely](projekti/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](projekti/dokumentaatio/tyoaikakirjanito.md)

## Asennus

Siirry kansioon `projekti`

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
poetry run invoke start
```

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

Komenorivi käyttöliittymä
```
poetry run invoke commandline
```
(invokessa on ongelma tekstin syötteessä. Komennolla `poetry run python3 src/index.py commandline` saa ongelman korjattua)