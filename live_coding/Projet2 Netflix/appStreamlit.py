import streamlit as st
import plotly as px
import pandas as pd
import joblib

df = pd.read_csv("dfFeatures.csv")
titresDeFilms = df.Series_Title.values
knn = joblib.load('recoNetflox.joblib')

st.title('Netflop')
st.image("https://hips.hearstapps.com/hmg-prod/images/netflix-1597403529.gif")

# affiche une boite de saise avec de l'auto completion sur tous les films!
film = st.selectbox(
    'Quel film as-tu vu récemment ?',
    titresDeFilms)

st.write("Film indiqué : ", film)

position = df[df.Series_Title == film].index[0]
distances, index = knn.kneighbors(df.drop("Series_Title", axis=1).values[position].reshape(1, -1))
recommandations = df.Series_Title.iloc[index[0]].values

for film in recommandations[1:6]:
    st.markdown("- " + film)

st.write("Bon visionnage 😎🍿🎬")