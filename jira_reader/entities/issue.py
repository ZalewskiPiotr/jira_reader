class Issue:
    """
    Klasa przechowuje podstawowe informacje o issue z Jiry

    Klasa zawiera metody i atrybuty, które pozwalają na obsługę obiektu 'issue' z Jiry

    Atrybuty:
    ---------
    - name
        Zawartość pola 'description' z obiektu 'issue'. Faktycznie jest to nazwa 'issue'
    - key
        Zawartość pola 'key' z obiektu 'issue'. Faktycznie jest to identyfikator 'issue'
    - budget_usage
        Zużycie budżetu w postaci procentowej wyliczone w metodzie 'calculate_budget_usage'
    - estimated_budget_usage
        Szacowane zużycie budżetu w postaci procentowej wyliczone w metodzie 'calculate_estimated_budget_usage'

    Metody:
    -------
    - _calculate_budget_usage(self, budget: float, logged_time: float):
        Wyliczenie użycia budżetu
    - _calculate_estimated_budget_usage(self, budget: float, logged_time: float, remaining_time: float) -> float:
        Wyliczenie przewidywanego zużycia budżetu
    """

    def __init__(self, name: str, key: str):
        """
        Definicja zmiennych instancji klasy

        :param name: Nazwa issue
        :type name: str
        :param key: Identyfikator issue
        :type key: str
        """
        self._name: str = name
        self._key: str = key
        self._budget_usage: float = 0
        self._estimated_budget_usage: float = 0

    @property
    def name(self) -> str:
        """
        Zawartość pola 'description' z obiektu 'issue'. Faktycznie jest to nazwa 'issue'

        :return: Nazwa issue
        :rtype: str
        """
        return self._name

    @property
    def key(self) -> str:
        """
        Zawartość pola 'key' z obiektu 'issue'. Faktycznie jest to identyfikator 'issue'

        :return: Identyfikator issue
        :rtype: str
        """
        return self._key

    @property
    def budget_usage(self) -> float:
        """
        Zużycie budżetu w postaci procentowej wyliczone w metodzie 'calculate_budget_usage'

        :return: Zużycie budżetu w postaci procentowej
        :rtype: float
        """
        return self._budget_usage

    @property
    def estimated_budget_usage(self) -> float:
        """
        Szacowane zużycie budżetu w postaci procentowej wyliczone w metodzie 'calculate_estimated_budget_usage'

        :return: Szacowane zużycie budżetu w postaci procentowej
        :rtype: float
        """
        return self._estimated_budget_usage

    def _calculate_budget_usage(self, budget: float, logged_time: float):
        """ Wyliczenie użycia budżetu

        Metoda na podstawie podanego budżetu i zalogowanego czasu wylicza procent użycia budżetu

        :param budget: Budżet zadania w dniach
        :type budget: float
        :param logged_time: Zalogowany czas w godzinach
        :type logged_time: float
        :return: ---
        :rtype: ---
        """
        if budget > 0:
            budget_usage = ((logged_time / 8) / budget) * 100
            self._budget_usage = round(budget_usage, 2)

    def _calculate_estimated_budget_usage(self, budget: float, logged_time: float, remaining_time: float) -> float:
        """ Wyliczenie przewidywanego zużycia budżetu

        Metoda na podstawia zalogowanego czasu i czasu który pozostał do zakończenia zadania, wylicza przewidywane
        procentowe zużycie budżetu zadania.

        :param budget: Budżet zadania w dniach
        :type budget: float
        :param logged_time: Zalogowany czas w godzinach
        :type logged_time: float
        :param remaining_time: Przewidywany pozostały czas w godzinach
        :type remaining_time: float
        :return: Przewidywane zużycie budżetu w procentach
        :rtype: float
        """
        if budget > 0:
            estimated_budget = (((logged_time + remaining_time) / 8) / budget) * 100
            self._estimated_budget_usage = round(estimated_budget, 2)

