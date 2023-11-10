class Main {
public static void main(String[] args) {
System.out.println("Hello world!")
}
}

##///////////////////////////////////////////////////////////////////


print( "Ma devise est 'Parler peu mais parler bien'." )
print( "Je m'appelle Camthalion" )
print( "Coucou !" )


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
classMain
{
    public
static
void
main( String[]
args) {
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
import static

algorea.Robot. *;


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
    posActuelle = entrée.nextInt()
    int
    nbVillages = entrée.nextInt()
    int
    nbAccessibles = 0
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


# /////////////////////////////////////////////////

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
import algorea.Scanner;


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
    Scanner( System. in );
    int
    nbPaires = entrée.nextInt();
    for (int loop = 1; loop <= nbPaires; loop = loop + 1)
    {
        int xMin1 = entrée.nextInt();
    int xMax1 = entrée.nextInt();
    int yMin1 = entrée.nextInt();
    int yMax1 = entrée.nextInt();
    int xMin2 = entrée.nextInt();
    int xMax2 = entrée.nextInt();
    int yMin2 = entrée.nextInt();
    int yMax2 = entrée.nextInt();

    if ((xMax2 <= xMin1) | | (xMax1 <= xMin2) | | (yMax2 <= yMin1) | | (yMax1 <= yMin2))
    {
    System.out.println("NON");
    }
    else
    {
    System.out.println("OUI");
    }
    }
    }
    }
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


class Main {
static Scanner entrée = new Scanner(System.in );
public static void main(String[] args) {
int nbPoints = entrée.nextInt();

for (int loop = 1; loop <= nbPoints; loop = loop + 1) {
int x = entrée.nextInt();
int y = entrée.nextInt();
if (x < 0 | | x > 90 | | y < 0 | | y > 70) {
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


class Main {
static Scanner entrée = new Scanner(System.in );
public static void main(String[] args) {
int nbMesures = entrée.nextInt();
int tempMin = entrée.nextInt();
int tempMax = entrée.nextInt();
int numMesure = 0;
boolean tempValide = true;


while (numMesure < nbMesures & & tempValide)
    {
        int
    température = entrée.nextInt();
    tempValide = (tempMin <= température & & température <= tempMax);
    if (tempValide) {
    System.out.println("Rien à signaler");
    }
    else {
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
    {
        public
    static
    void
    main( String[]
    args)
    {
        Scanner
    entrée = new
    Scanner( System. in );
    int
    nombreMaximumPierres = entrée.nextInt();
    int
    nombrePierres = 0;
    int
    hauteur = 1;


while (nombrePierres + hauteur * hauteur <= nombreMaximumPierres)
    {
        nombrePierres = nombrePierres + hauteur * hauteur;
    hauteur = hauteur + 1;
    }
    System.out.println( hauteur - 1 );
    System.out.println( nombrePierres );
}
}


# *********************************************