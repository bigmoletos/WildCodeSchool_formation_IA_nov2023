import streamlit as st
import plotly.express as px
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

df = px.data.iris()

bar = px.bar(df.sepal_length)

titanic = sns.load_dataset("titanic").dropna()[["sex", "survived","class", "age"]]
titanic.sex = titanic.sex.replace(["male", "female"], [0, 1])
titanic["class"] = titanic["class"].replace(["First", "Second", "Third"], [1, 2, 3])


X = titanic.drop("survived", axis=1).values
y = titanic.survived.values

st.write(bar)
st.write(titanic)
st.write("Hello world !")

sexe = st.radio("Homme ou Femme ?",
                ["Homme", "Femme"])
if sexe == "Homme":
    sexe = 0
else:
    sexe = 1

classe = st.radio("1, 2 ou 3 ?",
                [1, 2, 3])

age = st.select_slider("Quel age as tu ?",
                range(1, 99))

#st.write(type(classe))


rm = RandomForestClassifier()
rm.fit(X, y)

st.write(f"Prédiction : {rm.predict([[sexe, age, classe]])}")

