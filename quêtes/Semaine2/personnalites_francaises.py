import json
import random
from datetime import datetime
"""programme  python pour choisir de maniere aleatoire une personnalite depuis le fichier json. Le programme  retourne tous les elements concernant cette personnlité:
on peut modifier le fichier pour corriger des données, dans ce cas on peut  l'enregistrer sous un autre nom. par exemple  rajouter à la fin la date "_modified_18nov2023" (personnilte_francaise_modified_18nov2023.json
Le programme  demande à l'utlisateur s'il veut modifer le fichier,
"""

# Lire le fichier JSON
with open(r"quêtes\data\json\liste_personnalite_francaise.json", 'r',encoding='utf-8') as f:
    data = json.load(f)
# print("data:", data)
# Choisir une personnalité au hasard avec toutes ses sous categories
personnalite = [p[key] for categorie in data.values() for p in categorie for key in p if key.startswith('Personnalités')]
print(f"Personnalité choisie : {personnalite}")
personnalite = random.choice(personnalite)
print(f"Personnalité choisie : {personnalite}")
# print(data[personnalite])

# # Créer une liste de tous les noms
# noms = [personnalite['nom'] for personnalite in data.values()]
# noms = list(data.keys())
#  parcourt chaque toutes les sous-categories du champ "Nom" et les mets dans la liste "noms"
noms = [p['Nom'] for categorie in data.values() for p in categorie]
print("noms:",noms)
# Choisir un nom au hasard
nom = random.choice(noms)
print("nom:",nom)


if nom is not None:
    print(f"Personnalité choisie : {nom}")
    # fait une liste de toutes les sous-categories du champ "Nom"
    #  s'il est égale = nom
    categorie_nom = [p for categorie in data.values() for p in categorie if p['Nom'] == nom]
    # categories = [[v for k, v in p.items()] for categorie in data.values() for p in categorie if p['Nom'] == nom]
    print("categorie_nom",categorie_nom)
    # Imprimer chaque champ et sa valeur
    for champ, valeur in nom.items():
        print(f"{champ}: {valeur}")
else:
    print("Aucune personnalité trouvée avec ce nom.")

# Demander à l'utilisateur s'il souhaite modifier le fichier
# modifier = input("Voulez-vous modifier le fichier ? (oui/non) ")

# if modifier.lower() in ('oui','o','yes','y'):
#     # Demander à l'utilisateur quel champ il souhaite modifier
#     champ = input("Quel champ souhaitez-vous modifier ? ")
#     nouvelle_valeur = input("Quelle est la nouvelle valeur ? ")

#     # Modifier le champ
#     data[personnalite][champ] = nouvelle_valeur
remplacer = input("Voulez-vous remplacer une entrée entière ? (oui/non) ")
if remplacer.lower() in ('oui', 'o', 'yes', 'y'):
    # Demander à l'utilisateur quelle entrée remplacer
    entree = input("Quelle entrée souhaitez-vous remplacer ? ")
    if entree in data.keys():
        # Demander les nouvelles données
        nouvelle_entree = input("Entrez les nouvelles données (au format JSON) : ")
        nouvelle_entree = json.loads(nouvelle_entree)

        # Remplacer l'entrée
        data[entree] = nouvelle_entree
    else:
        print("Entrée non reconnue.")

    # Enregistrer le fichier modifié avec un nouveau nom
    date_du_jour = datetime.now().strftime("%d%b%Y")
    with open(f'personnalites_francaises_modified_{date_du_jour}.json', 'w',encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)