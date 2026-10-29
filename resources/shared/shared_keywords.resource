*** Settings ***
Documentation     Alustariippumattomat keywordit.

*** Keywords ***
Not Implemented For This Platform
    [Documentation]    Runko keywordeille, joita ei ole vielä toteutettu tälle alustalle tai laitteelle.
    Fail    Not implemented for ${OS} / ${DEVICE}
