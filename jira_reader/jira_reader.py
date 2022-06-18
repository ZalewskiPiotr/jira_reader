""" Moduł sterujący programem 'Jira reader'

Ten moduł steruje przepływem wykonania programu.

Moduł zawiera funkcje:
-----------------------
- main()
    Główna funkcja sterująca przepływem programu
"""
# Standard library imports
# Third party imports
# Local imports
from jira_reader import jira


def main():
    """ Główna funkcja sterująca przepływem programu.

    Funkcja uruchamia kolejne funkcje i steruje przepływem danych pomiędzy funkcjami.
    """
    task_url = input('Podaj adres taska: ')
    username = input('Podaj nazwę użytkownika: ')
    password = input('Podaj hasło: ')

    print('Please wait... I\'m connecting to Jira...')
    content = jira.get_page_content(task_url, username, password)

    print('Please wait... I\'m gathering information about task...')
    estimated, remaining, logged = jira.get_information_about_task(content)
    print(estimated, remaining, logged)
