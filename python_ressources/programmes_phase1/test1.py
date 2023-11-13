import threading
from concurrent.futures import ThreadPoolExecutor
import os
import psutil
import random
import timeit
import time
from IPython.core.magics import *

livre = "km Zéro"
auteur = "Maude Ankaoua"
year = 2023
print(livre)
print("hello World")
# print ("à suivre")
print(f"un des meilleurs bouquin est {livre} de {auteur}")
print("un des meilleurs bouquin est " + livre +
      " de " + auteur + " en " + str(year))
# str $livre
# -----------------

plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
plateformes_sociales[1]

langage_de_programmation = "PYTHYONY"
print(langage_de_programmation[2])
print(langage_de_programmation[-1])

len(langage_de_programmation)

# -----------------
plateformes_sociales.append("X")
plateformes_sociales.remove("Facebook")
len(plateformes_sociales)

print(langage_de_programmation.count("Y"))
print(langage_de_programmation.index("Y"))

plateformes_sociales_tuple = (
    "Isap", "Facebook", "Instagram", "TikTok", "X", "Twitter")

resultat = "vrai" if "X" in plateformes_sociales_tuple else "faux"
print(resultat)
resultat = "vrai" if "A" in plateformes_sociales_tuple else "faux"
print(resultat)

nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

res = nouvelle_campagne["nom_de_campagne"]
print(res)
res = nouvelle_campagne["influenceurs_importants"]
print(res)

# -----------------
taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
# -----------------

taux_de_conversion_bis = dict()
taux_de_conversion_bis['facebook'] = 3.4
taux_de_conversion_bis['instagram'] = 1.2
res1 = len(taux_de_conversion_bis)
print(res1)

# -----------------

taux_de_conversion["X"] = 666
res2 = len(taux_de_conversion)
print("res2=" + str(res2))
res = taux_de_conversion["X"]
print(taux_de_conversion)
print(taux_de_conversion_bis)
print(res1)

# -----------------

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

# [['a', 'b', 'c'], [1, 2, 3]]
x[0]
# ['a', 'b', 'c']
# x[0][1]
print(x[1][0])  # 1
# -----------------

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
c, d = 0, 1
while a < 10:
    print("fibonacci: \n" + str(a))
    print('fibonacci2: ', c)
    # print(a)
    a, b = b, a+b
    c, d = d, c+d

# -----------------
i = 256*256
print('The value of i is', i)
# -----------------

# x = int(input('PLease enter a number: '))
min = -10
max = 10
x = random.randint(min, max)
print('The random value of x between ', min, ' to ', max, ' is', x)

if x < 0:
    x = 0
    print(' negative integers are convert into 0')
    print('The value of x=', x)
elif x == 0:
    print('Zero')
elif x == 1:
    print('One')
else:
    print('more')
# -----------------

for word in plateformes_sociales_tuple:
    print(word, len(word))


# -----------------

# Strategy:  Iterate over a copy
users1 = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users1.copy().items():
    if status == 'inactive':
        del users1[user]
print(users1)

# Strategy:  Create a new collection
users2 = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users2.items():
    if status == 'active':
        active_users[user] = status
# print(users2)
print(active_users)

# -----------------
for i in range(5):
    print(i)
print(list(range(5, 10)))
print(list(range(2023, 3012, 10)))
# -----------------
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# -----------------
sum(range(4))  # 0 + 1 + 2 + 3
# -----------------

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        print(n, ' is a prime number')

# -----------------

# mesure du temps d'execution de la fonction et de sa consommation memoire et CPU
# nombre d'execution de la boucle for afin de mesurer sa performance
# pour cela il faut faire les imports suivants:

    # import psutil
    # import timeit
    # from IPython.core.magics import *
    # import os
# # Pour limiter le programme à un seul thread
# from concurrent.futures import ThreadPoolExecutor

# with ThreadPoolExecutor(max_workers=1) as executor:
nombre_execution = 100
temps_execution = timeit.timeit(stmt='''for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        print(n, ' is a prime number')''',
                                number=nombre_execution)  # nombre d'execution de la boucle for afin de mesurer sa performance
# pour un affichage en s
print('Temps d\'exécution:', round(temps_execution, 3), 'secondes')
# pour un affichage en millisecondes
print(f"Temps d'exécution: {round(temps_execution * 1000)} millisecondes")

# -----------------

# Mesure la charge CPU
cpu_percent = psutil.cpu_percent()

# Mesure la consommation de mémoire
memory_info = psutil.Process().memory_info().rss

print(f"Charge CPU: {cpu_percent}%")
print(f"Consommation mémoire: {round(memory_info, 3)} octets")
# -----------------
# idem avec un affichage en Koctet ou Moctet et non en octet

# Afficher la charge CPU

process = psutil.Process(os.getpid())
memory_info = process.memory_info().rss / 1024 / 1024  # Convertir en Mo
print(f"Consommation mémoire: {round(memory_info)} Mo")
# Afficher les fichiers ouverts
fichiers_ouverts = process.open_files()
print(f"Fichiers ouverts: {len(fichiers_ouverts)}")

# Afficher le nombre de threads exécutés
nb_threads = process.num_threads()
print(f"Nombre de threads: {nb_threads}")
# -----------------
# Pour limiter le programme à un seul thread

# with ThreadPoolExecutor(max_workers=1) as executor:
# import timeit

nombre_execution = 100

# La fonction à exécuter


def programme_check():
    for n in range(2, 100):
        for x in range(2, n):
            if n % x == 0:
                print(n, '=', x, '*', n // x)
                break
        else:
            print(n, ' is a prime number')


with ThreadPoolExecutor(max_workers=1) as executor:
    programme_check()

# Mesurer le temps d'exécution
temps_execution = timeit.timeit(stmt=programme_check, number=nombre_execution)

# pour un affichage en s
print('Temps d\'exécution:', round(temps_execution, 3), 'secondes')

#  Afficher la charge CPU

process = psutil.Process(os.getpid())
memory_info = process.memory_info().rss / 1024 / 1024  # Convertir en Mo
print(f"Consommation mémoire: {round(memory_info)} Mo")
# Afficher les fichiers ouverts
fichiers_ouverts = process.open_files()
print(f"Fichiers ouverts: {len(fichiers_ouverts)}")

# Afficher le nombre de threads exécutés
nb_threads = process.num_threads()
print(f"Nombre de threads: {nb_threads}")
# L'ajustement du code pour exécuter dans un seul thread se fait
# en encapsulant simplement votre boucle for dans une fonction
# et en mesurant le temps d'exécution de cette fonction avec timeit.

# -----------------
# import concurrent.futures

# # Définir la fonction programme_check
# def programme_check2(n):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} = {x} * {n // x}")
#             break
#     else:
#         print(f"{n} is a prime number")

# # Créer une liste d'entrée
# input_list2 = list(range(2, 100))

# # Créer un objet ThreadPoolExecutor avec max_workers=1
# with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#     # Exécuter la fonction programme_check sur chaque élément de la liste d'entrée
#     results = executor.map(programme_check2, input_list2)

# # Itérer sur l'objet générateur pour afficher les résultats
# for result in results:
#     pass

# # Mesurer le temps d'exécution
# temps_execution = timeit.timeit(stmt=programme_check2(10), number=nombre_execution)

# # pour un affichage en s
# print('Temps d\'exécution:', round(temps_execution, 3), 'secondes')

# #  Afficher la charge CPU
# process = psutil.Process(os.getpid())
# memory_info = process.memory_info().rss / 1024 / 1024  # Convertir en Mo
# print(f"Consommation mémoire: {round(memory_info)} Mo")
# # Afficher les fichiers ouverts
# fichiers_ouverts = process.open_files()
# print(f"Fichiers ouverts: {len(fichiers_ouverts)}")

# # Afficher le nombre de threads exécutés
# nb_threads = process.num_threads()
# print(f"Nombre de threads: {nb_threads}")

# -----------------


# Définir la fonction à exécuter dans le thread
# def my_function():
#     while not stop_flag:
nombre_execution = 10

# La fonction à exécuter


def programme_check3(n):
    while not stop_flag:
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} = {x} * {n // x}")
                break
        else:
            print(f"{n} is a prime number")
            print("Hello from the thread!")


# Créer un drapeau pour indiquer que le thread doit s'arrêter
stop_flag = False

# Créer un nouvel objet Thread
# thread = threading.Thread(target=programme_check2)
thread = threading.Thread(
    target=lambda: [programme_check3(10) for n in range(2, 100)])

# Démarrer le thread
thread.start()

# Arrêter le thread en modifiant la valeur du drapeau
stop_flag = True

# Attendre que le thread se termine
thread.join()

# MESURES PERFORMANCE
# Mesurer le temps d'exécution
# temps_execution = timeit.timeit(lambda: thread.start(), number=nombre_execution)
# temps_execution = timeit.timeit(lambda: [programme_check3(10) for n in range(2, 100)], number=nombre_execution)
temps_execution = timeit.timeit(
    stmt=programme_check3(10), number=nombre_execution)
# pour un affichage en s
print('Temps d\'exécution:', round(temps_execution, 3), 'secondes')
# pour un affichage en millisecondes
print(f"Temps d'exécution: {round(temps_execution * 1000)} millisecondes")
#  Afficher la charge CPU
process3 = psutil.Process(os.getpid())
memory_info3 = process3.memory_info().rss / 1024 / 1024  # Convertir en Mo
print(f"Consommation mémoire: {round(memory_info3)} Mo")
# Afficher les fichiers ouverts
fichiers_ouverts3 = process3.open_files()
print(f"Fichiers ouverts: {len(fichiers_ouverts3)}")
# Afficher le nombre de threads exécutés
nb_threads3 = process3.num_threads()
print(f"Nombre de threads: {nb_threads3}")

# -----------------
plateformes_sociales.key()
# -----------------
print("\n\n end \n\n")
# -----------------
