import random
from flask import Flask, jsonify

# creation des datas
# on veut retourner des datas au format json car
# c'est le format pour les API rest
prenoms=["Eric","Fabrice","Yvan","Caroline","Imad","Franck","Paul","Michel"]
salaire=[2000,3000,3500,4000,4500,5000,5500,6000]
type_de_poste=["CDD","CDI","freelance","Portage"]
localisation=["france", "canada","thailande"]

# création de 300 données aléatoires
liste_prenom=[random.choice(prenoms) for p in range (1,300)]
liste_salaire=[random.choice(salaire) for p in range (1,300)]
liste_type_de_poste=[random.choice(type_de_poste) for p in range (1,300)]
liste_localisation=[random.choice(localisation) for p in range (1,300)]

dictionnaire={
    "prenoms":liste_prenom,
    "salaire": liste_salaire,
    "typeDePoste":liste_type_de_poste,
    "localidsation":liste_localisation
}

# on crée une application flask
app=Flask(__name__)
# donne la route par defaut
@app.route("/")
#  creation vue
def index():
    # on retourne un fichier au format json
    return jsonify(dictionnaire)
    # return "hello world!"


if __name__ == "__main__":
    app.run(debug=True)
