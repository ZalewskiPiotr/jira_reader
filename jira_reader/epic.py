# TODO: dodać testy jednostkowe
# Local imports
from issue import Issue


class Epic(Issue):
    """
    Klasa przechowuje podstawowe informacje o epiku z Jiry

    Klasa zawiera metody i atrybuty, które pozwalają na obsługę obiektu 'epic' z Jiry

    Atrybuty:
    ---------
    - time_estimated
        Zawartość pola 'time estimated' z obiektu 'epic'. Jest to pierwotnie zaplanowany czas na realizację zadania
    - time_remaining
        Zawartość pola 'time remaining' z obiektu 'epic'. Jest to pozostały szacowany czas na realizację zadania
    - time_spent
        Zawartość pola 'time spent' z obiektu 'epic'. Jest to zalogowany czas na realizację zadania
    - budget
        Zawartość pola 'Budżet' z obiektu 'epic'. Jest to budżet zadania.

    Metody:
    -------
    - brak
    """

    def __init__(self, name: str, key: str, estimated: float, remaining: float, spent: float, budget: float):
        """
        Definicja zmiennych instancji klasy

        :param name: Nazwa epika
        :type name: str
        :param key: Identyfikator epika
        :type key: str
        :param estimated: Pierwotnie planowany czas realizacji
        :type estimated: float
        :param remaining: Pozostały jeszcze czas do zakończenia zadania
        :type remaining: float
        :param spent: Czas zalogowany na zadanie
        :type spent: float
        :param budget: Budżet zadania
        :type budget: float
        """
        super().__init__(name, key)
        self._time_estimated: float = estimated
        self._time_remaining: float = remaining
        self._time_spent: float = spent
        self._budget: float = budget

    @property
    def time_estimated(self) -> float:
        """
        Zawartość pola 'time estimated' z obiektu 'epic'. Jest to pierwotnie zaplanowany czas na realizację zadania

        :return: Pierwotnie planowany czas
        :rtype: float
        """
        return self.time_estimated

    @property
    def time_remaining(self) -> float:
        """
        Zawartość pola 'time remaining' z obiektu 'epic'. Jest to pozostały szacowany czas na realizację zadania

        :return: Czas pozostały do zakończenia zadania
        :rtype: float
        """
        return self._time_remaining

    @property
    def time_spent(self) -> float:
        """
        Zawartość pola 'time spent' z obiektu 'epic'. Jest to zalogowany czas na realizację zadania

        :return: Zalogowany czas
        :rtype: float
        """
        return self._time_spent

    @property
    def budget(self) -> float:
        """
        Zawartość pola 'Budżet' z obiektu 'epic'. Jest to budżet zadania.

        :return: Budżet zadania
        :rtype: float
        """
        return self._budget
