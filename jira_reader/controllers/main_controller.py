# TODO: dodać dokumentację klasy
from prettytable import PrettyTable

class MainController:

    def show_epics_report(self):
        table = PrettyTable()
        table.field_names = ["Nazwa", "Id", "Budżet", "Czas szacowany", "Czas zalogowany", "Czas pozostały",
                             "Bieżące użycie budżetu", "Szacunkowe wykorzystanie budżetu"]
        table.add_row(['nazwa', '1', 'bud', 'time szac', 'time zal', 'time poz', 'usage', 'estim usage'])
        return table.get_string()
