# dictionnaire de termes --> URF : Utilitaire de Redirection de Fichiers / SC : Selecteur de Chemins / SEF : Selecteur d'Extension de Fichier
import tkinter as tk
from tkinter import ttk, Menu
from callbacks import select_files
from tkinter import filedialog as fd # apparement c'est pour les selections de fichiers
from SEF import SelecteurExtensionFichier

class SelecteurChemins(tk.Toplevel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        menubar = Menu(self)

        self.title('Selecteur de Chemins')
        self.config(menu=menubar)

        self.geometry('900x600-30-15')
        self.minsize(400,300)

        sef_window = SelecteurExtensionFichier(self)
        sef_window.withdraw()

        option_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Options", menu=option_menu, underline=0)
        option_menu.add_command(label="Ajouter un chemin", command=select_files, underline=0)     # ça redirigerai vers l'explo de fichier, sinon, vers le finder (idéalement mdr)
        option_menu.add_separator()                                                  
        option_menu.add_command(label='Quitter', command=self.destroy)

        # pour afficher correctement sur W et macOS
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass