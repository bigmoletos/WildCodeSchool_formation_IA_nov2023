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
