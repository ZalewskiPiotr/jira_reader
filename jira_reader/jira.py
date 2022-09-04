# Standard library imports
import re
# Third party imports
import bs4.element
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# Local imports


class Jira:
    """
    Klasa odczytuje dane ze stron Jiry

    Klasa zawiera funkcje, które są odpowiedzialne za pobieranie danych ze stron Jiry

    Atrybuty:
    ---------
    - brak

    Metody:
    -------
    - convert_text_time_to_hours(text_time: str) -> float:
        Zamiana ciągu znaków na godziny
    - login_jira(self, login_page_url: str, user: str, password: str):
        Logowanie do Jiry
    - get_page_content_selenium(self, url: str) -> str:
        Pobranie zawartości strony z Jiry
    - get_page_content(url: str, username: str, password: str):
        Pobranie zawartości strony internetowej
    - get_information_about_task(content: str) -> tuple[float, float, float]:
        Pobranie informacji o jednym tasku z Jiry
    - get_times(cls, tag_list: list[bs4.element.Tag]) -> tuple[float, float, float]:
        Pobranie informacji o sumarycznych czasach w epiku
    - get_information_about_epic(self, content: str) -> tuple[str, str, float, float, float, float]:
        Pobranie informacji o epiku z Jiry

    """

    def __init__(self):
        """
        Definicja zmiennych instancji klasy
        """
        self._selenium_driver = None

    def __del__(self):
        """
        Usunięcie webdrivera Selenium
        """
        self._selenium_driver.quit()

    @staticmethod
    def convert_text_time_to_hours(text_time: str) -> float:
        """ Zamiana ciągu znaków na godziny

        Funkcja zamienia otrzymany ciąg znaków na godziny. Ciąg znaków jest pobierany z Jiry i oprócz liczby zawiera
        oznaczenie dni lub godzin. Ciąg może przyjmować postacie: 'Not specified', '10d 3h', '7h', '5d', 3.5h. Dla
        wartości, które nie posiadają liczby funkcja zwraca 0.

        :param text_time: Ciąg znaków zawierający czas
        :type text_time: str
        :return: Ilość godzin ustalona na podstawie ciągu wejściowego
        :rtype: float
        """
        if text_time.lower() == 'not specified':
            return 0

        time_list_values = text_time.split()
        days = 0
        hours = 0
        for time in time_list_values:
            if 'd' in time:
                days = float(time[0:time.find('d')])
            if 'h' in time:
                hours = float(time[0:time.find('h')])
        total_time = days * 8 + hours
        return total_time

    # TODO: dodać testy jednostkowe: nieprawidłowy url (może sprawdzać po tytule strony); złe dane logowania; brak jednego z pól do logowania
    def login_jira(self, login_page_url: str, user: str, password: str):
        """ Logowanie do Jiry

        Metoda przeprowadza logowanie do Jiry. Najpierw należy wywołać logowanie do Jiry, a potem można korzystać z
        pozostałych metod tej klasy do pobierania zawartości stron.

        :param login_page_url: Adres url strony logowania
        :type login_page_url: str
        :param user: Nazywa użytkownika Jiry
        :type user: str
        :param password: Hasło do Jiry
        :type password: str
        :return: brak
        :rtype: ---
        """
        self._selenium_driver = webdriver.Chrome()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(login_page_url)
        driver.implicitly_wait(3)
        driver.find_element(By.ID, "login-form-username").send_keys(user)
        driver.find_element(By.ID, "login-form-password").send_keys(password)
        driver.find_element(By.ID, "login-form-submit").click()
        self._selenium_driver = driver

    # TODO: dodać testy jednostkowe: nieprawidłowy url;
    def get_page_content_selenium(self, url: str) -> str:
        """ Pobranie zawartości strony z Jiry

        Metoda pobiera zawartość strony i zwraca ją w postaci HTML

        :param url: Adres strony do pobrania
        :type url: str
        :return:  Zawartość strony web w postaci HTML
        :rtype: str
        """
        self._selenium_driver.get(url)
        return self._selenium_driver.page_source

    # TODO: to już chyba nie będzie potrzebne. Na razie dane pobieram z epika. Do przemyślenia.
    def get_information_about_task(self, content: str) -> tuple[float, float, float]:
        """ Pobranie informacji o jednym tasku z Jiry

        Funkcja otrzymuje stronę z Jiry z informacjami o jednym tasku. Na podstawie otrzymanej zawartości funkcja
        odszukuje informacje o czasie dotyczącym jednego taska.

        :param content: Zawartość strony Jiry z informacjami o jednym tasku w postaci HTML
        :type content: str
        :return: Odczytane informacje o czasie: estimated, remaining, logged. Czas podawany jest w godzinach.
        :rtype: tuple[float, float, float]
        """
        soup = BeautifulSoup(content, features='lxml')
        estimated_text = soup.find(id='tt_single_values_orig').text.strip()
        remaining_text = soup.find(id='tt_single_values_remain').text.strip()
        logged_text = soup.find(id='tt_single_values_spent').text.strip()

        estimated_time = self.convert_text_time_to_hours(estimated_text)
        remaining_time = self.convert_text_time_to_hours(remaining_text)
        logged_time = self.convert_text_time_to_hours(logged_text)

        return estimated_time, remaining_time, logged_time

    # TODO: tag_times może nie mieć atrybutu 'title' -> zrobić test jednostkowy
    @classmethod
    def get_times(cls, tag_list: list[bs4.element.Tag]) -> tuple[float, float, float]:
        """ Pobranie informacji o sumarycznych czasach w epiku

        Funkcja pobiera z przekazanego taga informacje o sumarycznych czasach na epiku.

        :param tag_list: lista tagów 'dd'. Prawidłowo na liście powinien być tylko jeden tag. Jeżeli pojawi się więcej,
        to trzeba zmienić sposób wyszukiwania tagów.
        :type tag_list: list[bs4.element.Tag]
        :return: Sumaryczna informacja o czasach z epika: spent, remaining, estimated
        :rtype: tuple[float, float, float]
        """
        if tag_list is None:
            raise TypeError("Nie znaleziono pozycji 'Time' w 'Summary Panel' dla epika")
        if len(tag_list) > 1 or len(tag_list) == 0:
            raise ValueError(f"Znaleziono nieprawidłową ilość ({len(tag_list)}) pozycji 'Time' w 'Summary Panel' dla "
                             f"epika.\n {tag_list}")

        time_tag = tag_list[0]
        time_string = time_tag['title']
        time_list = time_string.split('\n')

        spent = 0
        remaining = 0
        estimated = 0

        for time in time_list:
            time_values = time.split(':')
            if time_values[0].upper() == 'TIME SPENT':
                spent = cls.convert_text_time_to_hours(time_values[1])
            if time_values[0].upper() == 'REMAINING':
                remaining = cls.convert_text_time_to_hours(time_values[1])
            if time_values[0].upper() == 'ESTIMATED':
                estimated = cls.convert_text_time_to_hours(time_values[1])

        return spent, remaining, estimated

    # TODO: dodać testy jednostkowe
    def get_information_about_epic(self, content: str) -> tuple[str, str, float, float, float, float]:
        """ Pobranie informacji o epiku z Jiry
        Funkcja otrzymuje stronę z Jiry z informacjami o jednym epiku. Na podstawie otrzymanej zawartości funkcja
        odszukuje podstawowe informacje o wskazanym epiku.

        :param content: Zawartość strony Jiry z informacjami o jednym epiku w postaci HTML
        :type content: str
        :return: Odczytane informacje o epiku: nazwa, key, budżet, estimated time, logged time, remaining time.
        Czas podawany jest w godzinach.
        :rtype: tuple[str, str, float, float, float. float]
        """
        soup = BeautifulSoup(content, features='lxml')

        # Pobranie podstawowych informacji z epika
        epic_name = soup.find(id='summary-val').text.strip()
        epic_key = soup.find(id='key-val').text.strip()

        # TODO: poprawić pobieranie budżetu ze strony
        # Pobranie budżetu z epika
        # epic_budget = soup.find(id='customfield_12300-val').text.strip()

        # Pobranie czasów z epika: spent, remaining, estimated
        times_list = soup.find_all(class_='tt_values', title=re.compile('Time spent:'))
        spent_time, remaining_time, estimated_time = self.get_times(times_list)

        # TODO: odremować linijkę z epic_budget
        # return epic_name, epic_key, epic_budget, epic_estimated_time, epic_logged_time, epic_remaining_time
        return epic_name, epic_key, 0, estimated_time, spent_time, remaining_time

