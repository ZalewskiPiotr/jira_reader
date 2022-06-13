""" Skrypt uruchamiający i sterujący programem 'Jira reader'

Ten skrypt uruchamia program i steruje jego przepływem.

Uruchomienie skryptu odbywa się poprzez wywołanie:
`python runner.py`

Skrypt zawiera funkcje:
-----------------------
- main()
    Główna funkcja sterująca przepływem programu
"""
# Standard library imports
# Third party imports
# Local imports
import jira_reader as jr
import jira_reader.jira as jira


def test_func(number):
    return number + 2


def main():
    print(f"hello. My name is {__name__} and version is {jr.__version__}")

    task_url = input('Podaj adres taska: ')
    username = input('Podaj nazwę użytkownika: ')
    password = input('Podaj hasło: ')

    print('Please wait... I\'m connecting to Jira...')
    content = jira.get_page_content(task_url, username, password)

    print('Please wait... I\'m gathering information about task...')
    estimated, remaining, logged = jira.get_information_about_task(content)
    print(estimated, remaining, logged)


if __name__ == '__main__':
    main()
