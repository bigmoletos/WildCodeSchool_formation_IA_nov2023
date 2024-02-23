from joblib import load
import os

# Chemin absolu vers le fichier dataset
file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "..",
    "data_reduced",
    "X_reduced.joblib",
)

def load_X_reduced():
    try:
        with open(file_path, "rb") as f:
            X_reduced = load(f)  # Appelez load() sur l'objet fichier
        return X_reduced
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


# Charger X_reduced à partir d'un fichier
X_reduced = load_X_reduced()
# print("Valeur de X_reduced :", X_reduced)
# print("Type de X_reduced :", type(X_reduced))

