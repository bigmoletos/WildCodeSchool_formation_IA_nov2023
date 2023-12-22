import random
groups = {"groupe_1": ["Lam", "Ghizlaine", "Khaled", "Florian"],
          "groupe_2": ["Lucille", "Mbaye", "Cécile", "Rohan"],
          "groupe_3": ["Agathe", "Charlotte", "Charles", "Maxime"],
          "groupe_4": ["Gaelle", "Linh", "Meral"]}


for i in groups.values():
    print(i)
#   print(groups.values()[:i])
    print(type(i))

for i in groups.values():
    for v in i:
        print(v)
################################################################
""""
Mission 1
Below is a dictionary containing the number of French campuses that
 offer each kind of Wild Code School course.

wildcodeschool = { "data_analyst": 4, "data_scientist": 2, "dev_web": "13" }

Find a way to only display the keys that have int values.
"""
wildcodeschool = {
    "data_analyst": 4,
    "data_scientist": 2,
    "dev_web": "13"}
print(wildcodeschool)
list = {key: value for key, value in wildcodeschool.items()
        if isinstance(value, int)}
print(list)

################################################################
# Mission 8: Create a function that can swap the values of any two variables,
# such as if variable A = 1 and variable B = 2, after
# applying the function, variable A = 2 and B = 1


def swap_number(a, b):
    print(a, b)
    a, b = b, a
    print(a, b)
    return


# # test de la fonction
number1 = random.randint(1, 10)  # creation d'un nombre aleatoire
number2 = random.randint(1, 10)  # creation d'un nombre aleatoire
swap_number(number1, number2)
