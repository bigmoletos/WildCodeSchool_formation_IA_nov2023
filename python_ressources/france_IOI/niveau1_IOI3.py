import pylab  as plt
import random
from fonctionGraphe import *

# import matplotlib.pylot as plt
# import matplotlib.pylot as plt

# ****************************************
# ****************************************
# tracé de graphiques avec pylab integrant numpy ou matplotlib
# ****************************************
# ****************************************
# dessine un carre à l'aide de 2 tableaux sur x et y
# x = [x1, X2, X2, x1, x1]
# y = [y1, y1, y2, y2, y1]
# ***************************************
# size = [1, 1, 1, 1, 1, ]

# x = plt.array( [1, 6, 6, 1, 1] )
# y = plt.array( [1, 1, 5, 5, 1] )
# plt.scatter( x, y, s=size, c="coral", label="zone_A" )
# plt.plot( x, y )
#
# x = plt.array( [4, 9, 9, 4, 4] )
# y = plt.array( [3, 3, 8, 8, 3] )
# plt.scatter( x, y, s=size, c="coral", label="zone_A" )
# plt.plot( x, y )
#
# x = plt.array( [0, 21, 21, 0, 0] )
# y = plt.array( [0, 0, 16, 16, 0] )
# plt.scatter( x, y, s=size, c="blue", label="zone_B" )
# plt.plot( x, y )
#
# x = plt.array( [0, 30, 30, 0, 0] )
# y = plt.array( [0, 0, 6, 6, 0] )
# plt.scatter( x, y, s=size, c="red", label="zone_C" )
# plt.plot( x, y )
#
# x = plt.array( [0, 5, 5, 0, 0] )
# y = plt.array( [0, 0, 20, 20, 0] )
# plt.scatter( x, y, s=size, c="yellow", label="zone_D" )
# plt.plot( x, y )
#
# x = plt.array( [10, 25, 25, 10, 10] )
# y = plt.array( [10, 10, 18, 18, 10] )
# plt.scatter( x, y, s=size, c="green", label="zone_E" )
# plt.plot( x, y )
# [1, 12, 25, -7, 13, -15, 21, 4, 11]
# x = plt.array( [5, 10, 10, 5] )
# y = plt.array( [5, 5, 10, 10] )
# plt.scatter( x, y, s=size, c="blue", label="zone_F" )
# plt.plot( x, y )
# # **************
# plt.legend()
# plt.title( "zone de recouvrement" )
# plt.xlabel( "x" )
# plt.ylabel( "y" )
# plt.axis( "equal" )

# ********************************************
# creation auto des graphes avec creation auto des tableaux
# ********************************************
# list = [1, 1, 6, 1, 5, 4, 9, 3, 8]
# list[0] = random.randint( 1, 10 )
# nombrePairesZones = 1
# for loop in range( nombrePairesZones ):
#     # ********************************************
#     # liste aléatoire à chaque boucle
#     # ********************************************
#     list = [random.randint( -20, -1 ) for index in range( 9 )]
#     list[0] = nombrePairesZones
#     print( list )
#     # *******************************************
#     # Coordonnées zone A
#     # zone A axe x premier point
#     axeXminA = list[1]
#     # zone B axe x deuxieme point
#     axeXmaxA = list[2]
#     # zone A zone axe y premier point
#     axeYminA = list[3]
#     # zone A axe y deuxieme point
#     axeYmaxA = list[4]
#     # ***********************************************
#     # Coordonnées zone B
#     # ***********************************************
#     # zone B axe x premier point
#     axeXminB = list[5]
#     # zone B axe x deuxieme point
#     axeXmaxB = list[6]
#     # zone B zone axe y premier point
#     axeYminB = list[7]
#     # zone B axe y deuxieme point
#     axeYmaxB = list[8]
#     # ****************************************
#     # dessine un carre à l'aide de 2 tableaux sur x et y
#     # x = [x1, X2, X2, x1, x1]
#     # y = [y1, y1, y2, y2, y1]
#     # ***************************************
#     size = [1, 1, 1, 1, 1]
#     x = plt.array( [axeXminA, axeXmaxA, axeXmaxA, axeXminA, axeXminA] )
#     y = plt.array( [axeYminA, axeYminA, axeYmaxA, axeYmaxA, axeYminA] )
#     plt.scatter( x, y, s=size, c="blue", label="rectangle_A" )
#     plt.plot( x, y )
#
#     x = plt.array( [axeXminB, axeXmaxB, axeXmaxB, axeXminB, axeXminB] )
#     y = plt.array( [axeYminB, axeYminB, axeYmaxB, axeYmaxB, axeYminB] )
#     plt.scatter( x, y, s=size, c="blue", label="rectangle_B" )
#     plt.plot( x, y )
#     # **************
#     plt.grid( True )
#     plt.legend()
#     plt.title( "zone de recouvrement" )
#     plt.xlabel( "x" )
#     plt.ylabel( "y" )
#     plt.axis( "equal" )
#     plt.show()
#     plt.close()
# **********************
# graphe  de test
# def testGraphe():
#     nombrePairesZones = 1
#     for loop in range( nombrePairesZones ):
#         # ********************************************
#         # remplacer les valeurs de list par celles a tester
#         # ********************************************
#         # list = [1, 12, 25, -7, 13, -15, 21, 4, 11]
#         # list = [1, 5, 23, 16, 11, 10, 19, 5, 16]
#
#         global list
#         global title
#         global nomLabel1
#         # list = [1, -1, -19, -3, -13, -10, -8, -7, -6]
#         list[0] = nombrePairesZones
#         # *******************************************
#         # Coordonnées zone A
#         # zone A axe x premier point
#         axeXminA = list[1]
#         # zone B axe x deuxieme point
#         axeXmaxA = list[2]
#         # zone A zone axe y premier point
#         axeYminA = list[3]
#         # zone A axe y deuxieme point
#         axeYmaxA = list[4]
#         # ***********************************************
#         # Coordonnées zone B
#         # ***********************************************
#         # zone B axe x premier point
#         axeXminB = list[5]
#         # zone B axe x deuxieme point
#         axeXmaxB = list[6]
#         # zone B zone axe y premier point
#         axeYminB = list[7]
#         # zone B axe y deuxieme point
#         axeYmaxB = list[8]
#         # ****************************************
#         # dessine un carre à l'aide de 2 tableaux sur x et y
#         # x = [x1, X2, X2, x1, x1]
#         # y = [y1, y1, y2, y2, y1]
#         # ***************************************
#         size = [1, 1, 1, 1, 1]
#         x = plt.array( [axeXminA, axeXmaxA, axeXmaxA, axeXminA, axeXminA] )
#         y = plt.array( [axeYminA, axeYminA, axeYmaxA, axeYmaxA, axeYminA] )
#         plt.scatter( x, y, s=size, c="blue", label=nomLabel1)
#         plt.plot( x, y )
#
#         x = plt.array( [axeXminB, axeXmaxB, axeXmaxB, axeXminB, axeXminB] )
#         y = plt.array( [axeYminB, axeYminB, axeYmaxB, axeYmaxB, axeYminB] )
#         plt.scatter( x, y, s=size, c="blue", marker="o",label="rectangle_B_Test" ,alpha=0.3, edgecolors='none')
#         plt.plot( x, y ,marker="v")
#         # **************
#         plt.grid(True)
#         plt.legend()
#         plt.title( title)
#         plt.xlabel( "x" )
#         plt.ylabel( "y" )
#         plt.axis( "equal" )
#         plt.show()
#         # plt.close()
# **********************************
# tableaux Non
tabNon = [[1, 14, 20, 1, 6, 0, 2, 8, 11],
          [1, 22, 1, 4, 13, 8, 12, 0, 2],
          [1, 9, 11, 14, 4, 15, 12, 21, 23],
          [1, 1, 4, 5, 17, 7, 12, 24, 22],
          [1, 22, 16, 14, 13, 21, 1, 8, 4],
          [1, -16, -6, -3, -13, 6, 21, -1, 11],
          [1, 3, 0, 8, 15, 11, -8, 6, 3],
          [1, 2, -10, -20, -16, 11, 10, -11, 19],
          [1, -12, -2, -9, -9, -12, -2, 16, 16],
          [1, 20, 22, 20, -11, 20, -16, 22, -1],
          [1, -17, 8, 22, 3, 4, 19, -2, 3],
          [1, 10, 20, -4, -4, 0, -2, 7, -5],
          [1, -18, -9, -18, -20, -15, -10, -9, -2],
          [1, -7, -4, -3, -4, -13, -3, -18, -5],
          [1, -13, -18, -20, -15, -12, -3, -5, -19],
          [1, -15, -11, -5, -5, -3, -20, -9, -17],
          [1, -17, -7, -3, -9, -6, -8, -10, -17]]
# ************************
# for index in range( len( tabNon ) ):
#     print( index )
#     print( tabNon[index] )
# ***************************************
# tableaux oui
tabOui = [[1, 5, 23, 16, 11, 10, 19, 5, 16],
          [1, 10, 5, 14, 1, 8, 6, 7, 19],
          [1, 15, 4, 25, 13, 8, 18, 23, 1],
          [1, 10, 17, 0, 25, 15, 3, 20, 18],
          [1, 6, 2, 17, 20, 15, 5, 17, 20],
          [1, 13, -3, 20, -16, 4, 21, 18, -7],
          [1, -9, -4, -2, -13, -12, -7, -12, -17],
          [1, -20, -6, -8, -2, -13, -15, -11, -7],
          [1, -1, -19, -3, -13, -10, -8, -7, -6],
          [1, -9, -12, -1, -19, -4, -18, -19, -13],
          [1, -14, -4, -1, -15, -10, -2, -3, -7],
          [1, -12, -19, -13, -19, -7, -13, -16, -1],
          [1, -15, -16, -13, -8, -1, -16, -16, -8],
          [1, -13, -7, -19, -16, -12, -3, -8, -18],
          [1, -17, -1, -12, -7, -6, -15, -11, -17]]
# ***********************
# for index in range( len( tabOui ) ):
#     print( index )
#     print( tabOui[index] )

# ***************************************
# *******************************************

# pour qu'il y ait intersection il faut determiner les longeurs des cotés, savoir quelle est la zone la plus grande et determiner si
# projetée sur les axes x et y  on a  x1min <x2<x1max  ET  y1min<y2<y1max .
# les 2 zones etant de taille variable il faut que:
# maxgauche=max(x1,X2)
# mindroit=min(x1+largeur1, x2+largeur2)
# maxbas=max(y1, y2)
# minhaut=min(y1+hauteur1,y2+hauteur2)
# maxgauche<mindroit  ET maxbas<minhaut
# ************************************************
# import pylab  as plt
# import random
for index in range( len( tabOui ) ):
    list = tabOui[index]
    print( "tableauOui 1", list )
    # **************************
    # attributs pour la fonction graphique testGraphe()
    # **************************
    nombrePairesZones = 1
    title = "tableauOui1"
    nomLabel1 = "zoneA_Test"
    # concatenation string plus une variable nomLabel1+str(index)
    nomLabel1 = nomLabel1 + str( index )
    nomLabel2 = "zoneB_Test"
    nomLabel2 = nomLabel2 + str( index )
    # nombrePairesZones=1
    # testGraphe()
    # ************************
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
    # ***************************************
    largeurA = axeXmaxA - axeXminA
    largeurB = axeXmaxB - axeXminB
    hauteurA = axeYmaxA - axeYminA
    hauteurB = axeYmaxB - axeYminB

    maxgauche = max( axeXminA, axeXminB )
    mindroit = min( axeXminA + largeurA, axeXminB + largeurB )
    maxbas = max( axeYminA, axeYminB )
    minhaut = min( axeYminA + hauteurA, axeYminB + hauteurB )

    if (maxgauche <= mindroit and maxbas <= minhaut):
        # testGraphe()
        print( " tableauOui OUI 1" )
    else:
        # testGraphe()
        print( "tableauOui NON 1" )

for index in range( len( tabNon ) ):
    list = tabNon[index]
    print( "tableauNon 2", list )
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
    # ***************************************
    axeX1 = 0
    axeX2 = 0
    axeY1 = 0
    axeY2 = 0
    # ***************************************
    largeurA = axeXmaxA - axeXminA
    largeurB = axeXmaxB - axeXminB
    hauteurA = axeYmaxA - axeYminA
    hauteurB = axeYmaxB - axeYminB

    maxgauche = max( axeXminA, axeXminB )
    mindroit = min( axeXminA + largeurA, axeXminB + largeurB )
    maxbas = max( axeYminA, axeYminB )
    minhaut = min( axeYminA + hauteurA, axeYminB + hauteurB )

    if (maxgauche <= mindroit and maxbas <= minhaut):
        print( "tableauNon OUI 2" )
    else:
        print( "tableauNon NON 2" )
# ******************************************

for index in range( len( tabOui ) ):
    list = tabOui[index]
    print( "tableauOui bis", list )
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
    # ***************************************
    axeX1 = 0
    axeX2 = 0
    axeY1 = 0
    axeY2 = 0
    axeX3 = 0
    axeX4 = 0
    axeY3 = 0
    axeY4 = 0
    # ***************************************
    if (axeXminA == axeXminB and axeXmaxA == axeXmaxB and axeYminA == axeYminB and axeYmaxA == axeYmaxB):
        print( OUI )
    if ((axeXminA <= axeXminB <= axeXmaxA) and (axeYminA <= axeYminB <= axeYmaxA)):
        axeX1 = 1
    if ((axeXminA <= axeXmaxB <= axeXmaxA) and (axeYminA <= axeYminB <= axeYmaxA)):
        axeX2 = 1
    if ((axeXminA <= axeXminB <= axeXmaxA) and (axeYminA <= axeYmaxB <= axeYmaxA)):
        axeY1 = 1
    if ((axeXminA <= axeXmaxB <= axeXmaxA) and (axeYminA <= axeYmaxB <= axeYmaxA)):
        axeY2 = 1
    if ((axeXminA <= axeXminB <= axeXmaxA) and (axeYminB <= axeYminA <= axeYmaxB)):
        axeX3 = 1
    if ((axeXminA <= axeXmaxB <= axeXmaxA) and (axeYminB <= axeYminA <= axeYmaxB)):
        axeX4 = 1
    if ((axeXminA <= axeXminB <= axeXmaxA) and (axeYminB <= axeYmaxA <= axeYmaxB)):
        axeY3 = 1
    if ((axeXminA <= axeXmaxB <= axeXmaxA) and (axeYminB <= axeYmaxA <= axeYmaxB)):
        axeY4 = 1
    if (axeX1 == 1 or axeY1 == 1 or axeX2 == 1 or axeY2 == 1 or axeX3 == 1 or axeY3 == 1 or axeX2 == 4 or axeY4 == 1):
        print( "tableauOui OUI bis" )
    else:
        print( "tableauOui NON bis" )

# ***************************
# 4eme essai

for index in range( len( tabOui ) ):
    list = tabOui[index]
    print( "tableauOui bis", list )
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
    if (dX >= 0 and dY >= 0):
        print( "OUI 4" )
    else:
        print( "NON 4" )

for index in range( len( tabNon ) ):
    list = tabNon[index]
    print( "tableauNon 5", list )
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
    # *******************
    if (axeXmaxA == axeXmaxB):
        minDeXmax = axeXmaxB
    else:
        minDeXmax = min( axeXmaxA, axeXmaxB )
    if (axeXminA == axeXminB):
        maxDeXmin = axeXminB
    else:
        maxDeXmin = max( axeXminA, axeXminB )
    if (axeYmaxA == axeYmaxB):
        minDeYmax = axeYmaxB
    else:
        minDeYmax = min( axeYmaxA, axeYmaxB )
    if (axeYminA == axeYminB):
        maxDeYmin = axeYminB
    else:
        maxDeYmin = max( axeYminA, axeYminB )
     # ***********************************
    # dX = min(  axeXmaxA ,  axeXmaxB )  - max(  axeXminA ,  axeXminB )
    # dY = min(  axeYmaxA ,  axeYmaxB )  - max(  axeYminA ,  axeYminB )
    dX = minDeXmax - maxDeXmin
    dY = minDeYmax - maxDeYmin

    if (axeXminA == axeXminB and axeXmaxA == axeXmaxB and axeYminA == axeYminB and axeYmaxA == axeYmaxB):
        print( "OUI 5" )
    if (dX > 0 and dY >0):
        print( "OUI 5" )
    else:
        print( "NON 5" )
