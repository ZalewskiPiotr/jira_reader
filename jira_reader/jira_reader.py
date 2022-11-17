# Standard library imports
import traceback

# Third party imports
from prettytable import PrettyTable

# Local imports
from jira_reader import jira


class JiraReader:
    """
    Klasa odpowiada za logikę przepływu, który umożliwi zbudowanie raportu.

    Klasa jest modułem sterującym przepływem programu. Klasa sama nie pobiera danych z Jiry, ani nie wyświetla raportu.
    Dane z Jiry są pobierane poprzez moduł jira_reader.jira
    Raport na konsoli jest wyświetlany poprzez moduł jira_reader.console_view

    Atrybuty:
    ---------

    Metody:
    -------
    - __init__(self, login_url: str, username: str, password: str):
        Inicjalizacja klasy
    - show_task_report_in_console(self, task_url: str, username: str, password: str):
        Sterowanie procesem zbudowania raportu dla jednego taska z Jiry
    - show_main_epic_data(self, epic_key_list: list):
        Pobranie i wyświetlenie podstawowych informacji o epikach
    - print_table(data_to_show: list):
        Wyświetlenie raportu na ekranie
    - calculate_budget_usage(budget: float, logged_time: float) -> float:
        Wyliczenie użycia budżetu
    - convert_number_to_string_with_percent
        Dodanie znaku procentu do liczby
    """

    def __init__(self, jira_url: str, login_page: str, username: str, password: str):
        """ Inicjalizacja klasy

        Metoda w czasie inicjalizacji klasy zapamiętuje podane parametry logowania do Jiry

        :param jira_url: Adres url do Jiry
        :type jira_url: str
        :param login_page: Nazwa strony logowania do Jiry np. login.jsp
        :type login_page: str
        :param username: Nazwa użytkownika Jiry
        :type username: str
        :param password: Hasło użytkownika Jiry
        :type password: str
        """

        if len(jira_url.strip()) == 0:
            raise ValueError(f"Nieprawidłowy parametr jira_url: {jira_url}")
        if len(login_page.strip()) == 0:
            raise ValueError(f"Nieprawidłowy parametr login_page: {login_page}")
        if len(username.strip()) == 0:
            raise ValueError(f"Nieprawidłowy parametr username: {username}")
        if len(password.strip()) == 0:
            raise ValueError(f"Nieprawidłowy parametr password: {password}")

        self._jira_url = jira_url
        self._login_page = login_page
        self._username = username
        self._password = password
        self._login_url = f"{jira_url}/{login_page}"  # adres url dostrony logowania do Jiry

    # TODO: metoda nie jest wykorzystywana - chyba do usunięcia
    @staticmethod
    def show_task_report_in_console(task_url: str, username: str, password: str):
        """ Sterowanie procesem zbudowania raportu dla jednego taska z Jiry

        Metoda nadzoruje proces pobrania danych z Jiry oraz wyświetlenia raportu w konsoli dla podanego taska z Jiry.

        :param task_url: Adres url taska
        :type task_url: str
        :param username: Nazwa użytkownika, logującego się do Jiry
        :type username: str
        :param password: Hasło logującego się użytkownika
        :type password: str
        :return: ---
        :rtype: ---
        """
        print('Please wait... I\'m connecting to Jira...')
        jira_obj = jira.Jira()
        content = jira_obj.get_page_content(task_url, username, password)

        print('Please wait... I\'m gathering information about task...')
        estimated, remaining, logged = jira_obj.get_information_about_task(content)
        print(estimated, remaining, logged)

    def show_main_epic_data(self, epic_key_list: list):
        """ Pobranie i wyświetlenie podstawowych informacji o epikach

        Metoda pobiera z Jiry podstawowe dane o wskazanych epikach oraz wyświetla je na ekranie.

        :param epic_key_list: Lista
        :type epic_key_list:
        :return:
        :rtype:
        """
        jira_obj = jira.Jira()
        jira_obj.login_jira(self._login_url, self._username, self._password)

        data_from_jira = []
        for epic_key in epic_key_list:
            try:
                epic_url = f"{self._jira_url}/browse/{epic_key}"
                page_content = jira_obj.get_page_content_selenium(epic_url)
                name, key, budget, estimated, logged, remaining = jira_obj.get_information_about_epic(page_content)
                budget_usage = self.convert_number_to_string_with_percent(self.calculate_budget_usage(budget, logged))
                data_from_jira.append([name, key, budget, estimated, logged, remaining, budget_usage])
            except Exception as error:
                print(f"---------- Błąd dla epika: {str(epic_key).upper()} ----------")
                traceback.print_exception(error)
                print()

        self.print_table(data_from_jira)
        del jira_obj

    @staticmethod
    def print_table(data_to_show: list):
        """ Wyświetlenie raportu na ekranie

        Metoda wyświetla raport z odczytancyh danych na ekranie monitora.

        :param data_to_show: Dane w postaci listy do wyświetlenia
        :type data_to_show: list
        :return: ---
        :rtype: ---
        """
        table = PrettyTable()
        table.field_names = ["Nazwa", "Id", "Budżet", "Czas szacowany", "Czas zalogowany", "Czas pozostały",
                             "Użycie budżetu"]
        table.add_rows(data_to_show)
        print(table)

    @staticmethod
    def calculate_budget_usage(budget: float, logged_time: float) -> float:
        # TODO: trzeba dodać testy jednostkowe tej funkcji
        """ Wyliczenie użycia budżetu

        Metoda na podstawie podanego budżetu i zalogowanego czasu wylicza procent użycia budżetu

        :param budget: Budżet zadania w dniach
        :type budget: float
        :param logged_time: Zalogowany czas w godzinach
        :type logged_time: float
        :return: Użycie budżetu podane w wartości procentowej
        :rtype: float
        """
        if budget > 0:
            budget_usage = ((logged_time / 8) / budget) * 100
            return round(budget_usage, 2)
        else:
            return 0

    @staticmethod
    def convert_number_to_string_with_percent(number: float) -> str:
        """ Dodanie znaku procentu do liczby

        :param number: Liczba
        :type number: float
        :return: Liczba z dodanym procentem
        :rtype: str
        """
        return f"{str(number)} %"
