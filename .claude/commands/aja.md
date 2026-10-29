---
description: Aja testit ja analysoi tulos
argument-hint: <web|mobile> [robot-lisäargumentit]
allowed-tools: Bash(bash scripts/aja.sh:*), Read, Grep
---
Aja `bash scripts/aja.sh $ARGUMENTS`.
Jos testejä epäonnistuu: lue `results/<web|mobile>/output.xml` (ei koko log.htmlää), tunnista
epäonnistunut keyword ja syy (lokaattori, ajoitus, laite-ero, data, ympäristö) ja ehdota korjaus
oikeaan tiedostoon CLAUDE.md:n rakenteen mukaan. Älä muuta testitiedostoa, jos vika on toteutuksessa.
