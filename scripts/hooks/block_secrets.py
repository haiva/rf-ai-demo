#!/usr/bin/env python3
"""PreToolUse-hook: estää salasanojen kirjoittamisen tiedostoihin.

Salasanaa EI kirjoiteta tähän tiedostoon: hook lukee sen ympäristömuuttujasta YLE_PASSWORD
ja estää juuri sen arvon päätymisen mihinkään tiedostoon. Lisäksi estetään yleiset
'password = "literaali"' -muodot.

Exit code 2 estää työkalukutsun ja näyttää stderr-viestin Claudelle, joka korjaa toimintansa.
"""
import json
import os
import re
import sys

data = json.load(sys.stdin)
tool_input = data.get("tool_input", {})
path = tool_input.get("file_path", "")
texts = [tool_input.get("content", ""), tool_input.get("new_string", "")]
texts += [e.get("new_string", "") for e in tool_input.get("edits", [])]
text = "\n".join(t for t in texts if t)

if os.path.basename(path) == ".env":
    sys.exit(0)

secret = os.environ.get("YLE_PASSWORD", "")
hit = bool(secret) and secret in text
patterns = [
    r"(?i)password\s*[=:]\s*['\"][^'\"$%{<][^'\"]+['\"]",   # password = "literaali"
    r"(?i)\$\{\w*PASSWORD\w*\}\s{2,}[^\s$%#]",             # RF Variables-taulukon literaali
]
hit = hit or any(re.search(p, text) for p in patterns)
if hit:
    print("ESTETTY: tiedostoon ollaan kirjoittamassa salasanaa. Käytä "
          "%{YLE_PASSWORD}-ympäristömuuttujaa (CLAUDE.md, sääntö 6).", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
