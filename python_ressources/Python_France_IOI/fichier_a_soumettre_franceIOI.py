nombrePairesZones = int( input() )

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
    # ***************************************
    dX = min( axeXmaxA, axeXmaxB ) - max( axeXminA, axeXminB )
    dY = min( axeYmaxA, axeYmaxB ) - max( axeYminA, axeYminB )
    if (axeXminA == axeXminB and axeXmaxA == axeXmaxB and axeYminA == axeYminB and axeYmaxA == axeYmaxB):
        print( "OUI" )
    if (dX > 0 and dY > 0):
        print( "OUI" )
    else:
        print( "NON" )
