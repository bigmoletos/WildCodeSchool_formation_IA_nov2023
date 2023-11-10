class Main {
   public static void main(String[] args) {
      System.out.println("Hello world!");
   }
}

///////////////////////////////////
print("Ma devise est 'Parler peu mais parler bien'.")
print("Je m'appelle Camthalion")
print("Coucou !")

class Main {
   public static void main(String[] args) {
      System.out.println("Coucou !");
      System.out.println("Je m'appelle Camthalion");
      System.out.println("Ma devise est 'Parler peu mais parler bien'.");
   }
}

//////////////////////
Tout droit tu grimperas,
La clé tu trouveras,
Habile tu seras,
Quand tu les porteras,
Et avec le chef tu reviendras !
///////////////////////////////
class Main {
   public static void main(String[] args) {
      System.out.println("Tout droit tu grimperas,");
      System.out.println("La clé tu trouveras,");
      System.out.println("Habile tu seras,");
      System.out.println("Quand tu les porteras,");
      System.out.println("Et avec le chef tu reviendras !");
   }
}
//////////////////////////////
from robot import *
haut()
haut()
haut()
droite()
droite()
bas()
bas()
droite()
//////////////////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      haut();
      haut();
      haut();
      droite();
      droite();
      bas();
      bas();
      droite();
   }
}

from robot import *
deplacer(1, 3)
deplacer(1, 2)
deplacer(3, 1)
/////////////////////////////
n=4
print ("tour Hanoi avec ", n ," plateaux")
def hanoi(n,a=1,b=2,c=3):
    if (n > 0):
        hanoi(n-1, a , c ,b)
        print ("deplacer ", a ,"sur", c)
        hanoi(n-1, b , a , c)
hanoi(n,a=1,b=2,c=3)
/////////////////////////////////////
from robot import *
deplacer( 1 , 2 )
deplacer( 1 , 3 )
deplacer( 2 , 3 )
deplacer( 1 , 2 )
deplacer( 3 , 1 )
deplacer( 3 , 2 )
deplacer( 1 , 2 )
deplacer( 1 , 3 )
deplacer( 2 , 3 )
deplacer( 2 , 1 )
deplacer( 3 , 1 )
deplacer( 2 , 3 )
deplacer( 1 , 2 )
deplacer( 1 , 3 )
deplacer( 2 , 3 )
/////////////////
n=4
print ("tour Hanoi avec ", n ," plateaux")
def hanoi(n,a=1,b=2,c=3):
    if (n > 0):
        hanoi(n-1, a , c ,b)
        print ("deplacer( ", a ,",", c," )")
        hanoi(n-1, b , a , c)
hanoi(n,a=1,b=2,c=3)
/////////////////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      deplacer(1,2);
      deplacer(1,3);
      deplacer(2,3);
      
      deplacer(1,2);
      
      deplacer(3,1);
      deplacer(3,2);
      deplacer(1,2);
      
      
      deplacer(1,3);
      
      
      deplacer(2,3);
      deplacer(2,1);
      deplacer(3,1);
      
      deplacer(2,3);
      
      deplacer(1,2);
      deplacer(1,3);
      deplacer(2,3);
   }
}

//////////////
from robot import *
remplir(3)
transferer(3, 5)
remplir(3)
transferer(3, 5)
vider(5)
transferer(3, 5)
remplir(3)
transferer(3, 5)

/////////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      remplir(5);
      transferer(5, 3);
      vider(3);
      transferer(5, 3);
      remplir(5);
      transferer(5, 3);
   }
}
///////////////////////
for loop in range(135):
   print("Je dois respecter le Grand Sorcier.")

for loop in range(13):
   print("9 * 8 = 72")

/////////////////
class Main {
   public static void main(String[] args) {
      for (int loop = 1; loop <= 135; loop = loop + 1) {
         System.out.println("Je dois respecter le Grand Sorcier.");
      }
   }
}
///////////////////////
gauche()
droite()
ramasser()
deposer()


from robot import *
gauche()
gauche()
print("Bonjour, laissez-moi vous aider")
ramasser()
for loop in range(32):
   droite()
deposer()

///////////////////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      gauche();
      gauche();
      System.out.println("Bonjour, laissez-moi vous aider");
      ramasser();
      for (int loop = 1; loop <= 32; loop = loop + 1) {
         droite();
      }
      deposer();
   }
}

/////////////////////////////
from robot import *
droite()
ramasser()
droite()
ramasser()
gauche()
gauche()
deposer()


Aller à gauche
Aller à droite
Ramasser une bouse
Déposer les bouses



from robot import *
droite()
ramasser()
droite()
ramasser()
gauche()
gauche()
deposer()

from robot import *
for loop in range(15):
	droite()
	ramasser()
droite()
deposer()

///////////////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      for (int loop = 1; loop <= 15; loop = loop + 1) {
         droite();
         ramasser();
      }
      droite();
      deposer();
   }
}
//////////////////////

from robot import *
for loop in range(21):
	haut()
	droite()
for loop in range(21):
	gauche()
	bas()

////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      for (int loop = 1; loop <= 21; loop = loop + 1) {
         haut();
         droite();
      }
      for (int loop = 1; loop <= 21; loop = loop + 1) {
         gauche();
         bas();
      }
   }
}
//////////////
for loop in range(30):
   print("a_", end = "")
print("")
for loop in range(30):
   print("b_", end = "")
print("")
for loop in range(30):
   print("c_", end = "")
print("")
////////////////////////

for loop in range(20):
    for loop in range(20):
        print("O", end = "")
        print("X", end = "")
    print()
    for loop in range(20):
        print("X", end = "")
        print("O", end = "")
    print()
//////////////
for loop in range(20):
   for loop in range(20):
      print("OX", end = "")
   print()
   for loop in range(20):
      print("XO", end = "")
   print()	
/////////////////////
class Main {
   public static void main(String[] args) {
      for (int loop = 1; loop <= 20; loop = loop + 1) {
         for (int loop2 = 1; loop2 <= 20; loop2 = loop2 + 1) {
            System.out.print("OX");
         }
         System.out.println();
    
         for (int loop2 = 1; loop2 <= 20; loop2 = loop2 + 1) {
            System.out.print("XO");
         }
         System.out.println();
      }
   }
}	
///////////////

from robot import *

for loop in range(108):
	for loop in range(13):
		haut()
	for loop in range(13):
		droite()
	for loop in range(13):
		bas()
	for loop in range(13):
		gauche()
/////////////////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      for (int loop = 1; loop <= 108; loop = loop + 1) {
         for (int loop2 = 1; loop2 <= 13; loop2 = loop2 + 1) {
            haut();
         }
         for (int loop2 = 1; loop2 <= 13; loop2 = loop2 + 1) {
            droite();
         }
         for (int loop2 = 1; loop2 <= 13; loop2 = loop2 + 1) {
            bas();
         }
         for (int loop2 = 1; loop2 <= 13; loop2 = loop2 + 1) {
            gauche();
         }
      }
   }
}
///////////////////
Aller à gauche
Aller à droite
Ramasser les raisins
Déposer les raisins

gauche()
droite()
ramasser()
deposer()

from robot import *
for loop in range(20):
   ramasser()
   for loop in range(15):
      droite()
   deposer()
   for loop in range(15):
      gauche()
	
//////////////////
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      for (int loop = 1; loop <= 20; loop = loop + 1) {
         ramasser();
         for (int loop2 = 1; loop2 <= 15; loop2 = loop2 + 1) {
            droite();
         }
         deposer();
         for (int loop2 = 1; loop2 <= 15; loop2 = loop2 + 1) {
            gauche();
         }
      }
   }
}
/////////////////
from robot import *
haut()
haut()
droite()

from robot import *
#premiere montée de 9, tourner à droite, descendre de 8
for loop in range(9):
    print("haut")
print("droite")
for loop in range(8):
    print("bas")
print("droite")
#repete 3 fois monter de 8, tourner à droite descendre de 8, tourner à droite
for loop in range(3):
    for loop in range(8):
        print("haut")
    print("droite")
    for loop in range(8):
        print("bas")
    print("droite")
#  derniere monter de 8, tourner à droite, descendre de 9 sans tourner à droitee  
for loop in range(8):
    print("haut")
print("droite")
for loop in range(9):
    print("bas")
#retour au depart 
for loop in range(9):
    print("gauche")


from robot import *
#premiere montée de 9, tourner à droite, descendre de 8
for loop in range(9):
    haut()
droite()
for loop in range(8):
    bas()
droite()
#repete 3 fois monter de 8, tourner à droite descendre de 8, tourner à droite
for loop in range(3):
    for loop in range(8):
        haut()
    droite()
    for loop in range(8):
        bas()
    droite()
#  derniere monter de 8, tourner à droite, descendre de 9 sans tourner à droitee  
for loop in range(8):
    haut()
droite()
for loop in range(9):
    bas()
#retour au depart 
for loop in range(9):
    gauche()
	
	///////////////////
	from robot import *
haut()
# Allers-retours sur les 9 lignes du haut, pour les 8 premières colonnes
for loop in range(4):
   for loop in range(8):
      haut()
   droite()
   for loop in range(8):
      bas()
   droite()
# Deux dernières colonnes avec redescente jusqu'en bas
for loop in range(8):
   haut()
droite()
for loop in range(9):
   bas()
# Et on rentre à la position de départ
for loop in range(9):
   gauche()
   ///////////////////////
 
import static algorea.Robot.*;
class Main {
   public static void main(String[] args) {
      haut();
      // Allers-retours sur les 9 lignes du haut,
      // pour les 8 premières colonnes
      for (int loop = 1; loop <= 4; loop = loop + 1) {
         for (int loop2 = 1; loop2 <= 8; loop2 = loop2 + 1) {
            haut();
         }
         droite();
         for (int loop2 = 1; loop2 <= 8; loop2 = loop2 + 1) {
            bas();
         }
         droite();
      }
    
      // Deux dernières colonnes avec redescente jusqu'en bas
      for (int loop = 1; loop <= 8; loop = loop + 1) {
         haut();
      }
      droite();
      for (int loop = 1; loop <= 9; loop = loop + 1) {
         bas();
      }
    
      // Et on rentre à la position de départ
      for (int loop = 1; loop <= 9; loop = loop + 1) {
         gauche();
      }
   }
}
/////////////////////
print(12581 -11937)
///////////
#L'école est formée de 4 classes, constituées respectivement de 25, 30, 27 et 22 élèves. 
#Cependant, 8 élèves sont absents aujourd'hui. Sachant que chaque élève présent doit recevoir 3 bonbons,
#écrivez un programme qui calcule puis affiche le nombre total de bonbons nécessaires.
nombreEnfants=25+30+27+22-8
print(nombreEnfants*3)


/////////////////
# L'algoréathlon se constitue de trois étapes à effectuer chaque jour : 
# 2 km de natation, 34 km de cyclisme et 6 km de course à pied.
# Sachant qu'un sportif répète ces trois étapes pendant 3 jours de suite,
 # vous devez afficher la distance totale qu'il a parcourue à la fin du 1er jour, à la fin du 2e jour, puis à la fin de l'algoréathlon complet.
# Afin de rendre l'affichage convivial sur l'écran du robot, vous souhaitez mettre 
# les trois valeurs sur une même ligne, avec une espace entre chaque valeur et la suivante.
# Important : pour écrire ce programme, vous devez mémoriser la distance parcourue
 # en un jour en lui donnant un nom, puis utiliser ce nom pour calculer les trois réponses.
 # Appuyez-vous sur les explications ci-dessous.


distanceJournaliere=2+34+6
print("distance en  une journée: ",distanceJournaliere,end = " ")
print("distance en  2 journées: ",distanceJournaliere*2,end = " ")
print("distance en  3 journées: ",distanceJournaliere*3)

///////////////////
# # Ce que doit faire votre programme :
# # La cour carrée a été mesurée avec quatre bâtons de longueurs 
# respectives 17 m, 7 m, 5 m et 2 m. La longueur du côté de la cour est égale à 5 fois 
# le premier bâton plus 2 fois le second plus 1 fois le troisième plus 2 fois le quatrième.

# # Votre programme doit afficher deux lignes : la première doit contenir 
# la surface de la cour, et la seconde ligne doit contenir son périmètre. 
# Les résultats doivent être exprimés en mètres carrés et en mètres, respectivement, 
# mais vous ne devez pas afficher l'unité après la valeur numérique.

# # Important : dans votre programme, commencez par calculer la longueur du côté de la cour et l'enregistrer dans une variable.


longeurCoteCour=5*17+2*7+5+2*2
surfaceCour=longeurCoteCour*longeurCoteCour
print(surfaceCour)
perimetreCour=longeurCoteCour*4
print(perimetreCour)

///////////////////
# Le robot devra compter jusqu'à 100, c'est à dire afficher les entiers de 1 à 100,
 # un par ligne, et ensuite afficher
 # « J'arrive ! ». Ainsi, s'il ne devait compter que jusqu'à 3 au lieu de 100, 
 # votre robot devrait afficher :
n=1
for loop in range(100):
	print(n)
	n=n+1
print(	"J'arrive !")
/////////////
class Main {
   public static void main(String[] args) {
      int compte = 1;
      for (int loop = 1; loop <= 100; loop = loop + 1) {
         System.out.println(compte);
         compte = compte + 1;
      }
      System.out.println("J'arrive !");
   }
}
/////////////////////
# Ce que doit faire votre programme :
# Vous devez lire attentivement les programmes donnés ci-dessous 
# pour déterminer s'ils sont valides ou non, et ce sans essayer de les exécuter.
 # Pour chacun des 7 programmes, vous devez afficher sur une ligne 
 # soit la lettre « V » pour indiquer que le programme est valide, 
 # soit la lettre « I » pour indiquer qu'il est invalide. Par exemple,
 # si vous pensez que les 4 premiers programmes s'exécuteront
 # sans erreur et que les 3 suivants entraîneront des erreurs, faites afficher à votre programme :

print("V")
print("V")
print("I") 
print("I")
print("V")
print("I") 
print("I") 
////////////////////
# Votre programme devra lancer le décompte en partant de 100
 # puis annoncer le décollage, c'est-à-dire afficher une séquence d'annonces de la forme :
 
n=100
for loop in range(101):
	print(n)
	n=n-1
print("Décollage !")

////////////////
class Main {
   public static void main(String[] args) {
      int compte = 100;
      for (int loop = 1; loop <= 101; loop = loop + 1) {
         System.out.println(compte);
         compte = compte - 1;
      }
      System.out.println("Décollage !");
   }
}
/////////////
# Ce que doit faire votre programme :
# Sachant qu'il y a actuellement 1337 crapauds et que 
# leur nombre double chaque semaine, votre programme devra afficher
 # le nombre de crapauds qu'il y aura après la 12e semaine.
# Important : vous devez utiliser une boucle pour calculer le nombre de crapauds.

nbreCrapauds=1337
for loop in range(12):
	nbreCrapauds=nbreCrapauds*2
print(nbreCrapauds)


///////////////////
totalBonbons = 0
numTir = 1
for loop in range(50):
   totalBonbons = totalBonbons + numTir
   print(totalBonbons)
   numTir = numTir + 1
   /////////////////////
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
# dans l'ordre (de gauche à droite) et les ramener un par un à la case de départ.


from robot import *
anneau = 1
for loop in range(10):
   for loop in range(anneau):
      droite()
   ramasser()
   for loop in range(anneau):
      gauche()  
   deposer()
   anneau = anneau + 1
   /////////////////////////////
   Ce que doit faire votre programme :
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
   

nbreRang=17
somme=0
nbreCubesRdc=nbreRang*nbreRang*nbreRang
nbreEtages=nbreRang
for loop in range(9):
#	nbreRang=nbreRang-2
	nbreCubesRdc=nbreRang*nbreRang*nbreRang
	nbreRang=nbreRang-2
	somme=somme+nbreCubesRdc
#	print(nbreCubesRdc)
print(somme)
////////////////////////
nbCubes = 0
largeurArête = 1
for loop in range(9):
   nbCubes = nbCubes + largeurArête * largeurArête * largeurArête
   largeurArête = largeurArête + 2
print(nbCubes)

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

////////////////////
	
ligne = 1
for loop in range(20):
   colonne = 1
   for loop in range(20):
      print(colonne * ligne, end = " ")
      colonne = colonne + 1
   print()
   ligne = ligne + 1
//////////////////
class Main {
   public static void main(String[] args) {
      int ligne = 1;
      for (int loop1 = 1; loop1 <= 20; loop1 = loop1 + 1) {
         int colonne = 1;
         for (int loop2 = 1; loop2 <= 20; loop2 = loop2 + 1) {
            System.out.print((colonne * ligne) + " ");
            colonne = colonne + 1;
         }
         System.out.println();
         ligne = ligne + 1;
      }
   }
}
////////////////////////// 

largeur = int(input())
longeur = int(input())
print(largeur * longeur)  

/////////////////////////////
nbJours = int(input())
print(60 * 60 * 16 * nbJours


import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int nbJours = entrée.nextInt();
      System.out.println(nbJours * 16 * 60 * 60);
   }
}
	
/////////////////////////////////////
âgeCadet = int(input())
âgeAîné = int(input())
différence = âgeAîné - âgeCadet
print(différence)	
	
	
	import algorea.Scanner;
 
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int âgeCadet = entrée.nextInt();
      int âgeAîné = entrée.nextInt();
      int différence = âgeAîné - âgeCadet;
      System.out.println(différence);
   }
}

/////////////////////////////////////////
nbLignes = int(input())
for loop in range(nbLignes):
    print("Je dois suivre en cours")

import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int nbLignes = entrée.nextInt();
      for (int iLigne = 1; iLigne <= nbLignes; iLigne = iLigne + 1) {
         System.out.println("Je dois suivre en cours");
      }
   }
}

////////////////////////////
tempMin = int(input())
tempMax = int(input())
temperature = tempMin
for loop in range(tempMax - tempMin + 1):
   print(temperature)
   temperature = temperature + 1


	import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int tempMin = entrée.nextInt();
      int tempMax = entrée.nextInt();
      int température = tempMin;
      for (int loop = 1; loop <= tempMax - tempMin + 1; loop = loop + 1) {
         System.out.println(température);
         température = température + 1;
      }
   }
}
///////////////////////////////////
# Le nombre 1 × 2 × 3 × … × n s'appelle la factorielle de n (ou « factorielle n »)
 # et se note « n! ». La factorielle est très utilisée en combinatoire 
 # car elle correspond en particulier au nombre de manières d'ordonner n éléments.

nbNombres = int(input())
étape = 0
résultat = 66
for loop in range(nbNombres):
   étape = étape + 1
   résultat = résultat * étape
   print(résultat)


import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int nbNombres = entrée.nextInt();
      int résultat = 66;
      for (int facteur = 1; facteur <= nbNombres; facteur = facteur + 1) {
         résultat = résultat * facteur;
         System.out.println(résultat);
      }
   }
}
///////////////////////////
# validation
# Il y a trois entiers à lire : la position de départ positionDepart,
 # la largeur d'un emplacement largeurEmplacement et le nombre de vendeurs nbVendeurs.

# Vous devez afficher une suite de nombres, partant de positionDepart 
# et augmentant de largeurEmplacement à chaque fois. 
# Il y a au total nbVendeurs augmentations à faire. 
# Vous devez afficher la valeur de chacun des nombres de la suite.

positionDépart = int(input())
largeurEmplacement = int(input())
nbVendeurs = int(input())
position = positionDépart
for iVendeur in range(nbVendeurs + 1):
   print(position)
   position = position + largeurEmplacement
   
import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int positionDépart = entrée.nextInt();
      int largeurEmplacement = entrée.nextInt();
      int nbVendeurs = entrée.nextInt();
      int position = positionDépart;
      for (int iVendeur = 0; iVendeur <= nbVendeurs; iVendeur = iVendeur + 1) {
         System.out.println(position);
         position = position + largeurEmplacement;
      }
   }
}   
   
   
///////////////////////////
totalKarvas = 0
for loop in range(20):
   nbBêtes = int(input())
   totalKarvas = totalKarvas + nbBêtes
print(totalKarvas)

import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int totalKarvas = 0;
      for (int loop = 1; loop <= 20; loop = loop + 1) {
         int nbBêtes = entrée.nextInt();
         totalKarvas = totalKarvas + nbBêtes;
      }
      System.out.println(totalKarvas);
   }
}
/////////////////////////////
largeurBas = int(input())
largeurHaut = int(input())
 
volume = 0
largeur = largeurHaut
for loop in range(largeurBas - largeurHaut + 1):
   volume = volume + largeur * largeur
   largeur = largeur + 1
 
print(volume)

import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int largeurBas = entrée.nextInt();
      int largeurHaut = entrée.nextInt();
      int volume = 0;
      int largeur = largeurHaut;
      for (int loop = 1; loop <= largeurBas - largeurHaut + 1; loop = loop + 1) {
         volume = volume + largeur * largeur;
         largeur = largeur + 1;
      }
      System.out.println(volume);
   }
}

# ////////////////////////////
#poids, son âge, la longueur de ses cornes et la hauteur au garrot
#afficher sa note,sachant qu'elle s'obtient en multipliant la longueur des cornes
#par la hauteur au garrot, 
#valeur à laquelle on ajoute le poids.

# 2
# 100
# 5
# 25
# 90
# 300
# 10
# 15
# 120

nbKarvas = int(input())
for loop in range(nbKarvas):
   poids = int(input())
   âge = int(input())
   longueurCornes = int(input())
   hauteurAuGarrot = int(input())
   print(longueurCornes * hauteurAuGarrot + poids)
	
	
	
import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int nbKarvas = entrée.nextInt();
      for (int loop = 1; loop <= nbKarvas; loop = loop + 1) {
         int poids = entrée.nextInt();
         entrée.nextInt(); // âge
         int longueurCornes = entrée.nextInt();
         int hauteurAuGarrot = entrée.nextInt();
         System.out.println(longueurCornes * hauteurAuGarrot + poids);
      }
   }
}
# ////////////////////////////////////

nbPaquets = int(input())
poidsPaquet = int(input())
if nbPaquets * poidsPaquet > 105:
   print("Surcharge !")
   
   
 import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int nbPaquets = entrée.nextInt();
      int poidsPaquet = entrée.nextInt();
      if (nbPaquets * poidsPaquet > 105) {
         System.out.println("Surcharge !");
      }
   }
}  

/////////////////////////////
numéroMatin = int(input())
numéroSoir = int(input())
écart = numéroSoir - numéroMatin
if écart < 0:
   écart = -écart
print(écart)

import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int numéroMatin = entrée.nextInt();
      int numéroSoir = entrée.nextInt();
      int écart = numéroSoir - numéroMatin;
      if (écart < 0) {
         écart = -écart;
      }
      System.out.println(écart);
   }
}
/////////////////////////////
#Votre programme lira un entier, l'heure d'arrivée, qui sera compris entre 0 et 12 inclus.
##0 correspond à midi, 1 à 1h de l'après-midi, etc. et 12 à minuit.
#Le prix de la chambre est de 10 pièces à midi, et augmente de 5 pièces chaque heure après midi.
#Il est donc de 15 pièces à 13h, etc. Il ne peut cependant pas dépasser 53 pièces.
#Votre programme devra afficher le prix à payer correspondant à l'heure d'arrivée donnée.)
heure = int(input())
prix = 10 + 5 * heure
if prix > 53:
   prix = 53
print(prix)


import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int heure = entrée.nextInt();
      int prix = 10 + 5 * heure;
      if (prix > 53) {
         prix = 53;
      }
      System.out.println(prix);
   }
   
   
   }
  ////////////////////////////////////////
# Votre programme devra lire deux entiers, la superficie d'un champ des Arignon
 # et la superficie d'un champ des Evaran. Si l'un des champs est plus grand 
 # d'au moins 10 m² (strictement) que l'autre champ, alors il faudra afficher le texte 
 # « La famille X a un champ trop grand », « X » devant bien sûr être remplacé 
 # par « Arignon » ou « Evaran » selon le cas.  
 
 superficieArignon = int(input())
superficieEvaran = int(input())
if superficieArignon > superficieEvaran + 10:
   print("La famille Arignon a un champ trop grand")
if superficieEvaran > superficieArignon + 10:
   print("La famille Evaran a un champ trop grand")
 
 
 import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int aireArignon = entrée.nextInt();
      int aireEvaran = entrée.nextInt();
      if (aireArignon  - aireEvaran  > 10) {
         System.out.println("La famille Arignon a un champ trop grand");
      }
      if (aireEvaran  - aireArignon  > 10) {
         System.out.println("La famille Evaran a un champ trop grand");
      }
   }
}

////////////////////////////////////////////////

# Votre programme doit lire l'âge d'une personne et 
# afficher soit « Tarif réduit » si cette personne a strictement moins de 21 ans, 
# soit « Tarif plein » dans le cas contraire

âge = int(input())
if âge < 21:
   print("Tarif réduit")
else:
   print("Tarif plein")





import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int âge = entrée.nextInt();
      if (âge < 21) {
         System.out.println("Tarif réduit");
      } else {
         System.out.println("Tarif plein");
      }
   }
}


////////////////////////////////////////////
# Votre programme devra lire un premier entier : le nombre
 # de membres nbMembres qui constituent une équipe. Ensuite, 
 # il devra lire les poids (en kilogrammes), au total nbMembres × 2, sachant que le premier poids est celui d'un joueur de la 1re équipe, le deuxième poids celui d'un joueur de la 2e équipe, le troisième la 1re équipe, le quatrième la 2e équipe, etc.

# Après avoir calculé le poids total de chaque équipe, vous devrez afficher le texte 
# « L'équipe X a un avantage » (en remplaçant X par la valeur 1 ou 2), en
 # considérant qu'une équipe est avantagée si elle a un poids total supérieur à 
 # celui de l'autre.

# Vous afficherez ensuite le texte « Poids total pour l'équipe 1 : 
# » suivi du poids de l'équipe 1, puis « Poids total pour l'équipe 2 :
 # » suivi du poids de l'équipe 2 (voir l'exemple ci-dessous).


nbMembres=int(input())
total=0
numeroEquipe=0
poidsEquipe1=0
poidsEquipe2=0

for loop in range(nbMembres):
    poidsJoeurEquipe1=int(input())
    poidsJoeurEquipe2=int(input())
    poidsEquipe1=poidsEquipe1+poidsJoeurEquipe1
    poidsEquipe2=poidsEquipe2+poidsJoeurEquipe2
    
if poidsEquipe1>poidsEquipe2:
    numeroEquipe=1
else:
    numeroEquipe=2   
print("L'équipe " ,numeroEquipe, " a un avantage")
print("Poids total pour l'équipe 1 : " ,poidsEquipe1)
print("Poids total pour l'équipe 2 : " ,poidsEquipe2)


nbPersonnes = int(input())
totalÉquipe1 = 0
totalÉquipe2 = 0
for loop in range(nbPersonnes):
   poids1 = int(input())
   poids2 = int(input())
   totalÉquipe1 = totalÉquipe1 + poids1
   totalÉquipe2 = totalÉquipe2 + poids2
if totalÉquipe1 > totalÉquipe2:
   print("L'équipe 1 a un avantage")
else:
   print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 :", totalÉquipe1)
print("Poids total pour l'équipe 2 :", totalÉquipe2)


import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int nbPersonnes = entrée.nextInt();
      int totalÉquipe1 = 0, totalÉquipe2 = 0;
      for (int loop = 1; loop <= nbPersonnes; loop = loop + 1) {
         int poids1 = entrée.nextInt();
         int poids2 = entrée.nextInt();
         totalÉquipe1 = totalÉquipe1 + poids1;
         totalÉquipe2 = totalÉquipe2 + poids2;
      }
      if (totalÉquipe1 > totalÉquipe2) {
         System.out.println("L'équipe 1 a un avantage");
      }
      else {
         System.out.println("L'équipe 2 a un avantage");
      }
      System.out.println("Poids total pour l'équipe 1 : " + totalÉquipe1);
      System.out.println("Poids total pour l'équipe 2 : " + totalÉquipe2);
   }
}
////////////////////////////////////////////////////////////////////////////
# Votre programme doit lire un entier : le code fourni par
# l'utilisateur. Si ce code correspond au code secret, qui est 64 741,
 # alors le programme devra afficher le texte « Bon festin ! ».
 # Sinon, il devra afficher « Allez-vous en ! ».


codeUtilisateur=int(input())


if codeUtilisateur!=64741:
    print("Allez-vous en !")
else:
    print("Bon festin !")
	
	
import algorea.Scanner;
class Main {
   static Scanner entrée = new Scanner(System.in);
   public static void main(String[] args) {
      int tentative = entrée.nextInt();
      if (tentative == 64741) {
         System.out.println("Bon festin !");
      } else {
         System.out.println("Allez-vous-en !");
      }
   }
}	









///////////////////////////////////////////























	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


   
   
   
   
   
	
