"""Laiteprofiili: työpöytäselain ilman näkyvää ikkunaa (CI)."""
BROWSER = "chromium"
HEADLESS = True
PLAYWRIGHT_DEVICE = ""    # tyhjä = ei laite-emulointia, käytetään viewportia
FORM_FACTOR = "desktop"   # -> device_specific/desktop/
VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080
LOCALE = "fi-FI"
