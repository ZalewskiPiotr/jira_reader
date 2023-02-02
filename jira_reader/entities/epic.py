# Local imports
from jira_reader.entities.issue import Issue


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
        self.time_estimated = estimated
        self.time_remaining = remaining
        self.time_spent = spent
        self.budget = budget
        super()._calculate_budget_usage(budget=budget, logged_time=spent)
        super()._calculate_estimated_budget_usage(budget=budget, logged_time=spent, remaining_time=remaining)

    @property
    def time_estimated(self) -> float:
        """
        Zawartość pola 'time estimated' z obiektu 'epic'. Jest to pierwotnie zaplanowany czas na realizację zadania

        :return: Pierwotnie planowany czas
        :rtype: float
        """
        return self._time_estimated

    @time_estimated.setter
    def time_estimated(self, value: float):
        self._time_estimated = value

    @property
    def time_remaining(self) -> float:
        """
        Zawartość pola 'time remaining' z obiektu 'epic'. Jest to pozostały szacowany czas na realizację zadania

        :return: Czas pozostały do zakończenia zadania
        :rtype: float
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, value: float):
        self._time_remaining = value

    @property
    def time_spent(self) -> float:
        """
        Zawartość pola 'time spent' z obiektu 'epic'. Jest to zalogowany czas na realizację zadania

        :return: Zalogowany czas
        :rtype: float
        """
        return self._time_spent

    @time_spent.setter
    def time_spent(self, value: float):
        self._time_spent = value

    @property
    def budget(self) -> float:
        """
        Zawartość pola 'Budżet' z obiektu 'epic'. Jest to budżet zadania.

        :return: Budżet zadania
        :rtype: float
        """
        return self._budget

    @budget.setter
    def budget(self, value: float):
        self._budget = value
