# TODO: dodać dokumentację klasy
# Standard library import
import configparser
import pathlib


class ConfigFile:

    def __init__(self, root_folder: pathlib.Path):
        self._root_folder = root_folder

    def config_check_file_exist(self):
        """ Sprawdzenie czy istnieje plik 'config.ini'

        Metoda sprawdza czy istnieje plik konfiguracyjny. Jeżeli nie istnieje, to zostaje utworzony. W pliku zostaje
        utworzona odpowiednia struktura ale plik nie jest uzupełniany danymi konfiguracyjnymi
        """
        config_file_path = self._config_get_path_to_ini_file()

        # Jak pliku nie ma to go zakładamy
        path_object = pathlib.Path(config_file_path)
        if not path_object.exists():
            self._config_create_ini_file(config_file_path)

    def config_load_epics(self) -> list:
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
        return pathlib.Path.joinpath(self._root_folder, config_file_name)

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
