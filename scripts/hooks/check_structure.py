#!/usr/bin/env python3
"""PostToolUse-hook: valvoo repon rakennesääntöjä deterministisesti.

1. tests/**/*.robot: ei Browser-keywordejä, lokaattoreita eikä Sleep-kutsuja.
2. .resource-tiedostot: ei kovakoodattuja lokaattoreita (kuuluvat UI_ids.py:hin).
3. Ei laitekohtaisia IF-ehtoja device_specific/-kansion ulkopuolella.
4. Robocop-lint virhetasolla, jos robocop on asennettu.

Exit code 2 -> stderr näytetään Claudelle, joka korjaa ongelman heti.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")
if not path.endswith((".robot", ".resource")):
    sys.exit(0)
p = Path(path)
try:
    content = p.read_text(encoding="utf-8")
except OSError:
    sys.exit(0)

parts = p.as_posix().split("/")
problems = []
LOW_LEVEL = {
    "Click", "Tap", "Fill Text", "Fill Secret", "Type Text", "Wait For Elements State",
    "Get Element", "Get Element Count", "Get Text", "New Browser", "New Context", "New Page",
    "Go To", "Keyboard Key", "Get Device", "Sleep",
}
LOCATOR_RE = re.compile(r"(css=|xpath=|//\w+\[|\[data-testid|role=\w+\[|>>>|#[a-z][\w-]+\s)")
DEVICE_IF_RE = re.compile(r"^\s+(IF|ELSE IF)\s+.*(FORM_FACTOR|PLAYWRIGHT_DEVICE|DEVICE)", re.M)

for n, line in enumerate(content.splitlines(), 1):
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        continue
    if "tests" in parts and line.startswith((" ", "\t")):
        first = re.split(r"\s{2,}|\t", stripped)[0]
        if first in LOW_LEVEL:
            problems.append(f"{path}:{n}: matalan tason keyword '{first}' testitiedostossa "
                            "-> siirrä resources/web/:iin (sääntö 1)")
    if LOCATOR_RE.search(line):
        problems.append(f"{path}:{n}: lokaattori {'testissä' if 'tests' in parts else 'resource-tiedostossa'} "
                        "-> UI_ids.py (sääntö 4)")

if "device_specific" not in parts and "setups_teardowns.resource" not in parts[-1]:
    for m in DEVICE_IF_RE.finditer(content):
        line_no = content[:m.start()].count("\n") + 1
        problems.append(f"{path}:{line_no}: laitekohtainen IF-ehto -> device_specific/<FORM_FACTOR>/ (sääntö 3)")

root = Path(__file__).resolve().parents[2]
robocop = next((str(c) for c in (root / ".venv/bin/robocop", root / ".venv/Scripts/robocop.exe") if c.exists()),
               shutil.which("robocop"))
if robocop:
    r = subprocess.run([robocop, "check", "--threshold", "E", path], capture_output=True, text=True)
    if r.returncode != 0 and r.stdout.strip():
        problems.append("Robocop:\n" + r.stdout.strip())

if problems:
    print("RAKENNETARKISTUS EPÄONNISTUI:\n" + "\n".join(problems), file=sys.stderr)
    sys.exit(2)
sys.exit(0)
