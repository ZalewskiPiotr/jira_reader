""" Skrypt uruchamiający program 'Jira reader'

Ten skrypt uruchamia program.

Uruchomienie skryptu odbywa się poprzez wywołanie:
`python runner.py`

Skrypt zawiera funkcje:
-----------------------
- show_program_metadata()
    Wyświetlenie metadanych programu
"""
# Standard library imports
# Third party imports
# Local imports
import jira_reader
from jira_reader import jira_reader as jr


def show_program_metadata():
    """ Wyświetlenie metadanych programu

    Funkcja wyświetla informacje o programie pobrane z pliku __init__.py pakietu jira_reader
    :return: ---
    :rtype: ---
    """
    print('-' * 30, f"Program: {jira_reader.__program_name__} ({jira_reader.__name__})", '-' * 30)
    print(f"Wersja: {jira_reader.__version__}")
    print(f"Autor: {jira_reader.__author__}")
    print(f"Wiki: {jira_reader.__wiki__}")
    print('-' * 96)


if __name__ == '__main__':
    show_program_metadata()
    jr.main()

