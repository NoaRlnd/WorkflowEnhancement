
# dictionnaire de termes --> URF : Utilitaire de Redirection de Fichiers / SC : Selecteur de Chemins / SEF : Selecteur d'Extension de Fichier
import tkinter as tk
from tkinter import ttk, Menu, filedialog, messagebox
import json
import os

class SelecteurChemins(tk.Toplevel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Titre et dimensions
        self.title('Sélecteur de Chemins')
        self.geometry('900x600-30-15')
        self.minsize(400, 300)

        # Données en mémoire
        self.chemins = []  # Liste des chemins sélectionnés
        self.associations = {}  # Dictionnaire {chemin: [fichiers]}
        self.json_file = "associations.json"

        # Charger les données si elles existent
        self.charger()

        # Menu principal
        menubar = Menu(self)
        self.config(menu=menubar)

        option_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Options", menu=option_menu, underline=0)
        option_menu.add_command(label="Ajouter un chemin", command=self.ajouter_chemin)
        option_menu.add_command(label="Associer des fichiers", command=self.associer_fichiers)
        option_menu.add_separator()
        option_menu.add_command(label='Sauvegarder', command=self.sauvegarder)
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

    # Ajouter un chemin
    def ajouter_chemin(self):
        chemin = filedialog.askdirectory(title="Sélectionner un dossier")
        if chemin:
            if chemin not in self.chemins:
                self.chemins.append(chemin)
                self.associations[chemin] = []
                self.mettre_a_jour_tree()
            else:
                messagebox.showinfo("Info", "Ce chemin est déjà ajouté.")

    # Associer des fichiers à un chemin
    def associer_fichiers(self):
        if not self.chemins:
            messagebox.showwarning("Attention", "Ajoutez d'abord un chemin.")
            return

        # Choisir le chemin cible
        chemin_cible = self.selectionner_chemin()
        if not chemin_cible:
            return

        # Sélectionner les fichiers
        filetypes = (('Tous les fichiers', '*.*'),)
        fichiers = filedialog.askopenfilenames(title="Sélectionner des fichiers", filetypes=filetypes)
        if fichiers:
            self.associations[chemin_cible].extend(fichiers)
            self.mettre_a_jour_tree()

    # Fenêtre pour choisir un chemin existant
    def selectionner_chemin(self):
        choix = tk.simpledialog.askstring("Chemin cible", f"Chemins disponibles :\n{chr(10).join(self.chemins)}\n\nEntrez le chemin exact :")
        if choix in self.chemins:
            return choix
        else:
            messagebox.showerror("Erreur", "Chemin invalide.")
            return None

    # Mettre à jour l'affichage
    def mettre_a_jour_tree(self):
        self.tree.delete(*self.tree.get_children())
        for chemin, fichiers in self.associations.items():
            fichiers_str = ", ".join([os.path.basename(f) for f in fichiers])
            self.tree.insert("", "end", values=(chemin, fichiers_str))

    # Sauvegarder en JSON
    def sauvegarder(self):
        with open(self.json_file, "w", encoding="utf-8") as f:
            json.dump(self.associations, f, indent=4)
        messagebox.showinfo("Sauvegarde", "Données sauvegardées avec succès.")

    # Charger depuis JSON
    def charger(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as f:
                self.associations = json.load(f)
            self.chemins = list(self.associations.keys())