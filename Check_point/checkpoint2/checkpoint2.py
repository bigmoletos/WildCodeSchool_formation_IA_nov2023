# %% [markdown]
# # Import

# %%
import os
import io
import re
import nltk
import gzip
import spacy
import string
import random
import secrets
import datetime
import requests
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import svm
import plotly.io as pio
from sklearn import tree
from typing import Counter
import plotly.express as px
from fuzzywuzzy import fuzz
from joblib import dump, load
from bs4 import BeautifulSoup
import category_encoders as ce
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import plotly.graph_objects as go
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from textblob import TextBlob, Word
from scipy.cluster import hierarchy
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer
from sklearn.decomposition import PCA
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import silhouette_score
from sklearn.ensemble import IsolationForest
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import AgglomerativeClustering
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from scipy.spatial.distance import pdist, squareform
from textblob_fr import PatternTagger, PatternAnalyzer
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from flask import Flask, request, render_template, session, url_for, redirect
from sklearn.preprocessing import (MaxAbsScaler, MinMaxScaler, Normalizer,
                                   PowerTransformer, QuantileTransformer, RobustScaler, StandardScaler)
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, TargetEncoder


# %% [markdown]
# # Pandas
#
# Créer une dataframe via le lien suivant : http://bit.ly/imdbratings
#
# Répondre aux questions suivantes:
# - Quelle est la durée moyenne des films ayant le star_rating médian le plus bas de tous les genres ?
# - Quelle est la durée médiane des films policiers dont le contenu_rating est de R ?
# - Quels sont les 5 acteurs qui apparaissent le plus souvent ? Dans quels genres de film jouent-ils le plus souvent ?
# - Y a t'il une corrélation entre genre et le star_rating ? Démontrez le par un test statistique.
# - Y a t'il une corrélation entre les 15 acteurs les plus souvent présent et le star-rating ? Démontré le par un test statistique.
# - Transformez la colonne star_rating pour avoir un type int en arrondissant les données à l'entier le plus proche
# - Le star_rating et la duration sont-ils normalement distribués ? Démontrez le par un test statistique.

# %% [markdown]
# ### Chargement du dataset
#

# %%
df_original = pd.read_csv("imdb_1000.csv",  encoding="utf-8")
df = df_original.copy()
# Résumé des informations du dataframe
your_dataframe = df
print("#"+"#"*20)
print(f"====liste des colonnes numeriques====: \n{
      your_dataframe.select_dtypes(include=[np.number]).columns.tolist()}\n")
print("#"+"#"*20)
print(f"====liste des colonnes non numeriques====: \n{
      your_dataframe.select_dtypes(exclude=[np.number]).columns.tolist()} ")
print("#"+"#"*20)
print("#"+"-"*79)
print(f"\n====shape====: {your_dataframe.shape} \n====list columns==== :\n{      your_dataframe.columns.tolist()} ")
print(f"====Noms des colonnes avec au moins une valeur NA==== : {      your_dataframe.columns[your_dataframe.isna().any()].tolist()}")
print("#"+"#"*20)
print(f"====Nombre de lignes avec au moins une valeur NA==== : {      your_dataframe.isna().any(axis=1).sum()}")
print("#"+"#"*20)
print(f"====Colonne avec des na==== :{your_dataframe.isna().sum()} \n")
print("#"+"#"*20)
print(f"\ndf ====head==== :\n{your_dataframe.head(2)} \n")
print("#"+"#"*20)
print(f"\ndf ====describe==== :\n{your_dataframe.describe()} \n")
print("#"+"-"*79)
print("valeurs uniques des colonnes:")
for col in your_dataframe.columns:
    print("#"+"#"*20)
    print(f"====colonne====: {col} \n====nb valeur uniques====:{
          your_dataframe[col].nunique()} ")
    if your_dataframe[col].nunique() < 15:
        print(r", ".join(
            f"'{item}'" for item in your_dataframe[col].unique().tolist()))
    else:
        unique_values = your_dataframe[col].unique()[:15]
        print("====15 premiers====: \n" +
              ", ".join(f"'{item}'" for item in unique_values))
print("#"+"-"*79)


# %% [markdown]
# ### Quelle est la durée moyenne des films ayant le star_rating médian le plus bas de tous les genres ?
#

# %%
#  filtre les genres en fonction de la valeur mediane de leur notation
filtre_genre_star_rating_mediane = df.groupby('genre')['star_rating'].median().sort_values(ascending=True)
print(f"\n filtre les genres en fonction de la valeur mediane de leur notation:\n{ filtre_genre_star_rating_mediane} \n")
# extrait le genre ayant la valeur mediane la plus petite, On autrait aussi pu prendre la première valeur car le df est classé dans l'ordre croissant
minimum_filtre_genre_star_rating_mediane = filtre_genre_star_rating_mediane.idxmin()
print(f"\n genre ayant la valeur mediane la plus petitee:\n{ minimum_filtre_genre_star_rating_mediane} \n")
# Maintenant que l'on cconnait le genre ayant la valeur mediane des notation la plus faible on calcule la moyenne de la durée des films "thriller"
duree_moyenne_film_minimum_filtre_genre_star_rating_mediane = df[df['genre']
                                                                 == minimum_filtre_genre_star_rating_mediane]['duration'].mean()
print(f"\nLa durée moyenne des films ayant le star_rating médian le plus bas de tous les genres
      :\n{duree_moyenne_film_minimum_filtre_genre_star_rating_mediane} min dont le genre est '{minimum_filtre_genre_star_rating_mediane}'\n")


# %% [markdown]
# ### Quelle est la durée médiane des films policiers dont le contenu_rating est de R ?
#

# %%
#  On filtre les films policiers 'cirme'  ayant un 'content_rating" de R
filtre_film_policier_content_rating = df[(
    df['genre'] == 'Crime') & (df['content_rating'] == 'R')]
print(f"\nfiltre les films policiers 'cirme'  ayant un 'content_rating' de R :\n{
      filtre_film_policier_content_rating} \n")
# on prend la valeur méidane de la dureée 'duration'
durée_mediane = filtre_film_policier_content_rating['duration'].median()
print(f"\nDurée médiane des films policiers dont le contenu_rating est R :\n{
      durée_mediane} min \n")


# %% [markdown]
# ### Quels sont les 5 acteurs qui apparaissent le plus souvent ? Dans quels genres de film jouent-ils le plus souvent ?
#

# %%
# il faut extriare les acteurs de la liste actors_list et supprimer le u, les ' , les [] et splitter sur la virgule
liste_acteurs = df['actors_list'].apply(
    lambda x: x.strip("[]").replace('u', ''))
liste_acteurs = liste_acteurs.apply(lambda x: x.replace("'", "").split(", "))
liste_acteurs
# faire une colonne par nom d'acteur pour compter leur nom bre d'apparitions avec explode, noous avons aussi u probléme d'encodage qu'i lfaut traiter avec des caractéres comme \\xfc
explode_liste_acteurs = [acteur.encode("latin-1").decode("unicode_escape")
                         for ligne_acteurs in liste_acteurs for acteur in ligne_acteurs]
# liste_acteurs.split(", ")
explode_liste_acteurs
# On compte les 5 premiers nombre des valeurs uniques de la liste explode_liste_acteurs


def extract_liste_acteurs(liste_acteurs, nombre_acteurs):
    extract_liste_acteurs = Counter(liste_acteurs).most_common(nombre_acteurs)
    return extract_liste_acteurs


top_5_acteurs = extract_liste_acteurs(explode_liste_acteurs, 5)
print(f"\n top_5_acteurs:\n{top_5_acteurs} \n")


# faire le lien entre les acteurs et leur genre
genre_top5_acteurs = []
for acteur in top_5_acteurs:
    filtre_ligne = df['actors_list'].str.contains(acteur[0])
    genre = df[filtre_ligne]['genre'].mode()[0]
    genre_top5_acteurs.append((acteur[0], genre))

# top_5_actors_genres = {actor[0]: df[df['actors_list'].str.contains(actor[0])]['genre'].mode()[0] for actor in top_5_actors}
for i in genre_top5_acteurs:
    print(f"Acteur : {i[0]:->20}  Genre le plus courant :{"-"*10} {i[1]}")
# genre_top5_acteurs


# %%
def liste_categories_acteurs(extract_n_acteurs):
    # faire le lien entre les acteurs et leur genre
    liste_categories_acteurs = []
    for acteur in extract_n_acteurs:
        liste_items = []  # Réinitialiser liste_items pour chaque acteur
        for col in df.columns:
            if col in ('genre', 'star_rating'):
                # print(f"nom colonne:{col}  ")
                filtre_ligne = df['actors_list'].str.contains(acteur[0])
                mode = df[filtre_ligne][col].mode(dropna=True)
                if not mode.empty:
                    col_items = mode[0]
                else:
                    col_items = ""
                liste_items.append((col, col_items))
                # print(f"\nliste_items :{liste_items} ")
        liste_categories_acteurs.append((acteur[0], liste_items))
    return liste_categories_acteurs


# %% [markdown]
# ### Y a t'il une corrélation entre genre et le star_rating ? Démontrez le par un test statistique.
#

# %%
# listes colonnes
df_numeric = df.select_dtypes(include=['float64', 'int64'])
df_non_numeric = df.select_dtypes(exclude=['float64', 'int64'])

# convertion  colonne 'genre' en variables numériques
df_genre_dummies = pd.get_dummies(df['genre'])


# Concatenation des colonnes numériques avec les  colonnes converties avec dummies
df_numeric_dummies = pd.concat([df_numeric, df_genre_dummies], axis=1)

#  matrice de corrélation
corr_matrix_dummies = df_numeric_dummies.corr()

#  heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix_dummies, cmap="coolwarm")
plt.title(" matrice de corrélation avec dummies sur genre")
plt.show()


# %%
from scipy.stats import chi2_contingency
import numpy as np

# Créez une table de corrélation entre le genre et le star_rating
table_correlation = pd.crosstab(df['genre'], df['star_rating'])

# Calculez la statistique du Chi carré avec chi2_contingency
res = chi2_contingency(table_correlation)
print(f"\nres :\n{res} \n")
print(f"\nla correlation entre genre et star_rating est de p_value {
      res.pvalue:.2%} \n")

plt.figure(figsize=(6, 5))
sns.heatmap(table_correlation, cmap="coolwarm")
plt.title(" table de contingence ")
plt.show()


# %% [markdown]
# ### Y a t'il une corrélation entre les 15 acteurs les plus souvent présent et le star-rating ? Démontré le par un test statistique.
#

# %%
top_15_acteurs = extract_liste_acteurs(explode_liste_acteurs, 18)
# print(f"\ntop_15_acteurs :\n{top_15_acteurs} \n")
top15_acteur_items = liste_categories_acteurs(top_15_acteurs)
print(top15_acteur_items)


# %%
from scipy.stats import pearsonr
# top_15_actors = [actor[0] for actor in Counter(all_actors).most_common(15)]
top15_acteur_items

start_rating_par_acteur = [(acteur, attribut[1]) for acteur,
                           attributs in top15_acteur_items for attribut in attributs if attribut[0] == 'star_rating' and attribut[1]]
# print(f"\nstart_rating_par_acteur:\n{start_rating_par_acteur} \n")

# Calcul correlation
correlation_res = []
for actor, _ in start_rating_par_acteur:
    actor_ratings = df[df['actors_list'].str.contains(actor)]['star_rating']
    if len(actor_ratings) > 1:
        # corr, p_value = pearsonr(actor_ratings, actor_ratings)
        res = pearsonr(actor_ratings, actor_ratings)
        # correlation_results.append((actor, corr, p_value))
        correlation_res.append(
            (actor, round(res.statistic*100, 3), round(res.pvalue*100, 3)))
print(f"\ncorrelation_results :\n{correlation_res} \n")

# liste ety graphe
for acteur, stat, pvalue in correlation_res:
    print(f"acteur:{acteur:->20} : pvalue{"-"*20}= {pvalue}% \n")
    plt.scatter(acteur, pvalue)

plt.xlabel('Acteur')
plt.ylabel('Pvalue de corrélation de Pearson')
plt.title('Corrélation entre les 15 acteurs les plus cités et leur star_rating')
plt.xticks(rotation=45)
plt.show()


# %% [markdown]
# ### Transformez la colonne star_rating pour avoir un type int en arrondissant les données à l'entier le plus proche
#

# %%
# df['star_rating'] = df['star_rating'].astype(int)
df['star_rating_round'] = df['star_rating'].round().astype(int)
df['star_rating_round']


# %% [markdown]
# ###  Test de normalite. Le star_rating et la duration sont-ils normalement distribués ? Démontrez le par un test statistique.

# %%
import scipy.stats as stats

# Test de normalité pour 'star_rating'
stat, p_value_star_rating = stats.shapiro(df['star_rating_round'])
print(f"Statistique de test pour 'star_rating_round' : {
      stat:.2%}, p-value : {p_value_star_rating:.2%}\n")

if p < 0.05:
    print(f"\nstar_rating-round avec  p_value :{
          p_value_star_rating} aussi faible les données ne sont pas distribuées normalement")
else:
    print(f"\nstar_rating-round avec  p_value :{
          p_value_star_rating}  les données ne sont pas distribuées normalement")

# Test de normalité pour 'duration'
stat_duration, p_value_duration = stats.shapiro(df['duration'])
print(f"\nStatistique de test pour 'duration' : {
      stat_duration:.2%}, p-value : {p_value_duration:.2%}\n")

if p < 0.05:
    print(f"\nduration avec  p_value :\n{
          p_value_duration} aussi faible les données ne sont pas distribuées normalement\n")
else:
    print(f"\nduration avec  p_value :\n{
          p_value_duration}  les données ne sont pas distribuées normalement\n")


# %% [markdown]
# # Data visualisation
#
# Créer 5 graphiques en utilisant ce dataset > [Pokemon dataset](https://drive.google.com/file/d/116tn0wRma8wpELBAGzgcsHYPC9uUcgti/view):
# - Un camembert utilisant Matplotlib et une légende.
# - Un graphique linéaire utilisant Matplotlib avec une légende
# - Une heatmap utilisant Seaborn
# - Un boxplot utilisant seaborn
# - Un pairplot utilisant Seaborn

# %% [markdown]
# ### Chargement Dataframe et controle

# %%
df = pd.read_csv('pokemon.csv', sep=',',
                 index_col=False, encoding="ISO-8859-1")
df.drop('#', axis=1, inplace=True)
df


# %% [markdown]
# ### camembert utilisant Matplotlib et une légende

# %%
# figsize = (5, 5)
# fig = plot.pie(df, values='speed', names='type 1')
# fig = dtypes.value_counts().plot.pie()
# fig.show()
plt.figure(figsize=(10, 5))
df['Type 2'].value_counts().plot.pie()
plt.title('types 2 de Pokémon')
plt.legend()
plt.show()


# %% [markdown]
# ### graphique linéaire utilisant Matplotlib avec une légende
#

# %%
# ['Name', 'Type 1', 'Type 2', 'Legendary']
# ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']
df['Speed'].plot()
# plt.figure(figsize=(6,6))
plt.title('Vitesse des Pokémons')
plt.xlabel('Vitesse')
plt.ylabel('Nombre de Pokémons')
plt.legend(['Speed'])
plt.show()


# %% [markdown]
# ### heatmap utilisant Seaborn

# %%
# ['Name', 'Type 1', 'Type 2', 'Legendary']
# ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']
plt.figure(figsize=(20, 6))
sns.heatmap(df[['HP', 'Attack', 'Defense']], annot=True, cmap='coolwarm')
plt.title('Caractérisques  Pokémons')
plt.show()


# %% [markdown]
# ### boxplot utilisant seaborn

# %%
# ['Name', 'Type 1', 'Type 2', 'Legendary']
# ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['HP', 'Attack', 'Defense',
            'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']])
plt.title('Distribution des attaques, défenses et vitesses des Pokémon')
plt.show()


# %% [markdown]
# ### pairplot utilisant Seaborn

# %%
# ['Name', 'Type 1', 'Type 2', 'Legendary']
# ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']
sns.pairplot(df[['HP', 'Attack', 'Defense', 'Sp. Atk',
             'Sp. Def', 'Speed', 'Generation']])
plt.show()


# %% [markdown]
# # Fonction IA
#
# Créer une fonction prendra en paramètre un dataset, de choisir une ou plusieurs colonnes de features et une colonne de target, de choisir une tâche parmi **régression** (4 algorithmes différents), **classification** (4 algorithmes différents) et **clustering** (2 algorithmes différents), et enfin de faire une prédiction et d'observer les performances des modèles avec au moins 3 métriques. On pourra récupérer le modèle le plus performant ou tous les modèles. Il sera possible de les exporter via joblib ou pickle.
#
# La fonction nous permettra également de faire de la réduction de dimension (1 algorithme) avant de lancer un modèle en indiquant un taux de variance expliqué précis, de reshape les données pour que l'entrainement fonctionne, et de connaitre les meilleurs hyperparamètres via grid search.
#
# Il faut par contre que les données du dataset soient complètent et dans le bon type.

# %% [markdown]
# ## Choix dataset
#

# %%
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display
# crée la liste des datasets seaborn


def list_datasets_seaborn():
    datasets_seaborn = sns.get_dataset_names()
    return datasets_seaborn


# liste déroulante avec widget
liste_deroulante = widgets.Dropdown(
    options=list_datasets_seaborn(),
    description='Datasets      :',
)
display(liste_deroulante)

# Charger le dataset sélectionné


def charge_dataset(b):
    global df_original
    datasets_seaborn = list_datasets_seaborn()
    print(f"\n datasets_seaborn:\n{datasets_seaborn} \n")
    if liste_deroulante.value in datasets_seaborn:
        # Charger le dataset dans df
        df_original = sns.load_dataset(liste_deroulante.value)
        print(df_original.head())
    else:
        print("Le dataset demandé n'est pas disponible.")


# Bouton pour charger le dataset
bouton_chargment = widgets.Button(description="Charger le dataset")
bouton_chargment.on_click(charge_dataset)
display(bouton_chargment)
df_original


# %%
df = df_original.copy()
df


# %% [markdown]
# ## Analyse du dataset et classification automatique

# %%
import pandas as pd
import numpy as np


def determine_dataset_type(dataset):
    # Vérifie si le dataset est un DataFrame pandas (données structurées)
    if isinstance(dataset, pd.DataFrame):
        # Vérifie la présence de colonnes temporelles
        if any(pd.api.types.is_datetime64_any_dtype(dataset[col]) for col in dataset.columns):
            return "Time Series (Temporal Data)"
        # Vérifie la présence de colonnes spatiales (latitude/longitude)
        if 'latitude' in dataset.columns and 'longitude' in dataset.columns:
            return "Spatial Data"
        return "Structured Data"

    # Vérifie si le dataset est une série de textes ou de fichiers (données non structurées)
    if isinstance(dataset, (list, pd.Series)) and all(isinstance(x, str) for x in dataset):
        return "Unstructured Data (Text or Files)"

    # Vérifie si le dataset est sous forme de dictionnaires ou de JSON (semi-structuré)
    if isinstance(dataset, (dict, list)) and all(isinstance(x, (dict, list)) for x in dataset):
        return "Semi-Structured Data (e.g., JSON)"

    return "Unknown Type"


type_dataset = determine_dataset_type(df)

print(f"\ntype du dataset :\n{type_dataset} \n")


# %%
# Résumé des informations du dataframe
your_dataframe = df
print("#"+"-"*79)
print(f"\n====shape====: {your_dataframe.shape} \n====list columns==== :\n{      your_dataframe.columns.tolist()} ")
print("#"+"#"*20)
print(f"====liste des colonnes numeriques====: \n{      your_dataframe.select_dtypes(include=[np.number]).columns.tolist()}\n")
print("#"+"#"*20)
print(f"====liste des colonnes non numeriques====: \n{      your_dataframe.select_dtypes(exclude=[np.number]).columns.tolist()} ")
print("#"+"#"*20)
print("valeurs uniques des colonnes:")
for col in your_dataframe.columns:
    print("#"+"#"*20)
    print(f"====colonne====: {col} \n====nb valeur uniques====:{          your_dataframe[col].nunique()} ")
    if your_dataframe[col].nunique() < 15:
        print(r", ".join(
            f"'{item}'" for item in your_dataframe[col].unique().tolist()))
    else:
        unique_values = your_dataframe[col].unique()[:15]
        print("====15 premiers====: \n" +
              ", ".join(f"'{item}'" for item in unique_values))
print("#"+"-"*79)
print(f"====Noms des colonnes avec au moins une valeur NA==== : {
      your_dataframe.columns[your_dataframe.isna().any()].tolist()}")
print("#"+"#"*20)
print(f"====Nombre de lignes avec au moins une valeur NA==== : {
      your_dataframe.isna().any(axis=1).sum()}")
print("#"+"#"*20)
print(f"====Colonne avec des na==== :{your_dataframe.isna().sum()} \n")
print("#"+"#"*20)
print(f"\ndf ====head==== :\n{your_dataframe.head(2)} \n")
print("#"+"#"*20)
print(f"\ndf ====describe==== :\n{your_dataframe.describe()} \n")
print("#"+"-"*79)


# %% [markdown]
# ## Preprocessing des datasets
# ### Preprocessing pour les Données structurées

# %%
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def preprocess_structured_data(dataset):
    # Séparer les colonnes numériques et catégorielles
    numeric_cols = dataset.select_dtypes(include=[np.number]).columns
    categorical_cols = dataset.select_dtypes(exclude=[np.number]).columns

    # Imputation
    num_imputer = SimpleImputer(strategy='mean')
    cat_imputer = SimpleImputer(strategy='most_frequent')

    dataset[numeric_cols] = num_imputer.fit_transform(dataset[numeric_cols])
    dataset[categorical_cols] = cat_imputer.fit_transform(
        dataset[categorical_cols])

    # Normalisation pour les données numériques
    scaler = StandardScaler()
    dataset[numeric_cols] = pd.DataFrame(scaler.fit_transform(
        dataset[numeric_cols]), columns=numeric_cols)

    # Encodage One-Hot pour les données catégorielles
    encoder = OneHotEncoder()
    encoded_cat = encoder.fit_transform(dataset[categorical_cols]).toarray()
    encoded_cat_df = pd.DataFrame(
        encoded_cat, columns=encoder.get_feature_names_out(categorical_cols))

    # Concaténer les données numériques et catégorielles traitées
    dataset_preprocessed = pd.concat(
        [dataset[numeric_cols], encoded_cat_df], axis=1)

    return dataset_preprocessed


# %% [markdown]
# ### Preprocessing pour les Données non structurées

# %%
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_unstructured_data(dataset):
    # Prétraitement pour les données textuelles non structurées
    vectorizer = TfidfVectorizer(stop_words='english')
    dataset = vectorizer.fit_transform(dataset)
    return dataset


# %% [markdown]
# ### Preprocessing pour les Données de type times series

# %%
def preprocess_temporal_data(dataset):
    # Prétraitement pour les données temporelles
    dataset.fillna(method='ffill', inplace=True)
    return dataset


# %% [markdown]
# ### Preprocessing pour les Données Spatiales

# %%
from sklearn.preprocessing import MinMaxScaler


def preprocess_spatial_data(dataset):
    # Supposons que dataset est un DataFrame avec des colonnes 'latitude' et 'longitude'
    scaler = MinMaxScaler()
    dataset[['latitude', 'longitude']] = scaler.fit_transform(
        dataset[['latitude', 'longitude']])

    # Calcul d'une caractéristique dérivée, par exemple, la distance depuis le centre-ville
    city_center = (48.8566, 2.3522)  # Coordonnées de Paris, par exemple
    dataset['distance_from_center'] = np.sqrt(
        (dataset['latitude'] - city_center[0])**2 + (dataset['longitude'] - city_center[1])**2)

    return dataset


# Exemple d'utilisation
spatial_data = pd.DataFrame({
    'latitude': np.random.uniform(48.8, 48.9, 100),
    'longitude': np.random.uniform(2.3, 2.4, 100)
})
preprocessed_spatial_data = preprocess_spatial_data(spatial_data)


# %% [markdown]
# ### preprocessing pour les Données Semi-Structurées (JSON)

# %%
import json
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def preprocess_json_data(json_data):
    # Convertir le JSON en DataFrame
    dataset = pd.json_normalize(json_data)

    # Gérer les valeurs manquantes
    imputer = SimpleImputer(strategy='most_frequent')
    dataset = pd.DataFrame(imputer.fit_transform(
        dataset), columns=dataset.columns)

    # Encoder les variables catégorielles
    encoder = OneHotEncoder()
    encoded_columns = encoder.fit_transform(dataset[['interests']]).toarray()
    dataset = dataset.join(pd.DataFrame(
        encoded_columns, columns=encoder.get_feature_names_out(['interests'])))

    return dataset


# Exemple d'utilisation
json_data = [
    {"name": "Alice", "age": 30, "interests": "music"},
    {"name": "Bob", "age": 25, "interests": "sports"},
    # ... autres données
]
preprocessed_json_data = preprocess_json_data(json_data)


# %% [markdown]
# ### Fonction globale de preprocessing

# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import datetime


def preprocess_dataset(dataset):
    dataset_type = determine_dataset_type(dataset)

    if dataset_type == "Structured Data":
        dataset_preprocessed = preprocess_structured_data(dataset)
        return dataset_preprocessed

    elif dataset_type == "Unstructured Data (Text or Files)":
        dataset_preprocessed = preprocess_unstructured_data(dataset)
        return dataset_preprocessed

    elif dataset_type == "Time Series (Temporal Data)":
        dataset_preprocessed = preprocess_temporal_data(dataset)
        return dataset_preprocessed

    elif dataset_type == "Spatial Data":
        dataset_preprocessed = preprocess_spatial_data(dataset)
        return dataset_preprocessed

    elif dataset_type == "Semi-Structured Data (e.g., JSON)":
        dataset_preprocessed = preprocess_json_data(dataset)
        return dataset_preprocessed

    else:
        raise ValueError(
            "Type de dataset non reconnu ou non pris en charge pour le prétraitement")

    return dataset_preprocessed


# %%
df_pre = preprocess_dataset(df)
df_pre


# %% [markdown]
# ## Fonctions Machine learning

# %%
['regression',
 'classification',
 'clustering']


# %%
import joblib
import numpy as np
import seaborn as sns
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans, DBSCAN
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.metrics import accuracy_score, mean_squared_error, f1_score, precision_score, silhouette_score


def entrainer_et_evaluer_modeles(donnees, colonnes_features, colonne_cible, tache, choix_modele):
    """
    Entrainer et évaluer des modèles de machine learning en fonction de la tâche et du choix du modèle.

    :param donnees: DataFrame - le dataset à utiliser
    :param colonnes_features: list - liste des noms de colonnes à utiliser comme features
    :param colonne_cible: str - nom de la colonne cible pour la prédiction
    :param tache: str - type de tâche ('regression', 'classification', 'clustering')
    :param choix_modele: str - choix du modèle
    :return: dict - dictionnaire contenant les résultats d'évaluation pour le modèle choisi
    """
    # Séparer les features et la cible
    X = donnees[colonnes_features]
    y = donnees[colonne_cible]


    # Division des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Sélectionner le modèle et les hyperparamètres en fonction de la tâche et du choix de modèle
    modele, parametres = selectionner_modele_et_hyperparametres(tache, choix_modele)

    # Création du pipeline avec ACP
    pipeline = Pipeline([
        ('scaling', StandardScaler()),
        ('pca', PCA()),
        ('clf', modele)
    ])

    if tache != 'clustering':
            grid_search = GridSearchCV(pipeline, parametres, cv=5)
            grid_search.fit(X_train, y_train)
            print(f"Meilleurs paramètres {"-"*50}: {grid_search.best_params_}")
            print(f"Meilleur score (train) {"-"*50}: {grid_search.best_score_:.2%}")
            meilleur_modele = grid_search.best_estimator_
            score_test = meilleur_modele.score(X_test, y_test)
            print(f"Score sur l'ensemble de test {"-"*50}: {score_test:.2%}")
            return grid_search.best_score_, grid_search.best_params_, meilleur_modele
    else:
       modele.fit(X_train)
       labels = modele.labels_ if hasattr(modele, 'labels_') else None

        # Vérifier que le nombre de clusters est approprié
       if labels is not None and len(set(labels)) > 1 and len(set(labels)) < len(X_train):
           score = silhouette_score(X_train, labels)
           print(f"Score de silhouette {"-"*50}: {score:.2%}")
       else:
           score = None
           print("Score de silhouette non calculable.")
       return score, None, modele


def selectionner_modele_et_hyperparametres(tache, choix_modele):
    modeles = {
        'regression': {
            'RegressionLineaire': LinearRegression(),
            'Ridge': Ridge(),
            'Lasso': Lasso(),
            'SVR': SVR()
        },
        'classification': {
            'RegressionLogistique': LogisticRegression(),
            'KNN': KNeighborsClassifier(),
            'ArbreDecision': DecisionTreeClassifier(),
            'ForetAleatoire': RandomForestClassifier()
        },
        'clustering': {
            'KMeans': KMeans(),
            'DBSCAN': DBSCAN()
        }
    }

    hyperparametres = {
        'RegressionLineaire': {'pca__n_components': [2, 3, 4, 5]},
        'Ridge': {'pca__n_components': [2, 3, 4, 5], 'clf__alpha': [0.01, 0.1, 1, 10]},
        'Lasso': {'pca__n_components': [2, 3, 4, 5], 'clf__alpha': [0.01, 0.1, 1, 10]},
        'SVR': {'pca__n_components': [2, 3, 4, 5], 'clf__C': [0.1, 1, 10, 100], 'clf__gamma': [0.01, 0.1, 1]},
        'RegressionLogistique': {'pca__n_components': [2, 3, 4, 5], 'clf__C': [0.1, 1, 10, 100], 'clf__max_iter': [1000]},
        'KNN': {'pca__n_components': [2, 3, 4, 5], 'clf__n_neighbors': [3, 5, 7, 9]},
        'ArbreDecision': {'pca__n_components': [2, 3, 4, 5], 'clf__max_depth': [None, 10, 20, 30]},
        'ForetAleatoire': {'pca__n_components': [2, 3, 4, 5], 'clf__n_estimators': [50, 100, 200], 'clf__max_depth': [None, 10, 20, 30]},
        'KMeans': {'pca__n_components': [2, 3, 4, 5], 'clf__n_clusters': [2, 3, 4, 5], 'clf__n_init': [10]},
        'DBSCAN': {'pca__n_components': [2, 3, 4, 5], 'clf__eps': [0.1, 0.2, 0.5], 'clf__min_samples': [5, 10, 15]}
    }

    if choix_modele in modeles[tache]:
        modele = modeles[tache][choix_modele]
        parametres = hyperparametres[choix_modele]
    else:
        raise ValueError(
            "Combinaison de tâche et de modèle non prise en charge")

    return modele, parametres


# %% [markdown]
# ### Préparation dataset
#

# %%
import seaborn as sns
import pandas as pd
import numpy as np

# Résumé des informations du dataframe
# ====shape====: (344, 7)
# ====list columns==== :
# ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
# #####################
# ====liste des colonnes numeriques====:
# ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

# #####################
# ====liste des colonnes non numeriques====:
# ['species', 'island', 'sex']

# Chargement du dataset des pingouins
donnees_pingouins = sns.load_dataset('penguins')

# Nettoyage et prétraitement des données (suppression des valeurs NA et encodage des variables catégorielles)
donnees_pingouins.dropna(inplace=True)
donnees_pretraitees = pd.get_dummies(donnees_pingouins)

# Sélection des colonnes de features et de la colonne cible
colonnes_features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g',
                     'island_Biscoe', 'island_Dream', 'island_Torgersen', 'sex_Female', 'sex_Male']
colonne_cible = 'species_Adelie'


# %% [markdown]
# ### Preparation input pour choix de l'affichage

# %% [markdown]
# ajout choix optionnel

# %%
def afficher_menu_et_choisir_modele(tache_choix=None, modele_choix=None):
    taches = {
        '1': 'regression',
        '2': 'classification',
        '3': 'clustering'
    }
    modeles_par_tache = {
        'regression': {
            '1': 'RegressionLineaire',
            '2': 'Ridge',
            '3': 'Lasso',
            '4': 'SVR'
        },
        'classification': {
            '1': 'RegressionLogistique',
            '2': 'KNN',
            '3': 'ArbreDecision',
            '4': 'ForetAleatoire'
        },
        'clustering': {
            '1': 'KMeans',
            '2': 'DBSCAN'
        }
    }

    if not tache_choix:
        print("Choisissez le type de tâche:")
        for k, v in taches.items():
            print(f"{k}. {v}")
        tache_choix = input("Entrez le numéro de la tâche: ")

    tache = taches.get(tache_choix)

    if tache:
        if not modele_choix:
            print(f"Choisissez un modèle pour {tache}:")
            for k, v in modeles_par_tache[tache].items():
                print(f"{k}. {v}")
            modele_choix = input("Entrez le numéro du modèle: ")

        modele = modeles_par_tache[tache].get(modele_choix)

        return tache, modele
    else:
        print("Choix de tâche non valide.")
        return None, None


# %%
from joblib import dump

# Fonction pour sauvegarder le modèle entraîné
def sauvegarder_modele(modele, chemin_fichier):
    """
    Sauvegarde le modèle entraîné dans le chemin spécifié.

    :param modele: modèle scikit-learn entraîné
    :param chemin_fichier: chemin vers le fichier où le modèle sera sauvegardé
    """
    dump(modele, chemin_fichier)
    print(f"Modèle sauvegardé à l'emplacement : {chemin_fichier}")


# %% [markdown]
# ### Test via le menu input
#

# %%
# Exécution du menu et de la fonction d'entraînement
tache_choisie, modele_choisi = afficher_menu_et_choisir_modele()
if modele_choisi:
    entrainer_et_evaluer_modeles(
        donnees_pretraitees, colonnes_features, colonne_cible, tache_choisie, modele_choisi)


# %% [markdown]
# ### Teste de toutes les possibilités:

# %%
# Test de toutes les possibilités

meilleur_score = -np.inf
meilleure_combinaison = None
meilleurs_hyperparametres = None

for tache in ['1', '2', '3']:
    for modele in ['1', '2', '3', '4']:
        tache_choisie, modele_choisi = afficher_menu_et_choisir_modele(tache, modele)
        if modele_choisi:
            print(f"Test avec tâche {tache_choisie} et modèle {modele_choisi}")
            score, hyperparametres, _ = entrainer_et_evaluer_modeles(
                donnees_pretraitees, colonnes_features, colonne_cible, tache_choisie, modele_choisi)
            if score is not None and score > meilleur_score:
                meilleur_score = score
                meilleure_combinaison = (tache_choisie, modele_choisi)
                meilleurs_hyperparametres = hyperparametres

# Afficher la meilleure combinaison et les hyperparamètres correspondants
print(f"Meilleure combinaison: Tâche {meilleure_combinaison[0]}, Modèle {meilleure_combinaison[1]}")
print(f"Meilleurs hyperparamètres: {meilleurs_hyperparametres}")
print(f"Meilleur score: {meilleur_score}")



# %%
# Résumé des informations du dataframe
your_dataframe = df_pre
print("#"+"-"*79)
print(f"\n====shape====: {your_dataframe.shape} \n====list columns==== :\n{      your_dataframe.columns.tolist()} ")
print("#"+"#"*20)
print(f"====liste des colonnes numeriques====: \n{      your_dataframe.select_dtypes(include=[np.number]).columns.tolist()}\n")
print("#"+"#"*20)
print(f"====liste des colonnes non numeriques====: \n{      your_dataframe.select_dtypes(exclude=[np.number]).columns.tolist()} ")
print("#"+"#"*20)
print(f"====Noms des colonnes avec au moins une valeur NA==== : {      your_dataframe.columns[your_dataframe.isna().any()].tolist()}")
print("#"+"#"*20)
print(f"====Nombre de lignes avec au moins une valeur NA==== : {      your_dataframe.isna().any(axis=1).sum()}")
print("valeurs uniques des colonnes:")
for col in your_dataframe.columns:
    print("#"+"#"*20)
    print(f"====colonne====: {col} \n====nb valeur uniques====:{          your_dataframe[col].nunique()} ")
    if your_dataframe[col].nunique() < 15:
        print(r", ".join(
            f"'{item}'" for item in your_dataframe[col].unique().tolist()))
    else:
        unique_values = your_dataframe[col].unique()[:15]
        print("====15 premiers====: \n" +
              ", ".join(f"'{item}'" for item in unique_values))
print("#"+"-"*79)
print("#"+"#"*20)
print(f"====Colonne avec des na==== :{your_dataframe.isna().sum()} \n")
print("#"+"#"*20)
print(f"\ndf ====head==== :\n{your_dataframe.head(2)} \n")
print("#"+"#"*20)
print(f"\ndf ====describe==== :\n{your_dataframe.describe()} \n")
print("#"+"-"*79)


# %% [markdown]
# ## Graphiques
# ### Exploration des Données
#

# %% [markdown]
# Histogrammes (pour bill_length_mm,

# %%
plt.figure(figsize=(8, 4))
sns.histplot(donnees_pingouins['bill_length_mm'], kde=True)
plt.title('Histogramme de Longueur du Bec')
plt.show()


# %% [markdown]
# Boxplots (pour bill_depth_mm,

# %%
plt.figure(figsize=(8, 4))
sns.boxplot(x=donnees_pingouins['bill_depth_mm'])
plt.title('Boxplot de Profondeur du Bec')
plt.show()


# %% [markdown]
# Graphes à Barres

# %%
plt.figure(figsize=(8, 4))
sns.countplot(x=donnees_pingouins['species'])
plt.title('Distribution des Espèces de Pingouins')
plt.show()


# %% [markdown]
# Graphes de Dispersion (pour bill_length_mm et flipper_length_mm)

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', hue='species', data=donnees_pingouins)
plt.title('Scatter Plot entre Longueur du Bec et Longueur de l’Aileron')
plt.show()


# %% [markdown]
# ### Évaluation des Modèles

# %%
conf_mat = confusion_matrix(y_test, predictions)
sns.heatmap(conf_mat, annot=True, fmt='d')
plt.title('Matrice de Confusion')
plt.ylabel('Vérité')
plt.xlabel('Prédiction')
plt.show()



# %% [markdown]
# ### Résultats des Modèles de Clustering

# %%

plt.figure(figsize=(8, 6))
sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', hue=kmeans.labels_, data=donnees_pingouins)
plt.title('Clusters de Pingouins par KMeans')
plt.show()


# %%


# %% [markdown]
# ###  Analyse en Composantes Principales (ACP)

# %% [markdown]
# Variance Expliquée par les Composantes (après l'ajustement de PCA sur les données)

# %%
import matplotlib.pyplot as plt

def plot_pca_variance(pca):
    plt.figure(figsize=(8, 4))
    plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_)
    plt.ylabel('Variance expliquée')
    plt.xlabel('Composantes principales')
    plt.plot(range(1, len(pca.explained_variance_ratio_) + 1),
             np.cumsum(pca.explained_variance_ratio_),
             c='red',
             label="Cumul de la variance expliquée")
    plt.legend(loc='upper left')
    plt.show()


# %%
donnees_pingouins.select_dtypes('float64','int64')


# %%
donnees_pingouins.select_dtypes('object')


# %%
# Histogramme
plt.figure(figsize=(8, 4))
sns.histplot(donnees_pingouins.select_dtypes('float64','int64'), kde=True)
plt.title('Histogramme de var_numerique')
plt.show()

# Boxplot
plt.figure(figsize=(8, 4))
sns.boxplot(donnees_pingouins.select_dtypes('float64','int64'))
plt.title('Boxplot de var_numerique')
plt.show()


# %% [markdown]
# Graphes de Dispersion

# %%
plt.figure(figsize=(8, 6))
sns.scatterplot(x='species', y='bill_length_mm', data=donnees_pingouins)
plt.title('Scatter Plot ')
plt.show()


# %% [markdown]
# Graphes de Corrélation

# %%
corr_matrix = donnees_pingouins.select_dtypes('float64','int64').corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap de Corrélation')
plt.show()


# %%
from sklearn.metrics import roc_curve, auc

# Calcul des taux de vrais positifs et faux positifs
fpr, tpr, seuils = roc_curve(y_test, predictions_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taux de Faux Positif')
plt.ylabel('Taux de Vrais Positif')
plt.title('Courbe ROC')
plt.legend(loc="lower right")
plt.show()


# %% [markdown]
# ## Fonction graphique globale

# %%
def generer_graphiques(donnees, X_train, y_train, modele, tache, choix_modele):
    # Sous-fonction pour afficher les histogrammes
    def afficher_histogrammes():
        for colonne in donnees.select_dtypes(include='number').columns:
            sns.histplot(donnees[colonne], kde=True)
            plt.title(f'Histogramme de {colonne}')
            plt.show()

    # Sous-fonction pour afficher les boxplots
    def afficher_boxplots():
        for colonne in donnees.select_dtypes(include='number').columns:
            sns.boxplot(x=donnees[colonne])
            plt.title(f'Boxplot de {colonne}')
            plt.show()

    # Sous-fonction pour afficher la variance expliquée par PCA (si PCA est utilisé)
    def afficher_variance_pca():
        if 'pca' in [step[0] for step in modele.steps]:
            pca = modele.named_steps['pca']
            plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_)
            plt.plot(range(1, len(pca.explained_variance_ratio_) + 1),
                     np.cumsum(pca.explained_variance_ratio_),
                     c='red',
                     label="Cumul de la variance expliquée")
            plt.xlabel('Composantes principales')
            plt.ylabel('Variance expliquée')
            plt.title('Variance Expliquée par les Composantes PCA')
            plt.legend(loc='upper left')
            plt.show()

    # Sous-fonction pour afficher les clusters (si un modèle de clustering est utilisé)
    def afficher_clusters():
        if tache == 'clustering':
            labels = modele.named_steps['clf'].labels_
            sns.scatterplot(x=X_train['bill_length_mm'], y=X_train['flipper_length_mm'], hue=labels)
            plt.title('Clusters des Pingouins')
            plt.show()

    # Appeler les sous-fonctions en fonction de la tâche et du modèle
    if tache in ['regression', 'classification']:
        afficher_histogrammes()
        afficher_boxplots()
        afficher_variance_pca()
    elif tache == 'clustering':
        afficher_clusters()


# %% [markdown]
# ### Teste toutes les possiblités et sort les graphes

# %%
def tester_et_visualiser_modeles(donnees, colonnes_features, colonne_cible):
    meilleur_score = -np.inf
    meilleure_combinaison = None
    meilleurs_hyperparametres = None
    meilleur_modele = None
    X_train_meilleur = None
    y_train_meilleur = None

    for tache in ['1', '2', '3']:
        for modele in ['1', '2', '3', '4']:
            tache_choisie, modele_choisi = afficher_menu_et_choisir_modele(tache, modele)
            if modele_choisi:
                print(f"Test avec tâche {tache_choisie} et modèle {modele_choisi}")
                score, hyperparametres, modele_entraine = entrainer_et_evaluer_modeles(
                    donnees, colonnes_features, colonne_cible, tache_choisie, modele_choisi)
                if score is not None and score > meilleur_score:
                    meilleur_score = score
                    meilleure_combinaison = (tache_choisie, modele_choisi)
                    meilleurs_hyperparametres = hyperparametres
                    meilleur_modele = modele_entraine
                    X_train_meilleur, X_test, y_train_meilleur, y_test = train_test_split(donnees[colonnes_features], donnees[colonne_cible], test_size=0.2)

    # Affichage des résultats
    print(f"Meilleure combinaison: Tâche {meilleure_combinaison[0]}, Modèle {meilleure_combinaison[1]}")
    print(f"Meilleurs hyperparamètres: {meilleurs_hyperparametres}")
    print(f"Meilleur score: {meilleur_score}")

    # Générer des graphiques pour la meilleure combinaison
    if meilleur_modele:
        generer_graphiques(donnees, X_train_meilleur, y_train_meilleur, meilleur_modele, meilleure_combinaison[0], meilleure_combinaison[1])

# Appel de la fonction avec les données
tester_et_visualiser_modeles(donnees_pretraitees, colonnes_features, colonne_cible)


# %% [markdown]
# ## Generalisation à n'importe quel dataset

# %% [markdown]
#


