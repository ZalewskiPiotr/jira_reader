# Standard library imports

# Third party imports
import requests
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
    - get_page_content(url: str, username: str, password: str):
        Pobranie zawartości strony internetowej
    - get_information_about_task(content: str) -> tuple[float, float, float]:
        Pobranie informacji o jednym tasku z Jiry
    """

    # TODO: zajrzyj na warning, że metoda może być statyczna
    def convert_text_time_to_hours(self, text_time: str) -> float:
        """ Zamiana ciągu znaków na godziny

        Funkcja zamienia otrzymany ciąg znaków na godziny. Ciąg znaków jest pobierany z Jiry i oprócz liczby zawiera
        oznaczenie dni lub godzin. Ciąg może przyjmować postacie: 'Not specified', '10d 3h', '7h', '5d', 3.5h. Dla wartości,
        które nie posiadają liczby funkcja zwraca 0.

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

    # TODO: zajrzyj na warning, że metoda może być statyczna
    def get_page_content(self, url: str, username: str, password: str) -> str:
        """ Pobranie zawartości strony internetowej

        Funkcja na podstawie podanego adresu url pobiera zawartość strony, która znajduje się pod podanym adresem. Ponieważ
        program dedykowany jest do pobierania zawartości stron Jiry, to wymagane jest także podanie danych do logowania
        do Jiry.

        :param url: Adres strony do pobrania
        :type url: str
        :param username: Nazwa użytkownika Jiry
        :type username: str
        :param password: Hasło użytkownika Jiry
        :type password: str
        :return: Zawartość strony www w postaci HTML
        :rtype: str
        """
        session = requests.Session()
        session.auth = (username, password)

        # TODO: powalczyć jeszcze z weryfikacją certyfikatu -> patrz info od Marka
        response = session.get(url, verify=False)
        if not response.ok:
            response.raise_for_status()
        return response.text

    def get_information_about_task(self, content: str) -> tuple[float, float, float]:
        """ Pobranie informacji o jednym tasku z Jiry

        Funkcja otrzymuje stronę z Jiry z informacjami o jednym tasku. Na podstawie otrzymanej zawartości funkcja odszukuje
        informacje o czasie dotyczącym jednego taska.

        :param content: Zawartość strony Jiry z informacjami o jednym tasku w postaci HTML
        :type content: str
        :return: Odczytane informacje o czasie: estimated, remaining, logged
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
