#!/usr/bin/env bash
# Ajaa testit laiteprofiililla. Windowsissa: Git Bash.
# Käyttö: bash scripts/aja.sh web|mobile [robotin lisäargumentit, esim. --dryrun tai --include smoke]
# Oletukset voi ohittaa ympäristömuuttujilla: DEVICE, EXEC_ENV
set -euo pipefail
cd "$(dirname "$0")/.."

PROFILE="${1:-web}"; shift || true
case "$PROFILE" in
  web)    DEVICE="${DEVICE:-chromium_desktop}" ;;
  mobile) DEVICE="${DEVICE:-pixel_7}" ;;
  *) echo "Tuntematon profiili: $PROFILE (web|mobile)"; exit 1 ;;
esac

# Projektin venv ensin, vaikka sitä ei olisi aktivoitu
if   [ -x .venv/bin/robot ];         then ROBOT=.venv/bin/robot
elif [ -x .venv/Scripts/robot.exe ]; then ROBOT=.venv/Scripts/robot.exe
else ROBOT=robot; echo "Huom: .venv puuttuu, käytetään PATHin robot-komentoa" >&2
fi

# Browser kirjoittaa playwright-log.txt:n tulos-kansioon, joten se luodaan aina
mkdir -p "results/$PROFILE"

"$ROBOT" \
  --variable "OS:web" \
  --variable "DEVICE:$DEVICE" \
  --variable "EXEC_ENV:${EXEC_ENV:-TEST}" \
  --include web_test \
  --exclude wip \
  --outputdir "results/$PROFILE" \
  "$@" tests/
