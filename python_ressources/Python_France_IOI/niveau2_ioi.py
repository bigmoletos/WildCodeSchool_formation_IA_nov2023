# niveau algo du site france IOI
# Augmentation des taxes
# Pour faire face à des difficultés financières du gouvernement,
# la taxe sur les fruits et légumes a été augmentée.
# Il faut donc recalculer tous les prix afin de prendre en compte cette nouvelle taxe,
# que les commerçants vont bien entendu répercuter sur les clients.
# Ce que doit faire votre programme :
# Votre programme doit lire trois nombres décimaux :
# la valeur actuelle de la taxe sur les fruits et légumes (en pourcentage),
# la nouvelle valeur de la taxe (en pourcentage),
# puis le prix actuel d'un légume, taxes comprises, en euros.
# Il devra calculer et afficher le prix du légume avec la nouvelle valeur de la taxe, arrondi au centime près.
import math

tvaActuelle = float( input() )
tvaNew = float( input() )
oldPrixTTC = float( input() )
prixHT = True
# oldPrixTTC=PrixHT*(1+tvaActuelle/100)
prixHT = oldPrixTTC / (1 + tvaActuelle / 100)
newPrixTTC = round( prixHT * (1 + tvaNew / 100), 2 )
print( newPrixTTC )

# correction
from math import *

taxeActuelle = float( input() )
taxeFuture = float( input() )
prixLegume = float( input() )
nouveauPrix = prixLegume / (1 + taxeActuelle / 100) * (1 + taxeFuture / 100)
nouveauPrix = round( nouveauPrix * 100 ) / 100
print( nouveauPrix )

# en java

import algorea.Scanner;
import static

java.lang.Math. *;


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
    double
    taxeActuelle = entrée.nextDouble();
    double
    taxeFuture = entrée.nextDouble();
    double
    prixLégume = entrée.nextDouble();

    double
    nouveauPrix = \
        prixLégume / (1 + taxeActuelle / 100) * (1 + taxeFuture / 100);
    nouveauPrix = (double)
    round( nouveauPrix * 100 ) / 100;
    System.out.println( nouveauPrix );
    }
    }

    # ************************************************
    # Achat  de livres
    # Vous commencez à apprendre une nouvelle langue et décidez d'acheter quelques
    # livres pour vous entraîner. Vous trouvez un vendeur qui propose de nombreux livres à des prix avantageux.
    # Vous disposez d'une certaine somme d'argent et vous vous demandez combien de livres vous pouvez acheter,
    # sachant qu'ils sont tous au même prix.

    # Ce que doit faire votre programme :

    # Votre programme doit commencer par lire la somme d'argent dont vous disposez
    # et lira ensuite le prix d'un livre. Il devra ensuite afficher un entier, le plus grand nombre de livres
    # qu'il vous est possible d'acheter avec cette somme d'argent.
    # monPognon=float(input())
    # prixLivre=float(input())
    monPognon = 27
    prixLivre = 5
    quotient = monPognon // prixLivre
    modulo = monPognon % prixLivre
    # if(modulo==0):
    #     nbreLivres = quotient-1
    # else:
    #     nbreLivres = quotient
    nbreLivres = int( quotient )
    print( "quotient ", quotient )
    print( "modulo ", modulo )

    print( " nb livres ", nbreLivres )
    print( "verif:", nbreLivres * prixLivre, " inferieur a :", monPognon )

    # correction
    sommeArgent = int( input() )
    prixLivre = int( input() )
    print( sommeArgent // prixLivre )
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
        sommeArgent = entrée.nextInt();
        int
        prixLivre = entrée.nextInt();
        System.out.println( sommeArgent / prixLivre );
        }
        }

        # ***************************************
        #   Une belle récolte
        #    Ce que doit faire votre programme :
        #
        # Votre programme doit commencer par lire un entier nbPersonnes puis un entier nbFruits.
        # Il doit ensuite afficher "oui" si nbFruits est un multiple de nbPersonnes, et "non" dans le cas contraire.

    nbPersonnes = int( input() )
    nbFruits = int( input() )
    # nbPersonnes = 12
    # nbFruits = 156
    modulo = nbFruits % nbPersonnes
    if (modulo == 0):
        print( "oui" )
    else:
        print( "non" )

        # correction
        nbPersonnes = int( input() )
        nbFruits = int( input() )
        if (nbFruits % nbPersonnes) == 0:
            print( "oui" )
        else:
            print( "non" )

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
    nbPersonnes = entrée.nextInt();
    int
    nbFruits = entrée.nextInt();
    if ((nbFruits % nbPersonnes) == 0)
    {
    System.out.println("oui");
    }
    else
    {
    System.out.println("non");
    }
    }
    }

    # ***************************
    #           La roue de la fortune
    #           Lors de l'examen final à la fin de leurs études, la tradition veut que les élèves tirent
    #           un sujet au hasard. Tirer un numéro dans un chapeau n'étant pas très amusant,
    #           ils utilisent une roue comme celle-ci, qu'ils peuvent faire tourner dans un sens ou dans l'autre.
    #            Les enseignants, par expérience, arrivent toujours à estimer de combien de "zones" la roue va tourner
    #            et peuvent aller chercher le sujet et revenir, pendant que la roue tourne encore. Il faut,
    #            pour cela, calculer rapidement sur quelle zone le curseur va s'arrêter, en fonction du nombre
    #            de zones dont la roue va tourner. A vous de jouer !
    # Ce que doit faire votre programme :
    #
    # Votre programme doit commencer par lire un entier nbZones. Sachant que la roue va tourner de nbZones zones,
    # vous devez calculer (puis afficher) sur quelle zone le curseur va arriver.
    #
    # Ainsi, si la route tourne de +2 zones alors le curseur arrive sur la zone 2,
    # et si la roue tourne de -2 zones, alors le curseur arrive sur la zone 22.

    # nbZones=int(input())

    # nbZones=int(input(
    nbZones = 25
    modulo = nbZones % 24
    # il y a 24 zones
    print( modulo )
    # if(nbZones<0):
    #     zones = nbZones // 24 - 24
    # else:
    #     zones = nbZones // 24 + 24
    # print( zones )

    # correction java
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
        nbZones = entrée.nextInt();
        System.out.println( ((nbZones % 24) + 24) % 24 );
        }
        }

        # *******************************
        #     Visite de la mine
        #     Ce que doit faire votre programme :

        # Il existe 5 types de déplacements, représentés par 5 entiers différents : aller à gauche (1), aller à droite (2),
        # aller tout droit (3), monter (4) et descendre (5).
        #
        # Le premier entier à lire est le nombre total de déplacements (1000 au maximum). Ensuite, chaque déplacement
        # (représenté par un entier) est indiqué sur sa propre ligne.
        #
        # Vous devez afficher la suite des déplacements à faire pour aller de votre position actuelle à la sortie.

        # nbDeplacements = int( input() )
        nbDeplacements = 5
        parcours = []
        # tableauRef = [[1, 2], [3, 3], [4, 5]]
        for index in range( nbDeplacements ):
            deplacement = int( input() )
            if (deplacement == 2):
                deplacement = 1
            elif (deplacement == 1):
                deplacement = 2
            if (deplacement == 4):
                deplacement = 5
            elif (deplacement == 5):
                deplacement = 4
            parcours.append( deplacement )
        # print( parcours )
        # inversion valeur liste
        # parcours.reverse()
        parcours = [2, 1, 3, 5, 4]
        print( parcours )
        # parcours liste en sens inverse
        # for index in range(-1,-len(parcours),-1):
        # for index in reversed(parcours):
        for index in parcours[::-1]:
            # print(parcours[index])
            # print(parcours)
            print( index )

        # *correction
        deplacementInverse = [0, 2, 1, 3, 5, 4]
        nbDeplacements = int( input() )
        # on remplit le tableau avec des 0
        chemin = [0] * nbDeplacements
        # print(chemin)
        for numero in range( nbDeplacements ):
            chemin[numero] = int( input() )
        # print(chemin)
        # lecture inverse du tableau en utilisant comme index le tableau initial pour trouver valeur dans le tableau inverse
        # nbDeplacements-1 permet la lecture de la derniere entrée et non de la premiere, puis on prend un pas de -1, decomptant donc encore -1
        # on utilise l'indice "numero' pour trouver la bonne valeur dans le tableau inverse
        for numero in range( nbDeplacements - 1, -1, -1 ):
            deplacement = chemin[numero]
            print( "deplacement", deplacement )
            print( deplacementInverse[deplacement] )

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
            int[]
            deplacementInverse = {0, 2, 1, 3, 5, 4};

            int
            nbDeplacements = entrée.nextInt();
            int[]
            chemin = new
            int[nbDeplacements];

            for (int numero = 0; numero < nbDeplacements; numero = numero + 1)
            {
                chemin[numero] = entrée.nextInt();
            }

            for (int numero = nbDeplacements-1; numero >= 0; numero = numero - 1)
            {
            int deplacement = chemin[numero];
            System.out.println(deplacementInverse[deplacement]);
            }
            }
            }
        # ***************************************

        # Banquet municipal
        # Ce que doit faire votre programme :
        #
        # Votre programme devra lire deux entiers : le nombre total de positions sur la table (au maximum 1000)
        # et le nombre de changements de positions. Il devra ensuite lire, pour chaque position, un entier :
        # le numéro de la personne qui doit, actuellement, s'installer à cette position.
        #
        # Il faut lire ensuite les changements exprimés sous la forme de deux entiers chacun : position1 et position2.
        # Un changement (position1, position2) signifie que les deux personnes qui étaient à ses positions
        # doivent échanger leurs places (les positions sont indexées à partir de 0).
        #
        # Vous devrez afficher, pour chaque position, le numéro de la personne qui s'y trouve une fois tous les changements faits.
        #

# nombreTotalPositions=int(input())
# nombreChangementPositions=int(input())
nombreTotalPositions = 5
nombreChangementPositions = 3
tableauNumero = [0] * nombreTotalPositions
# creation tableau des personnes
for index in range( nombreTotalPositions ):
    # if not (numeroPersonne in tableauNumero):
    #     verif=True
    # else:
    #     verif=False
    while  (verif):
        numeroPersonne = int( input() )
        tableauNumero[index] = numeroPersonne
        print( tableauNumero )
print( tableauNumero )
# permutation de position
# tableauNumero = [1, 2, 3, 4, 5]
# changement=[0]*2*nombreChangementPositions
changement = []
# print( tableauNumero )
var = True
#    creation tableau des changements
for index in range( nombreChangementPositions ):
    position1 = int( input() )
    position2 = int( input() )
    # changement.append( position1 )
    # changement.append( position2 )
    var = tableauNumero[position2]
    tableauNumero[position2] = tableauNumero[position1]
    tableauNumero[position1] = var
    # print( tableauNumero )

print( tableauNumero )
