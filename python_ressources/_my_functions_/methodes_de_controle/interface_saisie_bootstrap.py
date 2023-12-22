import os
import tkinter as tk
from tkinter import messagebox, filedialog
from ttkbootstrap import Style as ttkb
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from datetime import datetime
import csv
import json
import pandas as pd
from dicttoxml import dicttoxml
from fpdf import FPDF
"""classe permettant d'enregistrer"""


class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        """Crée une nouvelle instance de la classe si elle n'existe pas déjà."""
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class EnregistreurFichier:
    """Classe pour l'enregistrement des données dans un fichier."""

    def __init__(self, repertoire, nom_fichier, donnees):
        self.chemin = os.path.join(repertoire, nom_fichier)
        self.donnees = donnees
        self.repertoire=repertoire

    def enregistrer(self):
        """Enregistre les données dans un fichier."""
        extension = os.path.splitext(self.chemin)[1]
        sous_repertoire = os.path.join(self.repertoire, extension.lstrip('.'))
        os.makedirs(sous_repertoire, exist_ok=True)
        chemin_complet = os.path.join(sous_repertoire, os.path.basename(self.chemin))


        if extension == 'txt':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                for cle, valeur in self.donnees.items():
                    f.write(f"{cle}: {valeur}\n")
        elif extension == 'csv':
            with open(chemin_complet, 'w', newline='', encoding='utf-8') as f:
                ecrivain = csv.writer(f)
                ecrivain.writerow(self.donnees.keys())
                ecrivain.writerow(self.donnees.values())
        elif extension == 'json':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                json.dump(self.donnees, f, ensure_ascii=False)
        elif extension == 'xml':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                f.write(dicttoxml(self.donnees).decode())
        elif extension == 'xlsx':
            df = pd.DataFrame([self.donnees])
            df.to_excel(chemin_complet, index=False)
        elif extension == 'pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for i, (cle, val) in enumerate(self.donnees.items()):
                pdf.cell(200, 10, txt=f"{cle}: {val}", ln=i+1, align='C')
            pdf.output(chemin_complet)
        elif extension == 'html':
            df = pd.DataFrame([self.donnees])
            df.to_html(chemin_complet)    

class Application(tk.Tk, metaclass=SingletonMeta):
    """Application pour la saisie des informations."""

    def __init__(self):
        super().__init__()
        self.title("Saisie des informations")
        # self.style = ttk.Style(theme='cyborg')
        # self.style = Style(theme='superhero')
        # self.style = ttkb(theme='superhero')
        self.style = ttkb(theme='darkly')
        self.style.theme_use()
        fenetre_style = self.style.master

        # Centrer la fenêtre et ajouter des marges
        self.geometry("500x850")
        self.configure(bg='white')
        self.pack_propagate(False)

        # Créer un cadre pour contenir tous les widgets
        cadre = tk.Frame(self, bg='white', padx=20, pady=10)
        cadre.pack(fill='both', expand=True)

        # Créer les champs de saisie avec les valeurs par défaut
        self.champs = ['Nom', 'Prénom', 'Adresse', 'Âge', 'Téléphone', 'Email', 'Répertoire par défaut',
                       'Nom de fichier']
        valeurs_par_defaut = ['Dupont', 'Marcel', '12 avenue du roi vert 56212 Montvers', '23 ans',
                              '06 08 52 36 24', 'dupont@free.fr', 'G:\programmation\python\openClassRoomModulePython\datas', f'test_enregistrement-{datetime.now().strftime("%d-%m-%y")}']
        self.entries = {}

        for champ, valeur_par_defaut in zip(self.champs, valeurs_par_defaut):
            frame = tk.Frame(cadre, bg='white')
            # Ajouter une marge verticale entre les champs
            frame.pack(fill='x', pady=10)
            label = tk.Label(frame, text=champ, bg='white')
            label.pack(side='left')
            entry = tk.Entry(frame)
            # Ajouter une valeur par défaut à chaque champ de saisie
            entry.insert(0, valeur_par_defaut)
            entry.pack(side='right', fill='x', expand=True)
            self.entries[champ] = entry

        # default separator style
        separateur=ttk.Separator(cadre,orient='horizontal',bootstyle="info")
        # info colored separator style - handle color
        separateur.pack(fill='x')
        # Créer la liste déroulante pour les extensions à exclure
        frame_extensions_a_exclure = tk.Frame(cadre, bg='white')
        frame_extensions_a_exclure.pack(fill='x',padx=20, pady=10)
        label_extensions_a_exclure = tk.Label(
            frame_extensions_a_exclure, text="Extensions à exclure", bg='white')
        label_extensions_a_exclure.pack(side='left')

        liste_extensions_a_exclure=['.txt', '.py', '.csv', '.xml', '.json', '.xlsx', '.html','.pdf']
        max_length = max(len(extensions_a_exclure) for extensions_a_exclure in liste_extensions_a_exclure)+2
        self.extensions_a_exclure = tk.Listbox(
            frame_extensions_a_exclure, selectmode='multiple', height=len(liste_extensions_a_exclure), width=max_length)
        for item in liste_extensions_a_exclure:
            self.extensions_a_exclure.insert('end', item)
        self.extensions_a_exclure.pack(side='right', fill=None, expand=False)

        # default separator style
        separateur=ttk.Separator(cadre,orient='horizontal',bootstyle="info")
        # info colored separator style - handle color
        separateur.pack(fill='x')

        # # Créer la liste déroulante pour le format du fichier à enregistrer
        # frame_format_fichier = tk.Frame(cadre, bg='white')
        # frame_format_fichier.pack(fill='x',padx=10, pady=10)
        # label_format_fichier = tk.Label(
        #     frame_format_fichier, text="Format du fichier", bg='white')
        # label_format_fichier.pack(side='left')
        # self.format_fichier_var = tk.StringVar()
        # liste_deroulante_format_fichier = tk.OptionMenu(frame_format_fichier, self.format_fichier_var,
        #                                                 '.txt', '.py', '.csv', '.xml',  '.html','.json', '.pdf', '.xlsx')
        # # Définir la largeur de la liste déroulante
        # liste_deroulante_format_fichier.config(width=20, height=50)
        # liste_deroulante_format_fichier.pack(
        #     side='left', fill=None, expand=False)
        # Créez un cadre pour la liste
        frame_format_fichier = tk.Frame(cadre, bg='white')
        frame_format_fichier.pack(fill='x', padx=10, pady=10)

        # Créez un label pour la liste
        label_format_fichier = tk.Label(frame_format_fichier, text="Format du fichier", bg='white')
        label_format_fichier.pack(side='left')

        # Créez une Listbox pour les formats de fichiers, au passage pour eviter d'avoir les lignes vides 
        # à la fin on limite le height au nombre d'entrées dans la liste
        formats_fichier = ['.txt', '.py', '.csv', '.xml',  '.html','.json', '.pdf', '.xlsx']
        # Obtenez la longueur de l'élément le plus long dans la liste pour limiter la taille de la fenetre
        max_length = max(len(format_fichier) for format_fichier in formats_fichier)+2
        # Créez une Listbox pour les formats de fichiers avec une hauteur égale au nombre d'éléments dans la liste
        liste_formats_fichier = tk.Listbox(frame_format_fichier, height=len(formats_fichier), width=max_length)
        liste_formats_fichier.pack(side='left', fill='both', expand=False)

        for format_fichier in formats_fichier:
            liste_formats_fichier.insert(tk.END, format_fichier)

        # default separator style
        separateur=ttk.Separator(cadre,orient='horizontal',bootstyle="info")
        # info colored separator style - handle color
        separateur.pack(fill='x')

        # Créer la checkbox pour les conditions contractuelles
        self.conditions_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(cadre, text="J'accepte les conditions contractuelles", variable=self.conditions_var,
                                  bg='white')
        checkbox.pack()
        # default separator style
        separateur=ttk.Separator(cadre,orient='horizontal',bootstyle="info")
        # info colored separator style - handle color
        separateur.pack(fill='x')
        # Créer les boutons OK et Annuler
        # # default style
        ttk.Button()
        # # Créez un cadre principal
        # voir plus haut la defintition du cadre
        # cadre = tk.Frame(bg='white')

        # # success style
        # Créez un cadre pour les boutons
        fenetre_style = tk.Frame(cadre, bg='red')
        # Créez un bouton OK dans le cadre des boutons
        bouton_succes=ttk.Button(fenetre_style, text="OK", command=self.valider, style=SUCCESS )
        bouton_succes.pack(side=LEFT,padx=10, pady=10)
        # Créez un bouton CANCEL dans le cadre des boutons
        bouton_cancel=ttk.Button(fenetre_style, text="ANNULER",command=self.annuler, style=DANGER )
        bouton_cancel.pack(side=RIGHT,padx=10, pady=10)
        # Ajoutez le cadre du style au cadre principal
        fenetre_style.pack(fill='x', pady=10)

        # frame_boutons = tk.Frame(cadre, bg='white')
        # frame_boutons.pack(fill='x', pady=10)

        # Ajoutez le cadre du style au cadre principal
        # fenetre_style.pack()

        # Affichez le cadre principal
        # cadre.pack()

        # bouton_ok = tk.Button(frame_boutons, text="OK", command=self.valider, bg='red')
        # bouton_ok.pack(side='left')
        # bouton_annuler = tk.Button(
        #     frame_boutons, text="Annuler", command=self.annuler, bg='orange')
        # bouton_annuler.pack(side='right')


#
    def valider(self):
        """Valide les entrées de l'utilisateur."""
        if not self.conditions_var.get():
            messagebox.showerror(
                "Erreur", "Vous devez accepter les conditions contractuelles.")
            return
        for champ, entry in self.entries.items():
            if not entry.get():
                messagebox.showerror("Erreur", f"Le champ {
                                     champ} est obligatoire.")
                return
        # Convertir les données en un dictionnaire
        donnees = {champ: entry.get() for champ, entry in self.entries.items()}
        # Enregistrer les données dans un fichier
        repertoire = self.entries['Répertoire par défaut'].get()
        nom_fichier = self.entries['Nom de fichier'].get(
        ) + self.format_fichier_var.get()
        enregistreur = EnregistreurFichier(repertoire, nom_fichier, donnees)
        enregistreur.enregistrer()
        messagebox.showinfo(
            "Succès", "Les données ont été enregistrées avec succès.")
        self.destroy()  # Fermer la fenêtre après l'enregistrement des données

    def annuler(self):
        """Annule les entrées de l'utilisateur et ferme la fenêtre."""
        self.destroy()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
