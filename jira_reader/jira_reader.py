# Standard library imports

# Third party imports

# Local imports
from jira_reader import jira


class JiraReader:
    """
    Klasa odpowiada za logikę przepływu, który umożliwi zbudowanie raportu.

    Klasa jest modułem sterującym przepływem programu. Klasa sama nie pobiera danych z Jiry, ani nie wyświetla raportu.
    Dane z Jiry są pobierane poprzez moduł jira_reader.jira
    Raport na konsoli jest wyświetlany poprzez moduł jira_reader.console_view

    Atrybuty:
    ---------

    Metody:
    -------
    - show_task_report_in_console(self, task_url: str, username: str, password: str):
        Sterowanie procesem zbudowania raportu dla jednego taska z Jiry
    """

    # TODO: zajrzyj na warning, że metoda może być statyczna
    def show_task_report_in_console(self, task_url: str, username: str, password: str):
        """ Sterowanie procesem zbudowania raportu dla jednego taska z Jiry

        Metoda nadzoruje proces pobrania danych z Jiry oraz wyświetlenia raportu w konsoli dla podanego taska z Jiry.

        :param task_url: Adres url taska
        :type task_url: str
        :param username: Nazwa użytkownika, logującego się do Jiry
        :type username: str
        :param password: Hasło logującego się użzytkownika
        :type password: str
        :return: ---
        :rtype: ---
        """
        print('Please wait... I\'m connecting to Jira...')
        jira_obj = jira.Jira()
        content = jira_obj.get_page_content(task_url, username, password)

        print('Please wait... I\'m gathering information about task...')
        estimated, remaining, logged = jira_obj.get_information_about_task(content)
        print(estimated, remaining, logged)

    # TODO: dodać poniższą funkcję do dokumentacji na górze klasy
    def show_current_budget_usage_in_console(self, epic_key_list: list, jira_url: str, username: str, password: str):
        """ Zastanowić się co ja chcę aby ta funkcja zrobiła -> budżet czy stosunek czasów planowanych, zalogowanych i
        tych co jeszcze zostały

        :param epic_key_list:
        :type epic_key_list:
        :param jira_url:
        :type jira_url:
        :param username:
        :type username:
        :param password:
        :type password:
        :return:
        :rtype:
        """
        raise NotImplementedError("Ta funkcja nie jest jeszcze gotowa")
