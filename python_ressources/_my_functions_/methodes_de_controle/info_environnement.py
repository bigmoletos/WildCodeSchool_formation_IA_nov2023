"""ce module fourni les informations concernant les respertoires et fichiers
"""
import os
import glob
import pprint

#  info sur l'environnement de travail
print("-"*50)
print("*"*50)
print("nom dossier du projet: ", os.path.dirname(__file__))

# Afficher le répertoire de travail actuel avec la path
print("*"*50)
repertoire_courant = os.getcwdb().decode('utf-8')
print("Répertoire de travail actuel :", repertoire_courant)
print("*"*50)

# liste de tous les fichiers avec les chemins complets
path_of_package = os.path.dirname(os.path.abspath(__file__))
# Nom du répertoire courant avec le path
name_of_package = os.path.basename(path_of_package)
# liste des dossiers avec chemin complet et extension
# eeeeeee
# def list_dirs(path): 
#     """ donne la liste des repertoires
# """
#     dossiers_a_exclure = [b'.git', b'.vscode', b'/.' ]
#     folders = []
#     for dirpath, dirnames in os.walk(path):
#         # dirnames[:] = any(element in chemin.encode('utf-8') for element in elements_a_verifier):
#         dirnames[:] = [d for d in dirnames if d not in dossiers_a_exclure]
#         folders.extend(os.path.join(dirpath, d) for d in dirnames)
#     return folders

# print("liste des dossiers ",list_dirs('.'))


# eeeeeeeee
liste_dir = glob.glob(os.path.dirname(__file__) + "/*.py")
print("liste dossiers :", liste_dir)
print("*"*50)
# Nom du répertoire courant avec path
print("Chemin du répertoire courant :", path_of_package)
# Nom du répertoire courant
print("*"*50)
print("Nom du répertoire courant :", name_of_package)
print("*"*50)
# Récupérer la liste de tous les fichiers dans le répertoire de travail actuel et ses sous-répertoires
# repertoire_courant = os.getcwdb()
# noms_fichiers = []
# for chemin, _, fichiers_dans_repertoire in os.walk(repertoire_courant):
#     # Ignorer les fichiers liés à Git, VS Code et les fichiers cachés
#     # chemin = chemin.decode('utf-8')
#     # print("chemin", chemin)
#     elements_a_verifier = [b'.git', b'.vscode', b'/.' ]
#     if any(element in chemin for element in elements_a_verifier):
#         continue
#     for nom_fichier in fichiers_dans_repertoire:
#         # Ignorer les fichiers cachés
#         if not nom_fichier.startswith(b'.'):
#             noms_fichiers.append(nom_fichier)

# noms_fichiers=[nom.decode('utf-8') for nom in noms_fichiers]
# print("Fichiers dans le répertoire de travail actuel et ses sous-répertoires :\n", len(noms_fichiers), noms_fichiers)

print("//"*50)
# Récupérer le répertoire de travail actuel
repertoire_courant = os.getcwd()

# Récupérer la liste de tous les noms de fichiers 
# dans le répertoire de travail actuel et ses sous-répertoires
noms_fichiers = []
for chemin, _, fichiers_dans_repertoire in os.walk(repertoire_courant):
    # Ignorer les fichiers liés à Git, VS Code et les fichiers cachés
    elements_a_verifier = [b'.git', b'.vscode', b'/.' ]
    if any(element in chemin.encode('utf-8') for element in elements_a_verifier):
        continue
    for nom_fichier in fichiers_dans_repertoire:
        # Ignorer les fichiers cachés
        if not nom_fichier.startswith('.'):
            # Ajouter seulement les fichiers (et non les répertoires)
            if os.path.isfile(os.path.join(chemin, nom_fichier)):
                noms_fichiers.append(nom_fichier)

# pprint.PrettyPrinter("Noms des fichiers dans le répertoire de travail actuel 
# et ses sous-répertoires 33 :\n",  len(noms_fichiers), noms_fichiers)
print("Noms des fichiers dans le répertoire de travail actuel et ses sous-répertoires 33 :\n", 
      noms_fichiers)
print("//"*50)



# Récupérer la liste de tous les dossiers dans le répertoire de travail actuel
dossiers = [nom for nom in os.listdir(repertoire_courant)
             if os.path.isdir(os.path.join(repertoire_courant, nom))]
# conversion en utf8 au lieu du format bytes
# dossiers = [nom.decode('utf-8') for nom in dossiers]
print("Dossiers dans le répertoire de travail actuel :", dossiers)

# liste des fichiers python du repertoire courant sans l'extension .py
list_python_files_without_ext = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
print("*"*50)
print("list_files without extension= ", list_python_files_without_ext)
print("*"*50)
# liste des fichiers python du repertoire courant avec l'extension .py
list_python_files_with_ext = [os.path.basename(
    f) for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
print("*"*50)
print("list_files with extension= ", list_python_files_with_ext)
print("*"*50)
# liste de tous les fichiers  repertoire courant
list_all_files_with_ext = [os.path.basename(
    f) for f in glob.glob(os.path.dirname(__file__) + "/*.*")]
print("*"*50)
print("list all files with extension= ", list_all_files_with_ext)
print("*"*50)


# Exclure spécifiquement le fichier '__init__'
list_python_files_without_ext.remove('__init__')

print("*"*50)
print("*##*"*25, "via fonction lister_fichiers(chemin, repertoires_ignores)","*#*"*25)
def lister_fichiers(chemin, repertoires_ignores):
    """
    Liste les fichiers dans un chemin donné, en ignorant certains répertoires spécifiques.
    
    Args:
        chemin (str): Le chemin du répertoire à analyser.
        repertoires_ignores (list): La liste des noms de répertoires à ignorer.
        
    Returns:
        list: La liste des noms de fichiers dans le chemin donné, sans les fichiers des répertoires ignorés.
    """
    noms_fichiers = []
    noms_dossiers = []
    # chemin_courant = []
    for chemin_courant, dossiers, fichiers in os.walk(chemin):
        dossiers[:] = [d for d in dossiers if d not in repertoires_ignores]
        noms_fichiers.extend(fichiers)
        noms_dossiers.extend(dossiers)
        # chemin_courant+=chemin_courant
        # chemin_courant.extend(chemin_courant)
    return  print("liste fichiers:\n", noms_fichiers, "taille: " ,len(noms_fichiers),
                  "\nliste dossiers: \n",noms_dossiers,"taille: " ,len(noms_dossiers),
                  "\nchemin_courant :", chemin_courant ,
                  "\n")

# Liste des répertoires à ignorer
repertoires_ignores = ['.git', '.vscode','__pycache__','__init__']
chemin_dossiers='.'
# Appel de la fonction
print(lister_fichiers(chemin_dossiers, repertoires_ignores))
print("*##*"*25, "via fonction lister_fichier ","*#*"*25)
print("-"*50)
