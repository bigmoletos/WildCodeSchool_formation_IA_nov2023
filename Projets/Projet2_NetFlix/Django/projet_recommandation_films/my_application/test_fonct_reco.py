from fonction_recommandation import recommandation_film
# pylint: disable=redefined-outer-name
from load_data import load_data
from load_modele_machine_learning import load_modele_machine_learning
from load_X_reduced import load_X_reduced
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# from sklearn.preprocessing import MinMaxScaler



# Charger le modèle une seule fois
try:
    my_dataframe = load_data()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données.")
    print(str(e))

# Charger le modèle machine learning
try:
    knn_recommandation = load_modele_machine_learning()
except Exception as e:
    print("Une erreur s'est produite lors du chargement du modele de machine learning.")
    print(str(e))

# Charger X_reduced une seule fois
try:
    X_reduced = load_X_reduced()
except Exception as e:
    print("Une erreur s'est produite lors du chargement de X_reduced.")
    print(str(e))

# index = df[df.Series_Title == film].index[0]
# distances, index = knn.kneighbors(df.drop("Series_Title", axis=1).values[position].reshape(1, -1))
# recommandations = df.Series_Title.iloc[index[0]].values


# le nom du film provient du formulaire
nom_film_test = 'Le dîner de cons'
#  fonction de recommandation de film

df_film_choisi_test, df_films_proches_test= recommandation_film(my_dataframe,X_reduced,nom_film_test)
print(f"\n df_film_choisi_test:\n{df_film_choisi_test} \n")
print(f"\n df_films_proches_test:\n{df_films_proches_test} \n")

