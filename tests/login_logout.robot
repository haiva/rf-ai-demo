*** Settings ***
Documentation     Kirjautuminen Yle Tunnuksella. Samat testit kaikille laitteille:
...               laite valitaan ajossa muuttujalla DEVICE (chromium_desktop | pixel_7).
Variables         ${CURDIR}/../resources/shared/environments.py    ${EXEC_ENV}
Variables         ${CURDIR}/../resources/${OS}/UI_ids.py
Variables         ${CURDIR}/../resources/${OS}/devices/${DEVICE}.py
Resource          ${CURDIR}/../resources/${OS}/keywords.resource
Resource          ${CURDIR}/../resources/shared/shared_keywords.resource

Suite Setup       Open App
Suite Teardown    Close App

*** Test Cases ***
Login Dialog Opens From Header
    [Documentation]    Valmis esimerkki: kaikki lokaattorit on vahvistettu työpöydällä.
    [Tags]    web_test    smoke
    When User Opens Login
    Then Login Form Should Be Shown

Login To Yle
    [Documentation]    HARJOITUS: vahvista LOGGED_IN_INDICATOR ja LOGOUT_BUTTON (/tutki-web),
    ...    poista sitten wip-tagi.
    [Tags]    web_test    smoke    wip
    Given User Should Not Be Logged In
    When Login From UI
    Then User Should Be Logged In
    [Teardown]    Logout User Test Teardown
