import pylab  as plt
import random
# graphe  de test
def testGraphe():
    global nombrePairesZones
    nombrePairesZones = 1
    for loop in range( nombrePairesZones ):
        # ********************************************
        # remplacer les valeurs de list par celles a tester
        # ********************************************
        # list = [1, 12, 25, -7, 13, -15, 21, 4, 11]
        # list = [1, 5, 23, 16, 11, 10, 19, 5, 16]
        global list
        global title
        global nomLabel1
        global nomLabel2
        # title="test"
        # nomLabel1="A"
        # nomLabel2="B"
        # print(list)
        # list = [1, -1, -19, -3, -13, -10, -8, -7, -6]
        # list = [1, -1, -19, -3, -13, -10, -8, -7, -6]
        list[0] = nombrePairesZones
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
        # ****************************************
        # dessine un carre à l'aide de 2 tableaux sur x et y
        # x = [x1, X2, X2, x1, x1]
        # y = [y1, y1, y2, y2, y1]
        # ***************************************
        size = [1, 1, 1, 1, 1]
        x = plt.array( [axeXminA, axeXmaxA, axeXmaxA, axeXminA, axeXminA] )
        y = plt.array( [axeYminA, axeYminA, axeYmaxA, axeYmaxA, axeYminA] )
        plt.scatter( x, y, s=size, c="blue", label=nomLabel1)
        plt.plot( x, y )

        x = plt.array( [axeXminB, axeXmaxB, axeXmaxB, axeXminB, axeXminB] )
        y = plt.array( [axeYminB, axeYminB, axeYmaxB, axeYmaxB, axeYminB] )
        plt.scatter( x, y, s=size, c="blue", marker="o",label=nomLabel2 ,alpha=0.3, edgecolors='none')
        plt.plot( x, y ,marker="v")
        # **************
        plt.grid(True)
        plt.legend()
        plt.title( title)
        plt.xlabel( "x" )
        plt.ylabel( "y" )
        plt.axis( "equal" )
        plt.show()
        # plt.close()
# testGraphe()
