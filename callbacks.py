import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def button_clicked():
    print("ton niveau est catastrophique")

def select_files():
    filetypes = (('fichier texte', '*txt'), ('tout fichier', '*.*'))                                # confirmer avec la comm les types de fichiers concernés
    filenames = fd.askopenfilenames(title='ouvrir un fichier', initialdir='/', filetypes=filetypes)
    showinfo(title='fichier selectionné', message=filenames)


def ajouter_chemin(self):
    chemin = fd.askdirectory(title="Sélectionner un dossier")
    if chemin:
        self.chemins.append(chemin)
        print(f"Chemin ajouté : {chemin}")