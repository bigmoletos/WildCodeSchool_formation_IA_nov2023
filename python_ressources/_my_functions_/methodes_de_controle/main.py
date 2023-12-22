from fonction_dossiers_fichiers import InformationsProjet
"""
donne les listes des fichiers et repertertoires avec ou sans extension
"""


def main():
    """fonction prioncipale permettant le lancement de la fonction "InformationsProjet()" de la classe
      G:\programmation\python\openClassRoomModulePython\_my_functions_\methodes_de_controle\fonction_dossiers_fichiers.py 
      """
    # Créer une instance de la classe InformationsProjet
    info_projet = InformationsProjet()

    # Tester toutes les fonctions
    print("**** Informations du nom du projet : ", info_projet.obtenir_info_projet())
    print("**** Répertoire de travail : ", info_projet.obtenir_repertoire_travail())
    print("**** Informations du package : ", info_projet.obtenir_info_package())
    print("**** Liste des répertoires : ", info_projet.obtenir_liste_repertoires())
    print("**** Fichiers dans le répertoire : ", info_projet.obtenir_fichiers_repertoire())
    print("**** Dossiers dans le répertoire de travail : ", info_projet.obtenir_dossiers_repertoire_travail())
    print("**** Fichiers Python sans extension : ", info_projet.obtenir_fichiers_python_sans_ext())

if __name__ == "__main__":
    main()