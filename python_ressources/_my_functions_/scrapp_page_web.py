import requests
import csv, json
from bs4 import BeautifulSoup
from colorama import Fore, Style
# from methodes_de_controle import controle_saisie_nom_fichier, controle_saisie_url
from methodes_de_controle.controle_saisie_url import controle_saisie_url
from methodes_de_controle.controle_saisie_nom_fichier import controle_saisie_fichier_de_sortie


def scrapp_page_web():
    """ copie le contenu d'une page web et le copie dans un fichier output.html
    idealemenent il faudrait pourvoir choisir la sortie du fichier 
    par ex en txt, json ou csvscra

    """
    while True:
        try:
            my_extension_fichier=''
            # choix type du type fichier
            menu_input="""
Veuillez choisir le format de sortie du fichier.
#1 pour une sortie .html
#2 pour une sortie .txt
#3 pour une sortie .csv
#4 pour une sortie .json
tapez votre choix:    """
            my_choice_type_fichier=input(menu_input)

            # Demander à l'utilisateur l'URL de la page web à scraper
            url=controle_saisie_url()

            # url = input("Veuillez entrer l'URL de la page web à scraper (par défaut https://www.google.com) : ")
            # if url == '':
            #     url = "https://www.google.com"
            # Demander à l'utilisateur le nom du fichier de sortie
            # nom_fichier = input("Veuillez entrer le nom du fichier de sortie : ")
            # controle_saisie_fichier_de_sortie()
            nom_fichier=controle_saisie_fichier_de_sortie()
            print(f"Résumé de vos choix: \n Type de sortie {my_choice_type_fichier} \n Nom du fichier {nom_fichier}.{my_extension_fichier}")
            
            
            # Faire une requête HTTP
            response = requests.get(url)

            # Utiliser BeautifulSoup pour analyser le contenu HTML
            soup = BeautifulSoup(response.text, 'html.parser')
                # Supprimer les balises script et style
            for script in soup(["script", "style", "header"]):
                script.decompose()
                # sortie en .html
                if my_choice_type_fichier=="1":
                        my_extension_fichier="html"
                        # Enregistrer le contenu HTML dans un fichier
                        with open(nom_fichier + ".html", "w", encoding='utf-8') as file:
                            file.write(str(soup))
                # sortie en .txt
                elif my_choice_type_fichier=="2":
                    my_extension_fichier="txt"
                    # Convertir le contenu HTML en une liste de lignes
                    content = str(soup).splitlines()

                    # Enregistrer le contenu en format CSV dans un fichier
                    with open(nom_fichier+ ".csv", "w", newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        for line in content:
                            writer.writerow([line])
                                    
                elif my_choice_type_fichier=="3":
                    my_extension_fichier="csv"
                    #  sortie en .csv
                    # Convertir le contenu HTML en une liste de lignes
                    content = str(soup).splitlines()

                    # Enregistrer le contenu en format CSV dans un fichier
                    with open(nom_fichier + ".csv", "w", newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        for line in content:
                            writer.writerow([line])

                    #  sortie en .json
                elif my_choice_type_fichier=="4":
                        my_extension_fichier="json"
                         # Convertir le contenu HTML en dictionnaire
                        content = {"html": str(soup)}

                        # Enregistrer le contenu en format JSON dans un fichier
                        with open(nom_fichier + ".json", "w", encoding='utf-8') as file:
                            json.dump(content, file, ensure_ascii=False, indent=4)
                else:
                    print("Choix non reconnu. Veuillez choisir parmi 1, 2, 3 ou 4.")

            #  traitement des erreurs
        except (Exception , ValueError) as e:
                # affiche en rouge le message d'erreur
                print(Fore.RED,"Une erreur inattendue s'est produite. Veuillez réessayer: ",e)
                print(Style.RESET_ALL)
                # menu pour proposer au user de stopper son programme
                error_message="""
                                Voulez-vous arrêter le programme ? 
                                si oui tapez O (oui) ou Y (yes) pour arrêter ou toute autre touche pour continuer :
                            """
                stop_program = input(error_message)
                if stop_program.lower() == 'o'or stop_program.lower() == 'y':
         
                    break 
        finally:
             print(f"votre traitement est terminé, votre fichier {Fore.GREEN}{nom_fichier}.{my_extension_fichier}{Style.RESET_ALL} est dispo")
            #  print(S3tyle.RESET_ALL)
             break
            


# url = "https://www.google.com"
# nom_fichier="scrap_page_google"



scrapp_page_web()
