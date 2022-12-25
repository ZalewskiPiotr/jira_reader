"""
Moduł zawiera testy jednostkowe dla modułu issue.py

Klasy:
------
- brak klas

Funkcje:
--------
- test_init_put_all_correct_attributes()
    Jeżeli przy tworzeniu obiektu zostaną podane prawidłowe wartości, to odpowiednie atrybuty obiektu powinny zwrócić
    podane wartości.
- test_calculate_budget_usage_put_correct_data_get_budget_usage_value()
    Jeżeli podane zostały prawidłowe wartości, to powinna zostać zwrócona wartość zużycia budżetu
- test_calculate_budget_usage_divide_by_zero()
    Jeżeli budżet wynosi 0, to metoda zwróci także 0

Wyjątki (exceptions):
---------------------
- brak
"""
# Local imports
from jira_reader.issue import Issue


def test_init_put_all_correct_attributes():
    """
    Jeżeli przy tworzeniu obiektu zostaną podane prawidłowe wartości, to odpowiednie atrybuty obiektu powinny zwrócić
    podane wartości.
    """
    name = "Nazwa taska"
    key = "AA-3434"

    issue = Issue(name=name, key=key)

    assert issue.name == name
    assert issue.key == key


def test_calculate_budget_usage_put_correct_data_get_budget_usage_value():
    """
    Jeżeli podane zostały prawidłowe wartości, to powinna zostać zwrócona wartość zużycia budżetu
    """
    budget = 10             # Podać dni
    logged_time = 5 * 8     # Podać godziny

    issue = Issue('testowe issue', 'testowy key')
    issue._calculate_budget_usage(budget=budget, logged_time=logged_time)
    assert issue.budget_usage == 50


def test_calculate_budget_usage_divide_by_zero():
    """
    Jeżeli budżet wynosi 0, to metoda zwróci także 0
    """
    budget = 0
    logged_time = 25

    issue = Issue('testowe issue', 'testowy key')
    issue._calculate_budget_usage(budget=budget, logged_time=logged_time)

    assert issue.budget_usage == 0
