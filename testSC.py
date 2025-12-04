import tkinter as tk
from tkinter import ttk, Menu
import os
from callbacks import ajouter_chemin, associer_fichiers, sauvegarder_json, charger_json

class SelecteurChemins(tk.Toplevel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Titre et dimensions
        self.title('Sélecteur de Chemins')
        self.geometry('900x600-30-15')
        self.minsize(400, 300)

        # Données en mémoire
        self.chemins = []
        self.associations = {}
        self.json_file = "associations.json"

        # Charger les données existantes
        self.associations = charger_json(self.json_file)
        self.chemins = list(self.associations.keys())

        # Menu principal
        menubar = Menu(self)
        self.config(menu=menubar)

        option_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Options", menu=option_menu, underline=0)
        option_menu.add_command(label="Ajouter un chemin", command=lambda: ajouter_chemin(self.chemins, self.associations, self.mettre_a_jour_tree))
        option_menu.add_command(label="Associer des fichiers", command=lambda: associer_fichiers(self.chemins, self.associations, self.mettre_a_jour_tree))
        option_menu.add_separator()
        option_menu.add_command(label='Sauvegarder', command=lambda: sauvegarder_json(self.associations, self.json_file))
        option_menu.add_command(label='Quitter', command=self.destroy)

        # Zone d'affichage des chemins et associations
        self.tree = ttk.Treeview(self, columns=("Chemin", "Fichiers"), show="headings")
        self.tree.heading("Chemin", text="Chemin")
        self.tree.heading("Fichiers", text="Fichiers associés")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # Remplir la vue avec les données existantes
        self.mettre_a_jour_tree()

        # DPI awareness pour Windows
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass

    def mettre_a_jour_tree(self):
        """Met à jour l'affichage du Treeview."""
        self.tree.delete(*self.tree.get_children())
        for chemin, fichiers in self.associations.items():
            fichiers_str = ", ".join([os.path.basename(f) for f in fichiers])
            self.tree.insert("", "end", values=(chemin, fichiers_str))