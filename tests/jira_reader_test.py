"""
Moduł zawiera testy jednostkowe dla modułu jira_reader.py

Klasy:
------
- brak klas

Funkcje:
--------
- test_init_if_put_empty_url_get_error():
    Jeżeli zostanie podany pusty adres url to powinien zostać zwrócony wyjątek ValueError
- test_init_if_put_empty_user_get_error():
    Jeżeli zostanie podana pusta nazwa użytkownika to powinien zostać zwrócony wyjątek ValueError
- test_init_if_put_empty_password_get_error():
     Jeżeli zostanie podane puste hasło to powinien zostać zwrócony wyjątek ValueError
- test_calculate_budget_usage_put_correct_data_get_budget_usage_value():
    Jeżeli podane zostały prawidłowe wartości, to powinna zostać zwrócona wartość zużycia budżetu
- test_calculate_budget_usage_divide_by_zero():
    Jeżeli budżet wynosi 0, to metoda zwróci także 0

Wyjątki (exceptions):
---------------------
- brak
"""

# Standard library imports
# Third party imports
import pytest
# Local Imports
import jira_reader.jira_reader as jr


def test_init_if_put_empty_jira_url_get_error():
    """
    Jeżeli zostanie podany pusty adres url do jiry to powinien zostać zwrócony wyjątek ValueError
    """
    url = ' '
    login_page = 'login.jsp'
    user = 'user name'
    password = 'secret password'
    with pytest.raises(ValueError):
        jr.JiraReader(url, login_page, user, password)


def test_init_if_put_empty_user_get_error():
    """
    Jeżeli zostanie podana pusta nazwa użytkownika to powinien zostać zwrócony wyjątek ValueError
    """
    url = 'http://www.adres.com'
    login_page = 'login.jsp'
    user = ''
    password = 'secret password'

    with pytest.raises(ValueError):
        jr.JiraReader(url, login_page, user, password)


def test_init_if_put_empty_password_get_error():
    """
    Jeżeli zostanie podane puste hasło to powinien zostać zwrócony wyjątek ValueError
    """
    url = 'http://www.adres.com'
    login_page = 'login.jsp'
    user = 'user name'
    password = ''

    with pytest.raises(ValueError):
        jr.JiraReader(url, login_page, user, password)


def test_init_if_put_empty_login_page_get_error():
    """
    Jeżeli zostanie podany pusty adres strony logowania to powinien zostać zwrócony wyjątek ValueError
    """
    url = 'http://www.adres.com'
    login_page = ' '
    user = 'user name'
    password = ''

    with pytest.raises(ValueError):
        jr.JiraReader(url, login_page, user, password)
