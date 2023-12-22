"""fonctions permettant de connaitre les fichiers et dossiers de l'environement
donne des listes"""
import os
import glob
from colorama import Fore, Style

class SingletonMeta(type):
    """utilisation du design pattern singleton."""
    _instances = {}

    def __call__(self, *args, **kwargs):
        """Crée une nouvelle instance de la classe si elle n'existe pas déjà."""
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]

class InformationsProjet(metaclass=SingletonMeta):
    """Classe pour obtenir des informations sur le projet."""

    repertoires_ignores = ['.git', '.vscode', '__pycache__', '__init__']

    def obtenir_info_projet(self):
        """Obtient le chemin du dossier du projet."""
        try:
            dossier_projet = os.path.dirname(__file__)
            return dossier_projet
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'obtention des informations du projet : ", e)

    def obtenir_repertoire_travail(self):
        """Obtient le répertoire de travail actuel."""
        try:
            repertoire_travail = os.getcwdb().decode('utf-8')
            return repertoire_travail
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'obtention du répertoire de travail : ", e)

    def obtenir_info_package(self):
        """Obtient le chemin et le nom du package."""
        try:
            chemin_package = os.path.dirname(os.path.abspath(__file__))
            nom_package = os.path.basename(chemin_package)
            return chemin_package, nom_package
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'obtention des informations du package : ", e)

    def obtenir_liste_repertoires(self):
        """Obtient la liste des répertoires."""
        try:
            liste_repertoires = glob.glob(os.path.dirname(__file__) + "/*.py")
            return liste_repertoires
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'obtention de la liste des répertoires : ", e)

    def obtenir_fichiers_repertoire(self):
        """Obtient la liste des fichiers dans le répertoire."""
        try:
            repertoire_courant = os.getcwd()
            noms_fichiers = []
            for chemin, _, fichiers_dans_repertoire in os.walk(repertoire_courant):
                if any(element in chemin for element in self.repertoires_ignores):
                    continue
                for nom_fichier in fichiers_dans_repertoire:
                    if not nom_fichier.startswith('.'):
                        if os.path.isfile(os.path.join(chemin, nom_fichier)):
                            noms_fichiers.append(nom_fichier)
            return noms_fichiers
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'obtention des fichiers dans le répertoire : ", e)


    # def obtenir_dossiers_repertoire_travail(self):
    #     """Obtient la liste des dossiers dans le répertoire de travail."""
    #     try:
    #         repertoire_travail = os.getcwd()
    #         dossiers = [nom for nom in os.listdir(repertoire_travail)
    #                     if os.path.isdir(os.path.join(repertoire_travail, nom))]
    #         return dossiers
    #     except Exception as e:
    #         print(Fore.RED + "Erreur lors de l'obtention des dossiers dans le répertoire de travail : ", e)
    def obtenir_dossiers_repertoire_travail(self):
        """Obtient la liste des dossiers dans le répertoire de travail."""
        try:
            repertoire_travail = os.getcwd()
            with os.scandir(repertoire_travail) as entries:
                dossiers = [entry.name for entry in entries if entry.is_dir()]
            return dossiers
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'obtention des dossiers dans le répertoire de travail : ", str(e))

    def obtenir_fichiers_python_sans_ext(self):
        """Obtient la liste des fichiers Python sans extension."""
        try:
            fichiers_python_sans_ext = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
            return fichiers_python_sans_ext
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'obtention des fichiers Python sans extension : ", str(e))

