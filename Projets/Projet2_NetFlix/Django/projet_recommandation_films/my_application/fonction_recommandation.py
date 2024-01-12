# pylint: disable=redefined-outer-name
from .load_data import load_data
from .load_modele_machine_learning import load_modele_machine_learning
from .load_X_reduced import load_X_reduced
import pandas as pd
import numpy as np
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
nom_film = 'Le dîner de cons'
#  fonction de recommandation de film

def recommandation_film(my_dataframe,X_reduced,nom_film):
    df = my_dataframe
    # liste des colonnes numériques
    liste_colonnes_numeriques = df.select_dtypes(include=[np.number]).columns.tolist()
    # print(f"liste_colonnes_numeriques :{liste_colonnes_numeriques}")
    # liste des colonnes non numériques
    liste_colonnes_non_numeriques = df.select_dtypes(
        exclude=[np.number]).columns.tolist()

    # Créer un objet MinMaxScaler
    # scaler = MinMaxScaler()
    # Ajuster le scaler aux données
    # scaler.fit(df[liste_colonnes_numeriques])
    # Transformer les données
    # data_scaled = scaler.transform(data)

    # Obtenir l'index et le tconst du film choisi
    index_film = df[df["title"] == nom_film]["tconst"].index[0]

    # # recherche des 10 voisins, 11 car il faut retirer le premier car c'est le meilleur voisin de lui-meme
    # knn_recommandation = NearestNeighbors(n_neighbors=11)
    # # Entraîner le modèle KNN sur X_reduced
    # knn_recommandation.fit(X_reduced)
    # # Pour inverser l'ACP
    # # X_original = acp.inverse_transform(X_reduced)
    # distances, indices = knn_recommandation.kneighbors([X_reduced[index_film].drop("title", axis=1)])
    distances, indices = knn_recommandation.kneighbors([X_reduced[index_film]])

    # Aplatir 'indices' en un tableau 1D
    indices_plat = indices.flatten()
    # Aplatir 'indices' en un tableau 1D
    distances_plat = distances.flatten()
    # print(f"distances_plat :\n{distances_plat} \n")

    # # inverse du minmaxscaler pour avoir les  valeurs originales
    # df_original_scaled = scaler.inverse_transform(df[liste_colonnes_numeriques])
    # # Convertir le tableau numpy inversé en DataFrame afin d'avoir  index et loc
    # df_original_scaled = pd.DataFrame(df_original_scaled, columns=liste_colonnes_numeriques)

    # liste pour stocker les informations des films
    films_proches = []
    # itérer sur chaque indice individuel
    for j in range(11):
        i = indices_plat[j]
        # print("INFO DATAFRAME",  df["title"])

        # Obtenir le tconst pour le film actuel
        tconst_film = df.loc[i, 'tconst']
        # Créer un dictionnaire avec les informations du film
        film = {
            'nom': df.loc[i, 'title'],
            'note moyenne': df.loc[i, 'averageRating'],
            # Convertir en int
            'nombre de votants': int(df.loc[i, 'numVotes']),
            'genres': df.loc[i, 'genres'],
            'acteurs et actrices': df[(df['tconst'] == tconst_film) & (df['category'].isin(['actor', 'actress']))]['primaryName'].tolist(),
            'director': df[(df['tconst'] == tconst_film) & (df['category'] == 'director')]['primaryName'].tolist(),
            'composer': df[(df['tconst'] == tconst_film) & (df['category'] == 'composer')]['primaryName'].tolist(),
            'distance': round(distances_plat[j], 3),
            # Arrondir à 3 chiffres après la virgule
            'année de sortie': int(df.loc[i, 'startYear'])
        }
        # Ajouter le dictionnaire à la liste
        films_proches.append(film)

    # Convertir la liste de dictionnaires en un DataFrame
    df_films_proches = pd.DataFrame(films_proches)
    # Retirer la première ligne de df_films_proches
    # on retire le premier de la liste car il correspond au film choisi
    df_film_choisi = df_films_proches.iloc[0:1].copy()
    # la prmeier ligne correspond au film choisi
    df_films_proches = df_films_proches.iloc[1:]
    # print(f"\n df_film_choisi:\n{df_film_choisi} \n")
    # print(f"\n df_films_proches:\n{df_films_proches} \n")
    # print(f"\ndf_films_proches :\n{df_films_proches} \n")
    return df_film_choisi, df_films_proches

