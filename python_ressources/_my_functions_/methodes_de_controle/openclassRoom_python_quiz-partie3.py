import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import csv


# url='G:\programmation\python\openClassRoomModulePython\_my_functions_\quiz-partie3.html'
url='http://127.0.0.1:3000/_my_functions_/quiz-partie3.html'


response=requests.get(url)
html=response.content

soup = BeautifulSoup(html, 'html.parser')

titre=soup.title.string
print(titre)

produits = []
for table in soup.find_all('table'):
    for tr in table.find_all('tr')[1:]:
        td = tr.find_all('td')
        nom = td[0].get_text()
        description = td[1].get_text()
        prix = td[2].get_text()
        quantite = td[3].get_text()
        produit = {
            'nom': nom,
            'description': description,
            'prix': prix,
            'quantite': quantite
        }
        produits.append(produit)

# print(produits)

# produits2 = []
# for table in soup.find_all('table'):
#     for tr in soup.find_all('tr')[1:]:
#         for td in soup.find_all('td'):
            # td=tr.find_all('td')
            # nom=get_text(td)
            # print(nom)
            # description=td.get_text()
            # prix=td.get_text()
            # quantite=td.get_text()
            # produit={
            #     'nom': nom,
            #     'description':description,
            #     'prix':prix,
            #     'quantite':quantite

            # }
            # produits2.append(produit)
            # print(td.get_text())
# print(td.get_text())
print("produits: ",produits)

taux_de_change = 0.8
for produit in produits:
    prix_dollar = produit['prix'].replace('$', '')
    print(prix_dollar)
    prix_dollar = float(prix_dollar)
    print(prix_dollar)

    prix_euro = prix_dollar * taux_de_change
    produit['prix'] = str(round(prix_euro, 2)) + '€'


print("produits: ",produits)

with open(f'{titre}.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['nom', 'description', 'prix', 'quantite']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for produit in produits:
        writer.writerow(produit)
