# TODO: dodać dokumentację klasy
#Standard library import
import configparser
import pathlib
import sys

# Third party imports
from prettytable import PrettyTable
import chromedriver_autoinstaller

# Local imports
import jira_reader


class MainController:

    def __init__(self, root_folder: pathlib.Path):
        self._root_folder = root_folder

    @staticmethod
    def load_program_metadata() -> []:
        """ Załadowanie informacji o programie

        Metoda ładuje z pliku __init__.py podstawowe inforamcje o programie

        :return: Informacje o programie w postaci listy: nazwa programu, wersja, autor, link do wiki
        :rtype: [name, version, author, wiki]
        """
        name = jira_reader.__program_name__
        version = jira_reader.__version__
        author = jira_reader.__author__
        wiki = jira_reader.__wiki__
        return [name, version, author, wiki]

    def setup(self):
        # TODO: koniecznie do pliku logu należy dodać to co się dzieje w tej funkcji
        # Instalacja sterownika do Chrome
        self._install_chrome_driver()
        # Załadowanie pliku konfiguracyjnego
        self._config_check_file_exist()

    @staticmethod
    def _install_chrome_driver():
        """ Instalacja webdrivera przeglądarki Chrome

        Metoda zawsze instaluje webdriver do wykrytej wersji przeglądarki Chrome. Webdriver potrzebny jest do obsługi
        Selenium.
        """
        chromedriver_autoinstaller.install()
        # TODO: jak już będzie obsłużony plik logu to dodać komunikat o zainstalowaniu sterownika Chrome
        # f"Zainstalowano sterownik przeglądarki Chrome w katalogu {chrome_driver_path}"

    def _config_check_file_exist(self):
        """ Sprawdzenie czy istnieje plik 'config.ini'

        Metoda sprawdza czy istnieje plik konfiguracyjny. Jeżeli nie istnieje, to zostaje utworzony. W pliku zostaje
        utworzona odpowiednia struktura ale plik nie jest uzupełniany danymi konfiguracyjnymi
        """
        config_file_path = self._config_get_path_to_ini_file()

        # Jak pliku nie ma to go zakładamy
        path_object = pathlib.Path(config_file_path)
        if not path_object.exists():
            self._config_create_ini_file(config_file_path)

    def _config_load_epics(self) -> list:
        config_file_path = self._config_get_path_to_ini_file()
        config = configparser.ConfigParser(allow_no_value=True)
        files = config.read(config_file_path)
        if len(files) == 0:
            raise FileNotFoundError(f"Nie znaleziono pliku konfiguracyjnego 'config.ini'")
        return list(config['epics'])

    def _config_get_path_to_ini_file(self) -> pathlib.Path:
        """ Pobranie ścieżki do pliku konfiguracyjnego programu

        :return: Ścieżka do pliku konfiguracyjnego
        :rtype:  pathlib.Path
        """
        config_file_name = 'config.ini'
        root_folder = self._root_folder
        return pathlib.Path.joinpath(root_folder, config_file_name)

    @staticmethod
    def _config_create_ini_file(config_path: pathlib.Path):
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

        # TODO: dodać info do pliku logu o założeniu pliku config.ini
        # TODO: wyświetlić jakieś info na ekranie (np. to na dole), że został utworzony pusty plik ini
        # print(f"Został utworzony plik 'config.ini' w katalogu głównym aplikacji. Należy uzupełnić plik na podstawie "
        #       f"instrukcji ze strony: "
        #       f"https://github.com/ZalewskiPiotr/jira_reader/wiki/0.-Funkcjonalno%C5%9B%C4%87-programu#konfiguracja")

    def show_epics_report(self):
        epic_list = self._config_load_epics()  # To już załadowanie konfiguracji epików
        # Metoda testowa. Do wyrzucenia po napisaniu metody pobierającej dane z Jiry
        table = PrettyTable()
        table.field_names = ["Nazwa", "Id", "Budżet", "Czas szacowany", "Czas zalogowany", "Czas pozostały",
                             "Bieżące użycie budżetu", "Szacunkowe wykorzystanie budżetu"]
        table.add_row(['nazwa', '1', 'bud', 'time szac', 'time zal', 'time poz', 'usage', 'estim usage'])
        return table.get_string()
