# __init__.py
import os
import glob

# Importer les classes du module ici
# from .methodes_de_controle import *

# Définir __all__ pour spécifier les modules à importer lors de l'importation *
# __all__ = ['controle_saisie_nom_fichier', 'controle_saisie_url', '_my_traitement_date_']


#  import de tous les modules et toutes les fonctions de ce dossier

list_files = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
# list_files = [os.path.basename(f)[:-3] for f in (path_of_package + "/*.py")]

# Exclure spécifiquement '__init__'
list_files.remove('__init__')
__all__ = list_files

# print("*"*50)
# print("all= ",__all__)
# print("*"*50)
# print("-"*50)
