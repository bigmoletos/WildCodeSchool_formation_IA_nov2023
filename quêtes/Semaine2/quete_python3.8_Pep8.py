# import random
# groups = {"groupe_1": ["Lam", "Ghizlaine", "Khaled", "Florian"],
#           "groupe_2": ["Lucille", "Mbaye", "Cécile", "Rohan"],
#           "groupe_3": ["Agathe", "Charlotte", "Charles", "Maxime"],
#           "groupe_4": ["Gaelle", "Linh", "Meral"]}


# for i in groups.values():
#     print(i)
# #   print(groups.values()[:i])
#     print(type(i))

# for i in groups.values():
#     for v in i:
#         print(v)
# ################################################################
# """"
# Mission 1
# Below is a dictionary containing the number of French campuses that
#  offer each kind of Wild Code School course.

# wildcodeschool = { "data_analyst": 4, "data_scientist": 2, "dev_web": "13" }

# Find a way to only display the keys that have int values.
# """
# wildcodeschool = {
#     "data_analyst": 4,
#     "data_scientist": 2,
#     "dev_web": "13"}
# print(wildcodeschool)
# list = {key: value for key, value in wildcodeschool.items()
#         if isinstance(value, int)}
# print(list)

# ################################################################
# # Mission 8: Create a function that can swap the values of any two variables,
# # such as if variable A = 1 and variable B = 2, after
# # applying the function, variable A = 2 and B = 1


# def swap_number(a, b):
#     print(a, b)
#     a, b = b, a
#     print(a, b)
#     return


# # # test de la fonction
# number1 = random.randint(1, 10)  # creation d'un nombre aleatoire
# number2 = random.randint(1, 10)  # creation d'un nombre aleatoire
# swap_number(number1, number2)

# # Caractéristiques de l'opération d'intersection entre deux listes


# class lists_inter:
#     def __init__(self, count_CommonElem, list1Num, list2Num):
#         self.count_CommonElem = count_CommonElem
#         self.list1Num = list1Num
#         self.list2Num = list2Num

# # Fonction de tri de la liste <listOf_lists_inter>


# def lists_inter_sort(e):
#     return e.count_CommonElem

# # Création d'une liste d'entiers aléatoires entre [a, b] et dont le nombre est aléatoire et appartient à [min, max]


# def intList_create(a, b, min, max):
#     numbers = []
#     maxLen = random.randint(min, max)
#     for i in range(0, maxLen):
#         numbers.append(random.randint(a, b))
#     return numbers

# # Nb. d'éléments communs des deux listes


# def count_CommonElm(list1, list2):
#     l1, l2 = len(list1), len(list2)
#     count = 0
#     if l1 < l2:
#         for i in range(0, l1):
#             n = list2.count(list1[i])
#             if n != 0:
#                 count += 1
#     else:
#         for i in range(0, l2):
#             n = list1.count(list2[i])
#             if n != 0:
#                 count += 1
#     return count


# # Création des listes et affichage des listes
# lists = []
# countList = 10
# for i in range(0, countList):
#     lists.append(intList_create(10, 50, 5, 15))
#     print("Liste", i + 1, ":", lists[i])

# # Les 2 listes ayant le plus grand nb. commun d'éléments parmi les <countList> listes
# listOf_lists_inter = []
# for i in range(0, countList):
#     for j in range(i + 1, countList):
#         n = count_CommonElm(lists[i], lists[j])
#         listOf_lists_inter.append(lists_inter(n, i + 1, j + 1))
# listOf_lists_inter.sort(reverse=True, key=lists_inter_sort)
# print("Les listes ", listOf_lists_inter[0].list1Num, "et", listOf_lists_inter[0].list2Num,
#       "ont le plus grand nb. d'éléments communs :", listOf_lists_inter[0].count_CommonElem)


# Mission 6: First, choose two arithmetical operations (such as +, -, *, or /)
# Then, create a function that takes in 3 numbers as parameters and carries out those operations, displays a message indicating if the result is positive, negative or zero, and finally returns the result.
# If a division by zero is attempted, display an error message.

# Example with multiplication and addition:
# Calling with 0, 32, 2 will compute (0*32)+2, will display "Positive result", and return 2

# Example with division and addition:
# Calling with 21, 0, 3 will try to compute (21/0)+2, will display "Divide-by-zero error"
import os
import glob


# repertoire actuel
repertoire_actuel=os.getcwd()
print(repertoire_actuel)

# liste des repertoire du dossier
print(glob.glob("*"))
print(glob.glob(".txt"))  #filtre les fichiers txt

print(glob.glob(repertoire_actuel))

filenames=glob.glob(".py")

# lecture du contenu de tous les fichiers python de mon repertoire
for file in filenames:
    with open(file,'r') as f:
        f.readlines()
