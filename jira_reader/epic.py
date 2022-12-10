# TODO: dodać dokumentację klasy
from issue import Issue


class Epic(Issue):

    def __init__(self, name: str, key: str, estimated: float, remaining: float, spent: float, budget: float):
        super().__init__(name, key)
        self._time_estimated: float = estimated
        self._time_remaining: float = remaining
        self._time_spent: float = spent
        self._budget: float = budget

    @property
    def time_estimated(self) -> float:
        return self.time_estimated

    @property
    def time_remaining(self) -> float:
        return self._time_remaining

    @property
    def time_spent(self) -> float:
        return self._time_spent

    @property
    def budget(self) -> float:
        return self._budget
