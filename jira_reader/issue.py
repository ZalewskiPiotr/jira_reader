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

    Metody:
    -------
    - calculate_budget_usage(self, budget: float, logged_time: float):
        Wyliczenie użycia budżetu
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
        self._budget_usage = 0

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
        else:
            self._budget_usage = 0

