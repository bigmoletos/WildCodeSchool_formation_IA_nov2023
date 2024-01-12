from .load_data import load_data
import pandas as pd
import numpy as np

# Charger le modèle une seule fois
try:
    df1 = load_data()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données.")
    print(str(e))
    df1 = pd.DataFrame()  # Créer un DataFrame vide en cas d'erreur

# fonction donnant les statisques d'un acteur


def stat_acteur(df1, acteur):
    df = df1.copy()
    df_acteur = None  # Initialiser df_acteur à None
    try:
        df_acteur = df[(df['primaryName'].str.contains(
            acteur, case=False, na=False))]
    except Exception as e:
        print(
            "Une erreur s'est produite lors de la recherche de l'acteur dans le dataframe.")
        print(str(e))
        return df_acteur

    try:
        nom_le_plus_frequent = df_acteur['primaryName'].mode()[0]
        print("Le nom le plus courament utilisé est :", nom_le_plus_frequent)
        df_acteur = df[df['primaryName'] == nom_le_plus_frequent]
    except Exception as e:
        print("Une erreur s'est produite lors de la recherche du nom le plus fréquent.")
        print(str(e))
        pass

    try:
        nombre_films = df_acteur.shape[0]
        premiere_annee = df_acteur['startYear'].min()
    except Exception as e:
        print("Une erreur s'est produite lors du calcul du nombre de films et de l'année du premier film.")
        print(str(e))
        pass

    films_info = None  # Définir une valeur par défaut

    try:
        df_acteur['startYear'] = df_acteur['startYear'].astype(int)
        films_info = df_acteur[['startYear', 'title', 'primaryName',
                                'genres', 'runtimeMinutes', 'averageRating', 'numVotes']].copy()

        # films_info.loc[:, 'casting'] = films_info.apply(
        #     lambda x: get_casting(x['title'], df_acteur), axis=1)
        # print(f"\ndf_acteur :\n{df_acteur} \n")
        # print(f"\n films_info:\n{films_info} \n")

    except Exception as e:
        print("Une erreur s'est produite lors de la création de la liste d'informations sur les films.")
        print(str(e))
        pass

    try:
        note_moyenne = df_acteur['averageRating'].mean()
    except Exception as e:
        print("Une erreur s'est produite lors du calcul de la note moyenne.")
        print(str(e))
        pass

    top_3_films = None  # Définir une valeur par défaut

    try:
        # Les 3 films de l'acteur qui ont eu le plus de succès
        top_3_films = df_acteur.sort_values(by='averageRating', ascending=False).head(
            3)[['title', 'startYear', 'averageRating', 'numVotes']]
    except Exception as e:
        print(
            "Une erreur s'est produite lors de la recherche des 3 films les plus réussis.")
        print(str(e))
        pass

    print(f"Depuis {premiere_annee:.0f}, {
          nom_le_plus_frequent} a participé à {nombre_films} films.")
    # print(f"Informations sur le casting des films :{
    #       films_info['casting'] if films_info is not None else 'Non disponible'}")
    print(f"La note moyenne de tous ses films est {note_moyenne:.2f}")
    print(f"\nLes 3 films de l'acteur qui ont eu le plus de succès sont :\n{
          top_3_films if top_3_films is not None else 'Non disponible'}")
    # print(f"Informations sur les films :{films_info}")

    return df_acteur
