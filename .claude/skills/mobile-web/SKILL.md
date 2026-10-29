---
name: mobile-web
description: Mobiiliselaimen emulointi Browser Libraryllä (laiteprofiilit, kosketus, mobiiliasettelun erot) tämän repon rakenteessa. Käytä aina kun työ koskee mobiiliprofiilia, pixel_7-laitetta tai device_specific/phone-kansiota.
---
# Mobiiliselain Browser Libraryllä

## Mitä tämä on – ja mitä ei
Playwrightin laiteprofiili emuloi mobiiliselainta: näytön koko, pikselitiheys, user agent,
kosketus ja mobiilitila. Se testaa **mobiiliverkkosivua**, ei natiivisovellusta. Natiivit
elementit, käyttöoikeuskyselyt ja ilmoitukset vaativat Appiumin ja oikean laitteen tai emulaattorin (ei tässä repossa).

## Avaus
```robotframework
${device}=    Get Device    ${PLAYWRIGHT_DEVICE}
New Context    &{device}    locale=${LOCALE}
```
Laiteprofiilin nimi tulee tiedostosta `resources/web/devices/<DEVICE>.py`. Jos nimeä ei löydy,
listaa saatavilla olevat profiilit `Get Devices`-keywordilla ja valitse lähin.

## Kosketus
Käytä `Tap`-keywordia painikkeisiin ja linkkeihin, kun testataan mobiilia. `Click` toimii usein
myös, mutta `Tap` vastaa käyttäjän toimintaa (vaatii laiteprofiilin, jossa hasTouch).

## Mobiiliasettelun erot – minne ne kuuluvat
- Ero toteutetaan keywordina tiedostoon `resources/web/device_specific/phone/keywords.resource`.
- Samanniminen keyword tehdään myös `device_specific/desktop/keywords.resource`-tiedostoon.
- **Ei erillisiä mobiilitestejä** ja **ei `IF`-ehtoja** laitteen mukaan muualla.
- Vain mobiilissa esiintyvät lokaattorit `UI_ids.py`:hin `MOBILE_`-etuliitteellä
  (esim. `MOBILE_MENU_BUTTON`).

## Tyypilliset erot yle.fi:n kaltaisilla sivuilla
- Yläpalkin toiminnot (haku, kirjautuminen) valikon takana.
- Elementit, jotka ovat DOMissa mutta piilossa: tarkista `visible`-tila, älä pelkkää olemassaoloa.
- Pidempi vieritys: Browser vierittää elementit näkyviin automaattisesti ennen klikkausta.
