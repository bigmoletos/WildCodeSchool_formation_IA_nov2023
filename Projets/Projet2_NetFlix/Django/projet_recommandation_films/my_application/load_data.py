import pickle
import os


# ce fichier charge notre DATASET

# Chemin absolu vers le fichier dataset
file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "..",
    "data_merged",
    "df_merged.pkl",
)


def load_data():
    try:
        with open(file_path, "rb") as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
    except pickle.UnpicklingError:
        print("Une erreur s'est produite lors de la désérialisation des données.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")



# # test data
# df = load_data()
# if df is not None:
#     # Afficher le premier film
#     premier_film = df.iloc[0]
#     print(f"\ndf premier_film:\n{premier_film} \n")
