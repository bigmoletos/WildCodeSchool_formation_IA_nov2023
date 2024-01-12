# pylint: disable=redefined-outer-name
from .load_data import load_data
from .load_modele_machine_learning import load_modele_machine_learning
from .load_X_reduced import load_X_reduced
import pandas as pd
import numpy as np

# Charger les données nécessaires pour la recommandation de films
try:
    my_dataframe = load_data()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données.")
    print(str(e))

# Charger le modèle de machine learning
try:
    modele_ml = load_modele_machine_learning()
except Exception as e:
    print("Une erreur s'est produite lors du chargement du modèle de machine learning.")
    print(str(e))

# Charger les données réduites pour le modèle
try:
    X_reduced = load_X_reduced()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données réduites.")
    print(str(e))

# Votre code pour la recommandation de films ici
# ...