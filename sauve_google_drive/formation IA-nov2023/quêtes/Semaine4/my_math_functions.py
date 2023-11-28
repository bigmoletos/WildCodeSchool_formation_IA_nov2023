import random

# 1 Square of a number: Create a function that returns the square of a number.


def calculate_square(nombre):
    return nombre*nombre

# -----------
# test de la fonction
# nombre_utilisateur=20
# print(calculate_square(nombre_utilisateur))


# 2 Cube of a number: Create a function that returns the cube of a number.
def calculate_cube(nombre):
    return nombre*nombre*nombre

# -----------
# test de la fonction
# nombre_utilisateur=2
# print(calculate_cube(nombre_utilisateur))

# 3 Absolute value: Create a function that returns the absolute value of a number.


def get_absolute_value(nombre):
    if nombre < 0:
        nombre *= -1
    return nombre

# -----------
# test de la fonction
# nombre_utilisateur=-2
# print(get_absolute_value(nombre_utilisateur))

# 4 Factorial of a number: Create a function that returns the factorial of a number.


def factorielle_number(nombre):
    resultat = 1
    for i in range(1, nombre+1):
        resultat *= i
    return resultat

# -----------
# test de la fonction
# nombre_utilisateur=5
# print(factorielle_number(nombre_utilisateur))

# from sre_constants import MAX_REPEAT
# 5 Mode of a list of numbers: Create a function that returns the mode of a list of numbers, for instance [68, 99, 65, 44, 77, 44, 44] --> 44.
# en francais on doit trouver l'élement le plus courant dans la liste


def mode_of_list(my_list):
    max_occurence = 0
    nombre_occurences = {}
    for i in my_list:
        if i in nombre_occurences:
            nombre_occurences[i] += 1
            # print(nombre_occurences," :", i)
        else:
            nombre_occurences[i] = 1
            # print(nombre_occurences," :", i)
    # print(nombre_occurences," :", i)
    # the_mode=max(nombre_occurences, key=nombre_occurences.get)  #solution courte mais utilisant la fonction max
    max = 0
    for k, v in nombre_occurences.items():

        the_mode = k
        if v > max:
            max += 1
            the_mode = k
            # print(max," v", v,"mode ",the_mode)
        # print(k,v)
    return the_mode

# #-----------
# # test de la fonction
# list_of_number=[68, 99,77, 65, 44, 77, 44, 44]
# print(mode_of_list(list_of_number))

# import random
# 6 Average of a list of numbers: Create a function that returns the average of a list of numbers.


def average_list(my_list):
    the_average = 0
    the_sum = 0
    # nombre_occurences={}
    for i in my_list:
        the_sum += i
        # print(" i", i, "mode ", the_sum)
        # print(k,v)
    the_average = the_sum/len(my_list)
    return the_average

# #-----------
# # test de la fonction
# list_of_number=[random.randint(0,50) for v in range(5) ]
# # list_of_number=[10, 10,10, 10, 44, 77, 44, 44]
# print("liste:",list_of_number," moyenne liste:",average_list(list_of_number))

# 7 Minimum of a list of numbers: Create a function that returns the minimum from within a list of numbers.


def minimum_of_list(my_list):
    the_minimum = my_list[0]
    if len(my_list) == 0:
        return None
    for i in my_list:
        # print(i)
        if i < the_minimum:
            the_minimum = i

    # print(the_minimum)
    return the_minimum

# #-----------
# # test de la fonction
# list_of_number=[random.randint(0,50) for v in range(5) ]

# print("liste:",list_of_number," le minimum de la liste est le :",minimum_of_list(list_of_number))


# 8 Maximum of a list of numbers: Create a function that returns the maximum from within a list of numbers.
def maximum_of_list(my_list):
    the_maximum = my_list[0]
    if len(my_list) == 0:
        return None
    for i in my_list:

        if i > the_maximum:
            the_maximum = i

    return the_maximum

# #-----------
# # test de la fonction
# list_of_number=[random.randint(0,50) for v in range(5) ]

# print("liste:",list_of_number," le minimum de la liste est le :",maximum_of_list(list_of_number))
