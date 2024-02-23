
import os
import joblib

# ce fichier charge notre modele de machine learning

# Chemin absolu vers le dump du modele machine: modele_machine_learning_joblib
# Projets\Projet2_NetFlix\modele_machine_learning_joblib\recommandation_film_netflix.joblib

import os
import joblib

# Chemin absolu vers le dump du modele machine: modele_machine_learning_joblib
file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "..",
    "modele_machine_learning_joblib",
    "recommandation_film_netflix.joblib",
)

def load_modele_machine_learning():
    try:
        # Charger le modèle à partir du chemin absolu
        knn_recommandation = joblib.load(file_path)
        return knn_recommandation
    except FileNotFoundError:
        print(f"Le modele de machine learning {file_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

# Charger le modèle
knn_recommandation = load_modele_machine_learning()

if knn_recommandation is not None:
    # Afficher les films
    print(f"\nModèle chargé avec succès :\n{knn_recommandation} \n")
else:
    print("Le modèle n'a pas pu être chargé.")
