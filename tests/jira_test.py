"""
Moduł zawiera testy jednostkowe dla modułu jira.py

Klasy:
------
- brak klas

Funkcje:
--------
- get_path_to_test_data(file_name: str, file_suffix: str) -> pathlib.PurePath:
    Ustalenie ścieżki do pliku z danymi potrzebnymi w czasie uruchomienia testów
- test_convert_text_time_to_hours_put_days_and_hours_get_total_hours()
    Jeżeli podany zostanie ciąg '10d 7h' zwrócona zostanie sumaryczna ilość godzin
- test_convert_text_time_to_hours_put_days_get_total_hours()
    Jeżeli podany zostanie ciąg '4d', zwrócona zostanie sumaryczna ilość godzin
- test_convert_text_time_to_hours_put_hours_get_hours()
    Jeżeli podany zostanie ciąg '5h', zwrócona zostanie sumaryczna ilość godzin
- test_convert_text_time_to_hours_put_hours_in_decimal_format_get_hours()
    Jeżeli podany zostanie ciąg '3.5h', zwrócona zostanie sumaryczna ilość godzin
- test_convert_text_time_to_hours_put_not_specified_string_get_zero()
    Jeżeli podany zostanie ciąg '', zwrócone zostanie zero
- test_convert_text_time_to_hours_put_empty_string_get_zero()
    Jeżeli podany zostanie ciąg 'Not specified', zwrócone zostanie zero
- test_get_information_about_task_put_correct_task_get_correct_values()
    Jeżeli podane zostaną prawidłowe wartości o tasku z Jiry, to zwrócone zostaną prawidłowe informacje o czasach.
- test_get_information_about_epic_put_correct_html_get_correct_values
    Jeżeli podany zostanie prawidłowy HTML z danymi epika, to zwrócone zostaną prawidłowe wartości
- test_get_times_put_none_tag_get_error()
    Jeżeli podany zostanie pusty obiekt (nie znaleziony w pliku HTML), to zwrócony zostanie wyjątek
- test_get_times_put_tag_list_get_error()
    Jeżeli podanych zostanie więcej tagów niż 1, to zwrócony zostanie wyjątek
- def test_get_times_put_tag_without_attribute_title_get_error()
    Jeżeli podanych zostanie tag bez atrybutu 'title', to zwrócony zostanie wyjątek
- test_get_times_put_correct_tag_get_correct_values()
    Jeżeli podany zostanie prawidłowy tag, to metoda zwróci czasy w postaci liczby godzin
- test_get_epic_budget_put_html_with_budget_get_budget_value()
    Jeżeli podany zostanie html z wartością budżetu to zwrócona zostanie wartość tego budżetu
- test_get_epic_budget_put_html_with_no_budget_get_zero_value()
    Jeżeli podany zostanie html bez wartości budżetu to zwrócona zostanie wartość 0
- test_get_epic_budget_put_html_with_many_budgets_get_error()
    Jeżeli podany zostanie html z kilkoma wartościami budżetu, to zwrócony zostanie wyjątek

Wyjątki (exceptions):
---------------------
- brak
"""
# Standard library imports
import pathlib
# Third party imports
import pytest
from bs4 import BeautifulSoup
# Local imports
from jira_reader import jira


def get_path_to_test_data(file_name: str, file_suffix: str) -> pathlib.PurePath:
    """
    Ustalenie ścieżki do pliku z danymi potrzebnymi w czasie uruchomienia testów
    :param file_name: Nazwa pliku z danymi do testów
    :type file_name: str
    :param file_suffix: Rozszerzenie pliku z danymi do testów
    :type file_suffix: str
    :return: Ścieżka do pliku z danymi do testów
    :rtype: pathlib.PurePath
    """
    working_directory_path = pathlib.Path.cwd()
    return working_directory_path.joinpath('data', file_name).with_suffix('.' + file_suffix)


def test_convert_text_time_to_hours_put_days_and_hours_get_total_hours():
    """
    Jeżeli podany zostanie ciąg '10d 7h' zwrócona zostanie sumaryczna ilość godzin
    """
    text_string = '10d 7h'
    jira_obj = jira.Jira()
    value = jira_obj.convert_text_time_to_hours(text_string)
    assert value == 10 * 8 + 7


def test_convert_text_time_to_hours_put_days_get_total_hours():
    """
    Jeżeli podany zostanie ciąg '5h', zwrócona zostanie sumaryczna ilość godzin
    """
    text_string = '5h'
    jira_obj = jira.Jira()
    value = jira_obj.convert_text_time_to_hours(text_string)
    assert value == 5


def test_convert_text_time_to_hours_put_hours_get_hours():
    """
    Jeżeli podany zostanie ciąg '4d', zwrócona zostanie sumaryczna ilość godzin
    """
    text_string = '4d'
    jira_obj = jira.Jira()
    value = jira_obj.convert_text_time_to_hours(text_string)
    assert value == 4 * 8


def test_convert_text_time_to_hours_put_hours_in_decimal_format_get_hours():
    """
    Jeżeli podany zostanie ciąg '3.5h', zwrócona zostanie sumaryczna ilość godzin
    """
    text_string = '3.5d'
    jira_obj = jira.Jira()
    value = jira_obj.convert_text_time_to_hours(text_string)
    assert value == 3.5 * 8


def test_convert_text_time_to_hours_put_not_specified_string_get_zero():
    """
    Jeżeli podany zostanie ciąg '', zwrócone zostanie zero
    """
    text_string = ''
    jira_obj = jira.Jira()
    value = jira_obj.convert_text_time_to_hours(text_string)
    assert value == 0


def test_convert_text_time_to_hours_put_empty_string_get_zero():
    """
    Jeżeli podany zostanie ciąg 'Not specified', zwrócone zostanie zero
    """
    text_string = 'Not specified'
    jira_obj = jira.Jira()
    value = jira_obj.convert_text_time_to_hours(text_string)
    assert value == 0


def test_get_information_about_task_put_correct_task_get_correct_values():
    """
    Jeżeli podane zostaną prawidłowe wartości o tasku z Jiry, to zwrócone zostaną prawidłowe informacje o czasach.
    """
    test_file_path = get_path_to_test_data('test_task', 'html')
    with open(test_file_path, 'r') as task_file:
        file_content = task_file.read()
    jira_obj = jira.Jira()
    estimated, remaining, logged = jira_obj.get_information_about_task(file_content)
    assert estimated == 0
    assert remaining == 7
    assert logged == 16


def test_get_information_about_epic_put_correct_html_get_correct_values():
    """
    Jeżeli podany zostanie prawidłowy HTML z danymi epika, to zwrócone zostaną prawidłowe wartości
    """
    test_file_path = get_path_to_test_data('test_epik', 'html')
    with open(test_file_path, 'r') as task_file:
        file_content = task_file.read()
    jira_obj = jira.Jira()
    name, key, budget, estimated, logged, remaining = jira_obj.get_information_about_epic(file_content)
    assert name == "WO E4 DW W5"
    assert key == "AEWO-1000"
    assert budget == 5
    assert estimated == 40.0
    assert logged == 43.5
    assert remaining == 0.0


def test_get_times_put_none_tag_get_error():
    """
    Jeżeli podany zostanie pusty obiekt (nie znaleziony w pliku HTML), to zwrócony zostanie wyjątek
    """
    html = ''
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.dd
    with pytest.raises(TypeError):
        jira.Jira.get_times(tag)


def test_get_times_put_tag_list_get_error():
    """
    Jeżeli podanych zostanie więcej tagów niż 1, to zwrócony zostanie wyjątek
    """
    html = '<dd class="tt_values" title="Time spent: 446.2h\nRemaining: 1.0h\nEstimated: 319.5h">446.2h / 319.5h</dd>' \
           '\n<dd class="tt_values" title="Time spent: 446.2h\nRemaining: 1.0h\nEstimated: 319.5h">446.2h / 319.5h</dd>'
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find_all('dd')
    with pytest.raises(ValueError):
        jira.Jira.get_times(tag)


def test_get_times_put_tag_without_attribute_title_get_error():
    """
    Jeżeli podanych zostanie tag bez atrybutu 'title', to zwrócony zostanie wyjątek
    """
    html = '<dd class="tt_values" no_title="Time spent: 46.2h\nRemaining: 1.0h\nEstimated: 319.5h">446.2h / 319.5h</dd>'
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find_all('dd')
    with pytest.raises(KeyError):
        jira.Jira.get_times(tag)


def test_get_times_put_correct_tag_get_correct_values():
    """
    Jeżeli podany zostanie prawidłowy tag, to metoda zwróci czasy w postaci liczby godzin
    """
    html = '<dd class="tt_values" title="Time spent: 446.2h\nRemaining: 1.0h\nEstimated: 319.5h">446.2h / 319.5h</dd>'
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find_all('dd')
    spent, remaining, estimated = jira.Jira.get_times(tag)
    assert spent == 446.2
    assert remaining == 1.0
    assert estimated == 319.5


def test_get_epic_budget_put_html_with_budget_get_budget_value():
    """
    Jeżeli podany zostanie html z wartością budżetu to zwrócona zostanie wartość tego budżetu
    """
    html ='<li id="rowForcustomfield_12300" class="item"> ' \
          '<div class="wrap"><strong title="Budżet zadania" class="name">Budżet zadania:</strong>' \
          '<div id="customfield_12300-val" class="value type-float editable-field inactive" data-fieldtype="float" ' \
          'data-fieldtypecompletekey="com.atlassian.jira.plugin.system.customfieldtypes:float"' \
          'title="Click to edit">5<span class="overlay-icon aui-icon aui-icon-small aui-iconfont-edit"></span></div>' \
          '</div></li>'
    soup = BeautifulSoup(html, 'html.parser')
    budget_tag_list = soup.find_all('strong', title='Budżet zadania')
    epic_budget = jira.Jira.get_epic_budget(budget_tag_list)
    assert epic_budget == 5


def test_get_epic_budget_put_html_with_no_budget_get_zero_value():
    """
    Jeżeli podany zostanie html bez wartości budżetu to zwrócona zostanie wartość 0
    """
    html ='<li id="rowForcustomfield_12300" class="item"> ' \
          '<div class="wrap"><strong title="Bez budżetu" class="name">Bez budżetu:</strong>' \
          '<div id="customfield_12300-val" class="value type-float editable-field inactive" data-fieldtype="float" ' \
          'data-fieldtypecompletekey="com.atlassian.jira.plugin.system.customfieldtypes:float"' \
          'title="Click to edit">5<span class="overlay-icon aui-icon aui-icon-small aui-iconfont-edit"></span></div>' \
          '</div></li>'
    soup = BeautifulSoup(html, 'html.parser')
    budget_tag_list = soup.find_all('strong', title='Budżet zadania')
    epic_budget = jira.Jira.get_epic_budget(budget_tag_list)
    assert epic_budget == 0


def test_get_epic_budget_put_html_with_many_budgets_get_error():
    """
    Jeżeli podany zostanie html z kilkoma wartościami budżetu, to zwrócony zostanie wyjątek
    """
    html ='<li id="rowForcustomfield_12300" class="item"> ' \
          '<div class="wrap"><strong title="Budżet zadania" class="name">Budżet zadania:</strong> ' \
          '<strong title="Budżet zadania" class="name">Budżet zadania:</strong>' \
          '<div id="customfield_12300-val" class="value type-float editable-field inactive" data-fieldtype="float" ' \
          'data-fieldtypecompletekey="com.atlassian.jira.plugin.system.customfieldtypes:float"' \
          'title="Click to edit">5<span class="overlay-icon aui-icon aui-icon-small aui-iconfont-edit"></span></div>' \
          '</div></li>'
    soup = BeautifulSoup(html, 'html.parser')
    budget_tag_list = soup.find_all('strong', title='Budżet zadania')
    with pytest.raises(ValueError):
        epic_budget = jira.Jira.get_epic_budget(budget_tag_list)

