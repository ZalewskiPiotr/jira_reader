"""
Moduł zawiera testy jednostkowe dla modułu task.py

Klasy:
------
- brak klas

Funkcje:
--------
- test_init_put_all_correct_attributes()
    Jeżeli przy tworzeniu obiektu zostaną podane prawidłowe wartości, to odpowiednie atrybuty obiektu powinny zwrócić
    podane wartości.
Wyjątki (exceptions):
---------------------
- brak
"""
# Local imports
from jira_reader.entities.task import Task


def test_init_put_all_correct_attributes():
    """
    Jeżeli przy tworzeniu obiektu zostaną podane prawidłowe wartości, to odpowiednie atrybuty obiektu powinny zwrócić
    podane wartości.
    """
    name = "Nazwa taska"
    key = "AA-3434"
    estimated = 23
    remaining = 12
    spent = 11
    status = "done"

    task = Task(name=name, key=key, sum_estimated=estimated, sum_remaining=remaining, sum_spent=spent, status=status)

    assert task.name == name
    assert task.key == key
    assert task.sum_estimated == estimated
    assert task.sum_remaining == remaining
    assert task.sum_spent == spent
    assert task.status == status
