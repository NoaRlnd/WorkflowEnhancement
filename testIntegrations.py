import tkinter as tk
from tkinter import ttk, Menu

root = tk.Tk()
menubar = Menu(root)

root.title('Test')
root.config(menu=menubar)
root.geometry('700x300-30-15')
root.minsize(350,150)

# Zone d'affichage des chemins et associations
root.tree = ttk.Treeview(root, columns=("Chemin", "Fichiers"), show="headings")
root.tree.heading("Chemin", text="Chemin")
root.tree.heading("Fichiers", text="Fichiers associés")
root.tree.pack(expand=True, fill="both", padx=10, pady=10)

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()