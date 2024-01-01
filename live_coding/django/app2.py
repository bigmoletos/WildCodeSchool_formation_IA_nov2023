import pandas as pd
import seaborn as sns
from django.http import HttpResponse
from django.views import View

# Chargement des données
titanic = sns.load_dataset("titanic")
iris = sns.load_dataset("iris")

class AccueilView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Ceci est une requête GET pour la page d\'accueil')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Ceci est une requête POST pour la page d\'accueil')

class IrisView(View):
    def get(self, request, *args, **kwargs):
        # Utilisez le dataframe iris ici
        return HttpResponse(f'Ceci est une requête GET pour la page Iris. Voici les premières lignes du dataframe Iris : {iris.head()}')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Ceci est une requête POST pour la page Iris')

class TitanicView(View):
    def get(self, request, *args, **kwargs):
        # Utilisez le dataframe titanic ici
        return HttpResponse(f'Ceci est une requête GET pour la page Titanic. Voici les premières lignes du dataframe Titanic : {titanic.head()}')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Ceci est une requête POST pour la page Titanic')
