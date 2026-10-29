---
description: Toteuta uusi ylätason testi molemmille laiteprofiileille repon rakennetta noudattaen
argument-hint: <testin kuvaus tai polku testitiedostoon>
---
Toteuta testi: $ARGUMENTS

Noudata CLAUDE.md:n sääntöjä ja tätä järjestystä:

1. **Suunnitelma** (älä kirjoita vielä): ylätason askeleet Given/When/Then-muodossa. Jokaiselle:
   onko keyword jo olemassa (grep `resources/`), laajennetaanko vai luodaanko uusi, ja mihin
   tiedostoon muutos menee (`keywords.resource` vai `device_specific/<desktop|phone>/`).
   Odota hyväksyntäni.
2. **Tutki**: työpöytä kuten /tutki-web, mobiili kuten /tutki-mobiili. Käytä tarvittaessa
   `lokaattori-tutkija`-subagenttia, jotta pääkonteksti pysyy siistinä.
3. **Kirjoita**: `UI_ids.py` → `device_specific/` tai `keywords.resource` → testi `tests/`-kansioon.
4. **Dryrun**: `bash scripts/aja.sh web --dryrun` ja `bash scripts/aja.sh mobile --dryrun`.
5. **Katselmoi**: käytä `rakenne-katselmoija`-subagenttia ja korjaa kriittiset löydökset.
6. **Kysy**: ajetaanko testit itse (anna komennot) vai ajanko ja analysoinko ne (/aja).
7. **Raportoi**: muuttuneet tiedostot, uudet ja uudelleenkäytetyt keywordit, avoimet TODOt.
