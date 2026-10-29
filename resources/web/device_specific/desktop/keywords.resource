*** Settings ***
Documentation     Työpöytä: laitekohtaiset keywordit. Samat nimet kuin device_specific/phone/-kansiossa.
Library           Browser

*** Keywords ***
Login Entry Should Be Visible
    Wait For Elements State    ${LOGIN_ENTRY_BUTTON}    visible

Open Login Dialog
    [Documentation]    Avaa Yle Tunnus -dialogin yläpalkin Kirjaudu-painikkeesta.
    Click    ${LOGIN_ENTRY_BUTTON}
    Wait For Elements State    ${LOGIN_EMAIL_INPUT}    visible
