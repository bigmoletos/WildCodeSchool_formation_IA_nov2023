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
# """
# Pour cette mission, inspirée d'un jeu télévisé, tu vas essayer de résoudre le problème suivant: Tu dois combiner les variables avec des opérateurs mathématiques (*+-/) pour trouver le résultat 466.
# Tu assigneras le résultat à la variable answer.
# Attention, pour cette mission, chaque variable n'est utilisable qu'une seule fois.
# """
# import itertools

# # Définir les nombres et les opérations
# nombres = [12, 20, 15, 3, 30]
# operations = ['+', '-','*','/']
# liste_solutions=[]
# resultat_attendu=466

# # Générer toutes les permutations possibles des nombres et des opérations
# for nombres_perm in itertools.permutations(nombres):
#     for operations_perm in itertools.product(operations, repeat=len(nombres)-1):
#         # Construire et évaluer l'expression
#         expression = str(nombres_perm[0])
#         for i in range(1, len(nombres)):
#             expression += operations_perm[i-1] + str(nombres_perm[i])
#         if eval(expression) == resultat_attendu:
#             liste_solutions.append(expression)
#             print(f"Solution trouvée : {expression} = {resultat_attendu}")

# print(liste_solutions)
################################################################
# Pour cette mission, tu vas devoir concaténer des variables pour reproduire la phrase suivante:

# "1 bouche bouche bée qu'1 bouche bouche la bouche de douche de la boucherie."

# Pour y parvenir, tu peux additionner tes variables. Tu peux aussi modifier le
# type d'une variable, uniquement avec les built-in function.
# result = " ".join(song).title().split()
# var_1 = 1
# var_2 = "bouche"
# var_3 = "bée"
# var_4 = "la"
# var_5 = "qu'"
# var_6 = "de"
# var_7 = "douche"
# var_8 = "la"
# var_9 = "boucherie."
# phrase = str(var_1) + " " + var_2 + " " + var_2 + " " + var_3 + " " + var_5 + str(var_1) + " " + var_2 + " " + var_2 + " " + var_4 + " " + var_2 + " " + var_6 + " " + var_7 + " " + var_6 + " " + var_8 + " " + var_9
# print(phrase)
################################################################
# phrase = "Ton tonton tond un thon à Thonon."
# chaine_to_find='on'
# compte_mots_found=phrase.count(chaine_to_find)
# print(f"on trouve {compte_mots_found} fois la chaine de caractére '{chaine_to_find}' dans la phrase \n {phrase}")

################################################################
# """
# Tu sais ce qu'est le "chaining" ?
# Concrètement, il s'agit d'enchaîner des méthodes les unes après les autres (en série) pour arriver à tes fins.
# Un peu comme un bon footballeur ferait pour marquer un but (passement de jambes, crochet, petit-pont, frappe et but !), tu vas devoir enchaîner les méthodes les unes après les autres pour atteindre ton objectif.
# Ton objectif, c'est d'appliquer plusieurs méthodes les unes à la suites des autres (chaining) pour obtenir la phrase suivante:

# Ah mais vous savez, je ne pense pas qu'il y ai de bonnes ou de mauvaises situations.

# Tu as le droit d'utiliser plusieurs fois la même méthode.
# """
# phrase = "Ah maIS vows SavUZ, je ge PUHSe Pas qw'il y Ai de BoggUS ow de MawVaiSUS siTwatIOHs."
# phrase=phrase.replace("U","e").replace("w","u").replace("g","n").replace("H","n").lower()
# print(phrase)


################################################################
# mot='welcome'
# caractere_to_find="e"
# # positions=[i for i in range(len(chaine)) if chaine.startswith(sous_chaine, i)]
# # positions=[carac for i, carac in enumerate(mot)  if carac[i-1] == caractere_to_find]
# # positions = [carac+1 for carac in range(len(mot)) if mot[carac] == caractere_to_find]
# for i in positions:
#     print(i)

# print(positions)

################################################################
# pour faciliter la correction je ne fais pas les input('veuillez saisir un mot') et  input('veuillez le nombre de répetetions (un chiifre inférieur à 10)')
# mot='welcome'
# nombre_repetition=5
# print(mot*nombre_repetition)


################################################################
# """
# For each cell, execute the code and answer the question before moving on to the next.
# """
# import random
# names = ["Fredy", "Nicolas", "Alexandre"]
# test_list = ['Hi', 'my', 'name', 'is', "hi", "my","name", "is", "chickychicky"]

# test_list[8] = "Marshall"

# for i, val in enumerate(names):
#   print(val)
#   # print(type(val))
# print("""val est du type string

# i correspond à la clé et
# val correspond à la valeur
# """)

# for i in range(2,8,2):
#   print(test_list[i])
# for i in enumerate(names):
#   print(i)

# numbers = [2,3,1,5,9]

# for i in range(10,15):
#   numbers.append(i)
# print(numbers)
# random.randint(0,10)
# del numbers[0]
# numbers.insert(5, "hey hey hey")
# print(numbers)
# test_list = ['Hi', 'my', 'name', 'is', "hi", "my","name", "is", "chickychicky"]
# print(test_list)
# test_list = " ".join(test_list)
# print(test_list)
################################################################
# """
# # Preliminary note: sometimes, the challenge tells you to do something that is incompatible with some input (for instance, you ask for a position but the user enters some text, or an invalid number).

# # Here you can assume that all user input goes according to plan (the "happy path"). If you want an extra optional challenge, feel free to manage possible error cases!

# # Mission 1
# # Define a list, then display only the elements (and their position) that have even positions (0, 2, 4, 6...).

# # With test_list = ["a", "b", "c", "d", "e"], the script should display:
# # a at position 0
# # c at position 2
# # e at position 4

# """
# test_list = ["a", "b", "c", "d", "e"]
# for i, val in enumerate(test_list):
#     if i % 2==0:
#         print (val," est à la position ", i)


################################################################
# """
# Define a list, then ask for a position, then for a string. Then replace the list element at that position by the given string, and display the resulting list.

# For example, with the list test_list2 = ['hello', 'good morning', 'bye bye', 'have a good day'], the position 2 and the string yeah, you should display:
# ['hello', 'good morning', 'yeah', 'have a good day']
# """
# test_list2 = ['hello', 'good morning', 'bye bye', 'have a good day']

# position = int(input('position ? :'))
# position=2
# mot='yeah'
# test_list2[position] = mot
# print(test_list2)
# # for i, val in enumerate(test_list2):
# #     if i==position:


# # test_list3=[test_list3 for i, val in enumerate (test_liste2) ]

################################################################
# test_list2 = ['hello', 'good morning', 'bye bye', 'have a good day']
# mot= input('veuillez saisir un mot :')
# position = int(input('position ? :'))

# test_list2[position] = mot
# print(test_list2)


################################################################
# """
# Define a list, then ask for a position, then for a string.
# Then replace the list element at that position by the given string, and display the resulting list.

# For example, with the list test_list2 =
# ['hello', 'good morning', 'bye bye', 'have a good day'],
# the position 2 and the string yeah, you should display:
# """

# import random
# #création d'une liste aléatoire de 5 nombres compris entre 0 et 20
# my_list=[]
# my_list=[ random.randint(0,20) for i in range(0,5) ]
# print(my_list)
# # ask the user a number
# number=int(input('veuillez saisir un nombre entier: '))
# # put the number at the end of the list
# my_list.insert(len(str(number))+1,number )
# #  autre solution
# # my_list[-1]=number
# print(my_list)
# # remove the firts element
# del my_list[0]
# print(my_list)
################################################################
# """
# Define a list, then ask the user for a string. Then, insert the string in the list at a random position, and display the resulting list.

# For example, with the list test_list4 = ["p", "y", "t", "h", "o"] and the input n, you might get:
# """

# import random
# import string
# my_letters_list=[]
# # my_letters_list=random.randrange(0,20,2)
# # my_letters_list=random.choice(string.ascii_lowercase)
# # print(my_letters_list)
# my_letters_list=[random.choice(string.ascii_lowercase) for _ in range(5)]
# print(my_letters_list)
# # ask the user for a string.
# # lettre_minuscule=input('veuillez saisir une lettre en minuscule:')
# # lettre_minuscule=lettre_minuscule.lower()
# lettre_minuscule='ma saisie'

# #  insert the lettre_minuscule au hasard dans la list
# index_max_my_letters_list=len(my_letters_list)
# random_position=random.randrange(0,index_max_my_letters_list,1)
# print(random_position)
# my_letters_list[random_position]=lettre_minuscule
# print(my_letters_list)

################################################################
# """
# Create a list of integers.
# Then, display a list with the elements ordered from smallest to largest,
# using the right built-in function.

# With the list test_list5 = [3, 4, 0, -1, 35, 7], this will display:
# [-1, 0, 3, 4, 7, 35]
# """
# import random

# # création list d'integers
# my_integer_list=[random.randint(0,20) for _ in range (10)]
# print(my_integer_list)
# #  trie par ordre croissant des valeurs
# my_integer_list.sort()
# print(my_integer_list)
# # trie par ordre croissant des valeurs
# my_integer_list.sort(reverse=True)
# print(my_integer_list)


################################################################
# """"
# Mission 6
# Ask the user for a string,
# convert it to a list of characters with the list function,
# then ask for a single character.

# Remove the first occurrence of the character from the list,
# then display how many occurrences of the character remain in the list.

# For instance if you enter "Excellent work" then the letter "e", it will display:
# There are still 2 copies of e in the list
# """
# # Ask the user for a string
# # my_word=input("veuillez saisir une phrase")
# my_word = 'Excellent work my honor'
# print("pour faciliter la correction j'ai commenté la saisie et j'ai mis en dur :", my_word)
# # convert it to a list of characters with the list function
# # list_character = "".join(my_word)
# list_character = list(my_word)
# print(list_character)
# # then ask for a single character.
# # single_letter=input("veuillez saisir une lettre")
# single_letter = 'e'
# print("pour faciliter la correction j'ai commenté la saisie et j'ai mis en dur :", single_letter)

# # Remove the first occurrence of the character from the list
# for i, val in enumerate(list_character):
#     if val == single_letter:
#         firts_occurence=i
#         del list_character[firts_occurence]
#         break
# print(list_character)
# # then display how many occurrences of the character remain in the list
# nombre_occurence=list_character.count(single_letter)+ list_character.count(single_letter.upper())
# print(" il reste ", nombre_occurence," occurence"+("s" if nombre_occurence >1 else "")," de la lettre: ",single_letter )

################################################################
"""
Mission 7
Define three lists containing no duplicates.
Then, indicate (however you like)
the two that have the most elements in common (or all three if there's a tie).

For instance, with:
list_a = [1, 2, 4, 8, 16, 32]
list_b = [1, 2, 3, 5, 8, 13]
list_c = [2, 3, 5, 7, 11, 13]

Lists B and C have the most common elements!

"""
# des ensembles en Python offre plusieurs avantages, surtout lorsqu’il
# s’agit de trouver des éléments communs entre des listes :

# Rapidité : Les opérations sur les ensembles en Python
# sont généralement plus rapides que les opérations sur les listes, surtout pour les grandes listes. C’est parce que les ensembles sont implémentés comme des tables de hachage, ce qui permet des recherches et des insertions en temps constant.

# Unicité : Les ensembles garantissent l’unicité des éléments.
# Si vous avez une liste avec des doublons et que vous voulez éliminer les doublons,
#  vous pouvez simplement convertir la liste en un ensemble.

# Opérations d’ensemble : Les ensembles en Python
# supportent des opérations mathématiques comme l’union, l’intersection, la différence et la différence symétrique. Ces opérations peuvent être très utiles pour comparer des listes.

# Dans le cas de la comparaison de listes pour trouver des points communs,
# convertir les listes en ensembles permet d’utiliser
# l’opération d’intersection pour trouver facilement et rapidement
# les éléments communs. De plus, comme les ensembles garantissent
# l’unicité des éléments, cela évite de compter plusieurs fois
# le même élément si un élément apparaît plus d’une fois dans une liste.


# Define three lists containing no duplicates.
# list_a=[random.randint(0,100) for _ in range (10)]
import random
list_a = random.sample(range(0, 15), 10)
list_b = random.sample(range(0, 15), 10)
list_c = random.sample(range(0, 15), 10)

print("list_a: ",list_a)
print("list_b: ",list_b)
print("list_c: ",list_c)
# Then, indicate (however you like) the two that have the
#  most elements in common (or all three if there's a tie).
# onn transforme les listes en ensemble
ensemble_list_a = set(list_a)
ensemble_list_b = set(list_b)
ensemble_list_c = set(list_c)
print(ensemble_list_a)
print(ensemble_list_b)
print(ensemble_list_c)
#  recherche des points commun des ensembles
# points_communs1 = ensemble_list_a & ensemble_list_b & ensemble_list_c
list_points_communs_ab = ensemble_list_a & ensemble_list_b
list_points_communs_bc = ensemble_list_b & ensemble_list_c
list_points_communs_ac = ensemble_list_a & ensemble_list_c
# print(list_points_communs_ab)
# print(list_points_communs_bc)
# print(list_points_communs_ac)
points_communs_ab = len(ensemble_list_a & ensemble_list_b)
points_communs_bc = len(ensemble_list_b & ensemble_list_c)
points_communs_ac = len(ensemble_list_a & ensemble_list_c)
# print(points_communs_ab)
# print(points_communs_bc)
# print(points_communs_ac)
max_points_commun = max(
    points_communs_ab, points_communs_bc, points_communs_ac)
# print(max_points_commun)

#  cherche les  liste ayant le plus de points commun
if points_communs_ab == max_points_commun:
    print("les listes a et b ont le plus de points commun")
    print(list_points_communs_ab)
elif points_communs_bc == max_points_commun:
    print("les listes b et c ont le plus de points commun")
    print(list_points_communs_ab)
elif points_communs_ac == max_points_commun:
    print("les listes a et c ont le plus de points commun")
    print(list_points_communs_ac)


# list_points_communs_ab2=" ".join(list_points_communs_ab)
# print(list_points_communs_ab2)
# print(points_communs)
# print(list_a)
# print(list_b)
# print(list_c)


# print(list_a)
# print(list_b)
# print(list_c)
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
