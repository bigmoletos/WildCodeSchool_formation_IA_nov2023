import os
import io
import json
import base64
import pandas as pd
from django import forms
from django import forms
from pandas import DataFrame
from bs4 import BeautifulSoup
from django.urls import reverse
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django_select2.forms import Select2Widget
from my_application.load_data import load_data
from my_application.stat_acteur import stat_acteur
# from .fonction_recommandation import recommandation_film
from my_application.load_X_reduced import load_X_reduced
from my_application.scrapping_pochette import get_movie_poster
from my_application.load_modele_machine_learning import load_modele_machine_learning

#  Incluez d'autres importations nécessaires
# Projets\Projet2_NetFlix\Django\projet_recommandation_films\my_application\load_modele_machine_learning.py
# Charger le modèle une seule fois
try:
    df = load_data()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données.")
    print(str(e))

# Charger le modèle machine learning
try:
    load_modele_machine_learning()
except Exception as e:
    print("Une erreur s'est produite lors du chargement du modele de machine learning.")
    print(str(e))
# Charger X_reduced
try:
    X_reduced = load_X_reduced()
except Exception as e:
    print("Une erreur s'est produite lors du chargement du modele de machine learning.")
    print(str(e))

# print(f"\ncolonne :\n{df.columns.tolist()} \n")

# Utilisation de la classe datamanager
# Dans vos vues ou n'importe où dans votre application :
# df = DataManager.get_data()
# model = DataManager.get_model()
# X_reduced = DataManager.get_X_reduced()


def graphiques(request):
    # Préparez vos données depuis le DataFrame
    # Supposons que vous ayez une colonne "Note Moyenne" dans votre DataFrame df
     # Chemins d'accès aux images
    barplot_image_path = '/my_application/static/images/barplot.png'
    scatterplot_image_path = '/my_application/static/images/scatterplot2.png'
    boxplot_image_path = '/my_application/static/images/boxplot2.png'

    data = df["averageRating"]

    # Vérifier si les images existent
    if os.path.exists(barplot_image_path) and os.path.exists(scatterplot_image_path) and os.path.exists(boxplot_image_path):
        # Charger les images existantes
        with open(barplot_image_path, "rb") as image_file:
            barplot_image_base64 = base64.b64encode(image_file.read()).decode()
        with open(scatterplot_image_path, "rb") as image_file:
            scatterplot_image_base64 = base64.b64encode(image_file.read()).decode()
        with open(boxplot_image_path, "rb") as image_file:
            boxplot_image_base64 = base64.b64encode(image_file.read()).decode()
    else:

        # Utilisez Matplotlib pour créer un graphique
        plt.figure(figsize=(10, 6))
        plt.bar(data.index, data.values)
        plt.xlabel("Films")
        plt.ylabel("Note Moyenne")
        plt.title("Note Moyenne par Film")

        # Enregistrez le graphique sous forme d'image
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        barplot_image_base64 = base64.b64encode(buffer.read()).decode()
        buffer.close()

        # Créez un scatterplot et enregistrez-le sous forme d'image
        plt.figure(figsize=(10, 6))
        plt.scatter(data.index, data.values, c="r",
                    marker="o", label="Note Moyenne")
        plt.xlabel("Films")
        plt.ylabel("Note Moyenne")
        plt.title("Scatterplot de Note Moyenne par Film")
        plt.legend()

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        scatterplot_image_base64 = base64.b64encode(buffer.read()).decode()
        buffer.close()

        # Créez un boxplot et enregistrez-le sous forme d'image
        plt.figure(figsize=(10, 6))
        plt.boxplot(data.values, vert=False)
        plt.xlabel("Note Moyenne")
        plt.title("Boxplot de Note Moyenne par Film")

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        boxplot_image_base64 = base64.b64encode(buffer.read()).decode()
        buffer.close()

        # Renvoyez les emplacements des images comme contexte
        context = {
            "barplot_image": barplot_image_base64,
            "scatterplot_image": scatterplot_image_base64,
            "boxplot_image": boxplot_image_base64,
        }

    return render(request, "graphe.html", context)


def accueil(request):
    return render(request, "accueil.html")
