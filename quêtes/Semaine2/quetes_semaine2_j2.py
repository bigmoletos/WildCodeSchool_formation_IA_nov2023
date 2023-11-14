################################################################
# people = {"Gontran": 23,
#           "Jason": 42,
#           "Ayoub": 27}


# for i in people:
#   print(i)
#   print(type(i))
# for i in people.keys():
#   print(type(i))
#   print(i)
# for i in people.values():
#   print(type(i))
#   print(i)
# for i in people.items():
#   print(i)
#   print(type(i))
# for i, age in people.items():
#   print(age)
#   print(i)
#   print(type(i))


################################################################
# people = {"Gontran": 23,
#           "Jason": 42,
#           "Ayoub": "27",
#           "Léo": [10,20,30],
#           "Rosario": {"Juan": 3,
#                       "Camelia": 6}}


# for i in people.values():
#   print(type(i))

# print("#"+"-"*50)

# people["Ayoub"] = int(people["Ayoub"])
# print(type(people))

# print("#"+"-"*50)

# for i in people.values():
#   print(type(i))
# print(people)
################################################################
# groups = {"groupe_1": ["Lam", "Ghizlaine", "Khaled", "Florian"],
#           "groupe_2": ["Lucille", "Mbaye", "Cécile", "Rohan"],
#           "groupe_3": ["Agathe", "Charlotte", "Charles", "Maxime"],
#           "groupe_4": ["Gaelle", "Linh", "Meral"]}


# for i in groups.values():
#   print(i)
# #   print(groups.values()[:i])
#   print(type(i))

# for i in groups.values():
#   for v in i:
#     print(v)
################################################################
# """"
# Mission 1
# Below is a dictionary containing the number of French campuses that offer each kind of Wild Code School course.

# wildcodeschool = { "data_analyst": 4, "data_scientist": 2, "dev_web": "13" }

# Find a way to only display the keys that have int values.
# """
# wildcodeschool =	{
#   "data_analyst": 4,
#   "data_scientist": 2,
#   "dev_web": "13"}
# print(wildcodeschool)
# list={key :value for key, value in wildcodeschool.items() if isinstance(value, int)}
# print(list)
################################################################
# """
# Mission 2
# For the same dictionary, find a way to display all the values that have a key that contains the letter "e".

# """
# list={key :value for key, value in wildcodeschool.items() if isinstance(value, str) and 'e' in key}
# print(list)
################################################################
# """Mission 3
# Within the same dictionary, change the type of the value of
#  the "dev_web" key to be an int. Then add a new key-value pair
#  which will be "total_campus" : 19, using a dictionary method.

# Change the value of "dev_web" to be and int :
# """
# wildcodeschool['dev_web']=int(wildcodeschool['dev_web'])
# print(type(wildcodeschool['dev_web']))
# print(wildcodeschool)
# # list

################################################################
# Pour supprimer la paire clé-valeur 'dev_web': 13, vous pouvez utiliser del
# del wildcodeschool['dev_web']
# # Pour supprimer la paire clé-valeur 'total_campus': 19, vous pouvez utiliser pop()
# wildcodeschool.pop('total_campus')

# print(wildcodeschool)
################################################################
# """
# Mission 5
# Still within the dictionary generated from Mission 3, find a way
#  to display the dictionary keys in alphabetical order.
# """
# dict_sorted=sorted(wildcodeschool.keys())
# print(dict_sorted)
################################################################
# """
# Mission 6
# Create a script that returns the same elements as the values() method, as a list.
# Example: for {'a': 1, 'b': 2, 'c': 3} it will create [1, 2, 3]
# """

# list_valeurs=[v for v in wildcodeschool.values()]
# print(list_valeurs)
################################################################
# quete 2.7
################################################################
# import nltk
# from nltk.corpus import words
# nltk.download('words')

# # Créer une liste de tous les mots anglais
# mots_anglais = set(words.words())
# # print(mots_anglais)

# # Créer une liste de mots français en supprimant les mots anglais
# # mots_francais = [mot for mot in mots_anglais if not mot.isascii()]
# # print(mots_francais)
# # Filtrer la liste pour ne garder que les mots de 4 à 10 lettres
# mots_de_quatre_a_dix_lettres = [mot for mot in mots_anglais if 4 <= len(mot) <= 10]

# # Prendre les 50 premiers mots
# mots_selectionnes = mots_de_quatre_a_dix_lettres[:50]

# print(mots_selectionnes)

################################################################
# import random
# import string

# # juste pour le fun Creation d'un  tuple de maniere aléatoire
# # creation d'un liste aléatoire de 3 integers
# list_integer=[random.randint(0,50) for v in range(3) ]
# print(list_integer)
# #creation d'une liste aléatoire de 3 mots avec 7 caractéres et se terminant par une voyelle et en excluant les lettres w et z
# # set crée un ensemble sans doublon et trié, string.ascii_lowercase correspond à toutes les lettres de l'alphabet francais
# voyelles = 'aeiou'
# lettres = ''.join(set(string.ascii_lowercase) - set('wz'))
# list_strings=["".join(random.choice(lettres) for mot in range(7))+random.choice(voyelles) for _ in range(3) ]
# print(list_strings)
# #création d'une liste aléatoire de 2 listes contenant 3 items chacun
#   # Création de la première liste avec trois objets Python : un entier, une chaîne de caractères et un tuple
# liste1 = [1, 'élément2', (1, 2)]

#   # Création de la deuxième liste avec trois objets Python : un flottant, une liste et un dictionnaire
# liste2 = [1.1, ['sous-élément1', 'sous-élément2'], {'clé': 'valeur'}]

#   # Affichage des listes
# print("Liste 1 :", liste1)
# print("Liste 2 :", liste2)
################################################################
mon_tuple = (
    105, 206, 307,  # 3 entiers
    'chaine1', 'chaine2', 'chaine3',  # 3 chaînes de caractères
    ['élément1', 'élément2', 'élément3'], ['élément4', 'élément5',
                                           'élément6'],  # 2 listes contenant 3 éléments chacune
    # 2 dictionnaires contenant 3 items chacun
    {'clé1': 'valeur1', 'clé2': 'valeur2', 'clé3': 'valeur3'},
    {'clé4': 'valeur4', 'clé5': 'valeur5', 'clé6': 'valeur6'}
)
print(mon_tuple)
################################################################
"""
Now, access the second-to-last item in the second list.
"""
# on souhaite d'aprés mon tuple obtenir 'element5' donc l'avant dernier de la seconde liste
second_to_last_item = mon_tuple[7][-2]

print(second_to_last_item)
################################################################
"""
Mission 2
In the same tuple, access the last 4 elements using slicing.
"""
# on souhaite d'aprés mon tuple obtenir les 4 derniers elements n

les_quatres_derniers_element = mon_tuple[-4:]
print(les_quatres_derniers_element)
################################################################
"""
Mission 3
Change the value of the 4th element (the first string) of your tuple 
(since tuples are immutable, this means recreating a tuple where this element is changed).

"""
#  changement du 4 element donc de chaine1, comme c'est un string il est donc mutable
#  ce qui ne serait pas le cas des listes ou items
change_value_fourth_tuple = mon_tuple[:3] + ("chaineXXX",) + mon_tuple[4:]
print(change_value_fourth_tuple)
################################################################
"""
Mission 4
Create 2 tuples of the same length that contain only integers.

Then create a script that compares the sum of their elements and displays
 the tuple that has the highet total.
"""
compare_sum = ""
print(compare_sum)
################################################################
"""
Mission 5
Here's a tuple:

my_tuple = ("data analyst", "data scientist", "data engineer", "data architect")

Ask the user for a string, then for an integer position. 
Create an altered copy of my_tuple where the element at the given position is now the given string.

"""
position_integer = "5"

print()


################################################################
