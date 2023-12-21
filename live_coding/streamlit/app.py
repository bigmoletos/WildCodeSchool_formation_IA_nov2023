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
# st.write(titanic)
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
classe = st.radio(
    "Quel classe avez-vous choisi pour voyager? 1, 2 ou 3", [1, 2, 3])
age = st.slider("Quel âge avez-vous ?", 1, 99)
st.text(f"D'aprés vos parametres: \nsexe : {        sexe}, \nclasse : {classe}, \nage : {age} ans")
# Prédiction
# Mapper le choix à une valeur numérique
sexe = 0 if sexe == "Homme" else 1
prediction = rm.predict([[sexe, classe, age]])
saisie_formulaire = [sexe, classe, age]
# score = rm.score(X_test, saisie_formulaire)
score = rm.score(X_test, y_test)
prediction = "Désolé mais vous avez trés peu de chance de survivre au naufrage" if prediction == 0 else "Bravo vous avez de grandes chances de survivre au naufrage"
st.text(f"La prédiction est : \n{ prediction}, \navec un pourcentage de {score*100:.2f}%")

st.write(titanic)

df = px.data.iris()
bar = px.bar(df, x='sepal_length')
st.plotly_chart(bar)
st.write(df)
