"""
Moduł zawiera testy jednostkowe dla modułu epic.py

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
from jira_reader.epic import Epic


def test_init_put_all_correct_attributes():
    """
    Jeżeli przy tworzeniu obiektu zostaną podane prawidłowe wartości, to odpowiednie atrybuty obiektu powinny zwrócić
    podane wartości.
    """
    name = "Nazwa epika"
    key = "AA-3434"
    estimated = 23
    remaining = 12
    spent = 11
    budget = 150

    epic = Epic(name=name, key=key, estimated=estimated, remaining=remaining, spent=spent, budget=budget)

    assert epic.name == name
    assert epic.key == key
    assert epic.time_estimated == estimated
    assert epic.time_remaining == remaining
    assert epic.time_spent == spent
    assert epic.budget == budget
