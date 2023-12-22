"""enregistre des données txt dans un fichier au format
 pdf, xml, xlsx, json, csv ou html dans le repertoire "datas" 
 en créant un doissier portant le nom de l'extension du fichier"""
import os
import csv
import json
from dicttoxml import dicttoxml
from fpdf import FPDF
import pandas as pd
import openpyxl


class SingletonMeta(type):
    """Métaclasse pour le modèle Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Crée une nouvelle instance de la classe si elle n'existe pas déjà."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class EnregistreurFichier(metaclass=SingletonMeta):
    """Classe pour l'enregistrement des données dans un fichier."""

    def __init__(self, repertoire, nom_fichier, donnees, extension):
        """Initialise l'enregistreur avec le répertoire, le nom du fichier, les données et l'extension."""
        self.chemin = os.path.join(repertoire, f"{nom_fichier}.{extension}")
        self.donnees = donnees
        self.repertoire = repertoire
        self.extension = extension

    def enregistrer(self):
        """Enregistre les données dans un fichier."""
        sous_repertoire = os.path.join(self.repertoire, self.extension)
        os.makedirs(sous_repertoire, exist_ok=True)
        chemin_complet = os.path.join(sous_repertoire, os.path.basename(self.chemin))

        if self.extension == 'txt':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                for cle, valeur in self.donnees.items():
                    f.write(f"{cle}: {valeur}\n")
        elif self.extension == 'csv':
            with open(chemin_complet, 'w', newline='', encoding='utf-8') as f:
                ecrivain = csv.writer(f)
                ecrivain.writerow(self.donnees.keys())
                ecrivain.writerow(self.donnees.values())
        elif self.extension == 'json':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                json.dump(self.donnees, f, ensure_ascii=False)
        elif self.extension == 'xml':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                f.write(dicttoxml(self.donnees).decode())
        elif self.extension == 'xlsx':
            df = pd.DataFrame([self.donnees])
            df.to_excel(chemin_complet, index=False)
        elif self.extension == 'pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for i, (cle, val) in enumerate(self.donnees.items()):
                pdf.cell(200, 10, txt=f"{cle}: {val}", ln=i+1, align='C')
            pdf.output(chemin_complet)
        elif self.extension == 'html':
            df = pd.DataFrame([self.donnees])
            df.to_html(chemin_complet)


# teste la méthode en  lui passant des données txt
def test_enregistreur():
    """Teste la classe EnregistreurFichier."""
    repertoire = "datas"
    extension = "html"
    nom_fichier = "test_enregistrement2"
    donnees = {
        "Nom": "Dupont",
        "Prénom": "Marcel",
        "Adresse": "12 avenue du roi vert 56212 Montvers",
        "Âge": "23 ans",
        "Téléphone": "06 08 52 36 24",
        "Email": "dupont@free.fr",
        "Répertoire par défaut": r"G:\programmation\python\openClassRoomModulePython\datas",
        "Nom de fichier": "test_enregistrement-27-10-23"
    }

    enregistreur = EnregistreurFichier(repertoire, nom_fichier, donnees, extension)
    enregistreur.enregistrer()


if __name__ == "__main__":
    test_enregistreur()
