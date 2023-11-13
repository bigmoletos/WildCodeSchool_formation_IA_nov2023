################################################################
# Voici ci-dessous une liste. Chaque élément représente un mot. On aimerait que chacun des mots commencent par une majuscule.
# song = ['tsamina','mina','eh','eh','Waka','Waka','hee','he','tsamina','mina','zangalewa','this','time','for','africa']

# # On fait du chaining et on attribue le résultat à la variable result.
# result = " ".join(song).title().split()
# print(result)

# > ['Tsamina',
#  'Mina',
#  'Eh',
#  'Eh',
#  'Waka',
#  'Waka',
#  'Hee',
#  'He',
#  'Tsamina',
#  'Mina',
#  'Zangalewa',
#  'This',
#  'Time',
#  'For',
#  'Africa']
################################################################

# """
# Quete Python semaine 2
# fd FR Python 2.1 Comment on the code, debugging....ipynb
# """
# # initialisation du tableau vide 'une_macedoine'
# une_macedoine = []
# # boucle permetttant de remplir notre liste. De 4 à 120 exlcus en comptant par pas de 3
# for nectarifaire in range(4,120,3):
# #    on ne prend que les valeurs supérieures à 40
#   if nectarifaire > 40:
#     # Si le nom bre est superieur à 40, ajout des valeurs carotte et flageolet dans notre liste
#     une_macedoine.append("carotte")
#     une_macedoine.append("flageolet")

################################################################
# joga_bonito = []
# joga_bonito_1 = []
# compteur = 0

# for vvv in "Bonjour":
#   print("vvv:",vvv)
#   for v in vvv:
#     print("v:",v)
#     bonjour = "¿Hola qué tal amigos?"
#     joga_bonito.append((v, bonjour))
#     print("joga_bonito:",joga_bonito)
#   joga_bonito_1.append(v)
#   print("joga_bonito_1:",joga_bonito_1)
#   compteur += len(bonjour)
#   print("compteur:",compteur)
################################################################
# joga_bonito = []
# joga_bonito_1 = []
# compteur = 0

# for vvv in "Bonjour":
#   print("vvv:",vvv)
#   for v in vvv:
#     print("v:",v)
#     bonjour = "¿Hola qué tal amigos?"
#     joga_bonito.append((v, bonjour))
#     print("joga_bonito:",joga_bonito)
#   joga_bonito_1.append(v)
#   print("joga_bonito_1:",joga_bonito_1)
#   compteur += len(bonjour)
#   print("compteur:",compteur)
################################################################
"""
Pour cette mission, inspirée d'un jeu télévisé, tu vas essayer de résoudre le problème suivant:
Tu dois combiner les variables avec des opérateurs mathématiques (*+-/)
pour trouver le résultat 466.  
Tu assigneras le résultat à la variable `answer`.  
Attention, pour cette mission, chaque variable n'est utilisable qu'une seule fois.
"""
# var_1 = 12
# var_2 = 20
# var_3 = 15
# var_4 = 3
# var_5 = 30

# answer =466

# res = 466

# if answer == res:
#   print("Tu peux passer à la mission suivante.")

################################################################
# import math
# nombre = int(input("entrez un nombre entier positif: "))
# factorielle_nombre = 1
# for i in range(1, nombre+1):
#     factorielle_nombre *= i
#     print(i)

# print(f"la factorielle de {nombre} est : {factorielle_nombre}")

# # autre methode en utilisant les fonctions math
# print(f"la factorielle de {nombre} est : {math.factorial(int(nombre))}")


################################################################
# """
# Pour cette mission, inspirée d'un jeu télévisé, tu vas essayer de résoudre le problème suivant: Tu dois combiner les variables avec des opérateurs mathématiques (*+-/) pour trouver le résultat 466.
# Tu assigneras le résultat à la variable answer.
# Attention, pour cette mission, chaque variable n'est utilisable qu'une seule fois.
# """
# import operator
# import itertools

# # Définir les nombres et les opérations
# nombres = [12, 20, 15, 3, 30]
# operations = [operator.add, operator.sub, operator.mul, operator.floordiv]
# # # operations = [operator.add, operator.sub, operator.mul, operator.truediv]
# # operations = [operator.add, operator.sub,operator.countOf, operator.mul, operator.floordiv]
# operations = [operator.add, operator.sub]

# # Générer toutes les permutations possibles des nombres et des opérations
# for nombres_perm in itertools.permutations(nombres):
#     for operations_perm in itertools.product(operations, repeat=len(nombres)-1):
#         # Calculer le résultat de l'expression courante
#         resultat = nombres_perm[0]
#         for i in range(1, len(nombres)):
#             try:
#                 # Appliquer l'opération à 'resultat' et 'nombres_perm[i]'
#                 if operations_perm[i-1] == operator.floordiv and nombres_perm[i] == 0:
#                     # Ignorer les divisions par zéro
#                     break
#                 resultat = operations_perm[i-1]
#             except ZeroDivisionError:
#                 # Ignorer les divisions par zéro
#                 break
#         else:
#             # Vérifier si le résultat est 466
#             if resultat == 80:
#                 print("Solution trouvée :")
#                 print(nombres_perm, operations_perm)
#                 break

################################################################
"""
Pour cette mission, inspirée d'un jeu télévisé, tu vas essayer de résoudre le problème suivant: Tu dois combiner les variables avec des opérateurs mathématiques (*+-/) pour trouver le résultat 466.
Tu assigneras le résultat à la variable answer.
Attention, pour cette mission, chaque variable n'est utilisable qu'une seule fois.
"""
import itertools

# Définir les nombres et les opérations
nombres = [12, 20, 15, 3, 30]
operations = ['+', '-','*','/']
liste_solutions=[]
resultat_attendu=466

# Générer toutes les permutations possibles des nombres et des opérations
for nombres_perm in itertools.permutations(nombres):
    for operations_perm in itertools.product(operations, repeat=len(nombres)-1):
        # Construire et évaluer l'expression
        expression = str(nombres_perm[0])
        for i in range(1, len(nombres)):
            expression += operations_perm[i-1] + str(nombres_perm[i])
        if eval(expression) == resultat_attendu:
            liste_solutions.append(expression)
            print(f"Solution trouvée : {expression} = {resultat_attendu}")

print(liste_solutions)