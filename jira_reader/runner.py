""" Skrypt uruchamiający i sterujący programem 'Jira reader'

Ten skrypt uruchamia program i steruje jego przepływem.

Uruchomienie skryptu odbywa się poprzez wywołanie:
`python runner.py`

Skrypt zawiera funkcje:
-----------------------
- show_program_information()
    Wyświetlenie informacji o programie
- main()
    Główna funkcja sterująca przepływem programu
"""
# Standard library imports
# Third party imports
# Local imports
import jira_reader as jr
import jira_reader.jira as jira


def show_program_information():
    """ Wyświetlenie informacji o programie

    Funkcja wyświetla informacje o wersji programu oraz o jego autorze. Informacje te odczytuje z pliku __init.py__

    :return: ---
    :rtype: ---
    """
    # TODO: zmienić sposób pobierania numeru wersji. Trzeba otworzyć plik __init__.py i poszukać ciągu z wersją. Wtedy można usunąć import jira_reader as jr
    print(f"hello. My name is {__name__} and version is {jr.__version__} and author is {jr.__author__}")


def main():
    """ Główna funkcja sterująca przepływem programu.

    Funkcja uruchamia kolejne funkcje i steruje przepływem danych pomiędzy funkcjami.
    """
    show_program_information()

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
