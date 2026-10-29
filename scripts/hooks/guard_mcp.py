#!/usr/bin/env python3
"""PreToolUse-hook RF-MCP-kutsuille (mcp__robotmcp__*).

Estää kaksi asiaa, jotka CLAUDE.md kieltää:
1. Salasanan selväkielinen arvo kutsussa. Salasana syötetään vain Fill Secret -keywordilla
   ympäristömuuttujaviittauksena %{YLE_PASSWORD}, jolloin arvo ei päädy askelhistoriaan.
2. Komentoja ajavat tai tiedostojärjestelmää käsittelevät kirjastot ja keywordit
   (Process, OperatingSystem). Ne antaisivat agentille pääsyn koneeseen RF-MCP:n kautta
   ohi Claude Coden oman lupamallin.

Tarkistus on tekstipohjainen paras arvaus, ei täydellinen hiekkalaatikko.
Exit code 2 estää kutsun ja näyttää stderr-viestin Claudelle.
"""
import json
import os
import re
import sys

data = json.load(sys.stdin)
payload = json.dumps(data.get("tool_input", {}), ensure_ascii=False)

secret = os.environ.get("YLE_PASSWORD", "")
if secret and secret in payload:
    print("ESTETTY: RF-MCP-kutsussa on salasanan selväkielinen arvo. Käytä "
          "Fill Secret -keywordia ja viittausta %{YLE_PASSWORD}.", file=sys.stderr)
    sys.exit(2)

blocked = re.compile(
    r'"(Process|OperatingSystem)"'                     # kirjasto arvona
    r'|\b(Run Process|Start Process|Run And Return Rc|Run And Return Rc And Output'
    r'|Remove Directory|Remove File|Move Directory|Copy Directory|Create Binary File'
    r'|Set Environment Variable|Get Environment Variables)\b',
    re.IGNORECASE)
m = blocked.search(payload)
if m:
    print(f"ESTETTY: RF-MCP-kutsu käyttää kiellettyä kirjastoa tai keywordia ({m.group(0)}). "
          "Tässä repossa RF-MCP:llä käytetään vain Browser Librarya (CLAUDE.md, RF-MCP).",
          file=sys.stderr)
    sys.exit(2)
sys.exit(0)
