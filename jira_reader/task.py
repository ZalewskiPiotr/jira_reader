# Local imports
from jira_reader.issue import Issue


class Task(Issue):
    """
    Klasa przechowuje podstawowe informacje o tasku z Jiry

    Klasa zawiera metody i atrybuty, które pozwalają na obsługę obiektu 'task' lub 'story' z Jiry

    Atrybuty:
    ---------
    - sum_estimated
        Jest to pierwotnie zaplanowany czas na realizację taska i jego subtasków
    - sum_remaining
        Jest to pozostały szacowany czas na realizację taska i jego subtasków
    - sum_spent
        Jest to zalogowany czas na realizację taska i jego subtasków
    - status
        Status taska

    Metody:
    -------
    - brak
    """

    def __init__(self, name: str, key: str, sum_estimated: float, sum_remaining: float, sum_spent: float, status: str):
        """
        Definicja zmiennych instancji klasy

        :param name: Nazwa taska
        :type name: str
        :param key: Identyfikator taska
        :type key: str
        :param sum_estimated:  Pierwotnie zaplanowany czas na realizację taska i jego subtasków
        :type sum_estimated: float
        :param sum_remaining: Pozostały szacowany czas na realizację taska i jego subtasków
        :type sum_remaining: float
        :param sum_spent: Zalogowany czas na realizację taska i jego subtasków
        :type sum_spent: float
        :param status: Status taska
        :type status: str
        """
        super().__init__(name, key)
        self._sum_estimated: float = sum_estimated
        self._sum_remaining: float = sum_remaining
        self._sum_spent: float = sum_spent
        self._status: str = status

    @property
    def sum_estimated(self) -> float:
        """
        Jest to pierwotnie zaplanowany czas na realizację taska i jego subtasków

        :return: Pierwotnie zaplanowany czas na realizację taska i jego subtasków
        :rtype: float
        """
        return self._sum_estimated

    @property
    def sum_remaining(self) -> float:
        """
        Pozostały szacowany czas na realizację taska i jego subtasków

        :return: Pozostały szacowany czas na realizację taska i jego subtasków
        :rtype: float
        """
        return self._sum_remaining

    @property
    def sum_spent(self) -> float:
        """
        Jest to zalogowany czas na realizację taska i jego subtasków

        :return: Zalogowany czas na realizację taska i jego subtasków
        :rtype: float
        """
        return self._sum_spent

    @property
    def status(self) -> str:
        """
        Status taska

        :return: Status taska
        :rtype: str
        """
        return self._status
