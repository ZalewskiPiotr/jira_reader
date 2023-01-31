# TODO: dodać dokumentację klasy
# Standard library import
import pathlib

# Third party imports
from prettytable import PrettyTable
import chromedriver_autoinstaller

# Local imports
import jira_reader
from jira_reader.controllers.config_file import ConfigFile


class MainController:

    def __init__(self, root_folder: pathlib.Path):
        self._root_folder = root_folder
        self._config_file = ConfigFile(root_folder)

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
        self._config_file.config_check_file_exist()

    @staticmethod
    def _install_chrome_driver():
        """ Instalacja webdrivera przeglądarki Chrome

        Metoda zawsze instaluje webdriver do wykrytej wersji przeglądarki Chrome. Webdriver potrzebny jest do obsługi
        Selenium.
        """
        chromedriver_autoinstaller.install()
        # TODO: jak już będzie obsłużony plik logu to dodać komunikat o zainstalowaniu sterownika Chrome
        # f"Zainstalowano sterownik przeglądarki Chrome w katalogu {chrome_driver_path}"

    def show_epics_report(self):
        epic_list = self._config_file.config_load_epics()  # To już załadowanie konfiguracji epików
        # Metoda testowa. Do wyrzucenia po napisaniu metody pobierającej dane z Jiry
        table = PrettyTable()
        table.field_names = ["Nazwa", "Id", "Budżet", "Czas szacowany", "Czas zalogowany", "Czas pozostały",
                             "Bieżące użycie budżetu", "Szacunkowe wykorzystanie budżetu"]
        table.add_row(['nazwa', '1', 'bud', 'time szac', 'time zal', 'time poz', 'usage', 'estim usage'])
        return table.get_string()
