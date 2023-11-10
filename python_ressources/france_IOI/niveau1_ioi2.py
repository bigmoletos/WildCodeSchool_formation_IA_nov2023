# //correction java
class Main {
public static void main(String[] args) {
System.out.println("Hello world!")
}
}

##///////////////////////////////////////////////////////////////////


print( "Ma devise est 'Parler peu mais parler bien'." )
print( "Je m'appelle Camthalion" )
print( "Coucou !" )

# //correction java
class Main {
public static void main(String[] args) {
System.out.println("Coucou !")
System.out.println("Je m'appelle Camthalion")
System.out.println("Ma devise est 'Parler peu mais parler bien'.")
}
}

##//////////////////////////////////////////////


Tout
droit
tu
grimperas, La
clé
tu
trouveras, Habile
tu
seras, Quand
tu
les
porteras, Et
avec
le
chef
tu
reviendras !
# ///////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////
# //correction java
classMain{
    public static void main( String[] args) {
    System.out.println( "Tout droit tu grimperas," )
System.out.println( "La clé tu trouveras," )
System.out.println( "Habile tu seras," )
System.out.println( "Quand tu les porteras," )
System.out.println( "Et avec le chef tu reviendras !" )
}
}


# //////////////////////////////////////////////////////////////////////
from robot import *

haut()
haut()
haut()
droite()
droite()
bas()
bas()
droite()
# //////////////////////////////////////////////
# //correction java
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
haut()
haut()
haut()
droite()
droite()
bas()
bas()
droite()
}
}


from robot import *

deplacer( 1, 3 )
deplacer( 1, 2 )
deplacer( 3, 1 )
# /////////////////////////////////////////////////////
n = 4
print( "tour Hanoi avec ", n, " plateaux" )


def hanoi(n, a=1, b=2, c=3):
    if (n > 0):
        hanoi( n - 1, a, c, b )
        print( "deplacer ", a, "sur", c )
        hanoi( n - 1, b, a, c )


hanoi( n, a=1, b=2, c=3 )
# /////////////////////////////////////////////////////////////////////////////////////
from robot import *

deplacer( 1, 2 )
deplacer( 1, 3 )
deplacer( 2, 3 )
deplacer( 1, 2 )
deplacer( 3, 1 )
deplacer( 3, 2 )
deplacer( 1, 2 )
deplacer( 1, 3 )
deplacer( 2, 3 )
deplacer( 2, 1 )
deplacer( 3, 1 )
deplacer( 2, 3 )
deplacer( 1, 2 )
deplacer( 1, 3 )
deplacer( 2, 3 )
# // // // // // // // // // // // // /
n = 4
print( "tour Hanoi avec ", n, " plateaux" )


def hanoi(n, a=1, b=2, c=3):
    if (n > 0):
        hanoi( n - 1, a, c, b )
        print( "deplacer( ", a, ",", c, " )" )
        hanoi( n - 1, b, a, c )


hanoi( n, a=1, b=2, c=3 )
# /////////////////////////////////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)
deplacer(1, 2)
deplacer(3, 1)
deplacer(3, 2)
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)
deplacer(2, 1)
deplacer(3, 1)
deplacer(2, 3)
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)
}
}

# //////////////////////////////


from robot import *

remplir( 3 )
transferer( 3, 5 )
remplir( 3 )
transferer( 3, 5 )
vider( 5 )
transferer( 3, 5 )
remplir( 3 )
transferer( 3, 5 )

# /////////////////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
remplir(5)
transferer(5, 3)
vider(3)
transferer(5, 3)
remplir(5)
transferer(5, 3)
}
}
# ///////////////////////////////////////


for loop in range( 135 ):
    print( "Je dois respecter le Grand Sorcier." )

for loop in range( 13 ):
    print( "9 * 8 = 72" )


# // // // // // // // // // // // // /
# //correction java
class Main {
public static void main(String[] args) {
for (int loop = 1
loop <= 135
loop = loop + 1) {
System.out.println("Je dois respecter le Grand Sorcier.")
}
}
}
# ///////////////////////////////////////


gauche()
droite()
ramasser()
deposer()

from robot import *

gauche()
gauche()
print( "Bonjour, laissez-moi vous aider" )
ramasser()
for loop in range( 32 ):
    droite()
deposer()

# ///////////////////////////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
gauche()
gauche()
System.out.println("Bonjour, laissez-moi vous aider")
ramasser()
for (int loop = 1; loop <= 32
loop = loop + 1) {
droite()
}
deposer()
}
}

# /////////////////////////////////////////////////////


from robot import *

droite()
ramasser()
droite()
ramasser()
gauche()
gauche()
deposer()

# Aller à gauche Aller à droite Ramasser une bouse Déposer les  bouses

from robot import *

droite()
ramasser()
droite()
ramasser()
gauche()
gauche()
deposer()

from robot import *

for loop in range( 15 ):
    droite()
    ramasser()
droite()
deposer()

# ///////////////////////////////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
for (int loop = 1
loop <= 15
loop = loop + 1) {
droite()
ramasser()
}
droite()
deposer()
}
}
# //////////////////////////////////////////////


from robot import *

for loop in range( 21 ):
    haut()
    droite()
for loop in range( 21 ):
    gauche()
    bas()

# ////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
for (int loop = 1
loop <= 21
loop = loop + 1) {
haut()
droite()
}
for (int loop = 1
loop <= 21
loop = loop + 1) {
gauche()
bas()
}
}
}
# //////////////////////////////


for loop in range( 30 ):
    print( "a_", end="" )
print( "" )
for loop in range( 30 ):
    print( "b_", end="" )
print( "" )
for loop in range( 30 ):
    print( "c_", end="" )
print( "" )
# ////////////////////////////////////////////////////////
for loop in range( 20 ):
    for loop in range( 20 ):
        print( "O", end="" )
        print( "X", end="" )
    print()
    for loop in range( 20 ):
        print( "X", end="" )
        print( "O", end="" )
    print()
# //////////////////////////////
for loop in range( 20 ):
    for loop in range( 20 ):
        print( "OX", end="" )
    print()
    for loop in range( 20 ):
        print( "XO", end="" )
    print()


# /////////////////////////////////////////////
# //correction java
class Main {
public static void main(String[] args) {
for (int loop = 1
loop <= 20
loop = loop + 1) {
for (int loop2 = 1
loop2 <= 20
loop2 = loop2 + 1) {
System.out.print("OX")
}
System.out.println()
for (int loop2 = 1; loop2 <= 20
loop2 = loop2 + 1) {
System.out.print("XO")
}
System.out.println()
}
}
}
# ///////////////////////////////


from robot import *

for loop in range( 108 ):
    for loop in range( 13 ):
        haut()
    for loop in range( 13 ):
        droite()
    for loop in range( 13 ):
        bas()
    for loop in range( 13 ):
        gauche()
# /////////////////////////////////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
for (int loop = 1
loop <= 108
loop = loop + 1) {
for (int loop2 = 1
loop2 <= 13
loop2 = loop2 + 1) {
haut()
}
for (int loop2 = 1
loop2 <= 13
loop2 = loop2 + 1) {
droite()
}
for (int loop2 = 1
loop2 <= 13
loop2 = loop2 + 1) {
bas()
}
for (int loop2 = 1
loop2 <= 13
loop2 = loop2 + 1) {
gauche()
}
}
}
}
# ///////////////////////////////////////////


Aller
à
gauche
Aller
à
droite
Ramasser
les
raisins
Déposer
les
raisins

gauche()
droite()
ramasser()
deposer()

from robot import *

for loop in range( 20 ):
    ramasser()
    for loop in range( 15 ):
        droite()
    deposer()
    for loop in range( 15 ):
        gauche()

# //////////////////////////////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
for (int loop = 1
loop <= 20
loop = loop + 1) {
ramasser()
for (int loop2 = 1; loop2 <= 15
loop2 = loop2 + 1) {
droite()
}
deposer()
for (int loop2 = 1; loop2 <= 15
loop2 = loop2 + 1) {
gauche()
}
}
}
}

# // // // // // // // // // // // // /


from robot import *

haut()
haut()
droite()

from robot import *

# premiere montée de 9, tourner à droite, descendre de 8
for loop in range( 9 ):
    print( "haut" )
print( "droite" )
for loop in range( 8 ):
    print( "bas" )
print( "droite" )
# repete 3 fois monter de 8, tourner à droite descendre de 8, tourner à droite
for loop in range( 3 ):
    for loop in range( 8 ):
        print( "haut" )
    print( "droite" )
    for loop in range( 8 ):
        print( "bas" )
    print( "droite" )
#  derniere monter de 8, tourner à droite, descendre de 9 sans tourner à
#  droitee
for loop in range( 8 ):
    print( "haut" )
print( "droite" )
for loop in range( 9 ):
    print( "bas" )
# retour au depart
for loop in range( 9 ):
    print( "gauche" )

from robot import *

# premiere montée de 9, tourner à droite, descendre de 8
for loop in range( 9 ):
    haut()
droite()
for loop in range( 8 ):
    bas()
droite()
# repete 3 fois monter de 8, tourner à droite descendre de 8, tourner à droite
for loop in range( 3 ):
    for loop in range( 8 ):
        haut()
    droite()
    for loop in range( 8 ):
        bas()
    droite()
#  derniere monter de 8, tourner à droite, descendre de 9 sans tourner à
#  droitee
for loop in range( 8 ):
    haut()
droite()
for loop in range( 9 ):
    bas()
# retour au depart
for loop in range( 9 ):
    gauche()

    # ///////////////////////////////////////////
    from *
haut()
# Allers-retours sur les 9 lignes du haut, pour les 8 premières colonnes
for loop in range( 4 ):
    for loop in range( 8 ):
        haut()
    droite()
    for loop in range( 8 ):
        bas()
    droite()
# Deux dernières colonnes avec redescente jusqu'en bas
for loop in range( 8 ):
    haut()
droite()
for loop in range( 9 ):
    bas()
# Et on rentre à la position de départ
for loop in range( 9 ):
    gauche()
    # ///////////////////////////////////////
import static

algorea.Robot. *;

# //correction java
class Main {
public static void main(String[] args) {
haut() // Allers - retours sur les 9 lignes du haut,
// pour les 8 premières colonnes
for (int loop = 1; loop <= 4
loop = loop + 1) {
for (int loop2 = 1
loop2 <= 8
loop2 = loop2 + 1) {
haut()
}
droite()
for (int loop2 = 1; loop2 <= 8
loop2 = loop2 + 1) {
bas()
}
droite()
}

// Deux dernières colonnes avec redescente jusqu'en bas
for (int loop = 1
loop <= 8
loop = loop + 1) {
haut()
}
droite()
for (int loop = 1; loop <= 9
loop = loop + 1) {
bas()
} // Et on rentre à la position de départ
for (int loop = 1
loop <= 9
loop = loop + 1) {
gauche()
}
}
}
# /////////////////////////////////////////////


print( 12581 - 11937 )
# ///////////////////
# L'école est formée de 4 classes, constituées respectivement de 25, 30, 27 et
# 22 élèves.
# Cependant, 8 élèves sont absents aujourd'hui.  Sachant que chaque élève
# présent doit recevoir 3 bonbons,
# écrivez un programme qui calcule puis affiche le nombre total de bonbons
# nécessaires.
nombreEnfants = 25 + 30 + 27 + 22 - 8
print( nombreEnfants * 3 )

// // // // // // // // // // // // /
# L'algoréathlon se constitue de trois étapes à effectuer chaque jour :
# 2 km de natation, 34 km de cyclisme et 6 km de course à pied.
# Sachant qu'un sportif répète ces trois étapes pendant 3 jours de suite,
# vous devez afficher la distance totale qu'il a parcourue à la fin du 1er
# jour, à la fin du 2e jour, puis à la fin de l'algoréathlon complet.
# Afin de rendre l'affichage convivial sur l'écran du robot, vous souhaitez
# mettre
# les trois valeurs sur une même ligne, avec une espace entre chaque valeur et
# la suivante.
# Important : pour écrire ce programme, vous devez mémoriser la distance
# parcourue
# en un jour en lui donnant un nom, puis utiliser ce nom pour calculer les
# trois réponses.
# Appuyez-vous sur les explications ci-dessous.
distanceJournaliere = 2 + 34 + 6
print( "distance en  une journée: ", distanceJournaliere, end=" " )
print( "distance en  2 journées: ", distanceJournaliere * 2, end=" " )
print( "distance en  3 journées: ", distanceJournaliere * 3 )

# ///////////////////////////////////////////
# # Ce que doit faire votre programme :
# # La cour carrée a été mesurée avec quatre bâtons de longueurs
# respectives 17 m, 7 m, 5 m et 2 m.  La longueur du côté de la cour est égale
# à 5 fois
# le premier bâton plus 2 fois le second plus 1 fois le troisième plus 2 fois
# le quatrième.

# # Votre programme doit afficher deux lignes : la première doit contenir
# la surface de la cour, et la seconde ligne doit contenir son périmètre.
# Les résultats doivent être exprimés en mètres carrés et en mètres,
# respectivement,
# mais vous ne devez pas afficher l'unité après la valeur numérique.

# # Important : dans votre programme, commencez par calculer la longueur du
# côté de la cour et l'enregistrer dans une variable.
longeurCoteCour = 5 * 17 + 2 * 7 + 5 + 2 * 2
surfaceCour = longeurCoteCour * longeurCoteCour
print( surfaceCour )
perimetreCour = longeurCoteCour * 4
print( perimetreCour )

# ///////////////////////////////////////////
# Le robot devra compter jusqu'à 100, c'est à dire afficher les entiers de 1 à
# 100,
# un par ligne, et ensuite afficher
# « J'arrive !  ».  Ainsi, s'il ne devait compter que jusqu'à 3 au lieu de
# 100,
# votre robot devrait afficher :
n = 1
for loop in range( 100 ):
    print( n )
    n = n + 1
print( "J'arrive !" )


# /////////////////////////////
# //correction java
class Main {
public static void main(String[] args) {
int compte = 1;
for (int loop = 1; loop <= 100
loop = loop + 1) {
System.out.println(compte)
compte = compte + 1
}
System.out.println("J'arrive !")
}
}
# /////////////////////////////////////////////
# Ce que doit faire votre programme :
# Vous devez lire attentivement les programmes donnés ci-dessous
# pour déterminer s'ils sont valides ou non, et ce sans essayer de les
# exécuter.
# Pour chacun des 7 programmes, vous devez afficher sur une ligne
# soit la lettre « V » pour indiquer que le programme est valide,
# soit la lettre « I » pour indiquer qu'il est invalide.  Par exemple,
# si vous pensez que les 4 premiers programmes s'exécuteront
# sans erreur et que les 3 suivants entraîneront des erreurs, faites afficher
# à votre programme :


print( "V" )
print( "V" )
print( "I" )
print( "I" )
print( "V" )
print( "I" )
print( "I" )
# ////////////////////////////
# Votre programme devra lancer le décompte en partant de 100
# puis annoncer le décollage, c'est-à-dire afficher une séquence d'annonces de
# la forme :
n = 100
for loop in range( 101 ):
    print( n )
    n = n - 1
print( "Décollage !" )


# ////////////////////////////////
# //correction java
class Main {
public static void main(String[] args) {
int compte = 100;
for (int loop = 1; loop <= 101
loop = loop + 1) {
System.out.println(compte)
compte = compte - 1
}
System.out.println("Décollage !")
}
}
# /////////////////////////////
# Ce que doit faire votre programme :
# Sachant qu'il y a actuellement 1337 crapauds et que
# leur nombre double chaque semaine, votre programme devra afficher
# le nombre de crapauds qu'il y aura après la 12e semaine.
# Important : vous devez utiliser une boucle pour calculer le nombre de
# crapauds.


nbreCrapauds = 1337
for loop in range( 12 ):
    nbreCrapauds = nbreCrapauds * 2
print( nbreCrapauds )

# ///////////////////////////////////////////
totalBonbons = 0
numTir = 1
for loop in range( 50 ):
    totalBonbons = totalBonbons + numTir
    print( totalBonbons )
    numTir = numTir + 1
    # /////////////////////////////////////////////
from robot import *

droite()
ramasser()
gauche()
deposer()
droite()
droite()
ramasser()
gauche()
gauche()
deposer()

# Ce que doit faire votre programme :
# Schéma avec les anneaux
# Votre robot doit partir de la case de gauche (en orange),
# aller chercher les anneaux (les ronds sur fond bleu) 10 cases
# dans l'ordre (de gauche à droite) et les ramener un par un à la case de
# départ.
from robot import *

anneau = 1
for loop in range( 10 ):
    for loop in range( anneau ):
        droite()
    ramasser()
    for loop in range( anneau ):
        gauche()
    deposer()
    anneau = anneau + 1
    # /////////////////////////////////////////////////////
    Ce
    que
    doit
    faire
    votre
    programme:
    # L'objectif est de construire une tour à l'aide de petits
    # cubes en bois, sachant que la forme de cette tour consiste
    # en un ensemble de grands cubes placés les uns au-dessus des autres.
    # La base de la tour est un cube de taille 17×17×17,
    # c'est-à-dire composé de 17×17×17 = 4913 petits cubes.
    # Sur ce cube est posé un autre cube de taille 15×15×15.
    # Au-dessus de ce dernier se trouve un cube de 13×13×13.
    # La tour continue ainsi jusqu'à atteindre le sommet,
    # qui consiste en un cube de taille 1×1×1.
    # calculer le nombre de cubes nécessaires
    nbreRang = 17
somme = 0
nbreCubesRdc = nbreRang * nbreRang * nbreRang
nbreEtages = nbreRang
for loop in range( 9 ):
    #	nbreRang=nbreRang-2
    nbreCubesRdc = nbreRang * nbreRang * nbreRang
    nbreRang = nbreRang - 2
    somme = somme + nbreCubesRdc
#	print(nbreCubesRdc)
print( somme )
# ////////////////////////////////////////////////////////
nbCubes = 0
largeurArête = 1
for loop in range( 9 ):
    nbCubes = nbCubes + largeurArête * largeurArête * largeurArête
    largeurArête = largeurArête + 2
print( nbCubes )

# sur le site
# http://oeis.org/search?q=1%2C27%2C125%2C343%2C729%2C1331%2C2197%2C3375%2C4913&sort=&language=&go=Search
# on trouve la formule pour chaque ligne:
# a(n)=(2*n + 1)^3 en python cela donne
# a(n)=(2*n + 1)**3
# et pour le total
# n^2*(2*n^2-1)
# en python
# n**2*(2*n**2-1)
# somme==9**2*(2*9**2-1)=13041

# ////////////////////////////
ligne = 1
for loop in range( 20 ):
    colonne = 1
    for loop in range( 20 ):
        print( colonne * ligne, end=" " )
        colonne = colonne + 1
    print()
    ligne = ligne + 1


# //////////////////////////////////////////
# //correction java
class Main {
public static void main(String[] args) {
int ligne = 1;
for (int loop1 = 1; loop1 <= 20
loop1 = loop1 + 1) {
int colonne = 1;
for (int loop2 = 1; loop2 <= 20
loop2 = loop2 + 1) {
System.out.print((colonne * ligne) + " ")
colonne = colonne + 1
}
System.out.println()
ligne = ligne + 1
}
}
}
# //////////////////////////////////////////


largeur = int( input() )
longeur = int( input() )
print( largeur * longeur )

# /////////////////////////////////////////////////////
nbJours = int( input() )
print( 60 * 60 * 16 * nbJours

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int nbJours = entrée.nextInt()
System.out.println(nbJours * 16 * 60 * 60)
}
}

# /////////////////////////////////////////////////////////////////////////////////////


âgeCadet = int( input() )
âgeAîné = int( input() )
différence = âgeAîné - âgeCadet
print( différence )

import algorea.Scanner;

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int âgeCadet = entrée.nextInt()
int âgeAîné = entrée.nextInt()
int différence = âgeAîné - âgeCadet
System.out.println(différence)
}
}

# /////////////////////////////////////////////////////////////////////////////////


nbLignes = int( input() )
for loop in range( nbLignes ):
    print( "Je dois suivre en cours" )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int nbLignes = entrée.nextInt()
for (int iLigne = 1; iLigne <= nbLignes; iLigne = iLigne + 1) {
System.out.println("Je dois suivre en cours")
}
}
}

# ////////////////////////////////////////////////////////////


tempMin = int( input() )
tempMax = int( input() )
temperature = tempMin
for loop in range( tempMax - tempMin + 1 ):
    print( temperature )
    temperature = temperature + 1

    import algorea.Scanner;

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int tempMin = entrée.nextInt()
int tempMax = entrée.nextInt()
int température = tempMin
for (int loop = 1; loop <= tempMax - tempMin + 1
loop = loop + 1) {
System.out.println(température)
température = température + 1
}
}
}
# ///////////////////////////////////////////////////////////////////
# Le nombre 1 × 2 × 3 × … × n s'appelle la factorielle de n (ou « factorielle n
# »)
# et se note « n!  ».  La factorielle est très utilisée en combinatoire
# car elle correspond en particulier au nombre de manières d'ordonner n
# éléments.


nbNombres = int( input() )
étape = 0
résultat = 66
for loop in range( nbNombres ):
    étape = étape + 1
    résultat = résultat * étape
    print( résultat )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int nbNombres = entrée.nextInt()
int résultat = 66
for (int facteur = 1; facteur <= nbNombres; facteur = facteur + 1) {
résultat = résultat * facteur
System.out.println(résultat)
}
}
}
# ///////////////////////////////////////////////////////////
# validation
# Il y a trois entiers à lire : la position de départ positionDepart,
# la largeur d'un emplacement largeurEmplacement et le nombre de vendeurs
# nbVendeurs.

# Vous devez afficher une suite de nombres, partant de positionDepart
# et augmentant de largeurEmplacement à chaque fois.
# Il y a au total nbVendeurs augmentations à faire.
# Vous devez afficher la valeur de chacun des nombres de la suite.


positionDépart = int( input() )
largeurEmplacement = int( input() )
nbVendeurs = int( input() )
position = positionDépart
for iVendeur in range( nbVendeurs + 1 ):
    print( position )
    position = position + largeurEmplacement

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int positionDépart = entrée.nextInt()
int largeurEmplacement = entrée.nextInt()
int nbVendeurs = entrée.nextInt()
int position = positionDépart
for (int iVendeur = 0; iVendeur <= nbVendeurs; iVendeur = iVendeur + 1) {
System.out.println(position)
position = position + largeurEmplacement
}
}
}


# ///////////////////////////////////////////////////////////


totalKarvas = 0
for loop in range( 20 ):
    nbBêtes = int( input() )
    totalKarvas = totalKarvas + nbBêtes
print( totalKarvas )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int totalKarvas = 0;
for (int loop = 1; loop <= 20
loop = loop + 1) {
int nbBêtes = entrée.nextInt()
totalKarvas = totalKarvas + nbBêtes
}
System.out.println(totalKarvas)
}
}
# /////////////////////////////////////////////////////


largeurBas = int( input() )
largeurHaut = int( input() )

volume = 0
largeur = largeurHaut
for loop in range( largeurBas - largeurHaut + 1 ):
    volume = volume + largeur * largeur
    largeur = largeur + 1

print( volume )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int largeurBas = entrée.nextInt()
int largeurHaut = entrée.nextInt()
int volume = 0
int largeur = largeurHaut
for (int loop = 1; loop <= largeurBas - largeurHaut + 1
loop = loop + 1) {
volume = volume + largeur * largeur
largeur = largeur + 1
}
System.out.println(volume)
}
}

# #////////////////////////////////////////////////////////////
# poids, son âge, la longueur de ses cornes et la hauteur au garrot
# afficher sa note,sachant qu'elle s'obtient en multipliant la longueur des
# cornes
# par la hauteur au garrot,
# valeur à laquelle on ajoute le poids.

# 2
# 100
# 5
# 25
# 90
# 300
# 10
# 15
# 120


nbKarvas = int( input() )
for loop in range( nbKarvas ):
    poids = int( input() )
    âge = int( input() )
    longueurCornes = int( input() )
    hauteurAuGarrot = int( input() )
    print( longueurCornes * hauteurAuGarrot + poids )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int nbKarvas = entrée.nextInt()
for (int loop = 1; loop <= nbKarvas; loop = loop + 1) {
int poids = entrée.nextInt()
entrée.nextInt() // âge
int longueurCornes = entrée.nextInt()
int hauteurAuGarrot = entrée.nextInt()
System.out.println(longueurCornes * hauteurAuGarrot + poids)
}
}
}
# #////////////////////////////////////////////////////////////////////////////////////


nbPaquets = int( input() )
poidsPaquet = int( input() )
if nbPaquets * poidsPaquet > 105:
    print( "Surcharge !" )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int nbPaquets = entrée.nextInt()
int poidsPaquet = entrée.nextInt()
if (nbPaquets * poidsPaquet > 105) {
System.out.println("Surcharge !")
}
}
}

# /////////////////////////////////////////////////////


numéroMatin = int( input() )
numéroSoir = int( input() )
écart = numéroSoir - numéroMatin
if écart < 0:
    écart = -écart
print( écart )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int numéroMatin = entrée.nextInt()
int numéroSoir = entrée.nextInt()
int écart = numéroSoir - numéroMatin
if (écart < 0) {
écart = -écart
}
System.out.println(écart)
}
}
# /////////////////////////////////////////////////////
# Votre programme lira un entier, l'heure d'arrivée, qui sera compris entre 0 et
# 12 inclus.
##0 correspond à midi, 1 à 1h de l'après-midi, etc.  et 12 à minuit.
# Le prix de la chambre est de 10 pièces à midi, et augmente de 5 pièces chaque
# heure après midi.
# Il est donc de 15 pièces à 13h, etc.  Il ne peut cependant pas dépasser 53
# pièces.
# Votre programme devra afficher le prix à payer correspondant à l'heure
# d'arrivée donnée.)


heure = int( input() )
prix = 10 + 5 * heure
if prix > 53:
    prix = 53
print( prix )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int heure = entrée.nextInt()
int prix = 10 + 5 * heure
if (prix > 53) {
prix = 53
}
System.out.println(prix)
}

}
# ////////////////////////////////////////////////////////////////////////////////////////
# Votre programme devra lire deux entiers, la superficie d'un champ des Arignon


# et la superficie d'un champ des Evaran. Si l'un des champs est plus grand
# d'au moins 10 m² (strictement) que l'autre champ, alors il faudra afficher le texte
# « La famille X a un champ trop grand », « X » devant bien sûr être remplacé
# par « Arignon » ou « Evaran » selon le cas.


superficieArignon = int( input() )
superficieEvaran = int( input() )
if superficieArignon > superficieEvaran + 10:
    print( "La famille Arignon a un champ trop grand" )
if superficieEvaran > superficieArignon + 10:
    print( "La famille Evaran a un champ trop grand" )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int aireArignon = entrée.nextInt()
int aireEvaran = entrée.nextInt()
if (aireArignon - aireEvaran > 10) {
System.out.println("La famille Arignon a un champ trop grand")
}
if (aireEvaran - aireArignon > 10) {
System.out.println("La famille Evaran a un champ trop grand")
}
}
}

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Votre programme doit lire l'âge d'une personne et
# afficher soit « Tarif réduit » si cette personne a strictement moins de 21
# ans,
# soit « Tarif plein » dans le cas contraire


âge = int( input() )
if âge < 21:
    print( "Tarif réduit" )
else:
    print( "Tarif plein" )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int âge = entrée.nextInt()
if (âge < 21) {
System.out.println("Tarif réduit")
} else {
System.out.println("Tarif plein")
}
}
}
# ////////////////////////////////////////////////////////////////////////////////////
#=========================================================================================
# Vous arrivez devant un pont que vous devez absolument emprunter pour arriver avant la 
# nuit au village situé de l'autre côté de la rivière. Cependant, la traversée du pont 
# n'est pas gratuite et le tarif dépend de votre chance au jeu. En effet, le gardien vous
#  demande de lancer deux dés et le prix dépendra des valeurs que vous obtiendrez. 
#  Vous décidez d'écrire un programme pour vérifier qu'il applique bien le bon tarif.
# 
# Ce que doit faire votre programme :
# Votre programme doit lire deux entiers, compris entre 1 et 6, la valeur de chaque dé. 
# Si la somme est supérieure ou égale à 10, alors vous devez payer une taxe spéciale 
# (36 pièces). Sinon, vous payez deux fois la somme des valeurs des deux dés. 
# Votre programme devra afficher selon le cas le texte « Taxe spéciale ! » ou 
# bien « Taxe régulière », puis la somme à payer (sans indiquer l'unité).
# 
# Exemples
# Exemple 1
# entrée :
# 5
# 6
# sortie :
# Taxe spéciale !
# 36
# Exemple 2
# entrée :
# 4
# 3
# sortie :
# Taxe régulière
# 14
#=========================================================================================
resultatLancerDes1 = int(input())
resultatLancerDes2 = int(input())
if (resultatLancerDes1 + resultatLancerDes2) >= 10:
    print("Taxe Speciale !")
    print(36);
else:
    print("Taxe reguliére")
    print((resultatLancerDes1 + resultatLancerDes2)*2)

#=========================================================================================
# correction en java
#=========================================================================================
public class TraverseeDuPont {

    /**
     * @description
     *
     * @return void
     *
     * @method main
     * @class TraverseeDuPont
     * @version 1.0
     * @date mercredi 04 sept. 2019
     * @see
     *
     **/
    public static void main(String[] args) {
        Scanner keyboardInput = new Scanner(System.in);
        int resultatLancerDes1 = keyboardInput.nextInt();
        int resultatLancerDes2 = keyboardInput.nextInt();
        if ((resultatLancerDes1 + resultatLancerDes2) >= 10) {
            System.out.println("Taxe spéciale !");
            System.out.println(36);
        } else {
            System.out.println("Taxe régulière");
            System.out.println((resultatLancerDes1 + resultatLancerDes2) * 2);

        }

    }

}


# ////////////////////////////////////////////////////////////////////////////////////
# Votre programme devra lire un premier entier : le nombre
# de membres nbMembres qui constituent une équipe.  Ensuite,
# il devra lire les poids (en kilogrammes), au total nbMembres × 2, sachant
# que le premier poids est celui d'un joueur de la 1re équipe, le deuxième
# poids celui d'un joueur de la 2e équipe, le troisième la 1re équipe, le
# quatrième la 2e équipe, etc.

# Après avoir calculé le poids total de chaque équipe, vous devrez afficher le
# texte
# « L'équipe X a un avantage » (en remplaçant X par la valeur 1 ou 2), en
# considérant qu'une équipe est avantagée si elle a un poids total supérieur à
# celui de l'autre.

# Vous afficherez ensuite le texte « Poids total pour l'équipe 1 :
# » suivi du poids de l'équipe 1, puis « Poids total pour l'équipe 2 :
# » suivi du poids de l'équipe 2 (voir l'exemple ci-dessous).


nbMembres = int( input() )
total = 0
numeroEquipe = 0
poidsEquipe1 = 0
poidsEquipe2 = 0

for loop in range( nbMembres ):
    poidsJoeurEquipe1 = int( input() )
    poidsJoeurEquipe2 = int( input() )
    poidsEquipe1 = poidsEquipe1 + poidsJoeurEquipe1
    poidsEquipe2 = poidsEquipe2 + poidsJoeurEquipe2

if poidsEquipe1 > poidsEquipe2:
    numeroEquipe = 1
else:
    numeroEquipe = 2
print( "L'équipe ", numeroEquipe, " a un avantage" )
print( "Poids total pour l'équipe 1 : ", poidsEquipe1 )
print( "Poids total pour l'équipe 2 : ", poidsEquipe2 )

nbPersonnes = int( input() )
totalÉquipe1 = 0
totalÉquipe2 = 0
for loop in range( nbPersonnes ):
    poids1 = int( input() )
    poids2 = int( input() )
    totalÉquipe1 = totalÉquipe1 + poids1
    totalÉquipe2 = totalÉquipe2 + poids2
if totalÉquipe1 > totalÉquipe2:
    print( "L'équipe 1 a un avantage" )
else:
    print( "L'équipe 2 a un avantage" )
print( "Poids total pour l'équipe 1 :", totalÉquipe1 )
print( "Poids total pour l'équipe 2 :", totalÉquipe2 )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int nbPersonnes = entrée.nextInt()
int totalÉquipe1 = 0, totalÉquipe2 = 0
for (int loop = 1; loop <= nbPersonnes; loop = loop + 1) {
int poids1 = entrée.nextInt()
int poids2 = entrée.nextInt()
totalÉquipe1 = totalÉquipe1 + poids1
totalÉquipe2 = totalÉquipe2 + poids2
}
if (totalÉquipe1 > totalÉquipe2) {
System.out.println("L'équipe 1 a un avantage")
}
else {
System.out.println("L'équipe 2 a un avantage")
}
System.out.println("Poids total pour l'équipe 1 : " + totalÉquipe1)
System.out.println("Poids total pour l'équipe 2 : " + totalÉquipe2)
}
}
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Votre programme doit lire un entier : le code fourni par
# l'utilisateur.  Si ce code correspond au code secret, qui est 64 741,
# alors le programme devra afficher le texte « Bon festin !  ».
# Sinon, il devra afficher « Allez-vous en !  ».


codeUtilisateur = int( input() )

if codeUtilisateur != 64741:
    print( "Allez-vous en !" )
else:
    print( "Bon festin !" )

import algorea.Scanner

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in )
public static void main(String[] args) {
int tentative = entrée.nextInt()
if (tentative == 64741) {
System.out.println("Bon festin !")
} else {
System.out.println("Allez-vous-en !")
}
}
}








# ///////////////////////////////////////////////////////////////////////////////////////////////////


# Votre programme doit lire un entier : le code fourni par
# l'utilisateur.  Si ce code correspond au code secret, qui est 64 741,
# alors le programme devra afficher le texte « Bon festin !  ».
# Sinon, il devra afficher « Allez-vous en !  ».


codeUtilisateur = int( input() )
if codeUtilisateur != 64741:
    print( "Allez-vous en !" )
else:
    print( "Bon festin !" )
#=========================================================================================
# Villes et villages
#=========================================================================================
#=========================================================================================
# Au cours de votre périple, vous traversez de nombreux lieux habités. Pour chacun 
# d'entre eux, vous notez soigneusement sa population. Après quelques semaines de 
# voyage, vous avez vraiment l'impression qu'il y beaucoup de villages et très peu de villes.
# 
# Ce que doit faire votre programme :
# On vous donne le nombre d'habitants d'un certain nombre de lieux que vous visitez.
#  Une ville étant un lieu dont la population est strictement supérieure à 10 000 habitants,
#   déterminez combien de lieux sont des villes.
# 
# Votre programme doit lire un entier : le nombre de lieux. Il doit ensuite lire, pour 
# chaque lieu, un entier donnant le nombre de gens qui y habitent. Votre programme doit 
# alors afficher le nombre de villes.
# 
# Exemple
# entrée :
# 
# 6
# 1000
# 5000
# 15000
# 4780
# 0
# 23590
# sortie :
# 
# 2
#=========================================================================================
nombreDeLieux = int(input())
res=0
for i in range(nombreDeLieux):
    nbreHabitant = int(input())
    if nbreHabitant>10000:
       res=res+1
print(res)

#=========================================================================================
# correction
#=========================================================================================

nbLieux = int(input())
nbVilles = 0
for loop in range(nbLieux):
   population = int(input())
   if population > 10 * 1000:
      nbVilles = nbVilles + 1
print(nbVilles)

#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nbLieux = entrée.nextInt();
      int nbVilles = 0;
      for (int loop = 1; loop <= nbLieux; loop = loop + 1)
      {
         int population = entrée.nextInt();
         if (population > 10 * 1000)
         {
            nbVilles = nbVilles + 1;
         }
      }
      System.out.println(nbVilles);
   }
}


#=========================================================================================
# Calcul des déniveléesEntraînement
#=========================================================================================
#=========================================================================================
# Aujourd'hui c'est l'étape de montagne et vous allez devoir franchir plusieurs cols.
# Vous allez passer votre temps à monter, descendre, remonter, redescendre, etc... Vous
#  décidez de noter les différentes variations d'altitudes, afin de pouvoir calculer à la
#   fin de la journée quelle est la dénivelée totale que vous avez montée ainsi que la
#    dénivelée totale que vous avez descendue (les deux valeurs peuvent être différentes
#          car vous ne retournez pas à votre point de départ).
# 
# Ce que doit faire votre programme :
# Votre programme lira d'abord un entier représentant le nombre de montées et descentes
#  que vous avez réalisées. Pour chaque montée ou descente, il faut ensuite lire un entier
#   représentant la variation d'altitude, cet entier étant strictement positif dans le cas
#    d'une montée et strictement négatif dans le cas d'une descente (il n'y a rien à compter
#     pour les tronçons qui sont bien à plat). Votre programme devra afficher l'altitude 
#     totale montée puis l'altitude totale descendue (ces deux nombres sont positifs).
# 
# Exemple
# entrée :
# 
# 5
# 4
# 7
# -6
# -3
# 2
# sortie :
# 
# 13
# 9
#=========================================================================================
monteeDecsente = int(input())
 
totalMontee = 0
totalDescente = 0
 
for loop in range(monteeDecsente):
   altitude = int(input())
    
   if altitude > 0:
      totalMontee = totalMontee + altitude
   else :
      totalDescente = totalDescente + (-altitude)
print(totalMontee)
print(totalDescente)
#=========================================================================================
# print(cumulM , end="")
# print(cumulD, end="")
#=========================================================================================

#=========================================================================================
# correction
#=========================================================================================
nbVariations = int(input())
sommePos = 0
sommeNeg = 0
for loop in range(nbVariations):
   variation = int(input())
   if variation > 0:
      sommePos = sommePos + variation
   else:
      sommeNeg = sommeNeg - variation
print(sommePos)
print(sommeNeg)
#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nbVariations = entrée.nextInt();
      int sommePos = 0;
      int sommeNeg = 0;
      for (int loop = 1; loop <= nbVariations; loop = loop + 1)
      {
         int variation = entrée.nextInt();
         if (variation > 0)
         {
            sommePos = sommePos + variation;
         }
         else
         {
            sommeNeg = sommeNeg - variation;
         }
      }
      System.out.println(sommePos);
      System.out.println(sommeNeg);
   }
}



# ////////////////////////////////////////////////////////////////
# Votre programme doit d'abord lire un entier décrivant votre position actuelle
# sur la route, sous la forme d'un nombre de kilomètres par rapport au début
#  de la route.  Ensuite, il doit lire un entier donnant le nombre de villages.
#   Pour chaque village, il doit lire un entier décrivant la position de ce
#   village
#    le long de cette même route.  Votre programme doit alors afficher le
#    nombre de villages
#    qui se trouvent à une distance inférieure ou égale à 50 km de votre
#    position actuelle.
kmPositionActuelle = int( input() )
rayonActionMax = kmPositionActuelle + 50
rayonActionMin = kmPositionActuelle - 50
nbreVillage = int( input() )
totalVillagesDansLeRayon = 0
for loop in range( nbreVillage ):
    kmPositionVillage = int( input() )
    if kmPositionVillage >= rayonActionMin and kmPositionVillage <= rayonActionMax:
        totalVillagesDansLeRayon = totalVillagesDansLeRayon + 1
print( totalVillagesDansLeRayon )

posActuelle = int( input() )
nbVillages = int( input() )
nbAccessibles = 0
for loop in range( nbVillages ):
    posVillage = int( input() )
    ecart = posActuelle - posVillage
    if ecart < 0:
        ecart = -ecart
    if ecart <= 50:
        nbAccessibles = nbAccessibles + 1
print( nbAccessibles )

import algorea.Scanner

# //correction java
class Main   {
        public    static    void    main( String[]    args)    {
        Scanner    entrée = new    Scanner( System. in )
    int    posActuelle = entrée.nextInt()
    int    nbVillages = entrée.nextInt()
    int    nbAccessibles = 0
    for (int loop = 1; loop <= nbVillages; loop = loop + 1)
    {
        int posVillage = entrée.nextInt()
    int écart = posActuelle - posVillage
    if (écart < 0)
    {
    écart = -écart
    }
    if (écart <= 50)
    {
    nbAccessibles = nbAccessibles + 1
    }
    }
    System.out.println(nbAccessibles)
    }
    }
#=========================================================================================
# Étape la plus longue
#=========================================================================================
#=========================================================================================
# Dans votre petit carnet de voyage, vous avez noté la distance que vous avez parcourue 
# chaque jour. Aujourd'hui, vous êtes particulièrement en forme et vous décidez donc de 
# marcher plus que les jours précédents. Vous souhaitez utiliser un programme pour déterminer
#  quel est votre record pour l'instant.
# 
# Ce que doit faire votre programme :
# Votre programme doit d'abord lire un entier strictement positif, le nombre de jours de
#  marche effectués jusqu'à présent. Il doit ensuite lire, pour chaque jour, la distance 
#  parcourue ce jour-là. Il doit alors afficher la distance maximale parcourue en une journée.
# 
# Exemple
# entrée :
# 
# 6
# 36
# 14
# 38
# 28
# 29
# 31
# sortie :
# 
# 38
#=========================================================================================
nbreJourMarche=int(input())
max=0
for i in range(nbreJourMarche):
    distanceparcourue=int(input())
    if distanceparcourue>max:
        max=distanceparcourue
print(max)     

#=========================================================================================
# correction   
#=========================================================================================
nbJours = int(input())
distanceMax = 0
for loop in range(nbJours):
   distance = int(input())
   if distance > distanceMax:
      distanceMax = distance
print(distanceMax)

#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nbJours = entrée.nextInt();
      int distanceMax = 0;
      for (int loop = 1; loop <= nbJours; loop = loop + 1)
      {
         int distance = entrée.nextInt();
         if(distance > distanceMax)
         {
            distanceMax = distance;
         }
      }
      System.out.println(distanceMax);
   }
}

#=========================================================================================
# #=========================================================================================
# # Protection du village Entraînement
# #=========================================================================================
# Le village dans lequel vous avez passé la nuit est en pleine effervescence au matin : 
# encore une attaque de worgs pendant la nuit ! Les worgs sont de redoutables loups qui
#  vivent sur Algoréa et qui s'attaquent au bétail... et parfois même aux enfants.
# 
# C'est décidé, il va falloir construire une grande palissade tout autour du village. 
# Les habitants insistent pour que cette clôture soit rectangulaire et ait une face au Nord,
#  une au Sud, une à l'Est et une à l'Ouest, quitte à devoir travailler un peu plus que
# nécessaire. Ils ont maintenant besoin de votre aide pour savoir la quantité de bois dont 
# ils vont avoir besoin pour construire cette palissade.
# 
# Ce que doit faire votre programme :
# Le programme doit d'abord lire un entier strictement positif correspondant au nombre 
# de maisons. Ensuite, pour chaque maison, il doit lire la position horizontale 
# (l'abscisse, le "x") et sa position verticale (l'ordonnée, le "y") de cette maison. 
# Toutes les abscisses et ordonnées sont des entiers compris entre zéro et 1 million.
# 
# Le programme doit alors afficher le périmètre de la plus petite clôture rectangulaire
#  englobant toutes les maisons. Ce rectangle doit avoir ses côtés parallèles aux axes
#   du repère, comme montré sur l'illustration.
# 
# Représentation du premier exemple
# Représentation graphique du premier exemple
# Exemple
# entrée :
# 
# 4

# 1
# 5

# 5
# 3

# 4
# 6

# 2
# 9
# sortie :
# 
# 20
#=========================================================================================
nbreMaison=int(input())
xmax=0
ymax=0
xmin=10000000
ymin=10000000
for loop in range(nbreMaison):
    x = int(input())
    y = int(input())

    xmax = max(x, xmax)
    xmin = min(x, xmin)
    ymax = max(y, ymax)
    ymin = min(y, ymin)
print(xmax)
print(xmin)
print(ymax)
print(ymin)
largeur = ymax - ymin
hauteur = xmax - xmin
print(largeur*2 + hauteur*2)   
    

#=========================================================================================
# correction    
#=========================================================================================
nbMaisons = int(input())
xMin = 1000 * 1000
xMax = 0
yMin = 1000 * 1000
yMax = 0
for loop in range(nbMaisons):
   posX = int(input())
   posY = int(input())
   if posX < xMin:
      xMin = posX
   if posX > xMax:
      xMax = posX
   if posY < yMin:
      yMin = posY     
   if posY > yMax:
      yMax = posY
      
largeur = xMax - xMin
hauteur = yMax - yMin
perimetre = 2 * (largeur + hauteur)
print(perimetre)

#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nbMaisons = entrée.nextInt();
      
      int infini = 1000 * 1000;
      int xMin = infini, xMax = 0, yMin = infini, yMax = 0;
      
      for (int loop = 1; loop <= nbMaisons; loop = loop + 1)
      {
         int posX = entrée.nextInt();
         int posY = entrée.nextInt();
         if(posX < xMin)
         {
            xMin = posX;
         }
         if(posX > xMax)
         {
            xMax = posX;
         }
         if(posY < yMin)
         {
            yMin = posY;   
         }
         if(posY > yMax)
         {
            yMax = posY;
         }
      }     
      int largeur = xMax - xMin, hauteur = yMax - yMin;
      int périmètre = 2 * (largeur + hauteur);
      System.out.println(périmètre);
   }
}
    
    
    
    

#=========================================================================================
# Le juste prix
#=========================================================================================
# ////////////////////////////////////////////////////////////////
# Votre programme doit lire un entier nbMarchands (non nul) puis les nbMarchands
# entiers suivants, qui indiquent le prix des galettes chez chaque marchand,
# de la position 1 à la position nbMarchands.  Votre programme devra ensuite
# afficher
# la position du plus petit de ces prix.  En cas d'égalité entre deux prix, on
# prendra
# la position la plus grande.  Tous les prix et positions
# sont positifs et ne dépassent pas 1 million.
nbMarchands = int( input() )
position = 1
positionPrixMin = 0
prixGaletteMin = 10000000
for loop in range( nbMarchands ):
    prixGalette = int( input() )
    if prixGalette <= prixGaletteMin:
        prixGaletteMin = prixGalette
        positionPrixMin = position
    position = position + 1
print( positionPrixMin )

nbMarchands = int( input() )
minPrix = 1000 * 1000
posMinPrix = -1
pos = 1
for loop in range( nbMarchands ):
    prix = int( input() )
    if prix <= minPrix:
        minPrix = prix
        posMinPrix = pos
    pos = pos + 1
print( posMinPrix )

import algorea.Scanner

# //correction java
class Main


    {
        public
    static
    void
    main( String[]
    args)
    {
        Scanner
    entrée = new
    Scanner( System. in )
    int
    nbMarchands = entrée.nextInt()
    int
    infini = 1000 * 1000
    int
    minPrix = infini, posMinPrix = -1
    int
    position = 1
    for (int loop = 1; loop <= nbMarchands; loop = loop + 1)
    {
        int prix = entrée.nextInt()
    if (prix <= minPrix)
    {
    minPrix = prix
    posMinPrix = position
    }
    position = position + 1
    }
    System.out.println(posMinPrix)
    }
    }


import algorea.Scanner

# //correction java
class Main


    {
        public
    static
    void
    main( String[]
    args)
    {
        Scanner
    entrée = new
    Scanner( System. in )
    int
    nbMarchands = entrée.nextInt()
    int
    infini = 1000 * 1000
    int
    minPrix = infini, posMinPrix = -1
    for (int pos = 1; pos <= nbMarchands; pos = pos + 1)
    {
        int prix = entrée.nextInt()
    if (prix <= minPrix)
    {
    minPrix = prix
    posMinPrix = pos
    }
    }
    System.out.println(posMinPrix)
    }
    }

#=========================================================================================
# ICI debut Conditions avancées, opérateurs booléens
#=========================================================================================
#=========================================================================================
# L'arrivée à la capitale
#=========================================================================================
 
#=========================================================================================
# 1) Espion étranger
#=========================================================================================

#=========================================================================================
# Espion étrangerDécouverte
# Le gouverneur de la ville vous a convoqué dans son bureau pour une affaire d'une extrême 
# importance. En effet, un espion étranger s'est introduit dans la ville et il faut 
# absolument le démasquer. Heureusement, grâce à des informateurs grassement payés,
#  on sait à quelques jours près à quelle date l'espion est arrivé. Il suffira donc de 
#  regarder les registres des entrées de la ville puis d'aller interroger toutes les
#   personnes correspondantes.
# 
# Pour avoir une idée de l'ampleur de la tâche, le roi vous a demandé de calculer le nombre 
# de personnes qu'il faudra interroger.
# 
# Ce que doit faire votre programme :
# On vous donne un intervalle de temps pendant lequel on sait qu'un espion est arrivé, 
# puis la date d'arrivée d'un certain nombre de personnes. Déterminez combien de ces 
# personnes peuvent être cet espion.
# 
# Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de
#  l'intervalle pendant lequel on sait que l'espion est arrivé en ville. 
#  Il doit ensuite lire un entier nbEntrées, 
#  le nombre total de personnes entrées dans la ville, 
#  puis les nbEntrées nombres suivants qui 
#  représentent les dates d'entrée (non triées) des différentes personnes.
# 
# Votre programme doit afficher
#  le nombre de personnes entrées entre les deux dates données, incluses.
# 
# Exemple
# entrée :
# 
# 6
# 10
# 5
# 7
# 11
# 8
# 3
# 6
# sortie :
# 
# 3
# Commentaires
# Dans l'exemple, l'espion est entré dans la ville entre le jour 6 et le jour 10, et 5
#  personnes sont enregistrées dans les données de la ville. Dans le schéma ci-dessous, 
#  une colonne correspond à un jour (dont le numéro se trouve en haut), et l'intervalle 
#  est représenté par le segment à bouts ronds :
# 
# Schéma de l'exemple
# L'intervalle est projeté en bleu vers le bas.
# 
# Pour chaque personne Pi, on a représenté sa date d'entrée dans la ville avec une barre 
# (accompagnée du numéro de la personne). On voit que 3 dates se trouvent dans l'intervalle.
#=========================================================================================

import random

debut=int(input())
fin=int(input())
nbEntree=int(input())

#=========================================================================================
# liste=[0]*6
#=========================================================================================
res=0
for i in range(nbEntree):
    #=====================================================================================
    # liste[1]=random.randint(1, 31)
    # print("liste", liste)    
    #=====================================================================================
    dateEntree=int(input())
    
    if (debut <= dateEntree <= fin):
        res += 1
print( "resultat " ,res  )     




#=========================================================================================
# correction
#=========================================================================================
dateDébut = int(input())
dateFin = int(input())
nbEntrées = int(input())
nbPersonnes = 0
for loop in range(nbEntrées):
   date = int(input())
   if dateDébut <= date and date <= dateFin:
      nbPersonnes = nbPersonnes + 1
print(nbPersonnes)
#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int dateDébut = entrée.nextInt();
      int dateFin = entrée.nextInt();
      int nbEntrées = entrée.nextInt();
      int nbPersonnes = 0;
      for (int loop = 1; loop <= nbEntrées; loop = loop + 1)
      {
         int date = entrée.nextInt();
         if( (dateDébut <= date) && (date <= dateFin) )
         {
            nbPersonnes = nbPersonnes + 1;
         }
      }
      System.out.println(nbPersonnes);
   }
}   




#=========================================================================================
# Maison de l'espion
#=========================================================================================
#=========================================================================================
# On sait qu'un espion est présent dans la ville mais, grâce à des recoupements d'informations, 
# il a été possible de déterminer que l'espion était forcément dans une certaine zone de la ville.
#  Le gouverneur va donc envoyer des soldats fouiller chaque maison et interroger les habitants.
#   Afin de pouvoir estimer combien de temps va durer l'opération, il souhaiterait savoir 
#   combien de maisons sont présentes dans la zone en question.
# 
# Ce que doit faire votre programme :
# On vous décrit une zone de recherche rectangulaire, parallèle aux axes, puis la position 
# d'un certain nombre de maisons. Écrivez un programme qui détermine combien de maisons sont 
# dans cette zone.
# 
# Votre programme devra lire, dans l'ordre : l'abscisse minimale, l'abscisse maximale, 
# l'ordonnée minimale et l'ordonnée maximale du rectangle. Il lira ensuite le nombre total
#  de maisons, puis pour chaque maison, son abscisse et son ordonnée.
# 
# Votre programme devra déterminer puis afficher le nombre de maisons qui se trouvent dans
#  la zone de recherche. Si une maison est exactement sur le bord de la zone, elle doit ête
#   comptée.
# 
# Sur l'exemple suivant, il y a 12 maisons, dont 5 sont dans la zone de recherche (en bleu) : 
# Plan explicatif
# 
# Exemple
# entrée :
# 
# 1
# 4
# 1
# 8

# 12

# 1
# 7

# 1
# 9

# 2
# 3

# 3
# 2

# 3
# 4

# 3
# 6

# 3
# 9

# 5
# 3

# 5
# 8

# 7
# 5

# 8
# 2

# 8
# 8
# sortie :
# 
# 5
#=========================================================================================

xmin=int(input())
xmax=int(input())
ymin=int(input())
ymax=int(input())
nb_total_maison = int(input())
nb_maison = 0
for i in range(nb_total_maison):
   x_maison = int(input())
   y_maison = int(input())
   if (xmin <= x_maison  <= xmax) and (ymin <= y_maison <= ymax) : 
         nb_maison += 1
print(nb_maison)


#=========================================================================================
# correction
#=========================================================================================
xMin = int(input())
xMax = int(input())
yMin = int(input())
yMax = int(input())
nbMaisons = int(input())
nbAFouiller = 0
for loop in range(nbMaisons):
   x = int(input())
   y = int(input())
   if (xMin <= x) and (x <= xMax) and (yMin <= y) and (y <= yMax):
      nbAFouiller = nbAFouiller + 1
print(nbAFouiller)

#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int xMin = entrée.nextInt();
      int xMax = entrée.nextInt();
      int yMin = entrée.nextInt();
      int yMax = entrée.nextInt();
      int nbMaisons = entrée.nextInt();
      int nbAFouiller = 0;
      
      for (int loop = 1; loop <= nbMaisons; loop = loop + 1)
      {
         int x = entrée.nextInt();
         int y = entrée.nextInt();
         if( (xMin <= x) && (x <= xMax) && (yMin <= y) && (y <= yMax))
         {
            nbAFouiller = nbAFouiller + 1;
         }
      }
      System.out.println(nbAFouiller);
   }
}

#=========================================================================================
# Nombre de jours dans le moisEntraînement
#=========================================================================================
#=========================================================================================
# Les soldats de la garnison de la ville sont payés à la journée et pas au mois, ce qui fait que leur salaire n'est pas le même selon le mois. Le trésorier étant malade et les soldats voulant être payés vous vous proposez pour le remplacer. Certains soldats revenant de mission à l'extérieur, ils doivent recevoir leur paye pour les mois précédents également. Afin de ne pas faire d'erreur, vous décidez d'écrire un programme pour vous aider.
# 
# Ce que doit faire votre programme :
# Écrivez un programme qui lit un numéro de mois algoréen, et affiche le nombre de jours de celui-ci. Les Algoréens disposent de leur propre calendrier. Voici les informations dont vous avez besoin :
# 
# Numéro du mois    Nombre de jours
# 1    30
# 2    30
# 3    30
# 4    31
# 5    31
# 6    31
# 7    30
# 8    30
# 9    30
# 10    31
# 11    29
# Exemple
# entrée :
# 
# 6
# sortie :
# 
# 31
#=========================================================================================

#=========================================================================================
# tableauCalendrierAlgoreen = [[] for i in range( 12 )]
#=========================================================================================
# for i in tableauCalendrierAlgoreen:
#     tableauCalendrierAlgoreen[0]=30
#     tableauCalendrierAlgoreen[1]=29
#     tableauCalendrierAlgoreen[2]=31
#     tableauCalendrierAlgoreen[3]=28
#     for j in tableauCalendrierAlgoreen:
#         tableauCalendrierAlgoreen[0]=1,30
#         tableauCalendrierAlgoreen[1]=2
#         tableauCalendrierAlgoreen[2]=3
#         tableauCalendrierAlgoreen[3]=4
#=========================================================================================
#=========================================================================================
# tableau avec tuple automatique et incrementale        
#=========================================================================================
numeroMois=int(input())
numeroMois=numeroMois-1
tableauCalendrierAlgoreen = [30, 30, 30, 31, 31, 31, 30, 30, 30,31, 29]
#=========================================================================================
# for i, elt in enumerate(tableauCalendrierAlgoreen):
#=========================================================================================
    #=====================================================================================
    # print("À l'indice {} se trouve {}.".format(i, elt))
    # print("{}{}".format(numeroMois, elt))
    #=====================================================================================
print(tableauCalendrierAlgoreen[numeroMois])


#=========================================================================================
# correction
#=========================================================================================
numero = int(input())
if numero == 11:
   print(29)
else:
   if ( (4 <= numero) and (numero <= 6) ) or (numero == 10):
      print(31)
   else:
      print(30)
      
#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int numéro = entrée.nextInt();
       
      if(numéro == 11)
      {
         System.out.println("29");
      }
      else
      {
         if( ( (4 <= numéro) && (numéro <= 6) ) || (numéro == 10) )
         {
            System.out.println("31");
         }
         else
         {
            System.out.println("30");
         }
      }
   }
}

#=========================================================================================
# Amitié entre gardesEntraînement
#=========================================================================================
#=========================================================================================
# Comme dans tout métier, certains soldats sont devenus amis, et on peut facilement dire 
# si deux soldats sont amis : si à un moment ils sont de garde en même temps alors ils 
# sont amis, sinon ils ne le sont pas. Afin de développer les relations amicales entre les
#  soldats, le colonel en charge des tours de garde souhaiterait autant que possible mettre
#   en binôme des soldats qui ne sont pas encore amis. Il vous demande votre aide pour
#    déterminer si deux soldats sont amis ou pas.
# 
# Ce que doit faire votre programme :
# Vous devez écrire un programme qui détermine si deux soldats ont été de garde en même temps.
# 
# Votre programme doit lire quatre entiers : la date du début et la date de fin (incluse) du
#  service du premier soldat puis celles du second soldat.
# 
# Si les deux soldats ont, à un moment (même une seule seconde), été de garde en même temps
#  le programme devra écrire "Amis" et sinon "Pas amis".
# Exemple 1
# entrée :
# 2
# 5
# 3
# 6
# sortie :Amis
# Exemple 2
# 
# entrée :
# 1
# 5
# 10
# 15
# sortie :Pas amis
# 
# Exemple 3
# 
# entrée :
# 2
# 4
# 4
# 6
# sortie :Amis
#=========================================================================================

dateDebut1 = int(input())
dateFin1 = int(input())
dateDebut2 = int(input())
dateFin2 = int(input())

if (dateFin2 > dateDebut1 and dateFin1 >= dateFin2)or(dateFin2 > dateDebut1 and dateFin1 >=dateDebut2):
    print("Amis")
else:
    print("Pas amis")
    
#=========================================================================================
# correction
#=========================================================================================
dateDebutPremier = int(input())
dateFinPremier = int(input())
dateDebutSecond = int(input())
dateFinSecond = int(input())
if (dateFinSecond < dateDebutPremier) or (dateFinPremier < dateDebutSecond):
   print("Pas amis")
else:
   print("Amis")
   
#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int dateDébutPremier = entrée.nextInt();
      int dateFinPremier = entrée.nextInt();
      int dateDébutSecond = entrée.nextInt();
      int dateFinSecond = entrée.nextInt();
       
      if ( (dateFinSecond < dateDébutPremier) || (dateFinPremier < dateDébutSecond) )
      {
         System.out.println("Pas amis");
      }
      else
      {
         System.out.println("Amis");
      }
   }
}

    
#=========================================================================================
# #=========================================================================================
# # Nombre de personnes à la fête
# #=========================================================================================
# Le gouverneur a organisé une petite fête à laquelle tous les notables étaient invités. 
# Il souhaiterait à présent faire réaliser une petite affiche vantant le succès de la fête
# et indiquant en particulier le nombre de personnes présentes au moment le plus intense de la fête.
# 
# Ce que doit faire votre programme :
# On vous décrit les arrivées et départs des participants d'une fête, et votre programme 
# doit afficher le nombre maximum de personnes qui ont été présentes au même moment. 
# Chacun des invités est identifié par un numéro.
# 
# Le premier entier à lire est nbPersonnes : le nombre total de personnes qui se sont rendues 
# à la fête. Ensuite, il y a 2 × nbPersonnes entiers à lire, dans l'ordre chronologique 
# des arrivées et départs. Si l'entier est positif, c'est que la personne de numéro
#  correspondant vient d'arriver, s'il est négatif, elle vient de partir. Une fois 
#  qu'une personne est partie, elle ne revient pas.
# 
# Votre programme doit déterminer puis afficher le nombre maximum de personnes qui étaient 
# là simultanément.
# 
# Exemple
# entrée :
# 
# 5

# 1
# 2

# -1
# 3

# 4
# -2

# -4
# 5

# -3
# -5
# sortie :
# 
# 3
# Commentaires
# Au cours de la fête décrite par l'exemple, on a donc les flux suivants :
# 
# l'invité n°1 entre ;
# l'invité n°2 entre ;
# l'invité n°1 sort ;
# l'invité n°3 entre ;
# l'invité n°4 entre ;
# l'invité n°2 sort…
# Le nombre de présents est maximal lors de l'arrivée de la personne n°4 : 
# il y a alors trois invités qui sont arrivés et restés.
#=========================================================================================

nbPersonnes = int(input())
nbPresent = 0
MAxPresent = 0
for i in range(nbPersonnes * 2):
    mouvementPersonne = int(input())
    if mouvementPersonne > 0 :
          nbPresent = nbPresent + 1
          if nbPresent > MAxPresent :
             MAxPresent = nbPresent
       
    elif mouvementPersonne <= 0 :
          nbPresent = nbPresent - 1
       
print(MAxPresent)
   
   
   
#=========================================================================================
# correction    
#=========================================================================================
nbPersonnes = int(input())
nbMax = 0
nbActuel = 0
for loop in range(nbPersonnes * 2):
   numero = int(input())
   if numero > 0:
      nbActuel = nbActuel + 1
      if nbActuel > nbMax:
         nbMax = nbActuel
   else:
      nbActuel = nbActuel - 1
print(nbMax)
#=========================================================================================
# correction java    
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nbPersonnes = entrée.nextInt();
      int nbMax = 0, nbActuel = 0;
      for (int loop = 1; loop <= nbPersonnes * 2; loop = loop + 1)
      {
         int numéro = entrée.nextInt();
         if(numéro > 0)
         {
            nbActuel = nbActuel + 1;
            if(nbActuel > nbMax)
            {
               nbMax = nbActuel;
            }
         }
         else
         {
            nbActuel = nbActuel - 1;
         }
      }
      System.out.println(nbMax);
   }
}



# /////////////////////////////////////////////////
#=========================================================================================
# Casernes de pompiers
#=========================================================================================
# Votre programme doit lire la description de plusieurs paires de zones
# rectangulaires,
    # et pour chacune, déterminer si les deux rectangles s'intersectent.

# Vous devez lire un premier entier, le nombre de paires de zones
# que votre programme devra tester.  Ensuite, pour chaque paire possible,
# deux zones rectangulaires et parallèles aux axes vous sont données l'une après
# l'autre.
# Chaque zone est décrite par 4 entiers : son abscisse minimale et maximale puis
# son ordonnée minimale et maximale.

# Sur cet exemple, la zone du bas est donc décrite par les 4 entiers (1, 6, 1,
# 5) et l'autre par (4, 9, 3, 8) :
nombrePairesZones = int( input() )
validationAxeX = 0
validationAxeY = 0

for loop in range( nombrePairesZones ):
    # Coordonnées zone A
    # zone A axe x premier point
    axeXminA = int( input() )
    # zone A axe x deuxieme point
    axeXmaxA = int( input() )
    # zone A zone axe y premier point
    axeYminA = int( input() )
    # zone A axe y deuxieme point
    axeYmaxA = int( input() )

    # Coordonnées zone B
    # zone B axe x premier point
    axeXminB = int( input() )
    # zone B axe x deuxieme point
    axeXmaxB = int( input() )
    # zone B zone axe y premier point
    axeYminB = int( input() )
    # zone B axe y deuxieme point
    axeYmaxB = int( input() )

    # pour qu'il y ait intersection il faut que sur l'axe des X au moins un des
    # 2 points de la zone B soit compris entre les 2 points de la ZoneA(min et
    # max) ou idem sur l'axe Y
    if (((axeXminA < axeXminB and axeXminB < axeXmaxA) or (axeXminA < axeXmaxB and axeXmaxB < axeXmaxA)) and (
            (axeYminA < axeYminB and axeYminB < axeYmaxA) or (axeYminA < axeYmaxB and axeYmaxB < axeYmaxA))):
        print( "OUI" )
    else:
        print( "NON" )

    # autre possibilite de tests
    if ((axeXminA <= axeXminB and axeXminB <= axeXmaxA) and (axeYminA <= axeYminB and axeYminB <= axeYmaxA)):
        # (axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA)):
        axeX1 = 1
    elif ((axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA) and (axeYminA <= axeYminB and axeYminB <= axeYmaxA)):
        # (axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA)):
        axeX2 = 1
    elif ((axeXminA <= axeXminB and axeXminB <= axeXmaxA) and (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
        # (axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA)):
        axeY1 = 1
    elif ((axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA) and (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
        # (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
        axeY2 = 1
    if (axeX1 == 1 or axeY1 == 1 or axeX2 == 1 or axeY2 == 1):
        print( "OUI autre methode" )
    else:
        # if((axeYminA < axeYminB and axeYminB < axeYmaxA) or (axeYminA < axeYmaxB
        # and axeYmaxB < axeYmaxA))):
        print( "NON autre methode" )

# version avec une liste deja faite pour test


# list = [1, 1, 6, 1, 5, 4, 9, 3, 8]
# list = [1, 1, 6, 1, 5, 4, 9, 3, 8]
# list = [1, 1, 6, 1, 5, 4, 9, 3, 8]
# list = [1, 1, 6, 1, 5, 4, 9, 3, 8]
# list = [1, 10, 15, 10, 5, 33, 58, 23, 5]
# creation d'un liste aleatoire avec n lignes sur n colonnes'
import random
# l'offset sert à de mettre des valeurs aleatoire qu'a partir de la colonne 1 et
# non 0
# car en zero nous avons le nombre de de paire qui doit rester constant à
# l'interieur de la boucle'
offsetPremiereColonne = 6
list = [random.randint( 0, 15 ) for offsetPremiereColonne in range( 9 )]
# list = [1, 1, 6, 1, 5, 4, 9, 3, 8]

list[0] = random.randint( 1, 10 )
nombrePairesZones = list[0]
# print( list )

# tableauSurfaceAoui = []
# tableauSurfaceBoui = []
# tableauSurfaceAnon = []
# tableauSurfaceBnon = []

# liste 2D imbriquée avec n imbrications
tableauSurfaceABnon = [[] for i in range( 2 )]
tableauSurfaceABoui = [[] for i in range( 2 )]
# autre ecriture possible
list2D = [[], []]
nombrePairesZones = 5
for loop in range( nombrePairesZones ):
    # ********************************************
    # liste aléatoire à chaque boucle
    # ********************************************
    list = [random.randint( 0, 25 ) for offsetPremiereColonne in range( 9 )]
    list[0] = nombrePairesZones
    print( list )
    axeX1 = 0
    axeX2 = 0
    axeY1 = 0
    axeY2 = 0
    # *******************************************
    # Coordonnées zone A
    # zone A axe x premier point
    axeXminA = list[1]
    # zone B axe x deuxieme point
    axeXmaxA = list[2]
    # zone A zone axe y premier point
    axeYminA = list[3]
    # zone A axe y deuxieme point
    axeYmaxA = list[4]
    # ***********************************************
    # Coordonnées zone B
    # ***********************************************
    # zone B axe x premier point
    axeXminB = list[5]
    # zone B axe x deuxieme point
    axeXmaxB = list[6]
    # zone B zone axe y premier point
    axeYminB = list[7]
    # zone B axe y deuxieme point
    axeYmaxB = list[8]
    # ***********************************************
    # impression liste et coordonnées
    # ***********************************************
    # print("nombrePairesZones: ",nombrePairesZones)
    # print("zone A \nxMin : ", axeXminA," xMax :",axeXmaxA, " \nyMin
    #:",axeYminA," yMax :", axeYmaxA)
    # print("zone B \nxMin :", axeXminB," xMax :",axeXmaxB," \nyMin :",
    # axeYminB," yMax :", axeYmaxB)

    # surfaceA = (axeXmaxA - axeXminA) * (axeYmaxA - axeYminA)
    # surfaceB = (axeXmaxB - axeXminB) * (axeYmaxB - axeYminB)
    # perimetreA = ((axeXmaxA - axeXminA) + (axeYmaxA - axeYminA)) * 2
    # perimetreB = ((axeXmaxB - axeXminB) + (axeYmaxB - axeYminB)) * 2
    # print( "surface A:", surfaceA )
    # print( "surface B:", surfaceB )
    # print( "perimetre A:", perimetreA )
    # print( "perimetre B:", perimetreB )

    # **********************************************
    # tests
    # **********************************************
    # pour qu'il y ait intersection il faut determiner les longeurs des cotés, savoir quelle est la zone la plus grande et determiner si
    # projetée sur les axes x et y  on a  x1min <x2<x1max  ET  y1min<y2<y1max .
    # les 2 zones etant de taille variable il faut que:
    # maxgauche=max(x1,X2)
    # mindroit=min(x1+largeur1, x2+largeur2)
    # maxbas=max(y1, y2)
    # minhaut=min(y1+hauteur1,y2+hauteur2)
    # maxgauche<mindroit  ET maxbas<minhaut
    # ************************************************
    # if (((axeXminA <= axeXminB and axeXminB <= axeXmaxA) or (axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA)) and (
    #         (axeYminA <= axeYminB and axeYminB <= axeYmaxA) or (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA))):
    #     print( "OUI", "ecart de surface: ", surfaceA - surfaceB, "ecart de perimetre: ", perimetreA - perimetreB )

    # autre possibilite de tests
    if ((axeXminA <= axeXminB and axeXminB <= axeXmaxA) and (axeYminA <= axeYminB and axeYminB <= axeYmaxA)):
        axeX1 = 1
    if ((axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA) and (axeYminA <= axeYminB and axeYminB <= axeYmaxA)):
        axeX2 = 1
    if ((axeXminA <= axeXminB and axeXminB <= axeXmaxA) and (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
        axeY1 = 1
    if ((axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA) and (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
        axeY2 = 1
    if (axeX1 == 1 or axeY1 == 1 or axeX2 == 1 or axeY2 == 1):
        print( "OUI" )
    else:
        print( "NON" )

#         tableauSurfaceAoui.append( surfaceA )
#         tableauSurfaceBoui.append( surfaceB )
#         tableauSurfaceABoui[0].append( surfaceA )
#         tableauSurfaceABoui[1].append( surfaceB )
#     else:
#         print( "NON", "ecart de surface: ", surfaceA - surfaceB, "ecart de perimetre: ", perimetreA - perimetreB )
#         tableauSurfaceAnon.append( surfaceA )
#         tableauSurfaceBnon.append( surfaceB )
#         tableauSurfaceABnon[0].append( surfaceA )
#         tableauSurfaceABnon[1].append( surfaceB )
#
# print( tableauSurfaceAoui, tableauSurfaceBoui )
# print( tableauSurfaceAnon, tableauSurfaceBnon )
#
# print( "tableau recap surface Oui zone A et B", tableauSurfaceABoui )
# print( "tableau recap surface non zone A et B", tableauSurfaceABnon )

# print( "hello3" )
# # autre possibilite de tests
# if ((axeXminA <= axeXminB and axeXminB <= axeXmaxA) and (axeYminA <= axeYminB and axeYminB <= axeYmaxA)):
#     # (axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA)):
#     axeX1 = 1
# elif ((axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA) and (axeYminA <= axeYminB and axeYminB <= axeYmaxA)):
#     # (axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA)):
#     axeX2 = 1
# elif ((axeXminA <= axeXminB and axeXminB <= axeXmaxA) and (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
#     # (axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA)):
#     axeY1 = 1
# elif ((axeXminA <= axeXmaxB and axeXmaxB <= axeXmaxA) and (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
#     # (axeYminA <= axeYmaxB and axeYmaxB <= axeYmaxA)):
#     axeY2 = 1
# if (axeX1 == 1 or axeY1 == 1 or axeX2 == 1 or axeY2 == 1):
#     print( "OUI autre methode" )
# else:
#     # if((axeYminA < axeYminB and axeYminB < axeYmaxA) or (axeYminA < axeYmaxB
#     # and axeYmaxB < axeYmaxA))):
#     print( "NON autre methode" )

# *********************************
# 3eme essai d'algo
# **********************************************
# pour qu'il y ait intersection il faut determiner les longeurs des cotés, savoir quelle est la zone la plus grande et determiner si
# projetée sur les axes x et y  on a  x1min <x2<x1max  ET  y1min<y2<y1max .
# les 2 zones etant de taille variable il faut que:
# maxgauche=max(x1,X2)
# mindroit=min(x1+largeur1, x2+largeur2)
# maxbas=max(y1, y2)
# minhaut=min(y1+hauteur1,y2+hauteur2)
# maxgauche<mindroit  ET maxbas<minhaut
# ************************************************
largeurA = axeXmaxA - axeXminA
largeurB = axeXmaxB - axeXminB
hauteurA = axeYmaxA - axeYminA
hauteurB = axeYmaxB - axeYminB

maxgauche = max( axeXminA, axeXminB )
mindroit = min( axeXminA + largeurA, axeXminB + largeurB )
maxbas = max( axeYminA, axeYminB )
minhaut = min( axeYminA + hauteurA, axeYminB + hauteurB )

if (maxgauche <= mindroit and maxbas <= minhaut):
    print( "OUI" )
else:
    print( "NON" )

# *********************************
# test tableaux automatique
import random

offsetPremiereColonne = 6
for loop in range( 10 ):
    list = [random.randint( -15, 15 ) for offsetPremiereColonne in range( 9 )]
    list[0] = 5
    print( "list ", list )
    list2 = [random.sample( (1, 2, 3, 4, 5, 6, 7, 8, 9), 1 ) for offsetPremiereColonne in range( 9 )]
    list2[0] = 5
    print( "list2 ", list2 )
    print( "random ", random.sample( (1, 2, 3, 4, 5, 6, 7, 8, 9), 1 ) )

# ********************************
# *********************************
# test tableaux automatique de OUI



# **********************************
# parcours tableau 2 dimensions
# **********************************
import random
ligne=5
colonne=2
tableau=[[0]*(colonne+1) for _ in range (ligne+1)]
tableau[1][1]="franck"
tableau[1][2]="desmedt"
print(tableau)
for l in range(0, ligne+1):
    tableau[l] = random.randint( 11, 20 )
    print( tableau[l])
    for c in range( 0, colonne + 1 ):
        tableau[c]=random.randint(0,10)
        print( tableau[c] )
        print(tableau[l],[c])
        print(tableau)

# **********************
# 4eme methode, fonctionne
nombrePairesZones = int( input() )
validationAxeX = 0
validationAxeY = 0

for loop in range( nombrePairesZones ):
    # Coordonnées zone A
    # zone A axe x premier point
    axeXminA = int( input() )
    # zone A axe x deuxieme point
    axeXmaxA = int( input() )
    # zone A zone axe y premier point
    axeYminA = int( input() )
    # zone A axe y deuxieme point
    axeYmaxA = int( input() )

    # Coordonnées zone B
    # zone B axe x premier point
    axeXminB = int( input() )
    # zone B axe x deuxieme point
    axeXmaxB = int( input() )
    # zone B zone axe y premier point
    axeYminB = int( input() )
    # zone B axe y deuxieme point
    axeYmaxB = int( input() )

    # ***************************************
    # trie dans l'ordre croissant des coordonnées A et B sur X et Y
    # print( "avant ", axeXminA, axeXmaxA, axeYminA, axeYmaxA, axeXminB, axeXmaxB, axeYminB, axeYmaxB )
    replace = ""
    if (axeXmaxA < axeXminA):
        replace = axeXmaxA
        axeXmaxA = axeXminA
        axeXminA = replace
    if (axeYmaxA < axeYminA):
        replace = axeYmaxA
        axeYmaxA = axeYminA
        axeYminA = replace

    if (axeXmaxB < axeXminB):
        replace = axeXmaxB
        axeXmaxB = axeXminB
        axeXminB = replace
    if (axeYmaxB < axeYminB):
        replace = axeYmaxB
        axeYmaxB = axeYminB
        axeYminB = replace
    # print( "apres ", axeXminA, axeXmaxA, axeYminA, axeYmaxA, axeXminB, axeXmaxB, axeYminB, axeYmaxB )

    # ***************************************
    # dX = (min( abs( axeXmaxA ), abs( axeXmaxB ) )) - (max( abs( axeXminA ), abs( axeXminB ) ))
    # dY = (min( abs( axeYmaxA ), abs( axeYmaxB ) )) - (max( abs( axeYminA ), abs( axeYminB ) ))
    dX = min( axeXmaxA, axeXmaxB ) - max( axeXminA, axeXminB )
    dY = min( axeYmaxA, axeYmaxB ) - max( axeYminA, axeYminB )
    # print( "max entre -6 et -10: ", max( -6, -10 ) )
    # print( "min entre -6 et -10: ", min( -6, -10 ) )
    # print( "min maxX", min( abs( axeXmaxA ), abs( axeXmaxB ) ) )
    # print( "max minX", max( abs( axeXminA ), abs( axeXminB ) ) )
    # print( "min maxY", min( abs( axeYmaxA ), abs( axeYmaxB ) ) )
    # print( "max minY", max( abs( axeYminA ), abs( axeYminB ) ) )
    # print( "dX: ", dX, "dY: ", dY )
    if (axeXminA == axeXminB and axeXmaxA == axeXmaxB and axeYminA == axeYminB and axeYmaxA == axeYmaxB):
        print( "OUI" )
    if (dX > 0 and dY > 0):
        print( "OUI" )
    else:
        print( "NON" )
# *************************************
# correction
nbPaires = int(input())
for loop in range(nbPaires):
   xMin1 = int(input())
   xMax1 = int(input())
   yMin1 = int(input())
   yMax1 = int(input())
   xMin2 = int(input())
   xMax2 = int(input())
   yMin2 = int(input())
   yMax2 = int(input())
   if ( (xMax2 <= xMin1) or (xMax1 <= xMin2) ) or ( (yMax2 <= yMin1) or (yMax1 <= yMin2) ):
      print("NON")
   else:
      print("OUI")
# en java
package javaProjets;

import java.util.Scanner;
public class TestAlgo {
    static Scanner entrée = new Scanner(System.in);

    public static void main(String[] args) {

        {

            int nbPaires = entrée.nextInt();
            for (int loop = 1; loop <= nbPaires; loop = loop + 1) {
                int xMin1 = entrée.nextInt();
                int xMax1 = entrée.nextInt();
                int yMin1 = entrée.nextInt();
                int yMax1 = entrée.nextInt();
                int xMin2 = entrée.nextInt();
                int xMax2 = entrée.nextInt();
                int yMin2 = entrée.nextInt();
                int yMax2 = entrée.nextInt();

                if ((xMax2 <= xMin1) || (xMax1 <= xMin2) || (yMax2 <= yMin1) || (yMax1 <= yMin2)) {
                    System.out.println("NON");
                } else {
                    System.out.println("OUI");
                }
            }
        }
    }
}


#=========================================================================================
# #=========================================================================================
# # Personne disparue
# #=========================================================================================
# Un personnage important de la cité n'est pas rentré chez lui hier soir et tout le monde 
# est à sa recherche. Or tout habitant de la ville a un numéro unique qui lui est associé 
# et doit signer une sorte de registre quand il sort de la ville. Vous souhaitez savoir si 
# le registre a été signé, auquel cas il faudra étendre les recherches à l'extérieur de la ville.
# 
# Ce que doit faire votre programme :
# On vous donne un entier, le numéro d'une personne recherchée, puis un entier tailleListe, 
# et enfin tailleListe entiers parmi lesquels vous devez chercher le numéro de la personne.
#  Si le numéro est présent dans la liste (il peut l'être plusieurs fois) vous devez afficher 
#  le texte "Sorti de la ville" sinon "Encore dans la ville".
# 
# Exemple
# entrée :
# 
# 42
# 5
# 1
# 7
# 172
# 2
# 41
# sortie :
# 
# Encore dans la ville
#=========================================================================================
numeropersonneRecherche=int(input())
tailleListe=int(input())
liste=[0]*tailleListe
situation=0    
#=========================================================================================
# print(liste)    
#=========================================================================================
for i in range(tailleListe):
    entierListe=int(input())
    liste[i]=entierListe
#=========================================================================================
# print(liste)    
#=========================================================================================

#=========================================================================================
# print(liste[2])
#=========================================================================================

for i in liste:
    #=====================================================================================
    # print(i)
    #=====================================================================================
    if(i==numeropersonneRecherche):
        situation=1
        #=================================================================================
        # print(i," sit",situation)
        #=================================================================================
       
        #=================================================================================
        # print("Sorti de la ville") 
        #=================================================================================
    #=====================================================================================
    # else:  
    #     situation=2
    #=====================================================================================
        #=================================================================================
        # print("Encore dans la ville")
        #=================================================================================

if (situation==1):
    print("Sorti de la ville") 
elif(situation==0):
    print("Encore dans la ville")
    
    
#=========================================================================================
# correction    
#=========================================================================================
numeroPersonne = int(input())
tailleListe = int(input())
estSorti  = False
for loop in range(tailleListe):
   numero = int(input())
   if numero == numeroPersonne:
      estSorti = True
if estSorti:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")
#=========================================================================================
# correction  java  
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int numéroPersonne = entrée.nextInt();
      int tailleListe = entrée.nextInt();
      boolean estSorti = false;
      
      for (int loop = 1; loop <= tailleListe; loop = loop + 1)
      {
         int numéro = entrée.nextInt();
         if(numéro == numéroPersonne)
         {
            estSorti = true;
         }
      }
       
      if(estSorti)
      {
         System.out.println("Sorti de la ville");
      }
      else
      {
         System.out.println("Encore dans la ville");
      }
   }
}

#=========================================================================================
# #=========================================================================================
# # La grande fête
# #=========================================================================================
# Un espion était présent à la grande fête organisée la semaine dernière par le gouverneur. 
# Bien qu'on n'ait pas pu l'identifier, on a réussi à intercepter son rapport et à estimer
#  en fonction de ce qu'il a pu voir, à quelle période il a été présent. Sachant pour 
#  chaque invité sa date d'arrivée et de départ, on aimerait interroger tous les suspects
#   potentiels. Vous souhaitez savoir combien de suspects il faudra interroger.
# 
# Ce que doit faire votre programme :
# On vous donne une période de temps à étudier, et les dates d'arrivée et de départ d'un 
# certain nombre d'invités d'une fête. Écrivez un programme qui détermine combien d'invités
#  ont été présents à un moment de la période étudiée.
# 
# Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de
#  la période étudiée. L'entier suivant, nbInvites, est le nombre total d'invités. Pour
#   chaque invité, votre programme doit ensuite lire deux entiers : sa date d'arrivée et
#    de départ. Un invité est suspect si la période à laquelle il a été présent intersecte
#     la période étudiée. Votre programme doit afficher le nombre d'invités suspects.
# 
# Exemple
# entrée :
# 
# 8
# 12
# 5

# 4
# 7

# 2
# 11

# 3
# 6

# 1
# 8

# 14
# 19
# sortie :
# 
# 2
#=========================================================================================
import random
#=========================================================================================
# liste = [8, 12, 6]
#=========================================================================================

liste = [random.randint(2, 30) for offsetPremiereColonne in range(3)]
#=========================================================================================
# boucle permettant de forcer la date de fin>date de début
#=========================================================================================
while not(liste[0] <= liste[1]):
     liste = [random.randint(2, 30) for offsetPremiereColonne in range(3)]     
print(" liste" , liste)

#=========================================================================================
# debut=int(input())
# fin=int(input())
# nbInvite=int(input())
#=========================================================================================

somme = 0 

debut = liste[0]
fin = liste[1] 
nbInvite = liste[2]

#=========================================================================================
# liste2 = [8, 12, 5,4, 7, 2, 11, 3, 6, 1, 8, 14, 19, 25, 5]
#=========================================================================================
j = 0
#=========================================================================================
# v=0
# liste2  = [random.randint( 1, 31) for offsetPremiereColonne in range(nbInvite * 2)]
# while not(liste2[v]<=liste2[v+1]):
#     liste2  = [random.randint( 1, 31) for offsetPremiereColonne in range(nbInvite * 2)]
#     v+=2
# print(" liste2" , liste2)
#=========================================================================================

L_size = nbInvite # int to pass to range
liste2 = []
for _ in range(L_size):
#=====================================================================================
# num = random.random() # create random num and append
#=====================================================================================
    
    num1 = random.randint(1,31) # create random num and append
    num2 = random.randint(1,31) # create random num and append
    while not(num2 >= num1):
        num1 = random.randint(1,31) # create random num and append
        num2 = random.randint(num2,31) # create random num and append
        
    liste2.append(num1)
    liste2.append(num2)
print ("liste2",liste2) 


for i in range(nbInvite):
    #=====================================================================================
    # arrive=int(input())
    # depart=int(input())
    #=====================================================================================
    #=====================================================================================
    # print("i", i," j", j)
    #=====================================================================================
   
    #=====================================================================================
    # liste2 = [4, 7, 2, 11, 3, 6, 1, 8, 14, 19, 25, 5]
    #=====================================================================================
   
    arrive = liste2[j]
    depart = liste2[j + 1]
    j +=  2
    #=====================================================================================
    print("debut ", debut, " fin ", fin, " arrive ", arrive, " depart ", depart)
    if (((debut <= arrive <= fin) or (debut <= depart <= fin))and (arrive<=debut and depart>=fin)):
    #=====================================================================================
    # if not((arrive>=debut and arrive<= fin) or (depart>=debut  and depart<= fin)):
    #=====================================================================================
    #=====================================================================================
    # if not((debut <= arrive and fin >= arrive) or (debut <= depart and fin >= depart)):
    #=====================================================================================
        
    #=====================================================================================
    # if not(arrive>=debut and depart <= fin):
    #=====================================================================================
    #=====================================================================================
    # if not((fin <= arrive)or (depart <= debut)):
    #=====================================================================================
        somme +=  1
        print("somme", somme)
print(somme)

#=========================================================================================
# ****************************************************************
#=========================================================================================

#=========================================================================================
#      PYTHON CREATION LISTE ALEATOIRE        
#  Avec python on peut générer des nombres aléatoires avec le module random. Exemple 
#  de comment créer une liste de nombres entiers aléatoires avec python
# 
#  import random
#  l = [random.randrange(0, 10) for i in range(20)]
#  l=[1, 9, 7, 3, 1, 5, 9, 4, 8, 1, 0, 7, 5, 4, 7, 2, 9, 5, 6, 2]
#  Pour créer une liste de nombres entiers aléatoires unique avec python:
# 
# import random
# l = random.sample(range(1,100), 10)
#  l=[10, 70, 11, 91, 84, 17, 29, 36, 61, 96]            
#=========================================================================================

#=========================================================================================
# VERSION AVEC UNE BOUCLE ET APPEND
# import random
# random.seed(0)
# #=========================================================================================
# # L_size = int(input("Enter a real number: ")) # int to pass to range
# #=========================================================================================
# L_size = 2 # int to pass to range
# L = []
# for _ in range(L_size):
#     #=====================================================================================
#     # num = random.random() # create random num and append
#     #=====================================================================================
#     num = random.random() # create random num and append
#     L.append(num)
# print (L)     
#=========================================================================================

#=========================================================================================
# *******************************
#=========================================================================================


#=========================================================================================
# version a soumettre   
#=========================================================================================
#=========================================================================================
# debut=int(input())
# fin=int(input())
# nbInvite=int(input())
# somme=0 
# 
# for i in range(nbInvite):
#     arrive=int(input())
#     depart=int(input())
#     if not(debut<=arrive and fin>=arrive) or (debut<=depart and fin>=depart):
#         somme=somme+1
# print(somme)
#=========================================================================================


#=========================================================================================
# correction
#=========================================================================================
espionDebut = int(input())
espionFin = int(input())
nbInvites = int(input())
nbSuspects = 0
for loop in range(nbInvites):
   debut = int(input())
   fin = int(input())
   if not( (espionFin < debut) or (fin < espionDebut) ):
      nbSuspects = nbSuspects + 1
print(nbSuspects)

#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int espionDébut = entrée.nextInt();
      int espionFin = entrée.nextInt();
      int nbInvités = entrée.nextInt();
       
      int nbSuspects = 0;
      for (int loop = 1; loop <= nbInvités; loop = loop + 1)
      {
         int début = entrée.nextInt();
         int fin = entrée.nextInt();
         if( !( (espionFin < début) || (fin < espionDébut) ) )
         {
            nbSuspects = nbSuspects + 1;
         }
      }
      System.out.println(nbSuspects);
   }
}

#=========================================================================================
# L'espion est démasqué !Entraînement
#=========================================================================================
#=========================================================================================
# Grâce à un certain nombre d'informateurs plus ou moins fiables, le chef de la police 
# a recueilli des indications qui devraient lui permettre enfin de démasquer cet espion
#  qui lui échappe depuis des semaines. La population de la ville étant relativement importante, 
#  il vous demande votre aide afin d'automatiser un peu les choses. Vous devez estimer la
#   probabilité qu'une personne soit un espion.
# 
# Ce que doit faire votre programme :
# Votre programme doit lire entier : un nombre de personnes à considérer. Ensuite, pour chaque 
# personne, il doit lire son signalement sous la forme de cinq entiers : sa taille en 
# centimètres, son âge en années, son poids en kilogrammes, un entier valant 1 si la personne 
# possède un cheval et 0 sinon, et un entier valant 1 si la personne à les cheveux bruns et 0 sinon.
# 
# On veut déterminer pour chaque personne à quel point elle correspond aux 5 critères suivants :
# 
# il aurait une taille supérieure ou égale à 178 cm et inférieure ou égale à 182 cm ;
# il aurait au moins 34 ans ;
# il pèserait strictement moins de 70 kg ;
# il n'a pas de cheval ;
# il a les cheveux bruns.
# Lorsque cela n'est pas précisé explicitement, les inégalités sont au sens large.
# 
# Pour chaque personne, vous devez tester tous les critères. S'ils sont vérifiés 
#tous 
# les 5, vous devez afficher « Très probable ».
# Si seulement 3 ou 4 sont vérifiés, vous  devez afficher « Probable ». 
# Si aucun n'est vérifié, vous devez afficher « Impossible »,
#  et dans les autres cas, vous devez afficher « Peu probable ».
# 
# Exemple
# entrée :
# 
# 1
# 180
# 40
# 65
# 0
# 1
# sortie :
# 
# Très probable
#=========================================================================================
import random
nbrePpersonne = int(input())
#=========================================================================================
# creation de tableau aléatoire
#=========================================================================================
liste=[0]*6
liste[0]=nbrePpersonne
for i in range(nbrePpersonne):
    liste[1]=random.randint(160, 190)
    liste[2]=random.randint(40, 90)
    liste[3]=random.randint(50, 95)
    liste[4]=random.randint(0,1)
    liste[5]=random.randint(0,1)
    #=====================================================================================
    # print("liste", liste)    
    #=====================================================================================


#=========================================================================================
# for loop in range(nbrePpersonne):
#=========================================================================================
    
    res = 0
    #=====================================================================================
    # taille = int(input())
    # age = int(input())
    # poids = int(input())
    # aUnCheval = int(input())
    # aCheveuxBrun = int(input())
    #=====================================================================================
    
    taille = liste[1]
    age = liste[2]
    poids= liste[3]
    aUnCheval = liste[4]
    aCheveuxBrun= liste[5]
    print( " taille 178 <= taille <= 182,/-/" ,"age >= 34,/-/ ","poids < 70 ,/-/","aUnCheval ==0 ,/-/","aCheveuxBrun ==1" )
    print( " taille" ,taille,"age",age,"poids",poids,"aUnCheval",aUnCheval,"aCheveuxBrun",aCheveuxBrun  )
    
    if (178 <= taille <= 182):
        res += 1
        print("taille ok")
        
    if (age >= 34):
        res += 1
        print("age ok")
        
    if(poids < 70):
        res += 1
        print("poids ok")
        
    if (aUnCheval==0):
        res += 1
        print("cheval ok")
       
    if(aCheveuxBrun==1):
        print("cheveux ok")
        res += 1
    print("res",res)   
        
    if(res == 5):
        print("Très probable")
    elif (res==3 or res==4):
        print("Probable")
    elif(res==1 or res==2):
        print("Peu probable")
    else:
        print("Impossible")
        
        
        

#=========================================================================================
# correction
#=========================================================================================
nbPersonnes = int(input())
for loop in range(nbPersonnes):
   nbCriteres = 0
   taille = int(input())
   if (178 <= taille) and (taille <= 182):
      nbCriteres = nbCriteres + 1
   age = int(input())
   if age >= 34:
      nbCriteres = nbCriteres + 1
   poids = int(input())
   if poids < 70:
      nbCriteres = nbCriteres + 1
   aCheval = int(input())
   if aCheval == 0:
      nbCriteres = nbCriteres + 1
   aLesCheveuxBruns = int(input())
   if aLesCheveuxBruns == 1:
      nbCriteres = nbCriteres + 1
   
   if nbCriteres == 0:
      print("Impossible")
   elif nbCriteres == 5:
      print("Très probable")
   elif nbCriteres >= 3:
      print("Probable")
   else:
      print("Peu probable")
#=========================================================================================
# correction java
#=========================================================================================

import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nbPersonnes = entrée.nextInt();
    
      for (int loop = 1; loop <= nbPersonnes; loop = loop + 1)
      {
         int taille = entrée.nextInt();
         int âge = entrée.nextInt();
         int poids = entrée.nextInt();
         int aCheval = entrée.nextInt();
         int aLesCheveuxBruns = entrée.nextInt();
         
         int nbCritères = 0;
         if((178 <= taille) && (taille <= 182))
         {
            nbCritères = nbCritères+ 1;
         }
         if(âge >= 34)
         {
            nbCritères = nbCritères+ 1;
         }
         if(poids < 70)
         {
            nbCritères = nbCritères+ 1;
         }
         if(aCheval == 0)
         {
            nbCritères = nbCritères+ 1;
         }
         if(aLesCheveuxBruns == 1)
         {
            nbCritères = nbCritères+ 1;
         }
           
         if(nbCritères == 0)
         {
            System.out.println("Impossible");
         }
         else if(nbCritères == 5)
         {
            System.out.println("Très probable");
         }
         else if(nbCritères >= 3)
         {
            System.out.println("Probable");
         }
         else
         {
            System.out.println("Peu probable");
         }
      }
   }
}
#=========================================================================================
# Département de médecine : contrôle d'une épidémie
# Afin de pouvoir mieux combattre les différentes épidémies, parfois très graves, qui 
# se développent régulièrement dans la région, le département de médecine de l'université 
# a lancé une grande étude. En particulier, les chercheurs s'intéressent à la vitesse de 
# propagation d'une épidémie et donc à la vitesse à laquelle des mesures sanitaires doivent êtres mises en place.
# 
# Ce que doit faire votre programme :
# Votre programme doit d'abord lire un entier, la population totale de la ville. Sachant
#  qu'une personne était malade au jour 1 et que chaque malade contamine deux nouvelles
#   personnes le jour suivant (et chacun des jours qui suivent), vous devez calculer à
#    partir de quel jour toute la population de la ville sera malade.
# 
# Exemples
# Exemple 1
# entrée : 3
# sortie : 2
# Exemple 2
# entrée : 10
# sortie : 4
# Commentaires
# On a 1 malade le premier jour, donc 2 nouveaux malades le second jour, soit un total de 
# 3 malades. On a donc 6 nouveaux malades au troisième jour, soit un total de 9 malades.
#  On a donc 18 nouveaux malades au quatrième jour, soit…
#=========================================================================================

#=========================================================================================
# site donnant un algo avec une suite d'entiers
# http://oeis.org/search?q=1%2C3%2C9%2C27&sort=&language=&go=Search
# 1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323
#=========================================================================================

populationTotaleVille = int(input())
nbMalade = 1
jour = 0
if (populationTotaleVille<=3):
    jour=2
    print(jour,"jours avec " , nbMalade,"malades" )
else:        
    while (nbMalade <= populationTotaleVille):
        #=====================================================================================
        # nbMalade = nbMalade+nbMalade*2
        #=====================================================================================
        #=====================================================================================
        # nbMalade = nbMalade*3
        #=====================================================================================
        nbMalade *= 3
        #=====================================================================================
        # print(" malades" , nbMalade)
        #=====================================================================================
        #=====================================================================================
        # print(" jour" , jour)
        #=====================================================================================
        jour += 1
    print(jour+1,"jours avec " , nbMalade,"malades" )
    
    
#=========================================================================================
# correction
#=========================================================================================
populationVille = int(input())
numJour = 1
nbMalades = 1
while nbMalades < populationVille:
   numJour = numJour + 1
   nbMalades = nbMalades * 3
print(numJour)
#=========================================================================================
# correction java
#=========================================================================================
import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int populationVille = entrée.nextInt();
      int numJour = 1;
      int nbMalades = 1;
      while (nbMalades < populationVille) {
         numJour = numJour + 1;
         nbMalades = nbMalades * 3;
      }
      System.out.println(numJour);
   }
}

#=========================================================================================
# **********
#=========================================================================================

#=========================================================================================
# Administration : comptes annuels
# Une grande partie du travail de l'administration de l'université, en plus de gérer 
# les enseignants, les étudiants, les cours… est de veiller au bon fonctionnement de 
# l'université et en particulier à ce que les comptes soient bien tenus. En particulier
#  il faut, une fois par an, faire un bilan annuel des dépenses.
# 
# Toutes les dépenses de l'année ont été enregistrées et classées dans une multitude 
# de dossiers et il faut maintenant calculer la somme de toutes ces dépenses. Mais 
# personne ne sait exactement combien de dépenses différentes ont été effectuées 
# durant l'année écoulée !
# 
# Ce que doit faire votre programme :
# Votre programme devra lire une suite d'entiers positifs et afficher leur somme.
#  On ne sait pas combien il y aura d'entiers, mais la suite se termine toujours par
#   la valeur -1 (qui n'est pas une dépense, juste un marqueur de fin).
# 
# Exemple 1
# entrée :
# 1000
# 2000
# 500
# -1
# sortie :3500

# Exemple 2
# entrée :-1
# sortie :0
#=========================================================================================

valeurEntier=0
somme=0
while not(valeurEntier==-1):
    valeurEntier=int(input())
    somme+=valeurEntier
print("somme " ,somme+1 )

#=========================================================================================
# correction
#=========================================================================================
sommeDépenses = 0
dépense = int(input())
while dépense != -1:
   sommeDépenses = sommeDépenses + dépense
   dépense = int(input())
print(sommeDépenses)

#=========================================================================================
# correction java 
#=========================================================================================

  import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int dépense = entrée.nextInt();
      int sommeDépenses = 0;
      while (dépense != -1)
      {
         sommeDépenses = sommeDépenses + dépense;
         dépense = entrée.nextInt();
      }
      System.out.println(sommeDépenses);
   }
}  
    

#=========================================================================================
# *******************
#=========================================================================================

#=========================================================================================
# Département de pédagogie : le « c'est plus, c'est moins »
# Dans une cité commerçante, il est important que les habitants soient forts en calcul 
# mental afin de pouvoir négocier leurs prix et choisir les meilleurs produits sans se 
# faire avoir. Le département de pédagogie de l'université a donc été sollicité afin de 
# mettre au point des exercices stimulants pour les enfants, qui vont les inciter à 
# travailler leur calcul mental.
# 
# Réalisant le potentiel que peut avoir votre robot dans un cadre pédagogique, les 
# chercheurs vous demandent de mettre au point un programme capable de faire jouer de
#  manière automatisée un enfant au jeu du « c'est plus, c'est moins » : l'enfant doit
#   deviner un nombre secret en faisant des propositions, et on lui répond chaque fois 
#   par « c'est plus » ou « c'est moins », jusqu'à ce qu'il ait trouvé le bon nombre.
# 
# L'objectif est bien sûr pour les enfants de trouver le bon nombre le plus rapidement possible !
# 
# Ce que doit faire votre programme :
# Votre programme doit d'abord lire un entier, le nombre que l'enfant devra trouver. Ensuite,
#  il devra lire les propositions du joueur, 
#  et afficher à chaque fois le texte « c'est plus » (l'enfant a proposé un nombre trop petit)
#   ou « c'est moins » (l'enfant a proposé un nombre trop grand) selon les cas, 
#   et recommencer tant que l'enfant n'a pas trouvé le bon nombre.
# 
# À la fin, il faudra afficher le texte « Nombre d'essais nécessaires : »
#  puis, à la ligne en dessous, le nombre d'essais qui ont été nécessaires.
# 
# On vous garantit que l'enfant finira par trouver la bonne valeur !
# 
# Exemples
# Exemple 1
# entrée :
# 5
# 1
# 2
# 3
# 4
# 5
# sortie :
# c'est plus
# c'est plus
# c'est plus
# c'est plus
# Nombre d'essais nécessaires :
# 5
# 
# Exemple 2
# entrée :
# 10
# 5
# 15
# 8
# 12
# 11
# 10
# sortie :
# 
# c'est plus
# c'est moins
# c'est plus
# c'est moins
# c'est moins
# Nombre d'essais nécessaires :
# 6
# 
# Exemple 3
# entrée :
# -50
# -80
# -50
# sortie :
# 
# c'est plus
# Nombre d'essais nécessaires :
# 2
#=========================================================================================
devineLeChiffre=int(input())
chiffreEnfant=0
nbreEssais=0

while (chiffreEnfant!=devineLeChiffre):
    chiffreEnfant=int(input())
    if (chiffreEnfant<devineLeChiffre):
        print("c'est plus")
    elif (chiffreEnfant>devineLeChiffre):
        print("c'est moins")
    nbreEssais+=1       
print( "Nombre d'essais nécessaires :\n" , nbreEssais )
    
    
#=========================================================================================
# correction    
#=========================================================================================
aDeviner = int(input())
proposition = int(input())
nbEssais = 1
while proposition != aDeviner:
   if proposition < aDeviner:
      print("c'est plus")
   if proposition > aDeviner:
      print("c'est moins")
   proposition = int(input())
   nbEssais = nbEssais + 1
print("Nombre d'essais nécessaires : ")
print(nbEssais)




#=========================================================================================
# correction    java
#=========================================================================================
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int àDeviner = entrée.nextInt();
      int proposition = àDeviner + 1;
      int nbEssais = 0;
      while (proposition != àDeviner)
      {
         proposition = entrée.nextInt();
         if (proposition < àDeviner)
         {
            System.out.println("c'est plus");
         }
         if (proposition > àDeviner)
         {
            System.out.println("c'est moins");
         }
         nbEssais = nbEssais + 1;
      }
      System.out.println("Nombre d'essais nécessaires : ");
      System.out.println(nbEssais);
   }
}    






 #========================================================================================
 # Zones de couleurs
 #========================================================================================
# ********************************
import random
# zone de couleur
#  Un espion a été démasqué dans la ville où vous vous trouvez.
#  Son interrogatoire n'a pas été très fructueux : la seule chose que vous savez, c'est qu'il espionnait
#  les savants de l'université, une puissance étrangère étant intéressée par leurs recherches.
#  Vous vous rendez donc à l'université pour discuter avec les chercheurs mais à peine arrivé,
#  vous êtes recruté comme assistant par le laboratoire d'étude du comportement humain.
#
# Celui-ci réalise une expérience consistant à demander à plusieurs personnes de placer
# chacune un jeton sur une table contenant des zones de différentes couleurs. Les chercheurs souhaitent
# ainsi étudier si le choix de la zone où une personne place son jeton est lié à la couleur des vêtements qu'elle porte.
# Ce que doit faire votre programme :
#
# Sur une table est placée une feuille de papier rectangulaire de 90 cm de large et 70 cm de haut,
# composée de zones de différentes couleurs, comme le décrit la figure ci-dessous. Un certain nombre de
# personnes placent l'une après l'autre un jeton où elles le souhaitent sur la table, à l'exception
# des frontières entre les différentes zones.
#
#
#
#  On vous donne en entrée le nombre de jetons qui ont été déposés, puis, pour chaque jeton, ses coordonnées
#  sur la feuille par rapport à l'origine en haut à gauche, sous la forme d'une abscisse et
#  d'une ordonnée entre −1 000 et 1 000.
#
# Votre programme devra qualifier chaque jeton avec l'un des textes suivants, en fonction de
# la couleur sur laquelle il se trouve :
#
#     « En dehors de la feuille »
#     « Dans une zone jaune »
#     « Dans une zone bleue »
#     « Dans une zone rouge »
#
# Essayez d'écrire votre programme de sorte qu'il y ait au maximum une condition par possibilité de texte affiché.

# jaune (90,70)-bleu-rouge
# bleu((10, 10),(10,55)),((25,10),(25,55)),(25,10,25,20),(85,55)
# blue(10,10, 10,55)(85,10,85,55) -(25,20,25,45)(50,20,50,45)
# rouge(15,60) ,(45,70)
# rouge(60,70),(85,70)

nbreJeton = int( input() )
# nbreJeton = 50

for loop in range( nbreJeton ):
    x= int( input() )
    y= int( input() )
    # x=random.randint(-10,100)
    # y=random.randint(-10,80)
    # print("x: ",x,"y: ",y)
    if not(0<=x<90 and 0<=y<70):
        print( "En dehors de la feuille" )
    elif((15<=x<45 or 60<=x<85) and 60<=y<70):
        print( "Dans une zone rouge" )
    elif((10<=x<85 and 10<=y<55) and not(25<=x<50 and  20<=y<45) ):
        print( "Dans une zone bleue" )
    else:
        print( "Dans une zone jaune" )

# correction:
nbJetons = int(input())
for loop in range(nbJetons):
   x = int(input())
   y = int(input())
   if x < 0 or x > 90 or y < 0 or y > 70:
      print("En dehors de la feuille")
   elif y > 60 and ((x > 15 and x < 45) or (x > 60 and x < 85)):
      print("Dans une zone rouge")
   elif x > 10 and x < 85 and y > 10 and y < 55 and not(x > 25 and x < 50 and y > 20 and y < 45):
      print("Dans une zone bleue")
   else:
      print("Dans une zone jaune")


# en java
import algorea.Scanner;

# //correction java
class Main {
static Scanner entrée = new Scanner(System.in );
public static void main(String[] args) {
int nbPoints = entrée.nextInt();

for (int loop = 1; loop <= nbPoints; loop = loop + 1) {
int x = entrée.nextInt();
int y = entrée.nextInt();
if (x < 0 || x > 90 || y < 0 || y > 70) {
System.out.println("En dehors de la feuille");
} else if (y > 60 & & ((x > 15 & & x < 45) | | (x > 60 & & x < 85))) {
System.out.println("Dans une zone rouge");
} else if (x > 10 & & x < 85 & & y > 10 & & y < 55 & & !(x > 25 & & x < 50 & & y > 20 & & y < 45)) {
System.out.println("Dans une zone bleue");
} else {
System.out.println("Dans une zone jaune");
}
}
}
}

# *********************************
# Département de chimie : mélange explosif

#
# Les chimistes de l'université ont mis au point un nouveau procédé de fabrication d'un onguent
# qui permet une cicatrisation très rapide des blessures. Ce procédé est cependant très long et
# nécessite une surveillance de tous les instants de la préparation en train de chauffer, et ce parfois
# pendant des heures. Confier cette tâche à un étudiant n'est pas possible, ils s'endorment toujours
# ou ne font pas attention… et cela risque alors d'exploser !
#
# Un dispositif automatique de surveillance de la préparation serait donc intéressant.
# Celui-ci surveillerait la température toutes les 15 secondes, et si celle-ci devient anormale alors
# une alarme devrait sonner, afin de prévenir tout le monde.
# Ce que doit faire votre programme :
#
# Votre programme devra lire trois entiers : le nombre total de mesures envisagées ainsi que la température
# minimum et maximum autorisées. Les entiers suivants seront les différentes températures relevées au cours du temps.
#
# Tant que les températures relevées restent dans le bon intervalle, votre programme devra écrire le
# texte « Rien à signaler », mais dès que la température n'est pas bonne il doit
# écrire le texte « Alerte !! » et s'arrêter.


nombreTotalMesures = 5
temperatureMinimum = -10
temperatureMaximum = 70
# temperatureEnregistre = temperatureMinimum
# temperatureEnregistre = int( input() )
nbMesure = 0
while nbMesure < nombreTotalMesures and temperatureMinimum <= temperatureEnregistre <= temperatureMaximum:
    temperatureEnregistre = int( input() )
    if (temperatureMinimum <= temperatureEnregistre <= temperatureMaximum):
        print( "Rien à signaler" )
    nbMesure = nbMesure + 1
if not (temperatureMinimum <= temperatureEnregistre <= temperatureMaximum):
    print( "Alerte !!" )

# correction
nbMesures = int(input())
tempMin = int(input())
tempMax = int(input())
numMesure = 0
tempValide = True
while numMesure < nbMesures and tempValide:
   température = int(input())
   tempValide = (tempMin <= température and température <= tempMax)
   if tempValide:
      print("Rien à signaler")
   else:
      print("Alerte !!")
   numMesure = numMesure + 1

 # en java
import algorea.Scanner;


import java.util.Scanner;

/**
 * @author franck Desmedt
 *
 */
public class TestAlgo {

    /**
     * @description
     *
     * @return void
     *
     * @method main
     * @class TestAlgo
     * @version 1.0
     * @date lundi 02 sept. 2019
     * @see
     *
     **/
    static Scanner entrée = new Scanner(System.in);

    public static void main(String[] args) {

        int nbMesures = entrée.nextInt();
        int tempMin = entrée.nextInt();
        int tempMax = entrée.nextInt();
        int numMesure = 0;
        boolean tempValide = true;

        while (numMesure < nbMesures && tempValide) {
            int température = entrée.nextInt();
            tempValide = (tempMin <= température && température <= tempMax);
            if (tempValide) {
                System.out.println("Rien à signaler");
            } else {
                System.out.println("Alerte !!");
            }
            numMesure = numMesure + 1;
        }
    }

}



# ********
#
#
# *************************
# Département d'architecture : construction d'une pyramide
# Les habitants adorent les constructions en forme de pyramide ; de nombreux bâtiments officiels
# ont d'ailleurs cette forme. Pour fêter les 150 ans de la construction de la ville,
# le gouverneur a demandé la construction d'une grande et majestueuse pyramide à l'entrée de la ville.
# Malheureusement, en ces périodes de rigueur budgétaire, il y a peu d'argent pour ce projet.
# Les architectes souhaitent cependant construire la plus grande pyramide possible étant donné le budget prévu.

# Ce que doit faire votre programme:
# Votre programme doit d'abord lire un entier : le nombre maximum de pierres dont pourra être composée la pyramide.
# Il devra ensuite calculer et afficher un entier : la hauteur de la plus grande pyramide qui pourra être construite,
# ainsi que le nombre de pierres qui sera nécessaire.


# nbrePierres=int(input())


nbrePierres = 26042
pierreUtiles = 0
hauteur = 1
resultat = 0
# while nbrePierres<pierreUtiles:
while (pierreUtiles + (hauteur ** 2)) <= nbrePierres:
    # print( "hauteur", hauteur )
    # if(pierreUtiles < nbrePierres):
    pierreUtiles = pierreUtiles + hauteur ** 2
    hauteur = hauteur + 1
    # print( "nombre de pierres necessaires ", pierreUtiles )
print( "hauteur", hauteur - 1 )
print( "nombre de pierres necessaires ", pierreUtiles )

# calcul par formule directe
n=6
pierreUtiles=n*(n+1)*(2*n+1)/6
print(pierreUtiles)

# **********************
# correction
nombreMaximumPierres = int( input() )
nombrePierres = 0
hauteur = 1
while nombrePierres + hauteur * hauteur <= nombreMaximumPierres:
    nombrePierres = nombrePierres + hauteur * hauteur
    hauteur = hauteur + 1
print( hauteur - 1 )
print( nombrePierres )

# *************
# java
import algorea.Scanner;

class Main
  public static void main(String[] args) {

        Scanner entrée = new Scanner(System.in);
        int nombreMaximumPierres = entrée.nextInt();
        int nombrePierres = 0;
        int hauteur = 1;

        while (nombrePierres + hauteur * hauteur <= nombreMaximumPierres) {
            nombrePierres = nombrePierres + hauteur * hauteur;
            hauteur = hauteur + 1;
        }
        System.out.println(hauteur - 1);
        System.out.println(nombrePierres);
    }
}


# *********************************************