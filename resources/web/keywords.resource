*** Settings ***
Documentation     Web (yle.fi): ylätason keywordien toteutus Browser Libraryllä.
...               Laitekohtaiset erot tulevat device_specific/${FORM_FACTOR}/-kansiosta.
Library           Browser
Resource          setups_teardowns.resource
Resource          navigation.resource
Resource          device_specific/${FORM_FACTOR}/keywords.resource

*** Keywords ***
User Opens Login
    Go To Front Page
    Open Login Dialog

Login Form Should Be Shown
    Wait For Elements State    ${LOGIN_DIALOG}    visible
    Wait For Elements State    ${LOGIN_EMAIL_INPUT}    visible
    Wait For Elements State    ${LOGIN_PASSWORD_INPUT}    visible

User Should Not Be Logged In
    Go To Front Page
    Login Entry Should Be Visible

Login From UI
    [Documentation]    Kirjautuu Yle Tunnuksella. Tunnukset ympäristömuuttujista.
    [Arguments]    ${username}=%{YLE_USER}    ${password}=%{YLE_PASSWORD}
    Open Login Dialog
    Fill Text    ${LOGIN_EMAIL_INPUT}    ${username}
    Fill Secret    ${LOGIN_PASSWORD_INPUT}    $password
    Click    ${LOGIN_SUBMIT_BUTTON}

User Should Be Logged In
    Wait For Elements State    ${LOGGED_IN_INDICATOR}    visible    timeout=15s
