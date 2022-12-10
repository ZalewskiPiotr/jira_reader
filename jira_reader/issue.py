# TODO: dodać dokumentację klasy
class Issue:
    def __init__(self, name: str, key: str):
        self._name: str = name
        self._key: str = key

    @property
    def name(self) -> str:
        return self._name

    @property
    def key(self) -> str:
        return self._key
