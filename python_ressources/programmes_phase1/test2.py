"""programme d'apprentissage de Python via opnclassroom oct2023"""
from datetime import datetime, timedelta
# from traitement_date import date_du_jour_long, intervalle_entre_dates, date_du_jour_court
from traitement_date import *
from _my_functions_._my_traitement_date_ import today_court, today_long, between_2dates


nom_contact = {"nom": "Jackson"}
# print(nom_contact.keys())
# print(nom_contact.values())

contact_infos = {"nom": "Jackson", "prenom": "Michael",
                 "telephone": "123-456-7890", "email": "j.michael@email.com"}
contact_infos["email"] = "jackson.michael@email.com"

# print(contact_infos)
# print(contact_infos.get("email"))
# print(contact_infos["email"])
# print(contact_infos.get("nom"))

contacts = []
contacts.append(contact_infos)
print(contacts)

# Créer une liste vide
ma_liste = []

# Ajouter un élément à la fin de la liste
ma_liste.append(1)

# Ajouter un élément à une position spécifique dans la liste
ma_liste.insert(0, 2)

# Ajouter plusieurs éléments à la fin de la liste
ma_liste.extend([3, 4, 5])

# Afficher la liste
# print(ma_liste)

nombre_de_sieges = 30
nombre_dinvites = 30

if nombre_dinvites < nombre_de_sieges:
    # autoriser plus d’invités
    print("il nous reste encore ", nombre_de_sieges-nombre_dinvites, " places")
elif nombre_dinvites == nombre_de_sieges:
    # ne pas autoriser plus d’invités
    print("nous sommes complets")
else:
    print("nous avons ", nombre_dinvites-nombre_de_sieges, " invités en trop")

resultat = "libre"
match resultat:
    case "correct":
        print("correct")
    case "libre":
        print("libre")
    case "full":
        print("full")

liste = [1, 2, 3, 4, 5]
# Boucle for sur la liste
for element in liste:
    if element == 3:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
    # Dans tous les autres cas, on exécute le reste du code
    print(element, "continue")


# Boucle for sur la liste
for element in liste:
    if element == 3:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        break
    # Dans tous les autres cas, on exécute le reste du code
    print(element, "break")

# ______________


# def print_welcome_message():
#     print("Bienvenue sur la mini-calculatrice !")

# """This is a docstring which describes the module"""
# #input des 2 nombres
# def input_two_number():
#     num1 = float(input("Entrez le premier nombre : "))
#     num2 = float(input("Entrez le deuxième nombre : "))
#     return num1, num2


# def print_menu_and_get_choice():
#     print("=== MENU ===")
#     print("1. Addition")
#     print("2. Soustraction")
#     print("3. Multiplication")
#     print("4. Division")

#     user_choice = input("Entrez votre choix (1-4) : ")

#     while user_choice not in ["1", "2", "3", "4"]:

#         user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

#     return user_choice


# def somme(a, b):
#     return a + b


# def substraction(a, b):
#     return a - b


# def multiplication(a, b):
#     return a * b


# def division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("Erreur : division par zéro")


# def run_calculation(user_choice):
#     num1, num2 = input_two_number()
#     match user_choice:
#         case '1':
#             result = sum(num1, num2)
#         case '2':
#             result = substraction(num1, num2)
#         case '3':
#             result = multiplication(num1, num2)
#         case '4':
#             result = division(num1, num2)
#         case _:
#             print("Choix invalide.")
#     return result


# if __name__ == '__main__':
#     print_welcome_message()
#     user_choice = print_menu_and_get_choice()
#     result = run_calculation(user_choice)
#     print(result)

ten_list = [[] for _ in range(10)]
print(ten_list)


start_date = datetime(2023, 1, 1)  # Date de départ
four_list = [["car", str(i), (start_date + timedelta(days=i)
                              ).strftime('%d-%m-%Y')] for i in range(10)]
print(four_list)

print(date_du_jour_long())
print(date_du_jour_court())

jours = intervalle_entre_dates(date_du_jour_court(), '06-11-2023')
print("Il y a ", jours, "jours entre ces deux dates.")

# idem depuis le package _my_fucntions_
print(today_long())
print(today_court())
jours = between_2dates(today_court(), '06-11-2023')
print("Il y a ", jours, "jours entre ces deux dates.")


