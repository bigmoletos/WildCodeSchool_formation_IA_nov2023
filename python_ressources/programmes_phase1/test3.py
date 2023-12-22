"""tests imports page html"""
from bs4 import BeautifulSoup
import requests


my_url = "https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296681-importez-des-packages-python"
my_page = requests.get(my_url)
print(my_page.status_code)
# print(my_page.content)


# Faire une requête HTTP à la page Web
my_url2 = "https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296681-importez-des-packages-python"
response = requests.get(my_url2)

# Analyser le contenu HTML de la page avec BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.find)

"""
# Trouver le paragraphe spécifique en utilisant son identifiant ou sa classe CSS
# (remplacez 'id_du_paragraphe' par l'identifiant réel du paragraphe)
paragraphe =soup.find('ul', {'id': 'r-8224241'})
# paragraphe = soup.find('ul#r-8224241')

# Extraire et afficher le texte du paragraphe
if paragraphe:
    texte = paragraphe.get_text()
    print(texte)
else:
    print("Paragraphe non trouvé")

"""
"""
# Trouver le titre "En résumé" en utilisant son identifiant
titre = soup.find('h3', {'id': "En-résumé"})
print(titre)
# Trouver le paragraphe suivant le titre en utilisant la méthode next_sibling
paragraphe = titre.next_sibling

# Extraire et afficher le texte du paragraphe
texte = paragraphe.get_text()
print(texte)
"""


""" 
# Trouver le titre "En résumé" en utilisant son identifiant
titre = soup.find('h3', {'id': 'r-8224251'})

# Trouver le paragraphe suivant le titre en utilisant la méthode next_sibling
element = titre
liste=[]
while element:
    element = element.next_sibling
    if element and element.name == 'ul':
        liste = element
        break

# Extraire et afficher le texte de la liste
if liste:
    for item in liste.find_all('li'):
        print(item.get_text())
else:
    print("Liste non trouvée")

"""


# Trouver le titre "En résumé"
# titre = soup.find(string="<h3 id='r-8224251' data-claire-element-id='33764638'><strong>En résumé</strong></h3>")

# Trouver le titre "En résumé"
# titre = soup.find('strong', string=lambda text: 'En résumé' in text)
# titre = soup.find('strong', tstring=lambda text: "En résumé" in text)
titre = soup.find('h3', id='r-8224251')
print("titre: ",titre)
# Trouver tout le texte suivant le titre
# element = titre
# resume_texte =""
# while element:
#     element = element.next_sibling
#     if element and element.name:
#         resume_texte += '\n\n' + element.get_text()

# print(resume_texte)
