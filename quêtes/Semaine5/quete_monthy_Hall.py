import numpy as np
import matplotlib.pyplot as plt

def play_games(strategy, nb_turns):
    # Initialiser les portes et les choix
    correct_doors = np.random.randint(0, 3, nb_turns) #choix 0 1 2 possibles
    first_choices = np.random.randint(0, 3, nb_turns)
    strategy_generator = alternate_strategy() # execution de la fonction de generation de keep ou change alernativement
    # Si la stratégie est de changer, le deuxième choix est réussi si le premier choix était incorrect
    # Si la stratégie est de garder, le deuxième choix est réussi si le premier choix était correct
    if np.any(strategy == "alternate"):
      strategy = next(strategy_generator)   # si nous avions change alors il mettra keep
      if strategy == "change":
          second_choices_success = (first_choices != correct_doors)
      elif strategy == "keep":
          second_choices_success = (first_choices == correct_doors)
    elif np.any(strategy == "change"):
        second_choices_success = (first_choices != correct_doors)
    elif np.any(strategy == "keep"):
        second_choices_success = (first_choices == correct_doors)
    else:
        raise ValueError("Strategy not recognized!")

    return second_choices_success

# fonction alternate pour créer de maniére alternative change puis keep
def alternate_strategy():
    while True:
        yield "change"
        yield "keep"

# ---------------------------
#TEST DU JEU
# nombre de parties
nombre_parties=10000

# Jouer plusieurs parties avec différentes stratégies
play_change = np.sum(play_games("change", nombre_parties))
play_keep = np.sum(play_games("keep", nombre_parties))

# Pour la stratégie "alternate", nous générons un tableau de stratégies aléatoires ("change" ou "keep") pour chaque partie
# strategies = np.random.choice(["change", "keep"], nombre_parties)
play_alternate = np.sum(play_games("alternate", nombre_parties))

# Créer une nouvelle figure
plt.figure(figsize=(10, 5))

# Créer le graphique à barres
plot = plt.bar([1, 2, 3],
               [play_change, play_keep, play_alternate],
               tick_label=["Change", "Keep", "Alternate"])

# Ajouter un titre au graphique avec le nombre de parties
plt.title(f"Résultats des différentes stratégies avec {nombre_parties:,} parties".replace(',', ' '))

# Ajouter des titres aux axes
plt.xlabel("Stratégie")
plt.ylabel("Nombre de victoires ")

# Afficher le graphique
plt.show()
