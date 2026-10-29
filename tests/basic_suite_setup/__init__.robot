*** Settings ***
Variables         ${CURDIR}/../../resources/shared/environments.py    ${EXEC_ENV}
Variables         ${CURDIR}/../../resources/${OS}/UI_ids.py
Variables         ${CURDIR}/../../resources/${OS}/devices/${DEVICE}.py
Resource          ${CURDIR}/../../resources/${OS}/keywords.resource
Resource          ${CURDIR}/../../resources/shared/shared_keywords.resource
Documentation     Perusjoukko: sovellus avataan kerran koko kansion suiteille.
Suite Setup       Open App
Suite Teardown    Close App
