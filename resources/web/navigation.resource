*** Settings ***
Documentation     Web: navigointi näkymästä toiseen (laitteesta riippumaton osa).
Library           Browser

*** Keywords ***
Go To Front Page
    Go To    ${WEB_BASE_URL}
