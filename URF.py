# Utilitaire de Redirection de Fichiers (URF). Permet de selectionner des chemins et de déplacer des fichiers dans les chemins spécifiés.
# Tout en permettant de les dupliquer et avec plusieurs extensions de fichiers pris en comptes.
# c'est une application destinée à un groupe d'utilisateurs macOS
# dictionnaire de termes --> URF : Utilitaire de Redirection de Fichiers / SC : Selecteur de Chemins / SEF : Selecteur d'Extension de Fichier
import tkinter as tk
from tkinter import ttk, Menu
from SC import SelecteurChemins

root = tk.Tk()
menubar = Menu(root)

root.title('Utilitaire de Redirection de Fichiers')
root.config(menu=menubar)
root.geometry('700x300-30-15')
root.minsize(350,150)

# fonctions d'appel de création de fenêtres secondaires
sc_window = SelecteurChemins(root)
sc_window.withdraw()

option_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Options", menu=option_menu, underline=0)
option_menu.add_command(label='Quitter', command=root.destroy)

file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Fichier", menu=file_menu, underline=0)
file_menu.add_command(label="Chemins", command=sc_window.deiconify, underline=0)

# pour afficher correctement sur W et macOS
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()