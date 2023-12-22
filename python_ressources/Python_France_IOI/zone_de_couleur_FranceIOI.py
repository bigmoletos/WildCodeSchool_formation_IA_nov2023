import random
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
    # carreJaune=False
    # bleu=False
    # rouge=False
    if not(0<=x<90 and 0<=y<70):
        print( "En dehors de la feuille" )
    elif((15<=x<45 or 60<=x<85) and 60<=y<70):
        # rouge=True
        print( "Dans une zone rouge" )
    elif((10<=x<85 and 10<=y<55) and not(25<=x<50 and  20<=y<45) ):
        # blue=True
        print( "Dans une zone bleue" )
    else:
        print( "Dans une zone jaune" )






