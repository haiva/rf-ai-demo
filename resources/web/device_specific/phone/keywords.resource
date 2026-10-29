*** Settings ***
Documentation     Mobiili: laitekohtaiset keywordit. Samat nimet kuin device_specific/desktop/-kansiossa.
...               Harjoitus: toteutus on lähtöarvaus, joka vahvistetaan /tutki-mobiili-komennolla.
...               Jos kirjautuminen on mobiilissa valikon takana, avaa ensin MOBILE_MENU_BUTTON.
Library           Browser

*** Keywords ***
Login Entry Should Be Visible
    Wait For Elements State    ${LOGIN_ENTRY_BUTTON}    visible

Open Login Dialog
    [Documentation]    Avaa Yle Tunnus -dialogin kosketuksella.
    Tap    ${LOGIN_ENTRY_BUTTON}
    Wait For Elements State    ${LOGIN_EMAIL_INPUT}    visible
