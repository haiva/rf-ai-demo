"""Laiteprofiili: työpöytäselain (Chromium, 1920x1080)."""
BROWSER = "chromium"
HEADLESS = False          # näkyvä selain; CI:ssä chromium_desktop_headless
PLAYWRIGHT_DEVICE = ""    # tyhjä = ei laite-emulointia, käytetään viewportia
FORM_FACTOR = "desktop"   # -> device_specific/desktop/
VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080
LOCALE = "fi-FI"
