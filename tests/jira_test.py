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

Wyjątki (exceptions):
---------------------
- brak
"""
# Standard library imports
import pathlib
# Third party imports
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
    value = jira.convert_text_time_to_hours(text_string)
    assert value == 10 * 8 + 7


def test_convert_text_time_to_hours_put_days_get_total_hours():
    """
    Jeżeli podany zostanie ciąg '5h', zwrócona zostanie sumaryczna ilość godzin
    """
    text_string = '5h'
    value = jira.convert_text_time_to_hours(text_string)
    assert value == 5


def test_convert_text_time_to_hours_put_hours_get_hours():
    """
    Jeżeli podany zostanie ciąg '4d', zwrócona zostanie sumaryczna ilość godzin
    """
    text_string = '4d'
    value = jira.convert_text_time_to_hours(text_string)
    assert value == 4 * 8


def test_convert_text_time_to_hours_put_hours_in_decimal_format_get_hours():
    """
    Jeżeli podany zostanie ciąg '3.5h', zwrócona zostanie sumaryczna ilość godzin
    """
    text_string = '3.5d'
    value = jira.convert_text_time_to_hours(text_string)
    assert value == 3.5 * 8


def test_convert_text_time_to_hours_put_not_specified_string_get_zero():
    """
    Jeżeli podany zostanie ciąg '', zwrócone zostanie zero
    """
    text_string = ''
    value = jira.convert_text_time_to_hours(text_string)
    assert value == 0


def test_convert_text_time_to_hours_put_empty_string_get_zero():
    """
    Jeżeli podany zostanie ciąg 'Not specified', zwrócone zostanie zero
    """
    text_string = 'Not specified'
    value = jira.convert_text_time_to_hours(text_string)
    assert value == 0


def test_get_information_about_task_put_correct_task_get_correct_values():
    """
    Jeżeli podane zostaną prawidłowe wartości o tasku z Jiry, to zwrócone zostaną prawidłowe informacje o czasach.
    """
    test_file_path = get_path_to_test_data('test_task', 'html')
    with open(test_file_path, 'r') as task_file:
        file_content = task_file.read()
    estimated, remaining, logged = jira.get_information_about_task(file_content)
    assert estimated == 0
    assert remaining == 7
    assert logged == 16
