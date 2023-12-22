import random


def triangle_plein():
  while True:
    try:
      hauteur_triangle = input("Veuillez entre la hauteur de triangle: ")
    except ValueError:
        hauteur_triangle = traduire_texte_chiffre(hauteur_triangle)
    try:
      hauteur_triangle = int(hauteur_triangle)
      symbol = input("Veuillez entre le symbole constituant votre triangle: ")
      insertion_parasite = False
      # print (parasite)
      # controle de la hauteur
      if hauteur_triangle < 3 or hauteur_triangle > 10:
        raise ValueError()

      # impression triangle
      message = symbol
      print(message)
      parasite = random.randint(0, 10)

      for i in range(1, hauteur_triangle+1):
        if i == 1 or i == hauteur_triangle:
            message += symbol
            print(message)
        if insertion_parasite != True:
            if i == random.randint(2, hauteur_triangle-1):
              # if i == random.randint(2,hauteur_triangle-1) :
                # cp== random.randint(2,hauteur_triangle-1)
                message += str(parasite)
                insertion_parasite = True
                print(message)
        else:
            message += symbol
            message = message.replace(str(parasite), symbol)
            print(message)

    except ValueError:
        print("Erreur : veuillez saisir une hauteur minimale de 3 et maximale de dix ")
    message = input("""Vous avez saisi des erreurs voulez-vous arreter le programme ou continuer ?
                  tapez Oui(o) pour arreter
                  tapez sur n'importe quelle touche pour continuer:  """)

    if message.lower() in ['o', 'oui', 'y', 'yes']:
        break

def traduire_texte_chiffre(texte):
  dico = {
      'un': 1,
      'deux': 2,
      'trois': 3,
      'quatre': 4,
      'cinq': 5,
      'six': 6,
      'sept': 7,
      'huit': 8,
      'neuf': 9,
      'dix': 10
}
  chiffre = dico[texte.lower()]

  return chiffre

#  test
triangle_plein()
