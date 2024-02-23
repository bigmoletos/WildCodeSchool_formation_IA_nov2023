# pylint: disable=undefined-variable
import random
from flask import Flask, jsonify

# importation  des datas
# on veut retourner des datas au format json car
# c'est le format pour les API rest
# Ce raccourci ouvre un fichier en mode lecture, lit toutes les lignes dans une liste,
# et imprime la liste. Un bloc try/except est utilisé pour attraper et gérer
# toute exception qui pourrait se produire lors de l'ouverture, de la lecture,
# ou de l'impression du fichier.
file="quêtes/semaine13/API_REST/velo_ville_nantes.json"

try:
    with open(file, "r") as f:
        dictionnaire = f.read().splitlines()
        print(dictionnaire)
except FileNotFoundError as e:
    print(f"Le fichier n'a pas été trouvé : {e}")
except PermissionError as e:
    print(f"Permission refusée : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")



# on crée une application flask
app=Flask(__name__)
# donne la route par defaut
@app.route("/api_nantes")
#  creation vue
def index():
    # on retourne un fichier au format json
    return jsonify(dictionnaire)
    # return "hello world!"


if __name__ == "__main__":
    app.run(debug=True,  port=5001)
