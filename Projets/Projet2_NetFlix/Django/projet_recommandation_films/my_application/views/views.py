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
from django.contrib.auth.decorators import login_required

# from django_select2.forms import Select2TextInputWidget

# Incluez d'autres importations nécessaires
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

@login_required
def accueil(request):
    return render(request, "accueil.html")
@login_required
def annexe(request):
    acteur = (
        request.POST.get(
            "acteur") if request.method == "POST" else request.GET.get("nom_acteur")
    )
    df_acteur = None
    acteur_stat = None
    premier_film = None
    nom_le_plus_frequent=None
    top_3_films=None
    if acteur:
        try:
            df_acteur, nom_le_plus_frequent, top_3_films, acteur_stat = stat_acteur(df, acteur)
            premier_film = df["title"][0]
            # Stocker df_acteur dans la session
            request.session["df_acteur"] = df_acteur.to_dict()
            request.session.modified = True  # Indiquer que la session a été modifiée
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à stat_acteur.")
            print(str(e))
    return render(request, "annexe.html", {
        "premier_film": premier_film,
        "df_acteur": df_acteur,
        "nom_le_plus_frequent": nom_le_plus_frequent,
        "top_3_films": top_3_films,
        })




def contact(request):
    return render(request, "contact.html")

@login_required
def etudes(request):
    return render(request, "etude.html")

@login_required
def analyse(request):
    return render(request, "analyse.html")
