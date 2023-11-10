# Vous commencez à être connu pour vos talents de programmeur, aussi lors de votre passage 
# dans la ville d'Incerto, le maire décide de vous inviter au grand banquet qu'il organise.
#  Le maire se charge lui-même de faire le plan de table mais il change toujours d'avis
#   et les serveurs doivent constamment changer de place les petites affiches sur 
#   lesquelles sont indiqués les noms des personnes.
# 
# Afin de l'aider, vous lui proposez d'utiliser votre robot pour déterminer la position
#  de chaque personne après tous les changements décidés par le maire.
# 
# Afin de simplifier le problème, on suppose que chaque personne est identifiée par un 
# numéro et qu'il n'y a qu'une seule très grande table.
# 
# Ce que doit faire votre programme :
# Votre programme devra lire deux entiers : le nombre total de positions sur la table
#  (au maximum 1000) et le nombre de changements de positions. Il devra ensuite lire,
#   pour chaque position, un entier : le numéro de la personne qui doit, actuellement,
#    s'installer à cette position.
# 
# Il faut lire ensuite les changements exprimés sous la forme de deux entiers chacun :
#  position1 et position2. Un changement (position1, position2) signifie que les deux
#   personnes qui étaient à ses positions doivent échanger leurs places (les positions 
# sont indexées à partir de 0).
# 
# Vous devrez afficher, pour chaque position, le numéro de la personne qui 
# s'y trouve une fois tous les changements faits.
#=========================================================================================
# Exemple
# entrée :
# 
# 5
# 3

# 1
# 2
# 3
# 4
# 5

# 1
# 2

# 1
# 3

# 4
# 0
# sortie :
# 
# 5
# 4
# 2
# 3
# 1
# Commentaires
# Evolution des numéros dans l'exemple :
# 
# Au début : 1,2,3,4,5
# Après le changement (1, 2) : 1,3,2,4,5
# Après le changement (1, 3) : 1,4,2,3,5
# Après le changement (4, 0) : 5,4,2,3,1
#=========================================================================================

from decoTitle import decoMyTitleWithWrap
#=========================================================================================
# import test
#=========================================================================================
import random
from builtins import range

decoMyTitleWithWrap("Le banquet municipal")

def leBanquetMunicipal():
    #=========================================================================================
    # nbreTotalDePosition=int(input())
    # nbreChangementDePosition=int(input())
    #=========================================================================================
    nbreTotalDePosition=random.randint( 0, 999 )
    nbreChangementDePosition=random.randint(0,nbreTotalDePosition-10)
    print("nbreTotalDePosition ", nbreTotalDePosition," nbreChangementDePosition ",nbreChangementDePosition)
    
    #=========================================================================================
    # tabNumero=[0]*nbreTotalDePosition
    # #=========================================================================================
    # # print(tabNumero)
    # #=========================================================================================
    # for i in range(nbreTotalDePosition):
    #     numeroPersonne=int(input())
    #     #=====================================================================================
    #     # print(numeroPersonne)
    #     #=====================================================================================
    #     tabNumero[i]=numeroPersonne
    # print(nbreTotalDePosition)
    # print(tabNumero)
    #=========================================================================================
    #=====================================================================================
    # tabNumero=[1,2,3,4,5]
    #=====================================================================================
    tabNumero=[random.randint( 0, nbreTotalDePosition ) for i in range( nbreTotalDePosition )]
    print("nouveau tabNumero ",tabNumero, "\n taille tableau:", len(tabNumero))
    
    for j in range(nbreChangementDePosition):
        #=====================================================================================
        # numeroPersonne=int(input())
        # nouvellePosition=int(input())
        #=====================================================================================
        numeroPersonne=tabNumero[random.randint(1,nbreTotalDePosition-10)]
        nouvellePosition=tabNumero[random.randint(0,nbreChangementDePosition-10)]
        print("numeroPersonne: ",numeroPersonne," nouvellePosition: ",nouvellePosition)
        if(numeroPersonne<len(tabNumero) and nouvellePosition>len(tabNumero )):
            constance=tabNumero[numeroPersonne]
            constance2=tabNumero[nouvellePosition]
            print("constance:",constance, " constance2: ",constance2)
            tabNumero[nouvellePosition]=constance
            tabNumero[numeroPersonne]=constance2
        else:
            print("valeur incompatible avec le nombre de position initiale")
        #=====================================================================================
        # tabNumero[numeroPersonne]=tabNumero[nouvellePosition]
        # tabNumero[nouvellePosition]=tabNumero[numeroPersonne]
        #=====================================================================================
        
        print("changement de position :",j+1)
        #=====================================================================================
        # print(tabNumero)
        #=====================================================================================
        
    print("tabnumero ",tabNumero)
    for index in tabNumero:
        print("index ",index)
    print("the end")
     
for i in range(2000):
    leBanquetMunicipal() 
#=========================================================================================
# version test
decoMyTitleWithWrap("version test")
#=========================================================================================

def versionAtesterSurleSite():
    nbreTotalDePosition=int(input())
    nbreChangementDePosition=int(input())
    nbreTotalDePosition=5
    nbreChangementDePosition=3
    tabNumero=[0]*nbreTotalDePosition
     
    for i in range(nbreTotalDePosition):
        numeroPersonne=int(input())
        tabNumero[i]=numeroPersonne
     
    for j in range(nbreChangementDePosition):
        numeroPersonne=int(input())
        nouvellePosition=int(input())
        constance=tabNumero[numeroPersonne]
        constance2=tabNumero[nouvellePosition]
        tabNumero[nouvellePosition]=constance
        tabNumero[numeroPersonne]=constance2
     
    for index in  tabNumero:
        print(index)
        
#=========================================================================================
# versionAtesterSurleSite()
#=========================================================================================
     
    