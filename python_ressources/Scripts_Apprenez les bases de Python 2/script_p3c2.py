import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content

# affiche la page HTML
print(page)

# transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")

# récupération de tous les titres
titres = soup.find_all("a", class_="gem-c-document-list__item-title")
titre_textes = []
for titre in titres:
	titre_textes.append(titre.string)

# récupération de toutes les descriptions
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
description_textes = []
for description in descriptions:
	description_textes.append(description.string)

