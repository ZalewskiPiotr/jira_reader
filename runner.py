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
import configparser

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
    """ Pobranie informacji o adresie url Jiry oraz danych do logowania do Jiry

    Funkcja pobiera od użytkownika dane do logowania oraz adres taska, dla którego mają zostać wyświetlone informacje.

    :return: adres url Jiry, nazwa użytkownika, hasło użytkownika
    :rtype: tuple[str, str, str]
    """
    url_for_task = input('Podaj adres Jiry: ')
    name_of_user = input('Podaj nazwę użytkownika: ')
    passwd = getpass.getpass(prompt='Podaj hasło: ', stream=None)
    return url_for_task, name_of_user, passwd


def get_configuration() -> list:
    config = configparser.ConfigParser(allow_no_value=True)
    files = config.read('config.ini')
    if len(files) == 0:
        raise FileNotFoundError(f"Nie znaleziono pliku konfiguracyjnego 'config.ini'")
    return list(config['epics'])


def main():
    """ Sterowanie przepływem programu

    Jest to główna funkcja, która steruje przepływem programu
    """
    show_program_metadata()
    epic_list = get_configuration()

    jira_url, username, password = get_data_for_connection_to_jira()
    # TODO: pobrać od usera albo jakoś inaczej zmienną 'login.jsp'. Dodam taką pozycję do pliku konfiguracyjnego. Na razie zostaje na stałe
    reader_jira = jr.JiraReader(jira_url, 'login.jsp', username, password)
    # reader.show_task_report_in_console(task_url, username, password)
    reader_jira.show_main_epic_data(epic_list)


if __name__ == '__main__':
    main()
