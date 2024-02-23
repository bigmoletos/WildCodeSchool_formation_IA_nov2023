# import os
# import sys
import requests
from bs4 import BeautifulSoup
# import site
# from robotexclusionrulesparser import RobotExclusionRulesParser


import urllib.robotparser
# URL de la page des compétitions
competitions_url = 'https://www.kaggle.com/competitions'

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.kaggle.com/robots.txt")
rp.read()

# Vérifier si le scraping est autorisé pour cette URL
if rp.can_fetch("*", "https://www.kaggle.com/competitions"):
    # Faire une requête GET pour obtenir le contenu de la page
    competitions_response = requests.get(competitions_url)

    # Analyser le contenu avec BeautifulSoup
    competitions_soup = BeautifulSoup(competitions_response.content, 'html.parser')

    # Trouver tous les éléments qui contiennent le nom des compétitions
    # Remplacez 'element' et 'class' par les bons noms d'éléments et de classes spécifiques à la structure de la page Kaggle
    competitions_elements = competitions_soup.find_all('element', class_='class')

    # Extraire et afficher le nom de chaque compétition
    for element in competitions_elements:
        print(element.text.strip())
else:
    print("Le scraping est interdit pour cette URL.")


# Vous pouvez maintenant vérifier chaque URL avant de faire du scraping de la même manière.
