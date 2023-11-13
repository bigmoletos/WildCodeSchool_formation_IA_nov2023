import requests
from bs4 import BeautifulSoup
import json
import csv

from controle_saisie_nom_fichier import controle_saisie_fichier_de_sortie


def web_scrapping(url, output_format):
    """ copie le contenu d'une page web et le copie dans un fichier output.html
    idealemenent il faudrait pourvoir choisir la sortie du fichier 
    par ex en txt, json ou csv

    """
    # Faire une requête HTTP
    response = requests.get(url)

    # Utiliser BeautifulSoup pour analyser le contenu HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Supprimer les balises script et style
    for script in soup(["script", "style", "header"]):
        script.decompose()

    # Enregistrer le contenu dans un fichier selon le format spécifié
    if output_format == "html":
        with open(output_filename, "w", encoding='utf-8') as file:
            file.write(str(soup))
    elif output_format == "json":
        content = {"html": str(soup)}
        with open(output_filename, "w", encoding='utf-8') as file:
            json.dump(content, file, ensure_ascii=False, indent=4)
    elif output_format == "csv":
        content = str(soup).splitlines()
        with open(output_filename, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for line in content:
                writer.writerow([line])
    elif output_format == "txt":
        with open(output_filename, "w", encoding='utf-8') as file:
            file.write(str(soup))
    else:
        raise ValueError("Format de sortie non reconnu. Veuillez choisir parmi 'html', 'json', 'csv' ou 'txt'.")


# def controle_saisie(nom_fichier):
#     # Supprimer les espaces de début et de fin
#     nom_fichier = nom_fichier.strip()

#     # Remplacer les autres espaces par un _
#     nom_fichier = nom_fichier.replace(' ', '_')

#     # Supprimer tous les caractères spéciaux
#     nom_fichier = re.sub('[^A-Za-z0-9_]+', '', nom_fichier)

#     # Vérifier si le nom du fichier commence par une lettre
#     if not nom_fichier[0].isalpha():
#         raise ValueError("Le nom du fichier doit commencer par une lettre.")

#     return nom_fichier

while True:
    try:
        # Demander à l'utilisateur l'URL de la page web à scraper
        url = input("Veuillez entrer l'URL de la page web à scraper (par défaut https://www.google.com) : ")
        if url == '':
            url = "https://www.google.com"

        # Demander à l'utilisateur le format de sortie souhaité
        menu_input = """Veuillez choisir le format de sortie du fichier.
#1 pour une sortie .html
#2 pour une sortie .txt
#3 pour une sortie .csv
#4 pour une sortie .json
Tapez votre choix (1, 2 ,3 ou 4): """
        my_choice_type_fichier = input(menu_input)
        if my_choice_type_fichier == "1":
            output_format = "html"
        elif my_choice_type_fichier == "2":
            output_format = "txt"
        elif my_choice_type_fichier == "3":
            output_format = "csv"
        elif my_choice_type_fichier == "4":
            output_format = "json"
        else:
            raise ValueError("Choix non reconnu. Veuillez choisir parmi 1, 2, 3 ou 4.")

        # Demander à l'utilisateur le nom du fichier, utilisation de la methode  controle_saisie_fichier_de_sortie
        # nom_fichier = input("Veuillez entrer le nom du fichier : ")
        # nom_fichier = controle_saisie(nom_fichier)
        nom_fichier=controle_saisie_fichier_de_sortie()

        # Utilisation de la fonction avec le format choisi
        web_scrapping(url, output_format, f"{nom_fichier}.{output_format}")

        print(f"Résumé de vos choix: \n Type de sortie {output_format} \n Nom du fichier {nom_fichier}.{output_format}")
        
        break  # Sortir de la boucle si tout s'est bien passé

    except ValueError as e:
        print(e)
        print("erreur de valeur, veuillez verifier vos saisies")
        
    except Exception as e:
        print("Une erreur inattendue s'est produite. Veuillez réessayer.")
        
    finally:
        stop_program = input("Voulez-vous arrêter le programme ? Tapez O pour arrêter ou toute autre touche pour continuer : ")
        if stop_program.lower() == 'o'or stop_program.lower() == 'y':
            break