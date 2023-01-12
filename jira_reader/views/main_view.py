# Standard import library
import tkinter as tk
# Local imports
from jira_reader.controllers.main_controller import MainController


# TODO: dodać dokumentację klasy
class MainView:
    def __init__(self):
        self._controller: MainController = None
        self._create_root_window()

    def _create_root_window(self):
        """
        W oknie jest grid 3x2.
        Wiersz 1 - widget z raportem o epikach
        Wiersz 2 - przyciski
        Wiersz 3 - pasek statusu
        W pionie resizowany jest wiersz 1. Wiersz 2 i 3 trzymają się dołu i nie zmieniają swojego rozmiaru w pionie
        :return:
        :rtype:
        """
        self._root = tk.Tk()
        self._root.title('Jira Reader')
        self._root.minsize(800, 600)

        # Konfiguracja grida
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure([0, 1], weight=1)

        # Raport o epikach
        self._txt_report = tk.Text(master=self._root)
        self._txt_report.grid(row=0, column=0, columnspan=2, sticky='nswe', pady=(5, 0), padx=2)

        # Przyciski
        self._btn_show_epics_report = tk.Button(master=self._root, text='Pokaż raport o epikach')
        self._btn_show_epics_report.grid(row=1, column=0, pady=(5, 0))

        self._btn_exit = tk.Button(master=self._root, text='Zakończ')
        self._btn_exit.grid(row=1, column=1, pady=(5, 0))

        # ##### Pasek statusu #####
        # Do komórki grida została dodana ramka w celu umożliwienia dodania kilku labeli. Ramka ma ustawiony pady tylko
        # od górnej krawędzi.
        frame_status_bar = tk.Frame(master=self._root)
        frame_status_bar.grid(row=2, column=0, columnspan=2,  sticky='we', pady=(10, 0))

        # Label z numerem wersji programu
        self._lbl_status_version = tk.Label(master=frame_status_bar, text='wersja', relief=tk.SUNKEN)
        self._lbl_status_version.pack(side='right', ipadx=5)

        # Label z informacjami o autorze
        self._lbl_status_author = tk.Label(master=frame_status_bar, text='autor', relief=tk.SUNKEN)
        self._lbl_status_author.pack(side='right', ipadx=5)

        # Label z informacjami o operacjach wykonywanych przez program. Label ten posiada możliwość resize-u
        self._lbl_status_info = tk.Label(master=frame_status_bar, text='status programu - operacje', anchor='w', relief=tk.SUNKEN)
        self._lbl_status_info.pack(side='left', fill=tk.BOTH, expand=tk.TRUE)

    def set_controller(self, controller: MainController):
        self._controller = controller

    def run(self):
        self._root.mainloop()