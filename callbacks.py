from tkinter import filedialog, messagebox, simpledialog
import json
import os

def ajouter_chemin(chemins, associations, update_callback):
    """Ajoute un chemin sélectionné par l'utilisateur."""
    chemin = filedialog.askdirectory(title="Sélectionner un dossier")
    if chemin:
        if chemin not in chemins:
            chemins.append(chemin) # met le chemin dans la liste des chemins
            associations[chemin] = [] # ajoute une entrée vide dans associations
            update_callback() # ça lance mettre_a_jour_tree()
        else:
            messagebox.showinfo("Info", "Ce chemin est déjà ajouté.")

def associer_fichiers(chemins, associations, update_callback):
    """Associe des fichiers à un chemin existant."""
    if not chemins:
        messagebox.showwarning("Attention", "Ajoutez d'abord un chemin.")
        return

    choix = simpledialog.askstring("Chemin cible", f"Chemins disponibles:\n{chr(10).join(chemins)}")
    if choix in chemins:
        fichiers = filedialog.askopenfilenames(title="Sélectionner des fichiers")
        if fichiers:
            associations[choix].extend(fichiers)
            update_callback()
    else:
        messagebox.showerror("Erreur", "Chemin invalide.")

def sauvegarder_json(data, filepath):
    """Sauvegarde les associations dans un fichier JSON."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    messagebox.showinfo("Sauvegarde", "Données sauvegardées avec succès.")

def charger_json(filepath):
    """Charge les associations depuis un fichier JSON."""
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}