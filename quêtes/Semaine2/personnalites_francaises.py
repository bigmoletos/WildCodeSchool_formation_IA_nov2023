import json
import random
from datetime import datetime
"""programme  python pour choisir de maniere aleatoire une personnalite depuis le fichier json. Le programme  retourne tous les elements concernant cette personnlité:
on peut modifier le fichier pour corriger des données, dans ce cas on peut  l'enregistrer sous un autre nom. par exemple  rajouter à la fin la date "_modified_18nov2023" (personnilte_francaise_modified_18nov2023.json
Le programme  demande à l'utlisateur s'il veut modifer le fichier,
"""

# Lire le fichier JSON
with open('quêtes\data\json\liste_personnalite_francaise.json', 'r') as f:
    data = json.load(f)

# Choisir une personnalité au hasard
personnalite = random.choice(list(data.keys()))
print(f"Personnalité choisie : {personnalite}")
print(json.dumps(data[personnalite], indent=4, ensure_ascii=False))

# Demander à l'utilisateur s'il souhaite modifier le fichier
modifier = input("Voulez-vous modifier le fichier ? (oui/non) ")

if modifier.lower() == 'oui':
    # Demander à l'utilisateur quel champ il souhaite modifier
    champ = input("Quel champ souhaitez-vous modifier ? ")
    nouvelle_valeur = input("Quelle est la nouvelle valeur ? ")

    # Modifier le champ
    data[personnalite][champ] = nouvelle_valeur

    # Enregistrer le fichier modifié avec un nouveau nom
    date_du_jour = datetime.now().strftime("%d%b%Y")
    with open(f'personnalites_francaises_modified_{date_du_jour}.json', 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)