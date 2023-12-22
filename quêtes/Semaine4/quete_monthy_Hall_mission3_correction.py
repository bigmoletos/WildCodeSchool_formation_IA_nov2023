import numpy as np
import matplotlib.pyplot as plt
import time
# %%time #permet de mesurer la charge processus  sous jupyter

start_time = time.time()

start_time = time.time()

print("Temps d'exécution : %s secondes" % (time.time() - start_time))
def play_games(strategy, nb_turns):
    # Initialiser les portes et les choix
    # correct_doors = np.random.randint(0, 3, nb_turns) #choix 0 1 2 possibles
    # first_choices = np.random.randint(0, 3, nb_turns)
    portes =np.array([1,2,3])
    bonne_porte=np.random.choice(portes, nb_turns)

    premier_choix=np.random.choice(portes, nb_turns)

    porte_restante=np.empty(nb_turns,dtype=int)
    # porte_restante=np.empty(nb_turns,dtype=int)
    porte_restante[bonne_porte == premier_choix] =0  # on filtre entre les 2 portes restantes
    porte_restante[bonne_porte != premier_choix] =1

    # deuxieme_choix=np.random.choice(portes, nb_turns)
    deuxieme_choix=np.empty(nb_turns,dtype=int)

    if strategie.lower() == "change":
        deuxieme_choix[bonne_porte == premier_choix] =0
        deuxieme_choix[bonne_porte != premier_choix] =1
         # on filtre entre les 2 portes restantes
    elif strategie.lower() == "garde":
        deuxieme_choix[bonne_porte == premier_choix] =0
        deuxieme_choix[bonne_porte != premier_choix] =1


    return deuxieme_choix.sum()
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
