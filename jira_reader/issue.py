# TODO: dodać testy jednostkowe
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

    Metody:
    -------
    - brak
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
