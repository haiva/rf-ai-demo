---
description: Tutki yle.fi:n näkymä mobiiliprofiililla (Pixel 7) RF-MCP:llä ja vertaa työpöytään
argument-hint: <näkymä tai toiminto, esim. "kirjautuminen">
---
Tutki näkymää "$ARGUMENTS" sivustolla yle.fi robotmcp-työkaluilla mobiiliprofiililla.

1. Lue `resources/web/devices/pixel_7.py`, `resources/web/UI_ids.py` ja
   `resources/web/device_specific/phone/keywords.resource`.
2. Avaa näkyvä selain laiteprofiililla: `${device}=  Get Device  Pixel 7` ja
   `New Context  &{device}  locale=fi-FI`. Hyväksy evästeistä vain välttämättömät.
   Salasana tarvittaessa vain `Fill Secret`-keywordilla viittauksena `%{YLE_PASSWORD}`.
3. Kulje näkymä läpi askel kerrallaan. Käytä kosketukseen `Tap`-keywordia.
4. Vertaa työpöytään: mitkä lokaattorit toimivat sellaisenaan, mitkä elementit ovat piilossa
   (esim. valikon takana) ja mitä mobiilissa on lisäksi.
5. Palauta taulukko: VAKIO_NIMI | lokaattori | sama kuin työpöydällä? | vahvistettu | huomio.
   Uudet, vain mobiilissa esiintyvät vakiot `MOBILE_`-etuliitteellä.

ÄLÄ kirjoita tiedostoihin. Ehdota lopuksi, mitkä keywordit kuuluvat
`device_specific/phone/keywords.resource`-tiedostoon.
