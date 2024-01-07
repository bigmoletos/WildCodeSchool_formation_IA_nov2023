from django.shortcuts import render, redirect
from .models import Film, Critique
from .load_data import load_data
from .stat_acteur import stat_acteur

# Charger le modèle une seule fois
try:
    df = load_data()
except Exception as e:
    print("Une erreur s'est produite lors du chargement des données.")
    print(str(e))


def actor_view(request):
    if request.method == 'POST':
        acteur = request.POST.get('acteur')
        try:
            df_acteur = stat_acteur(df, acteur)
            # Stocker df_acteur dans la session
            request.session['df_acteur'] = df_acteur.to_dict()
        except Exception as e:
            print("Une erreur s'est produite lors de l'appel à stat_acteur.")
            print(str(e))
        return redirect('kpi')  # Rediriger vers la vue 'kpi'


def accueil(request):
    return render(request, 'accueil.html')


def kpi(request):
    try:
        # Récupérer df_acteur de la session
        df_acteur = request.session.get('df_acteur')
        films = df["titles"]
    except Exception as e:
        print(
            "Une erreur s'est produite lors de la récupération des données de la session.")
        print(str(e))
    return render(request, 'kpi.html', {'films': films, 'df_acteur': df_acteur})


def recommendation(request):
    return render(request, 'recommendation.html')


def annexe(request):
    try:
        # Récupérer df_acteur de la session
        df_acteur = request.session.get('df_acteur')
        if df is not None and not df.empty:  # Vérifie si df est non vide
            premier_film = df["title"][0]
        else:
            premier_film = df["title"][0]
    except Exception as e:
        print(
            "Une erreur s'est produite lors de la récupération des données de la session.")
        print(str(e))
    return render(request, 'annexe.html', {'premier_film': premier_film, 'df_acteur': df_acteur})
