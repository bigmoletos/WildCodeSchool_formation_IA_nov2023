import pandas as pd
import os

def suppression_doublon_fichier(fichier, repertoire_destination):
    # Lire les données du fichier
    data = pd.read_csv(fichier)

    # Supprimer les doublons
    data.drop_duplicates(inplace=True)

    # Créer le nom du fichier de sortie en ajoutant "whitoutdoublon" à la fin
    base = os.path.basename(fichier)
    nom_sans_extension = os.path.splitext(base)[0]
    nouveau_nom = f"{nom_sans_extension}_whitoutdoublon.txt"

    # Écrire les données sans doublons dans un nouveau fichier
    if repertoire_destination:
        # Créer un chemin de fichier complet pour le fichier de sortie
        fichier_sortie = os.path.join(repertoire_destination, nouveau_nom)
    else:
        fichier_sortie = nouveau_nom

    data.to_csv(fichier_sortie, index=False)

fichier="commandes_git.txt"
repertoire="."
suppression_doublon_fichier (fichier,repertoire)