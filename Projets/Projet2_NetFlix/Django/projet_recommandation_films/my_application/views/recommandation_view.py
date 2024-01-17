import io
import base64
import json
import pandas as pd
from django import forms
from pandas import DataFrame
from django.forms import Form
from django.urls import reverse
import matplotlib.pyplot as plt
from django.shortcuts import render
from my_application.models import *
from django.http import JsonResponse
from django_select2 import forms as s2forms
from django.shortcuts import redirect, render
from django_select2.forms import Select2Widget
from my_application.load_data import load_data
from my_application.stat_acteur import stat_acteur
from my_application.load_X_reduced import load_X_reduced
from my_application.scrapping_pochette import get_movie_poster
from my_application.fonction_recommandation import recommandation_film
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


#  creation du formulaire pour l'autocompletion
# class FilmForm(s2forms.Form):
#     genre = forms.CharField(max_length=100, widget=forms.Select2Widget())
#     acteur_principal = forms.CharField(max_length=100)
#     année_de_sortie = forms.IntegerField()

#  creation du formulaire pour l'autocompletion
# class FilmForm(forms.Form):
#     # CHOICES = []  # Remplacez par vos options. Exemple : [('1', 'Option 1'), ('2', 'Option 2')]
#     film = forms.ChoiceField(
#         # choices=CHOICES,
#         widget=Select2Widget(
#             attrs={
#                 'style': 'width: 300px; background-color: #cccccc; color: #333333;',
#                 'class': 'select2',
#                 'data-autocomplete-url': '/autocomplete'  # L'URL pour les requêtes AJAX si nécessaire
#             }
#         ),
#         required=False,
#     )


# fonctionne 15janv16h30 avec l'autocompletion mais est trés lent
#  creation du formulaire pour l'autocompletion
class FilmForm(forms.Form):
    film = forms.CharField(
        widget=Select2Widget(
            attrs={
                'style': 'width: 300px; height: 40px; background-color: #ccccc; color: green;',
                'class': 'select2',  # Utilisez cette classe pour initialiser Select2 en JS
                'data-autocomplete-url': '/autocomplete'  # L'URL pour les requêtes AJAX
            }
        ),
        required=False,
    )


# fonctionne lundi 15dec14h mais sans l'autocompletion
# class FilmForm(forms.Form):
#     film = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'style': 'width: 200px; height: 30px;',
#                 'class': 'select2',  # Utilisez cette classe pour initialiser Select2 en JS
#                 'data-autocomplete-url': '/autocomplete'  # L'URL pour les requêtes AJAX
#             }
#         ),
#         required=False,
#     )

# gestion de l'url pour l'autocompletion
def autocomplete_view(request):
    query = request.GET.get('term', '')
    print(f"++++++query+++++++:  {query}")
    print(f"++++++request+++++++:  {request}")
    matching_titles = df['title'][df['title'].str.contains(query, case=False, na=False)].unique().tolist()
    results = [{'id': title, 'text': title} for title in matching_titles]
    return JsonResponse(results, safe=False)

def recommandation_view(request):
    # Initialisez le formulaire avec les films
    form = FilmForm()
    liste_films = []
    infos_film_choisi = None
    nom_film = None
    # Set choices for the film field
    film_titles = [(title, title) for title in df['title'].unique()]
    # auto completion
    # query = request.GET.get('term', '')
    # matching_titles = df['title'][df['title'].str.contains(query, case=False, na=False)].tolist()
    # titles = [{'id': title, 'text': title} for title in matching_titles]

    # form.fields['film'].choices = [('', 'Choisissez un film')] + film_titles
    print(f"++++++request.method+++++++:  {request.method}")
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            nom_film = form.cleaned_data['film']
            try:
                nom_film = form.cleaned_data['film']
                # Utilisez la fonction recommandation_film pour obtenir les films recommandés
                df_film_saisi, df_films_proches = recommandation_film(df, X_reduced, nom_film)
                liste_films = df_films_proches.to_dict("records")
                print(f"===df_film_saisi=== \n{df_film_saisi.info()}")
                print(f"===df_film_saisi head===\n {df_film_saisi.head(0)}")
                print(f"===df_film_saisi dtype===\n{df_film_saisi.dtypes}")
                print(f"===df_film_saisi shape ===\n{df_film_saisi.shape}")
                print(f"===df_film_saisi columns ===\n{df_film_saisi.columns.tolist()}")
                infos_film_choisi = df_film_saisi.to_dict("records")

                if infos_film_choisi:  # Vérifiez si la liste n'est pas vide
                    film_dict = infos_film_choisi[0]
                    print(f"===film_dict apres infos_film_choisi[0] ===\n{film_dict}")
                    infos_film_choisi = {k.replace(' ', '_'): v for k, v in film_dict.items()}
                else:
                    print("//////Aucun film trouvé////////")
                    infos_film_choisi = {}
                # infos_film_choisi = infos_film_choisi[0]
                # Modifier les clés pour supprimer les espaces
                # infos_film_choisi = {k.replace(' ', '_'): v for k, v in infos_film_choisi.items()}

                print(f"===infos_film_choisi apres rempalcement espaces===\n {infos_film_choisi}")
                # print(f"infos_film_choisi {infos_film_choisi.columns.tolist()}")
                # print(f"infos_film_choisi {infos_film_choisi.items.tolist()}")

                # Ajoutez votre logique pour les URLs des images ici
                for film in liste_films:
                    tconst = film.get("tconst")
                    film["image_de_la_pochette"] = get_movie_poster(
                        tconst, default_image_url="/static/images/Djangounchained.webp"
                    )
                    # film["image_de_la_pochette"] = get_movie_poster(tconst)

                    print(f"===film image_de_la_pochette===\n {film["image_de_la_pochette"]}")
                # Stocker le film dans la session
                request.session["film"] = nom_film
                request.session.modified = True

            except Exception as e:
                print("Une erreur s'est produite lors de l'appel à recommandation_film.")
                print(str(e))
                liste_films = None  # Réinitialisez liste_films à None si une exception est levée

    elif request.method == 'GET':
        # Ceci est pour gérer le rechargement de la page ou l'accès direct par GET
        nom_film = request.GET.get("nom_film")

    # Renvoyez le formulaire et les données au template
    return render(
        request,
        "recommandation.html",
        {
            "liste_des_films": liste_films,
            "film": nom_film,
            "infos_film": infos_film_choisi,
            "form": form,

        }
    )
# def recommandation(request):
#     nom_film = request.POST.get(
#         "film") if request.method == "POST" else request.GET.get("nom_film")
#     film_titles = [(title, title) for title in df['title'].unique()]  # Liste des films sous forme de tuples

#     liste_films = []
#     infos_film_choisi = None
#     # Obtenez la liste des titres de films depuis votre DataFrame
#     film_titles = df['title'].unique().tolist()
#     print(f"\n film_titles:\n{film_titles} \n")
#     # Créer une instance du formulaire et mettre à jour les choix
#     form = FilmForm()
#     # form.fields['film'].choices = [(titre, titre) for titre in film_titles]
#     # Lorsque vous créez une instance de votre formulaire, vous pouvez passer la liste des films comme ceci :
#     # form.fields['film'].choices += film_titles  # Ajoutez les titres des films aux choix du formulaire
#     # Affectation directe des choix de films
#     # form.fields['film'].choices = [('', 'Choisissez un film')] + film_titles
#      # Mettre à jour les choix du formulaire avec les titres des films
#     form.fields['film'].choices = form.fields['film'].choices + film_titles

#     # nom_film = request.POST.get("film") if request.method == "POST" else None
#     # form.fields['film'].widget.attrs['data-autocomplete-light-function'] = 'autocompleteLightFunction'
#     # form.fields['film'].widget.attrs['data-autocomplete-light-url'] = 'url_pour_autocompletion'  # remplacer par l'URL de votre vue d'autocomplétion

#     if nom_film:
#         try:
#             # Utilisez la fonction recommandation_film pour obtenir les films recommandés
#             # Remplacer 'recommandation_film' par votre fonction réelle
#             df_film_choisi, df_films_proches = recommandation_film(
#                 df, X_reduced, nom_film)
#             # Convertir le DataFrame en liste de dictionnaires
#             liste_films = df_films_proches.to_dict("records")
#             # Convertir le DataFrame en liste de dictionnaires pour le film choisi
#             infos_film_choisi = df_film_choisi.to_dict("records")

#             # liste_films_df_autocompletion=df['titles'].unique().tolist()
#             # Ajoutez votre logique pour les URLs des images ici
#             for film in liste_films:
#                 # Assurez-vous que 'get_movie_poster' est votre fonction réelle pour obtenir les pochettes de films
#                 tconst = film.get("tconst")
#                 film["image_de_la_pochette"] = get_movie_poster(
#                     tconst, default_image_url="/static/images/Djangounchained.webp")
#                 print(f"\nliste_films :\n{liste_films} \n")
#                 print(f"\ninfos_film_choisi :\n{infos_film_choisi} \n")
#                 print(f"\nliste_films :\n{liste_films} \n")
#             # Stocker le film dans la session
#             request.session["film"] = nom_film
#             request.session.modified = True

#         except Exception as e:
#             print("Une erreur s'est produite lors de l'appel à recommandation_film.")
#             print(str(e))
#             liste_films = None  # Si une exception est levée, réinitialisez liste_films à None

#     return render(
#         request,
#         "recommandation.html",
#         {
#             "liste_des_films": liste_films,
#             # "liste_films_df_autocompletion":liste_films_df_autocompletion,
#             "film": nom_film,
#             "infos_film": infos_film_choisi,
#             "film_titles": film_titles,
#             "form": form
#         }
#     )

# def recommandation(request):
#     nom_film = request.POST.get("film") if request.method == "POST" else request.GET.get("nom_film")
#     liste_films = []
#     infos_film_choisi = None
#     film_titles = df["title"].tolist()  # Obtenez la liste des titres de films depuis votre DataFrame
#     if nom_film:
#         try:
#             # Utilisez la fonction recommandation_film pour obtenir les films recommandés
#             df_film_choisi, df_films_proches = recommandation_film(df, X_reduced, nom_film)
#             liste_films = df_films_proches.to_dict("records")  # Convertir le DataFrame en liste de dictionnaires
#             infos_film_choisi = df_film_choisi.values.tolist()
#             print(f"\nliste_films :\n{liste_films} \n")
#             print(f"\ninfos_film_choisi :\n{infos_film_choisi} \n")
#             print(f"\nliste_films :\n{liste_films} \n")
#             # Mise à jour des choix du formulaire avec la liste des films
#             form = FilmForm()
#             form.fields['film'].choices = [(film, film) for film in liste_films]

#             # Obtenir les URLs des images pour chaque film recommandé
#             for film in liste_films:
#                 tconst = film.get("tconst")
#                 film["image_de_la_pochette"] = (
#                     get_movie_poster(tconst, default_image_url="/static/images/Djangounchained.webp")
#                     if tconst
#                     else "/static/images/Djangounchained.webp"
#                 )
#             # Stocker le film dans la session
#             request.session["film"] = nom_film
#             request.session.modified = True
#         except Exception as e:
#             print("Une erreur s'est produite lors de l'appel à recommandation_film.")
#             print(str(e))
#             liste_films = None  # Si une exception est levée, réinitialisez liste_films à None pour afficher le message d'erreur
#     return render(
#         request,
#         "recommandation.html",
#         {
#             "liste_des_films": liste_films,
#             "film": nom_film,
#             "infos_film": infos_film_choisi,
#             "film_titles": film_titles,
#             'form': form,
#         },  # Transmettez la liste des titres de films dans le contexte
#     )