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
list=[20,10,45,23,56,30,110,15,90,45,9,78,-12,-50,25,44,45,46,23,9,10,11,99]
# nombreTotalMesures=int(input())
# temperatureMinimum=int(input())
# temperatureMaximum=int(input())
nombreTotalMesures=5
temperatureMinimum=-10
temperatureMaximum=70

while nombreTotalMesures!=0 :
    # temperatureEnregistre=int(input())
    for index in range(len(list)):
        temperatureEnregistre=list[index]
        if(temperatureMinimum<=temperatureEnregistre<=temperatureMaximum):
            print(list[index],"Rien à signaler")
        else:
            print( list[index],"Alerte !!" )
    nombreTotalMesures=nombreTotalMesures-1
print( list[index], "Alerte !!" )

print("autre version\n")
# temperatureEnregistre = int(input())
nombreTotalMesures=5
temperatureMinimum=-10
temperatureMaximum=70
# temperatureEnregistre = temperatureMinimum
# temperatureEnregistre = int( input() )
nbMesure = 0
while nbMesure <= nombreTotalMesures and temperatureMinimum <= temperatureEnregistre <= temperatureMaximum:
    temperatureEnregistre = int( input() )
    if (temperatureMinimum <= temperatureEnregistre <= temperatureMaximum):
        print( "Rien à signaler" )
    nbMesure = nbMesure + 1
if not (temperatureMinimum <= temperatureEnregistre <= temperatureMaximum):
    print( "Alerte !!" )
