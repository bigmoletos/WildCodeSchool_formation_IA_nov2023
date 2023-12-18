from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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


@app.route("/formulaire", methods=["GET", "POST"])
def formulaire():
    if request.method == "POST":
        data = request.form["valeur"]
        return render_template("formulaire.html", resultat=data)
    else:
        return render_template("formulaire.html")


@app.route("/formulaireURL", methods=["GET", "POST"])
def formulaireURL():
    if request.method == "POST":
        data = request.args.get("valeur")
        return render_template("formulaireURL.html", resultat=data)
    if request.method == "GET":
        return render_template("formulaire.html")


@app.route("/formulaireIris", methods=["GET", "POST"])
def formulaireIris():
    if request.method == "POST":
        data = request.form["valeur"]
        # Use the model to make a prediction
        prediction = model.predict(np.array([data]))
        return render_template("formulaireIris.html", resultat=prediction)
    else:
        return render_template("formulaire.html")


@app.route("/plot")
def plot():
    # Define what this route does
    pass


if __name__ == "__main__":
    app.run(debug=True)
