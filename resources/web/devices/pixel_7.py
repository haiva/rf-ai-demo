"""Laiteprofiili: mobiiliselain, Playwrightin Pixel 7 -emulointi.

Get Device asettaa näytön koon, pikselitiheyden, user agentin, kosketuksen ja mobiilitilan.
Testaa mobiiliverkkosivua, ei natiivisovellusta.
"""
BROWSER = "chromium"
HEADLESS = False
PLAYWRIGHT_DEVICE = "Pixel 7"   # Playwrightin laiteprofiilin nimi
FORM_FACTOR = "phone"           # -> device_specific/phone/
LOCALE = "fi-FI"
