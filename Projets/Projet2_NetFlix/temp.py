import pandas as pd

# Fonction de traitement global de tous les dataframes
#  trie sur les colonnes à garder
#  trie sur les valeurs  à garder
duree_film_min = 80
duree_film_max = 180
nombre_votant_min = 100
note_moyenne_mini = 4
annee_min = "1980"
# liste_dataframes


def traitement_global_dataframes(liste_dataframes, duree_film_min, duree_film_max, nombre_votant_min, note_moyenne_mini, annee_min):
    # liste des noms de dataframes filtrés
    liste_dataframes_filtered = []
    for df in liste_dataframes:
        # filtre le dataset df_title_akas
        if df == 'df_title_akas3':
            df_name = "title_akas"
            my_dataframe = df
            # liste des colonnes à filtrer et à garder aprés filtre
            # liste colonnes: ['titleId', 'ordering', 'title', 'region', 'language', 'types', 'attributes', 'isOriginalTitle']`
            # on garde que les  colonnes suivantes ['titleId', 'title', 'region', 'types']`
            col_to_filtre = ['titleId', 'region', 'title', 'types']
            col_to_keep = ['titleId', 'region', 'title', 'types']
            # tableau des valeurs à garder par colonne
            liste_valeur_to_keep = {
                'types': ['imdbDisplay'],
                'region': ["FR"]
            }
            # fonction de traitement des colonnes et des valeurs d'un dataframe
            my_dataframe_filtered = traitement_dataframe(df_name, my_dataframe, col_to_filtre, col_to_keep,
                                                         liste_valeur_to_keep, duree_film_min, duree_film_max, nombre_votant_min, note_moyenne_mini, annee_min)
            my_dataframe_filtered = "df_title_akas3_filtered"
            liste_dataframes_filtered.append(my_dataframe_filtered)

        elif df == 'df_title_basics3':
            # initialisation des variables
            df_name = "title_basics"
            my_dataframe = df
            # liste des colonnes ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']
            col_to_filtre = ['tconst', 'titleType', 'primaryTitle',
                             'startYear',  'runtimeMinutes', 'genres']
            col_to_keep = ['tconst', 'primaryTitle',
                           'startYear', 'runtimeMinutes', 'genres']
            # tableau des valeurs à garder par colonne
            liste_valeur_to_keep = {
                "titleType": ['movie'],
                "genres": ['Action', 'Thriller', 'Adventure', 'Sci-Fi', 'Fantasy', 'Animation', 'War', 'Family', 'Musical', 'Mystery', 'Comedy',  'Drama'],
                "startYear": [annee_min],
                "runtimeMinutes": [duree_film_min, duree_film_max]
            }
            # fonction de traitement des colonnes et des valeurs d'un dataframe
            my_dataframe_filtered = traitement_dataframe(df_name, my_dataframe, col_to_filtre, col_to_keep,
                                                         liste_valeur_to_keep, duree_film_min, duree_film_max, nombre_votant_min, note_moyenne_mini, annee_min)
            # resultat
            my_dataframe_filtered = "df_title_basics_filtered"
            liste_dataframes_filtered.append(my_dataframe_filtered)

        elif df == 'df_title_crew3':
            # initialisation des variables
            df_name = "title.crew"
            my_dataframe = df
            # liste des colonnes ['tconst', 'directors', 'writers']
            col_to_filtre = ['tconst', 'directors']
            col_to_keep = col_to_filtre
            # tableau des valeurs à garder par colonne
            liste_valeur_to_keep = {}
            # fonction de traitement des colonnes et des valeurs d'un dataframe
            my_dataframe_filtered = traitement_dataframe(df_name, my_dataframe, col_to_filtre, col_to_keep,
                                                         liste_valeur_to_keep, duree_film_min, duree_film_max, nombre_votant_min, note_moyenne_mini, annee_min)
            # resultat
            my_dataframe_filtered = "df_title_crew_filtered"
            liste_dataframes_filtered.append(my_dataframe_filtered)

        elif df == 'df_title_ratings3':
            # initialisation des variables
            df_name = "title_ratings"
            my_dataframe = df
            # liste des colonnes ['tconst', 'averageRating', 'numVotes']
            col_to_filtre = ['tconst', 'averageRating', 'numVotes']
            col_to_keep = ['tconst', 'averageRating', 'numVotes']
            # tableau des valeurs à garder par colonne
            liste_valeur_to_keep = {
                "averageRating": [note_moyenne_mini],
                "numVotes": [nombre_votant_min]
            }
            # fonction de traitement des colonnes et des valeurs d'un dataframe
            my_dataframe_filtered = traitement_dataframe(df_name, my_dataframe, col_to_filtre, col_to_keep,
                                                         liste_valeur_to_keep, duree_film_min, duree_film_max, nombre_votant_min, note_moyenne_mini, annee_min)
            # resultat
            my_dataframe_filtered = "df_title_ratings_filtered"
            # fonction de traitement des colonnes et des valeurs d'un dataframe
            liste_dataframes_filtered.append(my_dataframe_filtered)

        elif df == 'df_name_basics3':
            # initialisation des variables
            df_name = "name_basics"
            my_dataframe = df
            # liste des colonnes ['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']
            col_to_filtre = ['nconst', 'primaryName']
            col_to_keep = ['nconst', 'primaryName']
            # tableau des valeurs à garder par colonne
            liste_valeur_to_keep = {}
            # fonction de traitement des colonnes et des valeurs d'un dataframe
            my_dataframe_filtered = traitement_dataframe(df_name, my_dataframe, col_to_filtre, col_to_keep,
                                                         liste_valeur_to_keep, duree_film_min, duree_film_max, nombre_votant_min, note_moyenne_mini, annee_min)
            # resultat
            my_dataframe_filtered = "df_name_basics_filtered"
            liste_dataframes_filtered.append(my_dataframe_filtered)

        elif df == 'df_title_principals3':
            # initialisation des variables
            df_name = "title_principals"
            my_dataframe = df
            #  liste des colonnes['tconst', 'ordering', 'nconst', 'category', 'job', 'characters']
            col_to_filtre = ["tconst", "nconst", "category"]
            col_to_keep = ["tconst", "nconst", "category"]
            # tableau des valeurs à garder par colonne
            liste_valeur_to_keep = {
                'category': ['self', 'director', 'producer', 'composer'
                             'editor', 'actor', 'actress', 'writer'],
            }
            # fonction de traitement des colonnes et des valeurs d'un dataframe
            my_dataframe_filtered = traitement_dataframe(df_name, my_dataframe, col_to_filtre, col_to_keep,
                                                         liste_valeur_to_keep, duree_film_min, duree_film_max, nombre_votant_min, note_moyenne_mini, annee_min)
            # resultat
            my_dataframe_filtered = "df_title_principals_filtered"
            liste_dataframes_filtered.append(my_dataframe_filtered)

    return my_dataframe_filtered

# fonction de traitement des colonnes et des valeurs d'un dataframe


def traitement_dataframe(nom_dataframe, my_dataframe, colonne_a_filtrer, colonne_a_garder, liste_valeur_a_garder):
    try:
        # On ne garde que les colonnes spécifiées
        my_dataframe = my_dataframe[colonne_a_filtrer]
    except KeyError:
        print("Erreur : Une ou plusieurs colonnes spécifiées ne sont pas présentes dans le DataFrame.")
        return

    # Si liste_valeur_a_garder est vide, on ne fait rien
    if liste_valeur_a_garder:

        for col in liste_valeur_a_garder:
            try:
                # Si la colonne est 'startYear', on ne garde que les films à partir de l'an 2000
                if col == "startYear":
                    my_dataframe[col] = pd.to_numeric(
                        my_dataframe[col], errors='coerce')
                    my_dataframe = my_dataframe[my_dataframe[col] >= int(
                        liste_valeur_a_garder[col][0])]

                # Si la colonne est 'runtimeMinutes', on ne garde que les films dont la durée est entre 120 et 180 minutes
                elif col == "runtimeMinutes":
                    my_dataframe[col] = pd.to_numeric(
                        my_dataframe[col], errors='coerce')
                    my_dataframe = my_dataframe[(my_dataframe[col] >= int(liste_valeur_a_garder[col][0])) & (
                        my_dataframe[col] <= int(liste_valeur_a_garder[col][1]))]

                # filtre les notes
                elif col == "averageRating":
                    # Convertissez les colonnes 'averageRating' et 'numVotes' en nombres
                    my_dataframe[col] = pd.to_numeric(
                        my_dataframe[col], errors='coerce')
                    # Gardez uniquement les lignes où 'averageRating' est supérieur à 8
                    my_dataframe = my_dataframe[(
                        my_dataframe[col] > liste_valeur_a_garder[col][0])]
                 # filtre le nombres de votant
                elif col == 'numVotes':
                    # Convertissez les colonnes 'averageRating' et 'numVotes' en nombres
                    my_dataframe[col] = pd.to_numeric(
                        my_dataframe[col], errors='coerce')
                    # Gardez uniquement les lignes où 'numVotes' est supérieur ou égal à 200
                    my_dataframe = my_dataframe[my_dataframe[col]
                                                >= liste_valeur_a_garder[col][0]]

                # Pour les autres colonnes, on ne garde que les valeurs spécifiées
                else:
                    filtre_to_keep = liste_valeur_a_garder[col]
                    filtre_type_category = my_dataframe[col].isin(
                        filtre_to_keep)
                    my_dataframe = my_dataframe[filtre_type_category]
                pass

            except KeyError:
                print(f"Erreur : La colonne '{
                      col}' n'est pas présente dans le DataFrame.")
                return
            except TypeError:
                print(f"Erreur : Les valeurs pour la colonne '{
                      col}' ne peuvent pas être converties en nombre.")
                return

    try:
        # Après le traitement, on ne garde que les colonnes finales spécifiées
        print(f"\ncolonne_a_garder :\n{colonne_a_garder} \n")
        my_dataframe = my_dataframe[colonne_a_garder]
    except KeyError:
        print("Erreur : Une ou plusieurs colonnes finales spécifiées ne sont pas présentes dans le DataFrame.")
        return
    # Suppression des \N des colonnes restantes
    # my_dataframe = my_dataframe.loc[:, ~(my_dataframe == r'\N').any()]
    my_dataframe = my_dataframe.replace(r'\N', pd.NA)
    my_dataframe = my_dataframe.dropna()

    # Sauvegarde du DataFrame dans le dossier data_filtered
    my_dataframe.to_pickle(f"data_filtered/df_{nom_dataframe}_filtered.pkl")

    # Retourne le DataFrame traité
    return my_dataframe
