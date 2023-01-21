# TODO: dodać dokumentację klasy
from prettytable import PrettyTable
import jira_reader


class MainController:

    @staticmethod
    def load_program_metadata() -> []:
        name = jira_reader.__program_name__
        version = jira_reader.__version__
        author = jira_reader.__author__
        wiki = jira_reader.__wiki__
        return [name, version, author, wiki]

    def show_epics_report(self):
        table = PrettyTable()
        table.field_names = ["Nazwa", "Id", "Budżet", "Czas szacowany", "Czas zalogowany", "Czas pozostały",
                             "Bieżące użycie budżetu", "Szacunkowe wykorzystanie budżetu"]
        table.add_row(['nazwa', '1', 'bud', 'time szac', 'time zal', 'time poz', 'usage', 'estim usage'])
        return table.get_string()
