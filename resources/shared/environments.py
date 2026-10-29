"""Ympäristökohtaiset muuttujat. Käyttö robot-tiedostossa:
    Variables    ${CURDIR}/../resources/shared/environments.py    ${EXEC_ENV}
"""

ENVIRONMENTS = {
    "TEST": {"WEB_BASE_URL": "https://yle.fi"},
}


def get_variables(exec_env="TEST"):
    return dict(ENVIRONMENTS[exec_env.upper()])
