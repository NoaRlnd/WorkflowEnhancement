# dictionnaire de termes --> URF : Utilitaire de Redirection de Fichiers / SC : Selecteur de Chemins / SEF : Selecteur d'Extension de Fichier
import tkinter as tk
from tkinter import ttk, Menu

class SelecteurExtensionFichier(tk.Toplevel):
    def __init__(self):
        super().__init__()

        menubar = Menu(self)

        self.title('Selecteur Extension de Fichier')
        self.config(menu=menubar)

        self.geometry('1000x1300-30-15')
        self.minsize(400,300)

        option_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Options", menu=option_menu, underline=0)
        option_menu.add_command(label='Quitter', command=self.destroy)

        # pour afficher correctement sur W et macOS
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            self.mainloop()