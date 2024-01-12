from django.shortcuts import render, redirect
from .load_data import load_data
from .fonction_recommandation import recommandation_film
from .load_modele_machine_learning import load_modele_machine_learning
from .load_X_reduced import load_X_reduced
from .scrapping_pochette import get_movie_poster
from .stat_acteur import stat_acteur
from pandas import DataFrame
from django.urls import reverse
import pandas as pd

# import joblib
# Projets\Projet2_NetFlix\Django\projet_recommandation_films\my_application\load_modele_machine_learning.py
# df = pd.read_csv("dfFeatures.csv")
# titresDeFilms = df.Series_Title.values
# knn = joblib.load('recoNetflox.joblib')


# Charger le modèle une seule fois
try:
    df = load_data()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données.")
    print(str(e))

# Charger le modèle machine learning
try:
    knn_recommandation = load_modele_machine_learning()
except Exception as e:
    print("Une erreur s'est produite lors du chargement du modele de machine learning.")
    print(str(e))
# Charger X_reduced
try:
    X_reduced = load_X_reduced()
except Exception as e:
    print("Une erreur s'est produite lors du chargement du modele de machine learning.")
    print(str(e))

from django.shortcuts import render
# Assurez-vous d'inclure les autres importations nécessaires ici

from .scrapping_pochette import get_movie_poster
from .fonction_recommandation import recommandation_film
# Incluez d'autres importations nécessaires

def recommandation(request):
    nom_film = request.POST.get('film') if request.method == 'POST' else request.GET.get('nom_film')
    liste_films = []
    if nom_film:
        try:
            # Utilisez la fonction recommandation_film pour obtenir les films recommandés
            df_film_choisi, df_films_proches = recommandation_film(df, X_reduced, nom_film)
            liste_films = df_films_proches.to_dict('records')  # Convertir le DataFrame en liste de dictionnaires
            # liste_films = df_films_proches.values.tolist()  # Convertir le DataFrame en liste de dictionnaires
            infos_film_choisi = df_film_choisi.values.tolist()
            print(f"\nliste_films :\n{liste_films} \n")
#             liste_films = [{'nom_du_film': 'Test Film', 'genre': 'Drama', 'acteurs': ['Actor 1', 'Actor 2'], 'note': '8.5'}
# ]
            # Obtenir les URLs des images pour chaque film recommandé
            for film in liste_films:
                tconst = film.get('tconst')
                film['image_de_la_pochette'] = get_movie_poster(tconst, default_image_url='/static/images/Djangounchained.webp') if tconst else '/static/images/Djangounchained.webp'

            # Stocker le film dans la session
            request.session['film'] = nom_film
            request.session.modified = True
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à recommandation_film.")
            print(str(e))

    return render(request, 'recommandation.html', {'liste_des_films': liste_films, 'film': nom_film, 'infos_film': infos_film_choisi})







# def recommandation(request):
#     nom_film = request.POST.get('film') if request.method == 'POST' else request.GET.get('nom_film')
#     infos_film_choisi = None
#     liste_films = []
#     if nom_film:
#         try:
#             # Utilisez la fonction recommandation_film pour obtenir les films recommandés
#             df_film_choisi, df_films_proches = recommandation_film(df, X_reduced, nom_film)
#             liste_films = df_films_proches.values.tolist()  # Convertir le DataFrame en liste
#             infos_film_choisi = df_film_choisi.values.tolist() # Convertir le DataFrame en liste de dictionnaires
#             # Obtenir les URLs des images pour chaque film recommandé
#             for film in liste_films:
#                 film['image_de_la_pochette'] = get_movie_poster(film['tconst'])  # Assurez-vous que 'tconst' est correct
#             # Stocker le film dans la session
#             request.session['film'] = nom_film
#             request.session.modified = True  # Indiquer que la session a été modifiée
#             print(f"\nliste_films :\n{liste_films} \nnom_film:\n {nom_film} \ninfos_film_choisi:\n{infos_film_choisi} \n")
#         except Exception as e:
#             print("Une erreur s'est produite lors de l'appel à recommandation_film.")
#             print(str(e))
#     # return render(request, 'recommandation.html', {'liste_des_films': liste_films, 'film': nom_film, 'infos_film': infos_film_choisi, })
#     return render(request, 'recommandation.html', {'liste_des_films': liste_films, 'film': nom_film})


# def recommandation(request):
#     nom_film = request.POST.get('film') if request.method == 'POST' else request.GET.get('nom_film')
#     infos_film_choisi=None
#     liste_films = None
#     if nom_film:
#         try:
#             # Utilisez la fonction recommandation_film pour obtenir les films recommandés
#             df_film_choisi, df_films_proches = recommandation_film(df,X_reduced, nom_film)
#             print(f"\nVIEW infos_film_choisi :\n{df_film_choisi} \n")
#             print(f"\nVIEW df_films_proches:\n{df_films_proches} \n")
#             liste_films = df_films_proches  # Convertir le DataFrame en liste
#             infos_film_choisi = df_film_choisi  # Convertir le DataFrame en liste
#             # Stocker le film dans la session
#             request.session['film'] = nom_film
#             request.session.modified = True  # Indiquer que la session a été modifiée
#         except Exception as e:
#             print("Une erreur s'est produite lors de l'appel à recommandation_film.")
#             print(str(e))
#     return render(request, 'recommandation.html', {'liste des films': liste_films, 'film': nom_film, 'infos film': infos_film_choisi})



# def actor_view(request):
#     acteur = request.POST.get(
#         'acteur') if request.method == 'POST' else request.GET.get('acteur')
#     df_acteur = None
#     if acteur:
#         try:
#             df_acteur = stat_acteur(df, acteur)
#             # Stocker df_acteur dans la session
#             request.session['df_acteur'] = df_acteur.to_dict()
#             request.session.modified = True  # Indiquer que la session a été modifiée
#         except Exception as e:
#             print("Une erreur s'est produite lors de l'appel à stat_acteur.")
#             print(str(e))
#     next_page = request.POST.get(
#         'next') if request.method == 'POST' else request.GET.get('next')
#     if next_page:
#         return redirect(next_page)
#     else:
#         # Rediriger vers une page par défaut si 'next' n'est pas fourni
#         return redirect('default_view')

def actor_view(request):
    acteur = request.POST.get(
        'acteur') if request.method == 'POST' else request.GET.get('acteur')
    df_acteur = None
    if acteur:
        try:
            df_acteur = stat_acteur(df, acteur)
            # Stocker df_acteur dans la session
            request.session['df_acteur'] = df_acteur.to_dict()
            request.session.modified = True  # Indiquer que la session a été modifiée
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à stat_acteur.")
            print(str(e))
    next_page = request.POST.get(
        'next') if request.method == 'POST' else request.GET.get('next')
    if next_page:
        # Construire l'URL de redirection avec le nom de l'acteur en paramètre
        next_page = reverse(next_page, kwargs={'acteur': acteur})
        return redirect(next_page)
    else:
        # Rediriger vers une page par défaut si 'next' n'est pas fourni
        return redirect('default_view')


def annexe(request):
    acteur = request.POST.get(
        'acteur') if request.method == 'POST' else request.GET.get('nom_acteur')
    df_acteur = None
    premier_film = None
    if acteur:
        try:
            df_acteur = stat_acteur(df, acteur)
            premier_film = df["titles"][0]
            # Stocker df_acteur dans la session
            request.session['df_acteur'] = df_acteur.to_dict()
            request.session.modified = True  # Indiquer que la session a été modifiée
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à stat_acteur.")
            print(str(e))
    return render(request, 'annexe.html', {'premier_film': premier_film, 'df_acteur': df_acteur})


def kpi(request):
    acteur = request.POST.get(
        'acteur') if request.method == 'POST' else request.GET.get('nom_acteur')
    df_acteur = None
    if acteur:
        try:
            df_acteur = stat_acteur(df, acteur)
            # Stocker df_acteur dans la session
            request.session['df_acteur'] = df_acteur.to_dict()
            request.session.modified = True  # Indiquer que la session a été modifiée
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à stat_acteur.")
            print(str(e))
    films = None
    try:
        # Récupérer df_acteur de la session
        df_acteur_dict = request.session.get('df_acteur')
        if df_acteur_dict is not None:
            df_acteur = DataFrame(df_acteur_dict)
            df_acteur_html = df_acteur.to_html()
        films = df["titles"]
    except Exception as e:
        print(
            "Une erreur s'est produite lors de la récupération des données de la session.")
        print(str(e))
    return render(request, 'kpi.html', {'films': films, 'df_acteur': df_acteur_html})


def accueil(request):
    return render(request, 'accueil.html')
def contact(request):
    return render(request, 'contact.html')
def graphiques(request):
    return render(request, 'graphe.html')
def etudes(request):
    return render(request, 'etude.html')


# def kpi(request):
#     films = None
#     try:
#         # Récupérer df_acteur de la session
#         df_acteur = request.session.get('df_acteur')
#         films = df["titles"]
#     except Exception as e:
#         print(
#             "Une erreur s'est produite lors de la récupération des données de la session.")
#         print(str(e))
#     return render(request, 'kpi.html', {'films': films, 'df_acteur': df_acteur})


# def recommandation(request):
#     return render(request, 'recommandation.html')
