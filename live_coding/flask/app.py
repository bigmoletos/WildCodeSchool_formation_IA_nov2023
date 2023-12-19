from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
import pandas as pd

# Load the Iris dataset
df = px.data.iris()

# Prepare the data for training
X = df[['sepal_width', 'sepal_length', 'petal_width', 'petal_length']]
y = df['species']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Create the Flask application
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/formulaire.html", methods=["GET", "POST"])
def formulaire():
    if request.method == "POST":
        data = request.form["valeur"]
        return render_template("formulaire.html", resultat=data)
    else:
        return render_template("formulaire.html")


@app.route("/formulaireURL.html", methods=["GET", "POST"])
def formulaireURL():
    if request.method == "POST":
        data = request.args.get("valeur")
        return render_template("formulaireURL.html", resultat=data)
    if request.method == "GET":
        return render_template("formulaire.html")


@app.route("/formulaireIris", methods=["GET", "POST"])
def formulaireIris():
    if request.method == "POST":
        # Récupérer les valeurs du formulaire et les convertir en flottants
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        # Créer un tableau numpy à partir des valeurs
        data = np.array(
            [[sepal_length, sepal_width, petal_length, petal_width]])

        # Utiliser le modèle pour faire une prédiction
        prediction = model.predict(data)

        return render_template("formulaireIris.html", resultat=prediction)
    else:
        return render_template("formulaireIris.html")


@app.route("/graphe", methods=["GET", "POST"])
def formulaireGraphe():
    if request.method == "POST":
        # Récupérer les valeurs du formulaire et les convertir en flottants
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        # Créer un tableau numpy à partir des valeurs
        data = np.array(
            [[sepal_length, sepal_width, petal_length, petal_width]])

        # Utiliser le modèle pour faire une prédiction
        prediction = model.predict(data)
        # Accédez au premier élément de la liste
        prediction = prediction[0]

        # Générer le graphique
        # Créer un DataFrame pour les données du formulaire
        df_form = pd.DataFrame({
            'sepal_width': [sepal_width],
            'sepal_length': [sepal_length],
            'species': [prediction]
        })

        # Générer le graphique pour les données du DataFrame
        fig = px.scatter(df, x="sepal_width",
                         y="sepal_length", color="species")

        # Ajouter le graphique pour les données du formulaire
        fig_form = px.scatter(df_form, x="sepal_width", y="sepal_length", color="species",
                              hover_data=["species", "sepal_width", "sepal_length"])
        fig.add_trace(fig_form.data[0])

        # Mettre à jour la taille et la couleur des marqueurs pour les données du formulaire
        fig.data[-1].marker.size = 30
        fig.data[-1].marker.color = "grey"

        fig.update_layout(autosize=False, width=800, height=700)

        # Convertir le graphique en format HTML
        graph_html = fig.to_html(full_html=False)

        return render_template("formulaireGraphe.html",
                               resultat=prediction,
                               graph=graph_html,
                               sepal_length=sepal_length,
                               sepal_width=sepal_width,
                               petal_length=petal_length,
                               petal_width=petal_width)
    else:
        return render_template("formulaireGraphe.html")


if __name__ == "__main__":
    app.run(debug=True)
