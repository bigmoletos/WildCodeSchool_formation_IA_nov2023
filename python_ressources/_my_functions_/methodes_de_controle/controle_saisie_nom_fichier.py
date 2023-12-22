"""controle de saisie d'un nom de fichier"""
import re
from colorama import Fore, Style


def controle_saisie_fichier_de_sortie():
    """controle de la saisie du fichier de sortie afin d'avoir un nom:
    sans caractéres spéciaux
    espace au début ni à la fin
    remplacer les autres espaces par ds _
    et le nom doit commencer par une lettre"""
    while True:
        try:
            menu="""
                    Veuillez entrer le nom du fichier de sortie :
                    -sans espace ni au début ni à la fin
                    -le nom  doit commencer par une lettre
                    -caractéres speciaux interdits
                    entrez le nom: 
                """
            nom_fichier = input(menu)
            print(nom_fichier)
            # Supprimer tous les caractères spéciaux +-*/\.=#()[]{}
            nom_fichier = re.sub('[\\\+\-\*\/\.\=\(\)\{\}\[\]#]+','', nom_fichier)
            # print("2supp caract speciaux ", nom_fichier)

            # Supprimer tous les caractères qui ne sont pas des lettres min ou maj, des chiffres, des espaces ou des _
            nom_fichier = re.sub('[^A-Za-z0-9 _]+', '', nom_fichier)
            # print("1supp caract ", nom_fichier)

            
            # Supprimer les espaces de début et de fin
            nom_fichier = nom_fichier.strip()
            # print("3supp espaces début et fin", nom_fichier)

            # Supprime les _ au début du nom
            nom_fichier = nom_fichier.lstrip("_")
            # print("4supp les _ du début du fichier", nom_fichier)

            # Remplacer les autres espaces par un _
            nom_fichier = nom_fichier.replace(' ', '_').strip().lstrip("_")
            # print("5remplace les autres espaces par _", nom_fichier)

            # mettre le nom en minuscules 
            nom_fichier=nom_fichier.lower()
            # print("6nom final en minuscules", nom_fichier)

            # Vérifier si le nom du fichier commence par une lettre
            if not nom_fichier[0].isalpha() :
                raise ValueError("Le nom du fichier doit commencer par une lettre.")

            return nom_fichier
        #  traitement des erreurs
        except (Exception , ValueError) as e:
                # affiche en rouge le message d'erreur
                print(Fore.RED,"Une erreur inattendue s'est produite. Le nom ne doit pas commencer par un chiffre. Veuillez réessayer: ",e)
                print(Style.RESET_ALL)
                # menu pour proposer au user de stopper son programme
                error_message="""Voulez-vous arrêter le programme ? 
                si oui tapez O (oui) ou Y (yes) pour arrêter ou toute autre touche pour continuer :"""
                stop_program = input(error_message)
                if stop_program.lower() == 'o'or stop_program.lower() == 'y':
                    break
       
        # dans tous les cas donner le nom du fichier
        finally:
             print("nom de votre fichier: ",nom_fichier)

# nom_fichier=input("saisir nom de fichier")
# controle_saisie_fichier_de_sortie()