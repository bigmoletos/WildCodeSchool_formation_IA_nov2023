import streamlit as st
import plotly.express as px
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title('Le Titanic')
st.write('Hello, world!')

# Chargement des données
titanic = sns.load_dataset("titanic").dropna()[
    ["sex", "survived", "class", "age"]]
titanic["sex"] = titanic["sex"].replace(["male", "female"], [0, 1])
titanic["class"] = titanic["class"].replace(
    ["First", "Second", "Third"], [1, 2, 3])

# Préparation des données
X = titanic.drop("survived", axis=1)
y = titanic["survived"]

# Création des ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Choix du modèle
rm = RandomForestClassifier()
rm.fit(X_train, y_train)

# Création de l'interface Streamlit
sexe = st.radio("Vous êtes un Homme ou une femme", ["Homme", "Femme"])
classe = st.radio("Quel classe avez-vous choisi pour voyager: 1, 2 ou 3", [1, 2, 3])
age = st.slider("Quel âge avez-vous ?", 1, 99)

# Prédiction
prediction = rm.predict([[sexe, classe, age]])
st.write(f"La prédiction est : {prediction}")

df = px.data.iris()
bar = px.bar(df, x='sepal_length')
st.plotly_chart(bar)
st.write(df)
