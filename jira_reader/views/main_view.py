# Standard import library
import tkinter as tk
# Local imports
from jira_reader.controllers.main_controller import MainController


class MainView:
    """
    Klasa odpowiada za wygląd i zachowanie głównego okna programu.

    Atrybuty:
    ---------

    Metody:
    -------
    - __init__(self):
        Inicjalizacja klasy
    - def _create_root_window(self):
        Metoda tworzy widżety w głównym oknie programu
    - def _grid_configure(self):
        Metoda konfiguruje grid w oknie
    - _create_report_area(self):
        Metoda tworzy kontrolki do wyświetlenia raportu o epikach
    - _create_buttons(self):
        Metoda tworzy przyciski
    - _create_status_bar(self):
        Metoda tworzy pasek statusu
    - set_controller(self, controller: MainController):
        Metoda ustawia kontroler dla tego okna programu
    - run(self):
        Metoda uruchamia główną pętlę programu
    """
    def __init__(self):
        """ Inicjalizacja klasy

        Metoda tworzy główne okno programu oraz ustawia początkowe wartości zmiennych.
        """
        self._controller: MainController = None
        self._create_root_window()

    def _create_root_window(self):
        """ Metoda tworzy widżety w głównym oknie programu
        """
        self._root = tk.Tk()
        self._root.title('Jira Reader')
        self._root.minsize(800, 600)

        self._grid_configure()
        self._create_report_area()
        self._create_buttons()
        self._create_status_bar()

    def _grid_configure(self):
        """ Metoda konfiguruje grid w oknie

        W oknie jest grid 3x2.
        Wiersz 1 - widget z raportem o epikach
        Wiersz 2 - przyciski
        Wiersz 3 - pasek statusu
        W pionie resizowany jest wiersz 1. Wiersz 2 i 3 trzymają się dołu i nie zmieniają swojego rozmiaru w pionie
        """
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure([0, 1], weight=1)

    def _create_report_area(self):
        """ Metoda tworzy kontrolki do wyświetlenia raportu o epikach
        """
        self._txt_report = tk.Text(master=self._root)
        self._txt_report.grid(row=0, column=0, columnspan=2, sticky='nswe', pady=(5, 0), padx=2)

    def _create_buttons(self):
        """ Metoda tworzy przyciski

        Do komórki grida została dodana ramka w celu umożliwienia dodania kilku przycisków. Ramka ma ustawiony pady
        tylko od górnej krawędzi.
        """
        # Ramka
        frame_buttons = tk.Frame(master=self._root)
        frame_buttons.grid(row=1, column=0, columnspan=2, sticky='we', pady=(5, 0))

        # Przycisk 'Zakończ'
        self._btn_exit = tk.Button(master=frame_buttons, text='Zakończ')
        self._btn_exit.pack(side='right', padx=5)

        # Przycisk 'Pokaż raport o epikach'
        self._btn_show_epics_report = tk.Button(master=frame_buttons, text='Pokaż raport o epikach')
        self._btn_show_epics_report.pack(side='right')

    def _create_status_bar(self):
        """ Metoda tworzy pasek statusu

        Do komórki grida została dodana ramka w celu umożliwienia dodania kilku labeli. Ramka ma ustawiony pady tylko
        od górnej krawędzi.
        """
        # Ramka
        frame_status_bar = tk.Frame(master=self._root)
        frame_status_bar.grid(row=2, column=0, columnspan=2, sticky='we', pady=(10, 0))

        # Label z numerem wersji programu
        self._lbl_status_version = tk.Label(master=frame_status_bar, text='wersja', relief=tk.SUNKEN)
        self._lbl_status_version.pack(side='right', ipadx=5)

        # Label z informacjami o autorze
        self._lbl_status_author = tk.Label(master=frame_status_bar, text='autor', relief=tk.SUNKEN)
        self._lbl_status_author.pack(side='right', ipadx=5)

        # Label z informacjami o operacjach wykonywanych przez program. Label ten posiada możliwość resize-u
        self._lbl_status_info = tk.Label(master=frame_status_bar, text='status programu - operacje', anchor='w',
                                         relief=tk.SUNKEN)
        self._lbl_status_info.pack(side='left', fill=tk.BOTH, expand=tk.TRUE)

    def set_controller(self, controller: MainController):
        """ Metoda ustawia kontroler dla tego okna programu

        :param controller: Kontroler okna
        :type controller:  jira_reader.controllers.main_controller.MainController
        """
        self._controller = controller

    def run(self):
        """ Metoda uruchamia główną pętlę programu
        """
        self._root.mainloop()
