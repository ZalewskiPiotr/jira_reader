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
- create_ini_file(config_path: pathlib.Path)
    Utworzenie pliku konfiguracyjnego
- get_configuration() -> list:
    Pobranie konfiguracji programu z pliku 'ini'
- get_root_folder() -> pathlib.Path:
    Pobranie głównego katalogu programu
- get_config_path() -> pathlib.Path:
    Pobranie ścieżki do pliku konfiguracyjnego programu
- main()
    Sterowanie przepływem programu
"""
# Standard library imports
import getpass
import configparser
import pathlib
import sys

# Third party imports
import chromedriver_autoinstaller

# Local imports
import jira_reader
from jira_reader import jira_reader as jr
from jira_reader.controllers.main_controller import MainController
from jira_reader.views.main_view import MainView


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


def create_ini_file(config_path: pathlib.Path):
    """ Utworzenie pliku konfiguracyjnego

    :param config_path: Ścieżka do pliku
    :type config_path: pathlib.Path
    :return: ---
    :rtype: ---
    """
    config_parser = configparser.ConfigParser()
    config_parser.add_section('epics')
    with open(config_path, 'w') as config_file:
        config_parser.write(config_file)
    print(f"Został utworzony plik 'config.ini' w katalogu głównym aplikacji. Należy uzupełnić plik na podstawie "
          f"instrukcji ze strony: "
          f"https://github.com/ZalewskiPiotr/jira_reader/wiki/0.-Funkcjonalno%C5%9B%C4%87-programu#konfiguracja")


def get_configuration() -> list:
    """ Pobranie konfiguracji programu z pliku 'ini'

    :return: Lista epików
    :rtype: list
    """
    config_file_path = get_config_path()

    # Jak pliku nie ma to go zakładamy. Plik nie ma danych, więc wychodzimy z programu bo i tak nie będzie działał.
    path_object = pathlib.Path(config_file_path)
    if not path_object.exists():
        create_ini_file(config_file_path)
        sys.exit(0)

    config = configparser.ConfigParser(allow_no_value=True)
    files = config.read(config_file_path)
    if len(files) == 0:
        raise FileNotFoundError(f"Nie znaleziono pliku konfiguracyjnego 'config.ini'")
    return list(config['epics'])


def get_root_folder() -> pathlib.Path:
    """ Pobranie głównego katalogu programu

    Funkcja pobiera główny katalog programu. Katalog jest identyfikowany jako ten, w którym jest uruchamiany plik
    'runner.py'
    :return: Ścieżka do głównego katalogu programu
    :rtype: pathlib.Path
    """
    return pathlib.Path(__file__).resolve().parent


def get_config_path() -> pathlib.Path:
    """ Pobranie ścieżki do pliku konfiguracyjnego programu

    :return: Ścieżka do pliku konfiguracyjnego
    :rtype:  pathlib.Path
    """
    config_file_name = 'config.ini'
    root_folder = get_root_folder()
    return pathlib.Path.joinpath(root_folder, config_file_name)


def main():
    """ Sterowanie przepływem programu

    Jest to główna funkcja, która steruje przepływem programu
    """
    show_program_metadata()

    # Instalacja chrome driver
    chrome_driver_path = chromedriver_autoinstaller.install()
    if chrome_driver_path:
        print(f"Zainstalowano sterownik przeglądarki Chrome w katalogu {chrome_driver_path}")

    epic_list = get_configuration()

    jira_url, username, password = get_data_for_connection_to_jira()
    # TODO: pobrać od usera albo jakoś inaczej zmienną 'login.jsp'. Dodam taką pozycję do pliku konfiguracyjnego. Na razie zostaje na stałe
    reader_jira = jr.JiraReader(jira_url, 'login.jsp', username, password)
    # reader.show_task_report_in_console(task_url, username, password)
    reader_jira.show_main_epic_data(epic_list)


def main_2():
    main_view = MainView()
    controller = MainController()
    main_view.set_controller(controller)
    main_view.run()


if __name__ == '__main__':
    main_2()
    exit(0)
    main()
