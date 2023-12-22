"""
  ce programme est un jeu en python dont le but est de simuler le jeu télévisé
  du Monty Hall, un joueur choisit une porte parmi trois, sachant qu’une seule
  porte cache un prix.
  Après le premier choix du joueur, l’animateur, qui sait ce qui se trouve
  derrière chaque porte, ouvre une des deux portes restantes qui ne cache
  pas le prix.
  Le joueur peut alors changer son choix initial et choisir l’autre porte fermée.

"""
import matplotlib.pyplot as plt # import de la librairie pour faire les tracés
from random import choice  # import des librairies de randomisation

"""
  Création de la fonction  play_one_game avec strategy en parametre.
  “change”: le joueur change de porte après que l’animateur a ouvert une porte ou
  “keep”: le joueur garde son choix initial.
  La fonction renvoie True si le joueur gagne,
  c’est-à-dire si son choix final est la porte avec le prix et False sinon
"""
def play_one_game(strategy):

  doors = ['A', 'B', 'C']  # création d'une liste de 3 portes  A B et C
  # choix  aléatoire d'un porte
  correct_door = choice(doors)
  first_choice = choice(doors)
  doors.remove(first_choice) #suppression de la porte choisie, donne le choix restant
  # print("correct_door :",doors)
  #  boucle de traitement de
  while True:
    hint_door = choice(doors) # initialisation du la porte ouverte
    if hint_door != correct_door:
      doors.remove(hint_door) # on supprime la porte si elle ne correspond pas à la porte gagnante
      break
  # si le choix du joueur est "change"
  if strategy.lower() == "change":
      second_choice = choice(doors) #le joueur change de porte et choisit donc la porte restante de la liste "doors"
  elif strategy.lower() == "keep": # si le choix du joueur est "keep"
      second_choice = first_choice #le joueur garde sa porte initiale
  else:
      raise ValueError("Strategy not recognized!") #on léve une erreur si jamais il n'y avait aucun choix

  return second_choice == correct_door  #renvoie True si le choix final du joueur
  #  est la porte gagnante car (second_choice == correct_door), sinon on renvoie false

"""
  La fonction play_many_games simule plusieurs parties (nb_turns).
  Elle renvoie une liste de gains/pertes (1,0).
  strategy sera ou "change" ou "keep"
  nb_turn définit le nombre de partie à simuler
"""
def play_many_games(strategy, nb_turns):
    # retourne une liste en comprehension lancant la partie "play_one_game" qui retourne
    #  false ou true, la liste fait la taille du nombre de parties
    print(list(1 if play_one_game(strategy) else 0 for i in range(nb_turns)))
    return list(1 if play_one_game(strategy) else 0 for i in range(nb_turns))

"""
  affichage histogramme avec la librairie matplotlib du nombre de gains
  en fonction de la stratégie adoptée
  change ou keep sur un échantillon de 10 000 parties
"""
plot = plt.bar([1, 2],
               [sum(play_many_games("change", 10000)), sum(play_many_games("keep", 10000))],
               tick_label=["Change", "Keep"])