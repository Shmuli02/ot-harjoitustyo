# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/Shmuli02/ot-harjoitustyo/releases)

## Konfigurointi
Tallennukseen käytettävä tiedoston nimi on konfiguroitu .env-tiedostossa. 
```
DATABASE_FILENAME = database.sqlite
```

## Ohjelman käynnistäminen

Asenna riippuvuudet ennen sohjelman käynnistämistä
```
poetry install
```
Alkutoimenpiteet komennolla
```
poetry run invoke build
```
Graaffisen ohjelman voi käynnistää komennolla 
```
poetry run invoke start
```
Komentorivi ohjelman voi käynnistää komennolla
```
poetry run python3 src/index.py commandline
```
