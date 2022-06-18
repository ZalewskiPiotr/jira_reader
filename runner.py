""" Skrypt uruchamiający program 'Jira reader'

Ten skrypt uruchamia program.

Uruchomienie skryptu odbywa się poprzez wywołanie:
`python runner.py`

Skrypt zawiera funkcje:
-----------------------
- show_program_metadata()
    Wyświetlenie metadanych programu
- get_data_for_connection_to_jira() -> tuple[str, str, str]:
    Pobranie informacji o adresie url taska oraz danych do logowania do Jiry
- main()
    Sterowanie przepływem programu
"""
# Standard library imports
import getpass

# Third party imports

# Local imports
import jira_reader
from jira_reader import jira_reader as jr


def show_program_metadata():
    """ Wyświetlenie metadanych programu

    Funkcja wyświetla informacje o programie pobrane z pliku __init__.py pakietu jira_reader
    :return: ---
    :rtype: ---
    """
    print('-' * 30, f"Program: {jira_reader.__program_name__} ({jira_reader.__name__})", '-' * 30)
    print(f"Wersja: {jira_reader.__version__}")
    print(f"Autor: {jira_reader.__author__}")
    print(f"Wiki: {jira_reader.__wiki__}")
    print('-' * 96)


def get_data_for_connection_to_jira() -> tuple[str, str, str]:
    """ Pobranie informacji o adresie url taska oraz danych do logowania do Jiry

    Funkcja pobiera od użytkownika dane do logowania oraz adres taska, dla którego mają zostać wyświetlone informacje.

    :return: adres url taska z Jiry, nazwa użytkownika, hasło użytkownika
    :rtype: tuple[str, str, str]
    """
    url_for_task = input('Podaj adres taska: ')
    name_of_user = input('Podaj nazwę użytkownika: ')
    passwd = getpass.getpass(prompt='Podaj hasło: ', stream=None)
    return url_for_task, name_of_user, passwd


def main():
    """ Sterowanie przepływem programu

    Jest to główna funkcja, która steruje przepływem programu
    """
    show_program_metadata()
    task_url, username, password = get_data_for_connection_to_jira()
    jr.main(task_url, username, password)


if __name__ == '__main__':
    main()
