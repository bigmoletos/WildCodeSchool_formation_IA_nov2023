import my_math_functions as my
import random
#   variables
nombre1=random.randint(-10,50)
nombre2=3
list_of_number=[random.randint(0,50) for v in range(10) ]


# test fonctions
print(my.calculate_square(nombre1))
print(my.calculate_cube(nombre1))
print(my.get_absolute_value(nombre1))
print(my.factorielle_number(nombre1))

# test fonctions list
print("\n\n",list_of_number)

print(my.mode_of_list(list_of_number))
print(my.average_list(list_of_number))
print(my.minimum_of_list(list_of_number))
print(my.maximum_of_list(list_of_number))

# Projets/Toys_and_models/Toys_and_models/Toys_and_models-20231125.dbp
# Projets/Toys_and_models/PROJET 1 _ SQL Model company FR.docx
# sauve_google_drive/formation IA-nov2023/quêtes/Semaine1/franck-quête Exceler à Excel semaine1.xlsx