# Déclaration d'une variable
int x = 10;

# Opérations arithmétiques
int y = x + 1;

# Conditions
if (x > 5) {
  print("x est plus grand que 5");
}

# Boucles
for (int i = 0; i < 10; i++) {
  print(i);
}

# Fonctions
function add(int x, int y) {
  return x + y;
}

print(add(1, 2)); # affiche "3"

import mojo.hardware.gpu

# Accélérer le calcul de la fonction sinus
gpu.sin(x);

# Accélérer le calcul de la fonction cosinus
gpu.cos(x);

import numpy as np

# Calculer la fonction sinus
x = np.pi / 2
y = np.sin(x);

# Calculer la fonction cosinus
x = np.pi / 2
y = np.cos(x);



# Extrait de code
int x = 10;
int y = x + 1;
print(y); # affiche 11

# Voici un autre exemple de code Mojo qui utilise une boucle pour imprimer les nombres de 1 à 10 :

for (int i = 1; i <= 10; i++) {
  print(i);
}


mojo --version
Mojo version 1.0.0

# Mojo

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

print(matrix[0][0]); # affiche 1
print(matrix[1][1]); # affiche 5
print(matrix[2][2]); # affiche 9

#  Python
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

print(matrix[0][0]); # affiche 1
print(matrix[1][1]); # affiche 5
print(matrix[2][2]); # affiche 9

# Mojo
int x = 1000000000000000000;
int y = 2000000000000000000;

print(x + y); # affiche 3000000000000000000
#  Python
x = 1000000000000000000
y = 2000000000000000000

print(x + y); # affiche une erreur


FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl wget

RUN curl -LO https://github.com/modular-systems/mojo/releases/download/1.0.0/mojo-linux-amd64-1.0.0.tar.gz

RUN tar -xf mojo-linux-amd64-1.0.0.tar.gz

RUN mv mojo-linux-amd64-1.0.0/mojo /usr/local/bin/mojo

ENTRYPOINT ["mojo"]

# Mojo
def for_loop(n):
    for i in range(n):
        _ = 0

for_loop(1000000)

# Python
def for_loop(n):
    for i in range(n):
        pass

for_loop(1000000)


# Python
def square(x):
    return x * x

def for_loop_with_function(n):
    for i in range(n):
        square(i)

for_loop_with_function(1000000)

# Mojo
def square(x):
    return x * x

def for_loop_with_function(n):
    for i in range(n):
        _ = square(i)

for_loop_with_function(1000000)

# Python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def for_loop_with_recursive_function(n):
    for i in range(n):
        factorial(i)

for_loop_with_recursive_function(1000000)

# Mojo
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def for_loop_with_recursive_function(n):
    for i in range(n):
        _ = factorial(i)

for_loop_with_recursive_function(1000000)


# Python
def for_loop_with_nested_loops(n):
    for i in range(n):
        for j in range(n):
            pass

for_loop_with_nested_loops(1000000)

# Mojo
def for_loop_with_nested_loops(n):
    for i in range(n):
        for j in range(n):
            _ = 0

for_loop_with_nested_loops(1000000)


# Python
def for_loop_with_while_loop(n):
    i = 0
    while i < n:
        pass
        i += 1

for_loop_with_while_loop(1000000)

# Mojo
def for_loop_with_while_loop(n):
    i = 0
    while i < n:
        _ = 0
        i += 1

for_loop_with_while_loop(1000000)


#  calcul de la transformée de Fourier d'une image de 100 pixels de large et 100 pixels de haut.
 import numpy as np

def python_fft2d(x):
    return np.fft.fft2(x)

def mojo_fft2d(x):
    return mojo.fft2d(x)

x = np.random.randn(100, 100)

print("Temps de calcul en Python :", timeit.timeit(python_fft2d, args=(x,), number=1))
print("Temps de calcul en Mojo :", timeit.timeit(mojo_fft2d, args=(x,), number=1))
