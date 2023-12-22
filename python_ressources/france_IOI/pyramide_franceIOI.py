# *********************************
# Département d'architecture : construction d'une pyramide
# Les habitants adorent les constructions en forme de pyramide ; de nombreux bâtiments officiels
# ont d'ailleurs cette forme. Pour fêter les 150 ans de la construction de la ville,
# le gouverneur a demandé la construction d'une grande et majestueuse pyramide à l'entrée de la ville.
# Malheureusement, en ces périodes de rigueur budgétaire, il y a peu d'argent pour ce projet.
# Les architectes souhaitent cependant construire la plus grande pyramide possible étant donné le budget prévu.

# Ce que doit faire votre programme:
# Votre programme doit d'abord lire un entier : le nombre maximum de pierres dont pourra être composée la pyramide. 
# Il devra ensuite calculer et afficher un entier : la hauteur de la plus grande pyramide qui pourra être construite, 
# ainsi que le nombre de pierres qui sera nécessaire.


# nbrePierres=int(input())
nbrePierres = 26042
pierreUtiles = 0
hauteur = 1
resultat=0
# while nbrePierres<pierreUtiles:
while (pierreUtiles +(  hauteur **2))<= nbrePierres:
    # print( "hauteur", hauteur )
    # if(pierreUtiles < nbrePierres):
    pierreUtiles = pierreUtiles+ hauteur **2
    hauteur = hauteur + 1
    # print( "nombre de pierres necessaires ", pierreUtiles )
print( "hauteur", hauteur-1 )
print( "nombre de pierres necessaires ", pierreUtiles )

# calcul par formule directe
n=6
pierreUtiles=n*(n+1)*(2*n+1)/6
print(pierreUtiles)
# **********************
# correction
nombreMaximumPierres = int(input())
nombrePierres = 0
hauteur = 1
while nombrePierres + hauteur * hauteur <= nombreMaximumPierres:
   nombrePierres = nombrePierres + hauteur * hauteur
   hauteur = hauteur + 1
print(hauteur - 1)
print(nombrePierres)

# *************
# java
import algorea.Scanner;
class Main
{
   public static void main(String[] args)
   {
      Scanner entrée = new Scanner(System.in);
      int nombreMaximumPierres = entrée.nextInt();
      int nombrePierres = 0;
      int hauteur = 1;
      while (nombrePierres + hauteur * hauteur <= nombreMaximumPierres)
      {
         nombrePierres = nombrePierres + hauteur * hauteur;
         hauteur = hauteur + 1;
      }
      System.out.println(hauteur - 1);
      System.out.println(nombrePierres);
   }
}
