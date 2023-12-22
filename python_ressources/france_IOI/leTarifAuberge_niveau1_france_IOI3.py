#=========================================================================================
# france_IOI  niveau 1 chapitre 6
# Tarifs de l'aubergeEntraînement
# Imprimer    
# SujetRésoudreConseilsActivitéCorrection
# L'auberge dans laquelle vous vous arrêtez pour la nuit adapte ses prix en fonction 
# de l'âge du client et du poids de ses bagages. Les règles ne vous étant pas très claires,
#  vous décidez d'écrire un petit programme qui vous permettra facilement, 
#  à vous et à vos compagnons de voyage, de connaître le prix d'une nuit.
# 
# Ce que doit faire votre programme :
# Une chambre ne coûte rien si on a 60 ans (l'âge de l'aubergiste !) et 
# 5 écus si on a strictement moins de 10 ans. Pour les autres personnes 
# c'est 30 écus plus un supplément de 10 écus si on a au moins 20 kilos de bagages.
# 
# Votre programme doit lire deux entiers, l'âge et le poids des bagages
#  de la personne et doit afficher le prix, sous la forme d'un entier.
# 
# Exemple
# entrée :
# 
# 22
# 25
# sortie :
# 
# 40
#=========================================================================================
from platform import java_ver


age=int(input())
poidsBagage=int(input())
prixChambre=0
supplementBagage=0
if (age>=0  and age==60 ):
    prixChambre=0
elif(age>=0 and age<10):
    prixChambre=5
else:
    prixChambre=30
    
if(age!=60 and age>=10 and poidsBagage>=20):
    supplementBagage=10
    
print(prixChambre+supplementBagage)

#=========================================================================================
# correction
#=========================================================================================
age = int(input())
poids = int(input())
if age < 10:
   print(5)
else:
   if age == 60:
      print(0)
   else:
      if poids >= 20:
         print(40)
      else:
         print(30)
         

#=========================================================================================
# correction 
# import algorea.Scanner;
# class Main
# {
#    public static void main(String[] args)
#    {
#       Scanner entrée = new Scanner(System.in);
#       int âge = entrée.nextInt();
#       int poids = entrée.nextInt();
#       if(âge < 10)
#       {
#          System.out.println("5");
#       }
#       else
#       {
#          if(âge == 60)
#          {
#             System.out.println("0");
#          }
#          else
#          {
#             if(poids >= 20)
#             {
#                System.out.println("40");
#             }
#             else
#             {
#                System.out.println("30");
#             }
#          }
#       }
#    }
# }
#=========================================================================================

         