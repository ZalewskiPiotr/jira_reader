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

