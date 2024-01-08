from django.shortcuts import render, redirect
from .models import Film, Critique
from .load_data import load_data
from .stat_acteur import stat_acteur
from pandas import DataFrame
from django.urls import reverse
# Charger le modèle une seule fois
try:
    df = load_data()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données.")
    print(str(e))


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


def recommendation(request):
    return render(request, 'recommendation.html')
