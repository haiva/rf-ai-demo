"""Lokaattorit: yle.fi, Browser Library. Kaikki lokaattorit vain tähän tiedostoon.

- Vahvistetut lokaattorit on kokeiltu RF-MCP:llä oikeaa sivua vasten.
- 'TODO' vahvistetaan harjoituksissa (/tutki-web, /tutki-mobiili).
- Vain mobiilissa esiintyvät lokaattorit MOBILE_-etuliitteellä.
- Yle Tunnus -lomake on tunnus.yle.fi-iframessa: Browser läpäisee iframen '>>>'-erottimella.
"""

# --- Evästeet (vahvistettu) ---
COOKIE_CONSENT_REJECT_BUTTON = '#yle-consent-sdk-container >> role=button[name="Vain välttämättömät"]'

# --- Kirjautuminen, Yle Tunnus (vahvistettu työpöydällä) ---
LOGIN_ENTRY_BUTTON = '[data-testid="header-login-button"]'
LOGIN_DIALOG = '[data-testid="tunnus-sdk-dialog"]'
LOGIN_EMAIL_INPUT = '#tunnus-sdk__content >>> #emailAddress'
LOGIN_PASSWORD_INPUT = '#tunnus-sdk__content >>> [data-testid="password-input"]'
LOGIN_SUBMIT_BUTTON = '#tunnus-sdk__content >>> role=button[name="Kirjaudu sisään"]'

# --- Kirjautunut tila (harjoitus: vahvista /tutki-web) ---
LOGGED_IN_INDICATOR = "TODO"   # elementti, joka näkyy vain kirjautuneena
LOGOUT_BUTTON = "TODO"         # voi vaatia käyttäjävalikon avaamisen

# --- Mobiili (harjoitus: vahvista /tutki-mobiili) ---
MOBILE_MENU_BUTTON = "TODO"    # jos kirjautuminen tai haku on mobiilissa valikon takana
