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
