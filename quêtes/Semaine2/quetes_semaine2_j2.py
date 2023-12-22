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
# import random
# mon_tuple = (
#     105, 206, 307,  # 3 entiers
#     'chaine1', 'chaine2', 'chaine3',  # 3 chaînes de caractères
#     ['élément1', 'élément2', 'élément3'], ['élément4', 'élément5',
#                                            'élément6'],  # 2 listes contenant 3 éléments chacune
#     # 2 dictionnaires contenant 3 items chacun
#     {'clé1': 'valeur1', 'clé2': 'valeur2', 'clé3': 'valeur3'},
#     {'clé4': 'valeur4', 'clé5': 'valeur5', 'clé6': 'valeur6'}
# )
# print(mon_tuple)
################################################################
# """
# Now, access the second-to-last item in the second list.
# """
# # on souhaite d'aprés mon tuple obtenir 'element5' donc l'avant dernier de la seconde liste
# second_to_last_item = mon_tuple[7][-2]

# print(second_to_last_item)
################################################################
# """
# Mission 2
# In the same tuple, access the last 4 elements using slicing.
# """
# # on souhaite d'aprés mon tuple obtenir les 4 derniers elements n

# les_quatres_derniers_element = mon_tuple[-4:]
# print(les_quatres_derniers_element)
################################################################
# """
# Mission 3
# Change the value of the 4th element (the first string) of your tuple
# (since tuples are immutable, this means recreating a tuple where this element is changed).

# """
# #  changement du 4 element donc de chaine1, comme c'est un string il est donc mutable
# #  ce qui ne serait pas le cas des listes ou items
# change_value_fourth_tuple = mon_tuple[:3] + ("chaineXXX",) + mon_tuple[4:]
# print(change_value_fourth_tuple)
################################################################
# """
# Mission 4
# Create 2 tuples of the same length that contain only integers.

# Then create a script that compares the sum of their elements and displays
#  the tuple that has the highet total.
# """

# # creation d'un liste aléatoire de 3 integers
# tuple1 = [random.randint(0, 50) for v in range(8)]
# print(tuple1)
# tuple2 = [random.randint(0, 50) for v in range(8)]
# print(tuple2)
# sum_tuple1 = sum(tuple1)
# sum_tuple2 = sum(tuple2)
# # print(sum_tuple1)
# # print(sum_tuple2)
# if sum_tuple1 >= sum_tuple2:
#     print(
#         f"la somme des éléments du tuple1 ({sum_tuple1}) est plus grand ou égal à la somme des elements tuple2  ({sum_tuple2})")
# else:
#     print(
#         f"la somme des éléments du tuple2 ({sum_tuple2}) est plus grand que la somme des elements tuple1  ({sum_tuple1})")


################################################################
"""
Mission 5
Here's a tuple:

my_tuple = ("data analyst", "data scientist", "data engineer", "data architect")

Ask the user for a string, then for an integer position.
Create an altered copy of my_tuple where the element at the given position is now the given string.

"""
# print("#"*80)
# print("Ce programme va vous proposer de remplacer un element du tuple ci-dessous. \nPour cela nous allons créer un autre tuple")
# print("#"*80)
# my_tuple = ("data analyst", "data scientist",
#             "data engineer", "data architect")
# print(my_tuple)
# check_string = False
# while True:
#     try:
#         # saisi d'un mot entre 3 et 10 lettres avec controle de saisi
#         if not check_string:  # si le  mot à déja été saisi correctement il est inutile de redemander sa saisie
#             print("-"*20)
#             your_string = input(
#                 "veuillez saisir un mot entre 3 et  20 lettres max : ")
#             print("-"*20)
#             taille_your_string = len(your_string)
#             if not (2 < taille_your_string <= 20):  # le mot doit avoir entre 3 et 20 caractéres
#                 print("veuillez saisir un mot  entre 3 et 20 lettres max")
#                 raise ValueError
#             if not any(c.isalpha()  or c in(' ', '.' , '!',  '?') for c in your_string):   # le mot  doit contenir uniquement  des lettres ou de la ponctuation
#                 print("veuillez saisir du texte et rien d'autre, sans chiffre")
#                 raise ValueError  # lance l'exception
#             print(f"votre saisie : {your_string} est conforme")
#             check_string = True
#         # saisi d'un chiffre entre 1 et la taille maxi du tuple avec controle de saisi
#         print("-"*20)
#         position_integer = int(
#             input(f"veuillez saisir un chiffre entre 1 et {len(my_tuple)} : "))
#         print("-"*20)
#         if  position_integer > 0 and position_integer <= len(my_tuple):
#             # on crée un nouveau tuple avec le remplacement de l'élément
#             my_new_tuple = my_tuple[:position_integer-1] + \
#                 (your_string,) + my_tuple[position_integer:]
#             print("-"*20)
#             print(my_new_tuple)
#             print("-"*20)
#             break
#         else:
#             print(f"Votre saisie :  {position_integer} est non conforme. \nVotre chiffre doit être compris \n entre 1 et {
#                   len(my_tuple)} inclus")
#             raise ValueError
#     except ValueError:
#         # print(f"veuillez saisir un chiffre entre 1 et  {len(my_tuple)} inclus")
#         # print("Erreur : veuillez saisir uniquement des chiffres entier")
#         decision_stop_encore= input(
#             "Vous avez saisi des erreurs voulez-vous arreter le programme ou continuer ? \n  tapez Oui(O) pour arreter \n  tapez sur n'importe quelle touche pour continuer:  ")

#         if decision_stop_encore.lower() in ['o', 'oui', 'y', 'yes']:
#             break
# print("#"*80)


################################################################
# QUETE PYTHON 2.8
################################################################


# resultat = ''.join(c.upper() if c.lower() in 'aeiou' else c.lower()
#                    for c in user_input)
################################################################

# a_set = {"banana", "lemon", "lemon", "cherry", "lemon", "strawberry", "lemon"}
# this_set = {1, 2, 3, 1, 2, 4, 1, 4, 3, 5, 6, 8, 9, 8, 3, 7, 6, 8, 6, 8, 9}
# len(this_set)

################################################################
# Try to count the amount of unique values from this list, in one line of code.

# a_list = [1, 2, 3, 1, 2, 4, 1, 4, 3, 5, 6, 8, 9, 8, 3, 7, 6, 8, 6, 8, 9]
# a_list = set(a_list)
# print(a_list)
################################################################
# a_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# first_value = list(a_set)[0]  # on caste le set en liste
# print(first_value)

################################################################
# a_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# a_set.add(500)
# print(a_set)

################################################################
# # the first set
# first_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# # second set
# second_set = {100, 110, 120}
# # Ajouter les valeurs du first set au second set
# first_set.update(second_set)

# print(first_set)
################################################################

# a_set = {"banana", "grapes", "cherry", "pineapple", "kiwi", "strawberry"}

# b_set = {"lemon", "kiwi", "grapes", "blueberry", "watermelon"}

# # 1er solution
# comun_element=a_set & b_set
# # 2 éme solution
# comun_element=a_set.intersection(b_set)
################################################################
# """
# Comme tu peux le voir, il y avait un certain nombre de valeurs uniques. Il aurait fallu un peu de temps pour les trouver toutes.
# Nous pouvons maintenant passer à la construction du dictionnaire.
# """

# list_of_values = [24, 55, 19, 71, 42, 48, 37, 25, 74, 17, 65, 72, 91, 70, 47, 50, 15, 48, 27, 60, 67, 3, 20, 82, 57, 9, 76, 70, 89, 19, 93, 26, 85, 87, 0, 15, 80, 23, 78, 78, 33, 36, 31, 72, 57, 0, 40, 28, 56, 8, 62, 78, 95, 31, 51, 39, 0, 14, 73, 75, 60, 38, 97, 21, 43, 44, 17, 23, 79, 69, 10, 95, 73, 8, 30, 70, 43, 2, 7, 30, 68, 59, 79, 4, 50, 96, 19, 90, 23, 67, 15, 85, 27, 61, 10, 15, 62, 64, 30, 36, 11]
# print(f'Our list is {len(list_of_values)} values long.')

# set_of_values = set(list_of_values)
# print(f'Our list is {len(set_of_values)} values long.')

# dictionary_for_count = {} # Notice the dictionary has the same {} sets have
# for value in set_of_values:
#   dictionary_for_count[value] = list_of_values.count(value)
# print(dictionary_for_count)

################################################################
# Python 3.1
################################################################

# import random

# def sum_two_number_ter(number1, number2):
#    resultat=number1 + number2
#    print(f"the sum of {number1} + {number2} is equal to {resultat} ")
#    if resultat<10: return (f"your result {resultat} is less than 10")
#    elif resultat >= 10 and resultat <= 50: return(f"your result {resultat} is between 10 and 50")
#    else:return(f"your result {resultat} is greater than 50")


# # test de la fonction
# first_number=random.randint(1,30) # creation d'un chiffre aleatoire entre 1 et 30
# second_number=random.randint(1,20)
# sum_two_number_ter (first_number,second_number)

################################################################
"""

"""
# import random
# # Mission 2: Create a function that takes in 2 numbers as parameters, and returns a boolean indicating whether or not they are equal
# def sum_two_number_equal(number1, number2):
#    resultat=number1 + number2
#    print(f"the number {number1} + {number2} {'are not' if not number1==number2 else 'are' } equal ")
#    if  not number1==number2:
#     return False
#    else: return True


# # test de la fonction
# first_number=random.randint(1,3) # creation d'un chiffre aleatoire
# second_number=random.randint(1,3)
# sum_two_number_equal (first_number,second_number)
################################################################

# Mission 3: Create a function that takes a number as parameter, and returns the first 10 multiples of the number as a list
# Example: 2 -> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# import random

# def multiple_of_ten(number1):
#     resultat=[]
#     resultat=[number1*i for i in range(1,11) ]
#     print(f"liste des 10 premiers multiples de {number1} -> {resultat}")
#     return resultat


# # # test de la fonction
# number=random.randint(1,10) # creation d'un chiffre aleatoire
# multiple_of_ten (number)
################################################################
# # Mission 4: Create a function that takes a string as input, and return its vowels only, preserving case.
# # Example: "Antidisestablishmentarianism" -> "Aiieaieaiai"
# # Example: "TO BE OR NOT TO BE" -> "OEOOOE"
# import random
# import string

# def get_vowels(string_one):
#     list_vowels=[]
#     voyelles = 'aeiouAEIOU'
#     list_vowels="".join(vowel for vowel in string_one  if vowel in voyelles)
#     print(f" {f"liste des voyelles:'{list_vowels}' dans le mot '{string_one}'" if  len(list_vowels) !=0 else f"il n'y a pas de de voyelles dans le mot '{string_one}'"}")
#     # print(f" {"ok" if not len(list_vowels)==0 else "pas ok"}")
#     return


# # # test de la fonction
# string_one=''.join(random.choice(string.ascii_letters + '   ') for _ in range(25)) # création d'une chaine de caracteres avec des minuscules et majuscules
# string_one=' '.join(word for word in string_one.split() if len(word) > 2) # à partir chaine de caracteres création d'un phrase par splitant avec des mots de 3 mini

# get_vowels (string_one)
# # string_one="".join((random.choice(string.ascii_letters)+ (random.choice(" ") for _ in range(0,1)) )for _ in range(25) ) # creation d'une phrase avec des mots aleatoire avec des minuscules et des majuscules
# # string_one=string_one.strip()
# # string_one="".join(random.choice(string.ascii_letters) for _ in range(25) ) # creation d'une phrase avec des mots aleatoire avec des minuscules et des majuscules
################################################################
# # creation d'une phrase
# import random
# import string

# def generate_word(min_length=2): # taille minimale des mots
#     length = random.randint(min_length, 10)  # Longueur du mot
#     return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# def generate_sentence(max_length=25): #taille maxi de la phrase
#     sentence = ''
#     while len(sentence) < max_length:
#         word = generate_word()
#         if len(sentence) + len(word) + 1 > max_length:  # +1 pour l'espace
#             break
#         sentence += word + ' '
#     print(sentence.rstrip())
#     return sentence.rstrip()  # Supprime l'espace final

# output = generate_sentence()

################################################################
# Mission 5: Create a function that takes 2 numbers as parameters, and returns the result of a division operation.
# Test if the denominator is equal to 0 and if so, display a message that says: "You can't divide by zero".

# import random

# def division_number(a, b):
#     if b != 0:
#         result=a/b
#         result=round(result,2)
#         print(f"Division de {a} par {b} = {result}")
#         return result
#     else:
#         print("Erreur : You can't divide by zero")

# # test de la fonction
# first_number=random.randint(-10,10)
# second_number=random.randint(0,10)
# division_number(first_number, second_number)
################################################################
# # Mission 6: First, choose two arithmetical operations (such as +, -, *, or /)
# # Then, create a function that takes in 3 numbers as parameters and carries out those operations, displays a message indicating if the result is positive, negative or zero, and finally returns the result.
# # If a division by zero is attempted, display an error message.

# # Example with multiplication and addition:
# # Calling with 0, 32, 2 will compute (0*32)+2, will display "Positive result", and return 2

# # Example with division and addition:
# # Calling with 21, 0, 3 will try to compute (21/0)+2, will display "Divide-by-zero error"
# import random

# def calculate_rate_vecor(numbers):
#     print(numbers)
#     if len(numbers) < 2:
#         return "Erreur : la liste doit contenir au moins deux nombres"
#     if numbers[0] == 0:
#         print("Erreur : division par zéro")
#         return
#     division_rate = numbers[1]/numbers[0]
#     # print(division_rate)
#     sum_last_numbers=sum(numbers[3:]) # on additionne tous les termes à partir de 3éme
#     print(sum_last_numbers)
#     result = division_rate + numbers[2] + sum_last_numbers
#     # if sum_last_numbers >= 0 : result = division_rate + numbers[2]+ sum_last_numbers
#     result=round(result,2)
#     cas1=" + " if numbers[2]>0 else ' - '
#     cas2="+ la somme des autres chiffres " if sum_last_numbers >=0 else "- la somme des autres chiffres "
#     print(f"le resultat de {numbers[0]}/{numbers[1]}{cas1}{abs(numbers[2])} {cas2}({sum_last_numbers}) = {result}   ")
#     return
#     # print(f"le resultat de {numbers[0]}/{numbers[1]}{" + " if numbers[2]>0 else ' - '}{abs(numbers[2])} {"+ la somme des autres chiffres " if sum_last_numbers >=0 else "- la somme des autres chiffres "}({sum_last_numbers}) = {result}   ")
#     # return


# # test
# if __name__ == '__main__':
#     # numbers = [1, 2, 3]
#     numbers = [random.randint(-5,5) for _ in range(5)] # création d'une liste de chiffres aleatoires
#     calculate_rate_vecor(numbers)


################################################################
# Mission 7: Create a function that takes a number as a parameter that corresponds to gross salary and returns the net salary for executives.
# You can specify any amount of deductions, or base them on your country's example
# import random
# import locale
# from colorama import Fore, Style
# def calculate_net_salary(salary):
#     resultat=[]
#     rate_charge=23.6
#     resultat=salary*(100-rate_charge)/100
#     charge=salary - resultat
#     #  français pour le formatage des salaires
#     locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
#     salary_str = locale.format_string("%d", salary, grouping=True)
#     resultat_str = locale.format_string("%.2f", resultat, grouping=True)
#     charge_str=locale.format_string("%.2f", charge, grouping=True)
#     print(f"Votre salaire brut de\n {Fore.GREEN}{salary_str}€{Style.RESET_ALL} \ncorrespond à un salaire net de :\n {Fore.GREEN}{resultat_str}{Style.RESET_ALL}€ \navec un taux de {Fore.GREEN}{rate_charge}{Style.RESET_ALL} %  soit\n {Fore.GREEN}{charge_str}€{Style.RESET_ALL}\n de charges ")
#     return resultat


# # # test de la fonction
# number=random.randint(42153,90563) # creation d'un salaire aleatoire
# calculate_net_salary(number)



################################################################
# Mission 8: Create a function that can swap the values of any two variables,
# such as if variable A = 1 and variable B = 2, after applying the function, variable A = 2 and B = 1
import random
def swap_number(a, b):
    print(a,b)
    a,b=b,a
    print(a,b)
    return



# # test de la fonction
number1=random.randint(1,10) # creation d'un nombre aleatoire
number2=random.randint(1,10) # creation d'un nombre aleatoire
swap_number(number1, number2)

################################################################
# OS et GLOB
################################################################
import os
import glob
# repertoire actuel
repertoire_actuel=os.getcwd()
print("repertoire_actuel:",repertoire_actuel)

# liste des repertoire du dossier
print("liste des fichiers")
print(glob.glob("*"))
print("liste des fichiers txt")
print(glob.glob("*.txt"))  #filtre les fichiers txt
print("liste des repertoires")
print(glob.glob(repertoire_actuel))

filenames=glob.glob("*.py")
print("liste des fichiers python",filenames)

# lecture du contenu de tous les fichiers python de mon repertoire
for file in filenames:
    with open(file,'r') as f:
        print(f.read() )
    f.close()


with open("fichier.txt", "r") as f:
    liste=f.read().splitlines()

liste=[line.strip() for line in open("fichier.txt", "r")]

#############################################
#############################################
#############################################
