# %% [markdown]
# IMPORT THE BASIC LIBRARIES YOU THINK YOU WILL USE

# %%
import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
from datetime import datetime


# %% [markdown]
# The goal of this Quest is to do a one step ahead forecast of the Miles Traveled data.
# ## Data
#
# Info about this data set: https://fred.stlouisfed.org/series/TRFVOLUSM227NFWA
#
# Read in the data set "Miles_Traveled.csv". Figure out how to set the date to a datetime index columns

# %%
import requests
import os
import pandas as pd


def telecharger_et_charger_fichier(url, dossier_destination=None):
    """
    Télécharge un fichier depuis une URL donnée, le sauvegarde dans un dossier spécifié,
    Si le dossier n'existe pas il est crée
    Par defaut enregistre le fichier dans un repertoire ../datas qui est à la racine du projet
    et charge le fichier dans un DataFrame en fonction de son format.

    :param url: URL du fichier à télécharger.
    :param dossier_destination: Dossier de destination optionnel pour le fichier.
    :return: Tuple contenant le DataFrame original, sa copie, et le nom du fichier.
    """
    # Initialiser df_original et df à None
    df_original, df = None, None
    try:
        # Déterminer le nom du fichier à partir de l'URL
        nom_fichier = url.split('/')[-1]

        # Construire le chemin absolu du dossier de destination
        if dossier_destination is None:
            # Chemin par défaut relatif au script
            chemin_script = os.path.dirname(os.path.abspath(__file__))
            chemin_complet = os.path.join(
                chemin_script, "..", "datas", nom_fichier)
        else:
            # Utiliser le chemin de destination fourni
            chemin_complet = os.path.join(dossier_destination, nom_fichier)

        # Créer le dossier de destination s'il n'existe pas
        os.makedirs(os.path.dirname(chemin_complet), exist_ok=True)

        # Télécharger le fichier
        response = requests.get(url)
        response.raise_for_status()

        # Écrire le contenu dans le fichier de destination
        with open(chemin_complet, 'wb') as file:
            file.write(response.content)

        # Déterminer l'extension du fichier et charger dans un DataFrame
        extension = nom_fichier.split('.')[-1].lower()
        if extension in ['csv', 'txt']:
            df_original = pd.read_csv(chemin_complet, encoding='utf-8')
        elif extension == 'json':
            df_original = pd.read_json(
                chemin_complet, encoding='utf-8', orient='records')
        elif extension == 'xlsx':
            df_original = pd.read_excel(chemin_complet, index_col=0)
        else:
            print(f"Format de fichier non pris en charge : {extension}")

        # Faire une copie du DataFrame si celui-ci a été chargé
        if df_original is not None:
            df = df_original.copy()

        return df_original, df, chemin_complet

    except requests.HTTPError as http_err:
        print(f"Erreur HTTP lors du téléchargement du fichier : {http_err}")
        return None, None, None
    except Exception as err:
        print(
            f"Une erreur est survenue lors du téléchargement du fichier : {err}")
        return None, None, None


# %%
%%time
# Chargement du df
url="https://raw.githubusercontent.com/crajapax/GDAtrack3b/main/Miles_Traveled.csv"
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
# df_original, df, nom_fichier = telecharger_et_charger_csv(url)
df_original, df, nom_fichier = telecharger_et_charger_fichier( url, "datas/csv")


# %%
# fichier déja enrefistré suer le disque
df_original = pd.read_csv('Miles_Traveled.csv')


# %%
df = df_original.copy()


# %%
df


# %%
# pd.read_csv(path, encoding='utf-8')
# Convertir l'index en datetime si ce n'est pas déjà le cas
df["DATE"] = pd.to_datetime(df['DATE'])


# %%
#  colonne date en index
df.set_index('DATE', inplace=True)


# %%
df.describe


# %%
df.index


# %%
# data = pd.read_csv(path)
# set the date as the index of our dataframe, ie. each of our datapoints correspond to a date
# df.set_index('DATE',parse_dates=True)
# df=data.copy()
# df.index.reset_index()
# df.index=df.index.freq('MS')

df.index.asfreq = 'MS'


# %%
df


# %% [markdown]
# **Task: Change the column names to Value**

# %%
# CODE HERE
df.rename(columns={'TRFVOLUSM227NFWA': 'Value'}, inplace=True)
df


# %%


# %% [markdown]
# **TASK: Plot out the time series**

# %%
# CODE HERE
# Tracé de la série temporelle
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], marker='o')
plt.title('Série Temporelle des Valeurs')
plt.xlabel('Date')
plt.ylabel('Valeur')
plt.grid(True)
plt.show()


# %% [markdown]
# **TASK: Perform a Seasonal Decomposition on the model and plot out the ETS components**

# %%
from statsmodels.tsa.seasonal import seasonal_decompose

# Remplacer les valeurs manquantes par un remplissage vers l'avant
df_resampled_filled = df_resampled.fillna(method='ffill')

# Tentative de décomposition saisonnière à nouveau
decomposition_filled = seasonal_decompose(
    df_resampled_filled['Value'], model='additive')

# Tracer la décomposition saisonnière
plt.figure(figsize=(12, 8))
decomposition_filled.plot()
plt.show()


# %% [markdown]
# ## Train Test Split

# %% [markdown]
# **TASK: Figure out the length of the data set**

# %% [markdown]
# **TASK: Split the data into a train/test split where the test set is the last 12 months of data.**

# %%
df


# %%
# # Vérifier la forme de X_train
# print("Forme de X_train:", X_train.shape)

# # Vérifier si la date limite est appropriée
# print("Date limite:", date_limite)
# print("Dates maximales et minimales dans le DataFrame:",
#       df.index.max(), df.index.min())

# # Si X_train est vide, corrigez la division de vos données
# if X_train.shape[0] == 0:
#     print("X_train est vide. Vérifiez la division de vos données.")


# %%
# CODE HERE
# Importer la bibliothèque pandas
import pandas as pd

# S'assurer que les données sont triées par date
# df.sort_values(inplace=True)

# Définir une date un an (12 mois) avant la dernière date dans les données
date_limite = df.index.max() - pd.DateOffset(years=1)

# Créer les ensembles de données d'entraînement et de test
X_train = df[df.index <= date_limite]
X_test = df[df.index > date_limite]

# Séparer les valeurs cibles pour l'entraînement et le test
y_train = X_train['Value']
y_test = X_test['Value']

# Vous pouvez choisir de supprimer la colonne 'Value' de X_train et X_test si elle ne sert pas de caractéristique
# X_train = X_train.drop(columns=['Value'])
# X_test = X_test.drop(columns=['Value'])

# Enregistrer dans des fichiers
X_train.to_csv('train_Miles_Traveled.csv', encoding='utf-8')
X_test.to_csv('test_Miles_Traveled.csv', encoding='utf-8')
y_train.to_csv('y_train.csv', encoding='utf-8')
y_test.to_csv('y_test.csv', encoding='utf-8')


# %%
y_train


# %%
X_train


# %%
# Calcul de la longueur du jeu de données
longueur_dataset = len(df)

longueur_dataset


# %% [markdown]
# ## Scale Data

# %% [markdown]
# **TASK: Use a MinMaxScaler to scale the train and test sets into scaled versions.**

# %%
from sklearn.preprocessing import MinMaxScaler

# Création du scaler, qui mettra les données à l'échelle entre 0 et 1
scaler = MinMaxScaler(feature_range=(0, 1))

# Ajustement du scaler sur les données d'entraînement (X_train)
scaler.fit(X_train.values.reshape(-1, 1))

# Transformation des ensembles d'entraînement et de test (X)
X_train_scaled = scaler.transform(X_train.values.reshape(-1, 1))
X_test_scaled = scaler.transform(X_test.values.reshape(-1, 1))

# Transformation des cibles (y)
y_train_scaled = scaler.transform(y_train.values.reshape(-1, 1))
y_test_scaled = scaler.transform(y_test.values.reshape(-1, 1))

# Conversion des données mises à l'échelle en DataFrame pour une utilisation ultérieure
X_train_scaled_df = pd.DataFrame(
    X_train_scaled, index=X_train.index, columns=X_train.columns)
X_test_scaled_df = pd.DataFrame(
    X_test_scaled, index=X_test.index, columns=X_test.columns)

# Conversion des cibles mises à l'échelle en DataFrame (si nécessaire)
y_train_scaled_df = pd.DataFrame(
    y_train_scaled, index=y_train.index, columns=['Value'])
y_test_scaled_df = pd.DataFrame(
    y_test_scaled, index=y_test.index, columns=['Value'])

    # Remplir les NaN par interpolation
train_scaled = pd.DataFrame(train_scaled).interpolate().values

# Vérification  si des valeurs NaN existent
print("NaN dans train_scaled après interpolation:", np.isnan(train_scaled).any())



# %%
train_scaled_df.info()


# %% [markdown]
# # Time Series Generator
#
# We Create a TimeSeriesGenerator object based off the scaled_train data. The n_input is up to you, but at a minimum it should be at least 12. n_input refers to the window size, ie. length of your sequence.
# We want to do a one step ahead forecast.

# %%
train_scaled_df


# %%
import numpy as np

# Vérifier si des valeurs NaN ou infinies existent
print("NaN dans train_scaled:", np.isnan(train_scaled).any())
print("Infini dans train_scaled:", np.isinf(train_scaled).any())

# Des valeurs NaN ou infinies sont trouvées, vous devez les traiter avant l'entraînement


# %%
# Re-importation des bibliothèques nécessaires et rechargement des données
import pandas as pd

# Recharger les fichiers
train_df = pd.read_csv('train_Miles_Traveled.csv', index_col='DATE', parse_dates=True)
test_df = pd.read_csv('test_Miles_Traveled.csv', index_col='DATE', parse_dates=True)

# Vérifications de base sur les données

# Vérifier si des valeurs NaN existent dans les données d'entraînement et de test
nan_in_train = train_df.isna().any().any()
nan_in_test = test_df.isna().any().any()

# Vérifier les formes des DataFrames d'entraînement et de test
train_shape = train_df.shape
test_shape = test_df.shape

nan_in_train, nan_in_test, train_shape, test_shape


# %%
# Traitement des valeurs NaN dans train_df par interpolation
train_df_filled = train_df.interpolate()

# Vérifier à nouveau si des valeurs NaN existent
nan_in_train_filled = train_df_filled.isna().any().any()

# Afficher les premières lignes des données après interpolation
train_df_filled_head = train_df_filled.head()

nan_in_train_filled, train_df_filled_head


# %%
from keras.preprocessing.sequence import TimeseriesGenerator


# %%
n_input = 12  # you might need to test a variety of input values and test performance,
# but at least 12 to capture one cycle of seasonality

n_features = 1  # for univariate time series always 1

# Create input data from time series with generator object
# we put in the train data 2, once as actual train data, once as target variable, specify window length =n_input
# smaller batch sizes tend to work better
# CAREFUL: adjust the following 'scaled_train' to the name of your train object
generator = TimeseriesGenerator(
    train_df_filled, train_df_filled, sampling_rate=1, length=n_input, batch_size=1)

generator


# %% [markdown]
# TASK: inspect the output of the TimeSeriesGenerator

# %%
print("Taille de train_scaled_df:", train_scaled_df.shape)
n_input = min(n_input, len(train_scaled_df) - 1)  # Ajustez n_input si nécessaire


# %%
# Convertir train_scaled_df en numpy array
train_scaled_array = train_scaled_df.values

# Vérifier la forme
print("Forme de train_scaled_array:", train_scaled_array.shape)

# Recréer le TimeSeriesGenerator avec le numpy array
generator = TimeseriesGenerator(
    train_df_filled, train_df_filled, length=n_input, batch_size=1)

# Tenter d'itérer à nouveau sur les premiers lots
for i in range(2):
    x, y = generator[i]
    print(f"Lot {i+1}")
    print("X:", x)
    print("Y:", y)
    print('---' * 10)


# %% [markdown]
# ### Create the Model
#
# Create a Keras Sequential Model with as many LSTM units as you want and a final Dense Layer.

# %%
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.initializers import GlorotUniform

# Initialisation du modèle séquentiel
model = Sequential()

# Ajout d'une couche LSTM
model.add(LSTM(50, activation='tanh', input_shape=(n_input, n_features), kernel_initializer=GlorotUniform()))

# Ajout de la couche Dense finale
model.add(Dense(1))

# Compilation du modèle
model.compile(optimizer='adam', loss='mean_squared_error')

model.summary()


# %%
y_pred


# %%
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

# Faire des prédictions
y_pred = model.predict(X_test)

# Calculer MSE
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)

# Calculer MAPE
mape = mean_absolute_percentage_error(y_test, y_pred)
print("Mean Absolute Percentage Error (MAPE):", mape)


# %% [markdown]
# Fit the model to the generator (it should be a lot of epochs, but do as many as you have the patience for! :)**

# %%
# fit model
model.fit(generator, epochs=10)


# %% [markdown]
# **TASK: Plot the history of the loss that occured during training.**

# %%
# CODE HERE
import matplotlib.pyplot as plt

# Supposons que vous avez déjà formé votre modèle et enregistré l'historique
# history = model.fit(...)

# Extraire les valeurs de perte
loss = history.history['loss']

# Tracer le graphique de la perte
plt.figure(figsize=(10, 6))
plt.plot(loss, label='Training Loss')
plt.title('Historique de la perte durant l\'entraînement')
plt.xlabel('Époques')
plt.ylabel('Perte')
plt.legend()
plt.show()


# %%


# %%


# %% [markdown]
#

# %% [markdown]
# # Evaluate on Test Data
#
# Based on your test data and input size, create an appropriately sized "first evaluation batch"

# %%
first_eval_batch = scaled_train[-n_input:]


# %%
# Supposons que n_input est le nombre de pas de temps utilisés pour chaque séquence d'entrée
# et n_features est le nombre de caractéristiques par pas de temps

# Sélectionner les derniers points de données de l'ensemble d'entraînement
first_eval_batch = train_scaled[-n_input:]

# Redimensionner le lot pour correspondre au format attendu par le modèle
# Le nouveau format doit être [1, n_input, n_features]
first_eval_batch = first_eval_batch.reshape((1, n_input, n_features))

# Maintenant, vous pouvez utiliser ce lot pour faire une première prédiction
first_pred = model.predict(first_eval_batch)


# %%
first_eval_batch


# %%
# reshape the data to get it into the 3 dimensional shape needed for the keras model and model.predict()
# same dim as TimeSeriesGenerator output
first_eval_batch = first_eval_batch.reshape((1, n_input, n_features))


# %% [markdown]
# **TASK: predict the first point of the test dataset**

# %%
# Code here


# %%
#


# %% [markdown]
# ## Now let's put this logic in a for loop to predict into the future for the entire test range.
#
#
# **TASK: PAY CLOSE ATTENTION HERE TO WHAT IS BEING OUTPUTED AND IN WHAT DIMENSIONS. ADD YOUR OWN PRINT() STATEMENTS TO SEE WHAT IS TRULY GOING ON!!**

# %%
# FORECAST USING RNN MODEL

# list for holding predictions
test_predictions = []


# how far into feature will you foreacst (here just len test)
for i in range(len(test)):

    # get prediction 1 time stamp ahead of historical 12 points ([0] is for grabbing just the number instead of [array])
    current_pred = model.predict(current_batch)[0]

    # store that  prediction
    test_predictions.append(current_pred)

    # update current batch to now include prediction and drop first value
    # append current prediction and this is all teh code we need to forecast into the future, ie. into the testset
    current_batch = np.append(current_batch[:, 1:, :], [
                              [current_pred]], axis=1)


# %% [markdown]
# ## Inverse Transformations and Compare
#
# **TASK: Inverse Transform your new forecasted predictions to retrieve back the original and not the scaled values**

# %%
# invert scale to get back true predicted values!
# CODE HERE


# %%


# %%


# %% [markdown]
# **TASK: Create a new dataframe that has both the original test values and your predictions for them.**

# %%
# CODE HERE


# %%


# %% [markdown]
# **TASK: Plot out the test set against your own predicted values.**

# %%
# CODE HERE


# %%


# %% [markdown]
# # Saving Models
#
# **TASK: Optional, Save your model!**

# %%



