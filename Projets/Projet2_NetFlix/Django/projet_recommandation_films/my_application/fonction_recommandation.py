# pylint: disable=redefined-outer-name
from .load_data import load_data
from .load_modele_machine_learning import load_modele_machine_learning
from .load_X_reduced import load_X_reduced
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# from sklearn.preprocessing import MinMaxScaler

# Projets\Projet2_NetFlix\Django\projet_recommandation_films\my_application\fonction_recommandation.py

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
# nom_film_test = 'Le dîner de cons'

#  fonction de recommandation de film

def recommandation_film(my_dataframe, X_reduced, nom_film):
    df = my_dataframe
    print(f"nom_film saisi :{nom_film}")
    # liste des colonnes numériques
    liste_colonnes_numeriques = df.select_dtypes(
        include=[np.number]).columns.tolist()
    print(f"liste_colonnes_numeriques :{liste_colonnes_numeriques}")
    # liste des colonnes non numériques
    liste_colonnes_non_numeriques = df.select_dtypes(
        exclude=[np.number]).columns.tolist()
    print(f"liste_colonnes_numeriques :{liste_colonnes_non_numeriques}")

    # Créer un objet MinMaxScaler
    # scaler = MinMaxScaler()
    # Ajuster le scaler aux données
    # scaler.fit(df[liste_colonnes_numeriques])
    # Transformer les données
    # data_scaled = scaler.transform(data)
    if nom_film in df["title"].values:
    # Obtenir l'index et le tconst du film choisi
        index_film = df[df["title"] == nom_film]["tconst"].index[0]
        tconst_film_choisi = df["tconst"].loc[index_film]
    else:
        print(f"Film '{nom_film}' non trouvé dans le dataframe.")
        return []
    print(f"tconst_film_choisi :\n{tconst_film_choisi} \n")
    # # recherche des 10 voisins, 11 car il faut retirer le premier car c'est le meilleur voisin de lui-meme
    k=12
    knn_recommandation2 = NearestNeighbors(n_neighbors=k)
    # # Entraîner le modèle KNN sur X_reduced
    knn_recommandation2.fit(X_reduced)
    # # Pour inverser l'ACP
    # # X_original = acp.inverse_transform(X_reduced)

    # distances, indices = knn_recommandation.kneighbors([X_reduced[index_film].drop("title", axis=1)])
    # distances, indices = knn_recommandation.kneighbors([X_reduced[index_film]])
    distances, indices = knn_recommandation2.kneighbors(
        [X_reduced[index_film]])

    k_voisin=knn_recommandation.n_neighbors
    print(f"k_voisin :\n{k_voisin} \n")

    # Aplatir 'indices' en un tableau 1D
    indices_plat = indices.flatten()
    print(f"indices_plat :\n{indices_plat} \n")
    # Aplatir 'indices' en un tableau 1D
    distances_plat = distances.flatten()
    print(f"distances_plat :\n{distances_plat} \n")

    # # inverse du minmaxscaler pour avoir les  valeurs originales
    # df_original_scaled = scaler.inverse_transform(df[liste_colonnes_numeriques])
    # # Convertir le tableau numpy inversé en DataFrame afin d'avoir  index et loc
    # df_original_scaled = pd.DataFrame(df_original_scaled, columns=liste_colonnes_numeriques)

    # liste pour stocker les informations des films
    films_proches = []
    tconst_film = None
    # unique_tconsts = [tconst for tconst in df['tconst'].unique() ]

    # creation de la liste des tcons unique correspondant à la liste donnée par indice_plat
    unique_tconsts = [df.iloc[index_film]['tconst']
                      for index_film in indices_plat]
    unique_tconsts = list(set(unique_tconsts))
    # Retirer index_film de la liste
    if tconst_film_choisi in unique_tconsts :
        unique_tconsts.remove(tconst_film_choisi)
    print("+"*20)
    print(f" tconst_film1 :{tconst_film} ")
    print(f" unique_tconsts1 :{unique_tconsts} ")
    print("+"*20)
    # itérer sur chaque indice individuel
    for j in range(min(k_voisin, len(indices_plat))):
        i = indices_plat[j]
        # print(f" indice i {i} j {j}")
        # print("INFO DATAFRAME",  df["title"])

        # Obtenir le tconst pour le film actuel
        # tconst_film = df.loc[i, 'tconst']
        # tconst_film = unique_tconsts[j]
        tconst_film = unique_tconsts[j] if j < len(unique_tconsts) else None

        print("#"*20)
        print(f" tconst_film i {i} j {j}:{tconst_film} ")
        # print(f" nom film test:{df[(df['tconst'] == tconst_film)]['title'].iloc[0]} ")
        # print(f" distance:{distances_plat[j]} ")
        print("#"*20)
        if tconst_film and df[df['tconst'] == tconst_film].shape[0] > 0:
        # Créer un dictionnaire avec les informations du film
            film = {
                'nom': df[(df['tconst'] == tconst_film)]['title'].iloc[0],
                # 'nom': df.loc[i, 'title'],
                'note moyenne': df[(df['tconst'] == tconst_film)]['averageRating'].iloc[0],
                # 'note moyenne': df.loc[i, 'averageRating'],
                # Convertir en int
                'nombre de votants': int(df[(df['tconst'] == tconst_film)]['numVotes'].iloc[0]),
                # 'nombre de votants': int(df.loc[i, 'numVotes']),
                'genres': df[(df['tconst'] == tconst_film)]['genres'].iloc[0],
                # 'genres': df.loc[i, 'genres'],
                'acteurs et actrices': df[(df['tconst'] == tconst_film) & (df['category'].isin(['actor', 'actress']))]['primaryName'].tolist(),
                'director': df[(df['tconst'] == tconst_film) & (df['category'] == 'director')]['primaryName'].tolist(),
                'composer': df[(df['tconst'] == tconst_film) & (df['category'] == 'composer')]['primaryName'].tolist(),
                # 'distance': round(distances_plat[j], 3),
                # 'distance' :round((1 - (distances_plat[j] / max(distances_plat))) , 3),
                'distance': round(distances_plat[j], 3),
                # Arrondir à 3 chiffres après la virgule
                'année de sortie': int(df[(df['tconst'] == tconst_film)]['startYear'].iloc[0]),
                # 'année de sortie': int(df.loc[i, 'startYear'])
            }
            # Ajouter le dictionnaire à la liste
            films_proches.append(film)

    # print(f" films_proches:{films_proches} ")

    # print(f" films_proches with set:{films_proches} ")
    # Convertir la liste de dictionnaires en un DataFrame
    df_films_proches = pd.DataFrame(films_proches)
    # print(f" df_films_proches:{films_proches} ")
    # print(f" df_films_proches with unique:{df_films_proches['nom'].unique()} ")
    # Retirer la première ligne de df_films_proches
    # Le film choisi de la liste car il correspond au film choisi
    df_film_saisi = []
    film_saisi = {
                'nom': df[(df['title']==nom_film)]['title'].iloc[0],
                # 'nom': df.loc[i, 'title'],
                'note moyenne': df[(df['title']==nom_film)]['averageRating'].iloc[0],
                # Convertir en int
                'nombre de votants': int(df[(df['title']==nom_film)]['numVotes'].iloc[0]),
                'genres': df[(df['title']==nom_film)]['genres'].iloc[0],
                'acteurs et actrices': df[(df['title']==nom_film) & (df['category'].isin(['actor', 'actress']))]['primaryName'].tolist(),
                'director': df[(df['title']==nom_film) & (df['category'] == 'director')]['primaryName'].tolist(),
                'composer': df[(df['title']==nom_film) & (df['category'] == 'composer')]['primaryName'].tolist(),
                # Arrondir à 3 chiffres après la virgule
                'année de sortie': int(df[(df['title']==nom_film)]['startYear'].iloc[0]),
                # 'année de sortie': int(df.loc[i, 'startYear'])
            }
            # Ajouter le dictionnaire à la liste
    df_film_saisi.append(film_saisi)
    print(f"\n film_saisi:\n{film_saisi} \n")

    # df_film_choisi = df_films_proches.iloc[0:1].copy()
    df_film_saisi = pd.DataFrame(df_film_saisi)
    print(f"\n df_film_choisi:\n{df_film_saisi} \n")
    # lOn choisit les n premiers films
    df_films_proches = df_films_proches.iloc[0:8]
    print(f"\n df_films_proches:\n{df_films_proches} \n")
    # print(f"\ndf_films_proches :\n{df_films_proches} \n")

    return df_film_saisi, df_films_proches

# test

# df_film_choisi_test, df_films_proches_test= recommandation_film(my_dataframe,X_reduced,nom_film_test)
# print(f"\n df_film_choisi_test:\n{df_film_choisi_test} \n")
# print(f"\n df_films_proches_test:\n{df_films_proches_test} \n")

# ||||||||||||||||


'''df = merged_df3
nom_film = 'Le dîner de cons

# Obtenir l'index et le tconst du film choisi
index_film = df[df["title"] == nom_film]["tconst"].index[0]

# recherche des 10 voisins, 11 car il faut retirer le premier car c'est le meilleur voisin de lui-meme
knn_recommandation = NearestNeighbors(n_neighbors=11)
# Entraîner le modèle KNN sur X_reduced
knn_recommandation.fit(X_reduced)
# Pour inverser l'ACP
# X_original = acp.inverse_transform(X_reduced)
distances, indices = knn_recommandation.kneighbors([X_reduced[index_film]])

# Aplatir 'indices' en un tableau 1D
indices_plat = indices.flatten()
# Aplatir 'indices' en un tableau 1D
distances_plat = distances.flatten()
# print(f"distances_plat :\n{distances_plat} \n")

# liste pour stocker les informations des films
films_proches = []
# itérer sur chaque indice individuel
for j in range(11):
    i = indices_plat[j]
    # inverse du minmaxscaler pour avoir les  valeurs originales
    df_original_scaled = scaler.inverse_transform(df[liste_colonnes_numeriques])
    # Convertir le tableau numpy inversé en DataFrame afin d'avoir  index et loc
    df_original_scaled = pd.DataFrame(df_original_scaled, columns=liste_colonnes_numeriques)
    # ...
        # Obtenir le tconst pour le film actuel
    tconst_film = df.loc[i, 'tconst']
    # Créer un dictionnaire avec les informations du film
    film = {
        'nom': df.loc[i, 'title'],
        'note moyenne': df_original_scaled.loc[i, 'averageRating'],
        'nombre de votants': int(df_original_scaled.loc[i, 'numVotes']),  # Convertir en int
        'genres': df.loc[i, 'genres'],
        'acteurs et actrices': df[(df['tconst'] == tconst_film) & (df['category'].isin(['actor', 'actress']))]['primaryName'].tolist(),
        'director': df[(df['tconst'] == tconst_film) & (df['category'] == 'director')]['primaryName'].tolist(),
        'composer': df[(df['tconst'] == tconst_film) & (df['category'] == 'composer')]['primaryName'].tolist(),
        'distance': round(distances_plat[j], 3) ,
        'année de sortie': int(df.loc[i, 'startYear']) # Arrondir à 3 chiffres après la virgule
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
print(f"\n df_film_choisi:\n{df_film_choisi} \n")
print(f"\n df_films_proches:\n{df_films_proches} \n")
'''
