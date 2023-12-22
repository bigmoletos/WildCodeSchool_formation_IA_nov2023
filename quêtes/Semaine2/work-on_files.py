# pylint: disable=unspecified-encoding
import glob
import os

# repertoire actuel
repertoire_actuel = os.getcwd()
print("repertoire_actuel:", repertoire_actuel)

# liste des repertoire du dossier
print("liste des fichiers")
print(glob.glob("*"))
print("liste des fichiers txt")
print(glob.glob("*.txt"))  # filtre les fichiers txt
print("liste des repertoires")
print(glob.glob(repertoire_actuel))

filenames = glob.glob("*.py")
d={}
print("liste des fichiers python", filenames)
# creation d'un dictionnaire avec les noms des fichiers du repertoire et en valeurs les données des fichiers
for file in filenames:
    with open(file) as f:
        d[file]=f.read().splitlines()

# lecture du contenu de tous les fichiers python de mon repertoire
for file in filenames:
    with open(file, 'r') as f:
        print(f.read())
    f.close()
#  G:\programmation\WildCodeSchool\Formation_IA_DATA_nov2023\quêtes\Semaine2>

with open("quêtes\Semaine2\data_population.txt", "r") as f:
    liste = f.read().splitlines()
    print(liste)

file="quêtes\Semaine2\data_population.txt"
liste2 = [line.strip() for line in open("quêtes\Semaine2\data_population.txt", "r") ]
liste = [line.strip() for line in open(file, "r")] if os.path.isfile("fichier.txt") else []




print('liste2', liste2)
print("variable: ", liste2)

with open(file, "r") as f:
    liste = f.read().splitlines()
    print(liste)

#  taille d'un tableau
import numpy as np
tableau=np.array([1,2,3])
print(tableau.size)
#  faire un tableau de 0 avec 3 lignes et 2 colonnes
tableau2=np.zeros((3,2))
#  faire un tableau de 1 avec 3 lignes et 2 colonnes
tableau3=np.ones((3,2))

#  faire un tableau de 7 avec 3 lignes et 2 colonnes
tableau4=np.full((3,2),7)

#############################################
