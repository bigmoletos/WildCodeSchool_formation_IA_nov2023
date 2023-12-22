import random

def test1():
    tabNumero=[1,2,3,4,5]
    tabNumero=[0,2,1,4,3]
    tabNumero=[random.randint( 0, 1000 ) for i in range( 100 )]
    
    for index in tabNumero:
        numeroPersonne=tabNumero[random.randint(0,len(tabNumero)-1)]
        print("numeroPersonne ", numeroPersonne)
        #=====================================================================================
        # print(index)
        #=====================================================================================
        #=====================================================================================
        # print(tabNumero[index-1])
        #=====================================================================================
        #=====================================================================================
        # print(tabNumero)
        #=====================================================================================


def test2():
    nbreTotalDePosition=random.randint( 0, 999 )
    #=====================================================================================
    # print("nbreTotalDePosition ",nbreTotalDePosition,"nbreChangementDePosition ",nbreChangementDePosition)
    #=====================================================================================
    nbreChangementDePosition=random.randint(1,nbreTotalDePosition)
    print("nbreTotalDePosition ",nbreTotalDePosition,"nbreChangementDePosition ",nbreChangementDePosition)
    tabNumero=[random.randint( 0, nbreTotalDePosition ) for i in range( nbreTotalDePosition )]
    print("nouveau tabNumero ",tabNumero, "\ntaille tableau:", len(tabNumero))
    numeroPersonne=tabNumero[random.randint(1,nbreTotalDePosition)]
    print("numeroPersonne ",numeroPersonne)
    

for i in range(2000):
    test2()