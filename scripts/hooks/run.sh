#!/usr/bin/env bash
# Käynnistää Python-hookin projektin venvillä. Toimii macOS:llä, Linuxilla ja Windowsin Git Bashissa.
# Käyttö (.claude/settings.json): bash scripts/hooks/run.sh <hookin nimi ilman .py-päätettä>
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
for PY in "$ROOT/.venv/bin/python" "$ROOT/.venv/Scripts/python.exe" python3 python; do
  if command -v "$PY" >/dev/null 2>&1 || [ -x "$PY" ]; then
    exec "$PY" "$ROOT/scripts/hooks/$1.py"
  fi
done
echo "Hook: Pythonia ei löytynyt" >&2
exit 0
