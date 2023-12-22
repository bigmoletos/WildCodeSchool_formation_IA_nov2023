

# while True:
#     try:
#         borne1=int(input("veuillez entrer le premier chiffre: ").strip())
#         borne2=int(input("veuillez entrer le deuxième chiffre: ").strip())
       
#         print(f"vous avez entré les chiffres suivants: \n Borne1={borne1}\n Borne2={borne2}")
#         borne3=int(input("veuillez entrer le 3éme chiffre: ").strip())
        
       

#         if borne3<borne1 and borne3<borne2:
#             print(f"votre 3éme borne= {borne3} est \n inférieure à la borne1={borne1} ")
#         elif borne3>=borne1 and borne3<=borne2:
#             print(f"votre 3éme borne= {borne3} est \n comprise entre les borne1={borne1} et la borne2={borne2}")
#         else:
#             print(f"votre 3éme borne= {borne3} est \n superieure à la borne2={borne2} ")
        
#     except ValueError:
#         print("Erreur : veuillez saisir uniquement des chiffres entier")
#     message=input("""Vous avez saisi des erreurs voulez-vous arreter le programme ou continuer ?
#                   tapez Oui(o) pour arreter
#                   tapez sur n'importe quelle touche pour continuer:  """)
    
#     if message.lower()  in ['o', 'oui','y','yes']:
#         break
        

# for number in range(4,-1,-2) :
#     print(number)

# #table de muliplication de 1 à 10
# resultat=0
# # boucle de 1 à 10
# for table in range (1,11):
#     #je place réinitialise le tableau à chaque fois sinon il se rempli de toutes les tables
#     table_muliplication=[]
#     # print("table multiplication",table_muliplication)
#     print(f"la table de multiplication de {table} : ")
    
#     # boucle de 1 à  10 ou de 1 à 5 en fonction de la table
#     for multiplicateur in range (1,6 if table>=5 else 11):
#         resultat=table*multiplicateur
#         # j'ajoute à la liste "table_multiplication" le resultat du calcul
#         table_muliplication.append(str(resultat))

#     #je retire les [] et les '' du tableau en le convertissant 
#     # en string avec une jointure avec un espace " "
#     table_en_texte=" ".join(table_muliplication)
#         # print(f"{table} * {multiplicateur}  = {resultat}")
#     print(table_en_texte)


# # print("\n")
#         # Extraire les années, mois, jours, heures, minutes, secondes et millisecondes
#         annees = intervalle.days // 365
#         mois = (intervalle.days % 365) // 30
#         jours = (intervalle.days % 365) % 30
#         heures = intervalle.seconds // 3600
#         minutes = (intervalle.seconds % 3600) // 60
#         secondes = (intervalle.seconds % 3600) % 60
#         millisecondes = intervalle.microseconds // 1000

#         # Formater l'intervalle
#         intervalle_formate = f"{annees} années {mois} mois {jours} jours {heures} heures {
#             minutes} minutes {secondes} secondes {millisecondes} millisecondes"


# # ecrire un programme qui transforme les secondes en mois jour heure seconde
# # input en seconde
# nombre=int(input("veuillez saisir un chiffre entier de secondes"))
# # 1 mois = 30,416j, 1 années=365 j, 1jour 24h, 1heure 60minute 1 minute 60s

# year=nombre//365
# mois=nombre //30.4106
# days=nombre
# heures=nombre
# minutes=nombre
# print(f"avec  {nombre} on obtient {year} années {mois} mois {heures} jour {minutes} minutes")

"""
Les stocks des ingrédients nécessaires à la réalisation de l'onguent commencent à se vider et les savants vous chargent d'aller en ville acheter une certaine quantité de chaque ingrédient, afin de pouvoir continuer la production pendant le prochain mois.

Le comptable étant particulièrement pointilleux, il vous donnera exactement la quantité d'argent dont vous avez besoin, pas une pièce de plus. Heureusement vous savez à l'avance le prix de chaque ingrédient et la quantité dont vous avez besoin.

Ce que doit faire votre programme :
Il y a 10 ingrédients et ils ont tous un prix au kilo différent : 9, 5, 12, 15, 7, 42, 13, 10, 1 et 20.

Votre programme devra lire 10 entiers, le poids (en kilogrammes) qu'il faut acheter pour chaque ingrédient. Il devra calculer le coût total de ces achats.
"""

# # 402 au lieu de 771
# liste_prix_au_kilo=[9, 5, 12, 15, 7, 42, 13, 10, 1 ,20]
# cout_total=0
# # for prix in liste_prix_au_kilo:
# for prix in range(10):
#     poids=int(input("poids total: "))
#     # print("poids: ",poids)
#     # res=poids*prix
#     res=poids*liste_prix_au_kilo[prix]
#     # print("res: ",res)
#     cout_total =cout_total + res
#     # print("prix=",prix, "poids: ",poids, "res: ",res, "cout_total ", cout_total)
# print("prix total ",cout_total)


# Liste des prix au kilo pour chaque ingrédient
prix_kg = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]

# Initialiser le coût total à 0
cout_total = 0

# Pour chaque ingrédient
for i in range(10):
    # Lire le poids à acheter
    poids = int(input())
    # Ajouter le coût de cet ingrédient au coût total
    cout_total += poids * prix_kg[i]

# Afficher le coût total
print(cout_total)