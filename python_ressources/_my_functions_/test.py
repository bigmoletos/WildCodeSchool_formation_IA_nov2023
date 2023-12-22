import random
import numpy as np
from matplotlib import pyplot as plt

tests=[]
liste=["franck","Eric","michel","imad","paul","fabrice","yvan"]

#  Effectuer 1000 tests
nombre_de_tests=1000
tests = [random.choice(liste) for _ in range(nombre_de_tests)]

# Créer un dictionnaire pour compter les occurrences
occurrences = {candidat: tests.count(candidat) for candidat in liste}
print(occurrences)
print(tests.count(occurrences))

# Calculer la moyenne
moyenne = {candidat: occ / nombre_de_tests for candidat, occ in occurrences.items()}

print(f"{moyenne}")
# crée une liste de 100 points aléatoires tirés d’une distribution normale standard
#  (c’est-à-dire une distribution gaussienne avec une moyenne de 0 et un écart type de 1)
# avec comme point de départ 200 (represente la moyenne) donc entre 199 et 201
ys = 200 + np.random.randn(100)
y_randint =  np.random.randint(0, 10)
# y_randint=str(y_randint)
# print("ys",ys)
print("y_randint",y_randint)
x = [x for x in range(len(ys))]
x_randint = [x for x in range(len(str(y_randint)))]
print("x ",x)
print("x_randint ",x_randint)
# plt.plot(x, ys, '-')
# plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='y', alpha=0.9)
plt.plot(x_randint, y_randint, '-')
plt.fill_between(x_randint, y_randint, 10, where=(y_randint > 0.01), facecolor='y', alpha=0.9)

plt.title("Sample Visualization")
plt.show()
