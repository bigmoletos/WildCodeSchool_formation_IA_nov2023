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



def actor_view(request):
    acteur = request.GET.get("acteur")
    next_page = request.GET.get("next", 'accueil')  # Utilisez 'default_view' comme valeur par défaut
    df_acteur = None
    acteur_stat = None
    df_acteur_html=None
    nom_le_plus_frequent=None
    top_3_films=None
    if acteur:
        try:
            df_acteur, nom_le_plus_frequent, top_3_films,acteur_stat = stat_acteur(df, acteur)
            request.session["df_acteur"] = df_acteur.to_dict()
            request.session.modified = True
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à stat_acteur.")
            print(str(e))
    if next_page == 'kpi'and acteur:
        return redirect(reverse('kpi_acteur', kwargs={'acteur': acteur}))
    elif next_page== 'kpi':
        return redirect(reverse('kpi'))
    else:
        return redirect(reverse(next_page))



#  ce nom est erroné il s'agit nonp pas des KPI mais des informations concernant un acteur ou une actrice
def kpi(request,acteur=None):
# def kpi(request):
    # acteur = (request.POST.get(
    #         "acteur") if request.method == "POST" else request.GET.get("nom_acteur")
    # )
    acteur =acteur or request.GET.get("acteur","") if request.method == "GET" else request.POST.get("acteur")

    print(f"\request.method :\n{request.method} \n")
    print(f"\nacteur :\n{acteur} \n")
    df_acteur = None
    acteur_stat = None
    df_acteur_html=None
    nom_le_plus_frequent=None
    top_3_films=None
    if acteur:
        try:
            df_acteur, nom_le_plus_frequent, top_3_films,acteur_stat = stat_acteur(df, acteur)
            print(f"\acteur_stat :\n{acteur_stat} \n")
            print(f"\nnom_le_plus_frequent :\n{nom_le_plus_frequent} \n")
            print(f"\ntop_3_films :\n{top_3_films} \n")
            # Stocker df_acteur dans la session
            request.session["df_acteur"] = df_acteur.to_dict()
            request.session.modified = True  # Indiquer que la session a été modifiée
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à stat_acteur.")
            print(str(e))
    films = None
    df_acteur_html=None
    df_acteur_dict=None
    df_top_3_films=None
    df_acteur_list=None
    df_casting=None
    try:
        # Récupérer df_acteur de la session
        df_acteur_dict = request.session.get("df_acteur")
        print(f"\df_acteur_dict :\n{df_acteur_dict} \n")

        if df_acteur_dict is not None:
            df_acteur = DataFrame(df_acteur_dict)
            df_top_3_films=DataFrame(top_3_films)
            df_top_3_films=df_top_3_films.to_dict('records')
            df_acteur_list=df_acteur.to_dict('records')
            # df_acteur_html = df_acteur.to_html()
            # # Utiliser BeautifulSoup pour ajouter les classes Bootstrap
            # soup = BeautifulSoup(df_acteur_html, 'html.parser')
            # table = soup.find('table')
            # table['class'] = 'table table-striped table-hover'
            # # Convertir le tableau modifié en chaîne
            # df_acteur_html = str(table)
        films = df["title"]
        print(f"===\ndf_acteur==== :\n{df_acteur.columns.tolist()} \n")
        # print(f"\n top_3_films :\n{top_3_films} \n")
        # print(f"\n df_top_3_films :\n{df_top_3_films} \n")
        print(f"\ndf_acteur_list :\n{df_acteur_list} \n")

        # Initialisation d'un dictionnaire pour stocker les listes des acteurs pour chaque tconst
        acteurs_par_film = {}
        if df_acteur is not None:
            for tconst in df_acteur['tconst'].unique():
                # Filtrer le DataFrame initial pour obtenir les acteurs pour le tconst actuel
                print(f"\n ===colonne de df === :\n{df.columns.tolist()} \n")
                acteurs = df[df['tconst'] == tconst]['primaryName'].tolist()  # Remplacez 'nom_acteur' par le nom réel de la colonne
                print(f"\n ===acteurs_par_film=== :\n{acteurs} \n")
                # Stocker la liste des acteurs dans le dictionnaire avec tconst comme clé
                acteurs_par_film[tconst] = acteurs
        print(f"\n ===acteurs_par_film=== :\n{acteurs_par_film} \n")

    except Exception as e:
        print(
            "Une erreur s'est produite lors de la récupération des données de la session.")
        print(str(e))

    return render(request, "kpi.html", {
        "acteur":acteur_stat,
        "nom_saisi":acteur,
        "films": films,
        "nom_le_plus_frequent": nom_le_plus_frequent,
        "top_3_films": df_top_3_films,
        "df_acteur": df_acteur_list,
        "casting":acteurs_par_film,
        # "df_acteur": df_acteur_html
        })



# #  ce nom est erroné il s'agit nonp pas des KPI mais des informations concernant un acteur ou une actrice
# def kpi(request,acteur=None):
# # def kpi(request):
#     # acteur = (request.POST.get(
#     #         "acteur") if request.method == "POST" else request.GET.get("nom_acteur")
#     # )
#     acteur =acteur or request.GET.get("acteur","") if request.method == "GET" else request.POST.get("acteur")

#     print(f"\request.method :\n{request.method} \n")
#     print(f"\nacteur :\n{acteur} \n")
#     df_acteur = None
#     acteur_stat = None
#     df_acteur_html=None
#     nom_le_plus_frequent=None
#     top_3_films=None
#     if acteur:
#         try:
#             df_acteur, nom_le_plus_frequent, top_3_films,acteur_stat = stat_acteur(df, acteur)
#             print(f"\acteur_stat :\n{acteur_stat} \n")
#             print(f"\nnom_le_plus_frequent :\n{nom_le_plus_frequent} \n")
#             print(f"\ntop_3_films :\n{top_3_films} \n")
#             # Stocker df_acteur dans la session
#             request.session["df_acteur"] = df_acteur.to_dict()
#             request.session.modified = True  # Indiquer que la session a été modifiée
#         except Exception as e:
#             print("Une erreur s'est produite lors de l'appel à stat_acteur.")
#             print(str(e))
#     films = None
#     df_acteur_html=None
#     df_acteur_dict=None
#     try:
#         # Récupérer df_acteur de la session
#         df_acteur_dict = request.session.get("df_acteur")
#         print(f"\df_acteur_dict :\n{df_acteur_dict} \n")

#         if df_acteur_dict is not None:
#             df_acteur = DataFrame(df_acteur_dict)
#             df_acteur_html = df_acteur.to_html()
#             # Utiliser BeautifulSoup pour ajouter les classes Bootstrap
#             soup = BeautifulSoup(df_acteur_html, 'html.parser')
#             table = soup.find('table')
#             table['class'] = 'table table-striped table-hover'
#             # Convertir le tableau modifié en chaîne
#             df_acteur_html = str(table)
#         films = df["title"]
#         # print(f"\ndf_acteur :\n{df_acteur} \n")

#     except Exception as e:
#         print(
#             "Une erreur s'est produite lors de la récupération des données de la session.")
#         print(str(e))

#     return render(request, "kpi.html", {
#         "acteur":acteur_stat,
#         "films": films,
#         "nom_le_plus_frequent": nom_le_plus_frequent,
#         "top_3_films": top_3_films,
#         "df_acteur": df_acteur_html})
