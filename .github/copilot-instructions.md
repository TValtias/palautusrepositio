# Projektiohje

Projekti on `uv`-projekti. Suorita ajettavat komennot muodossa `uv run ...`
hakemistossa `viikko3/login`. Python-version tulee olla vähintään 3.14:

```bash
cd viikko3/login
uv sync
```

Käynnistä sovellus komennolla:

```bash
uv run python src/index.py
```

Flask-sovellus kuuntelee porttia 5001 osoitteessa `http://localhost:5001`.
Sovelluksen on oltava käynnissä testien aikana. Suorita Robot Framework
-testit toisessa terminaalissa:

```bash
cd viikko3/login
uv run robot src/tests
```

Käyttäjätunnuksen ja salasanan rekisteröinti- ja kirjautumisvalidointi
tapahtuu tiedostossa `src/services/user_service.py`. Reitit tiedostossa
`src/app.py` kutsuvat palvelua ja näyttävät sen virheilmoitukset.

## Viikko 4: tdd-ostoskori

Ohjeet koskevat hakemistoa `viikko4/tdd-ostoskori`. Aja testit komennolla:

```bash
uv run pytest
```

Yksittäisen testin voi ajaa esimerkiksi:

```bash
uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

- Älä muuta `ostos.py`- tai `tuote.py`-tiedostoja.
- Älä muokkaa testejä, ellei sitä erikseen pyydetä.
- Toteuta aina ehdottomasti pienin muutos, jolla testit menevät läpi.
- Pidä tämä ohjetiedosto tiiviinä.
