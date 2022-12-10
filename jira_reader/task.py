# TODO: dodać dokumentację klasy
from issue import Issue


class Task(Issue):

    def __init__(self, name: str, key: str, sum_estimated: float, sum_remaining: float, sum_spent: float, status: str):
        super().__init__(name, key)
        self._sum_estimated: float = sum_estimated
        self._sum_remaining: float = sum_remaining
        self._sum_spent: float = sum_spent
        self._status: str = status

    @property
    def sum_estimated(self) -> float:
        return self._sum_estimated

    @property
    def sum_remaining(self) -> float:
        return  self._sum_remaining

    @property
    def sum_spent(self) -> float:
        return self._sum_spent

    @property
    def status(self) -> str:
        return self._status
