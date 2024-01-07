from .models import Film, Critique
import pickle
from django.http import HttpResponse
from django.shortcuts import render
import os


# Chemin absolu vers le fichier
# file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
#     os.path.abspath(__file__)))), '..', 'data_merged', 'df_merged.pkl')

file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), '..', '..', 'data_merged', 'df_merged.pkl')


with open(file_path, 'rb') as file:
    model = pickle.load(file)


with open(file_path, 'rb') as file:
    model = pickle.load(file)


def accueil(request):
    films = Film.objects.all()
    return render(request, 'my_application/accueil.html', {'films': films})


def kpi(request):
    return render(request, 'my_application/kpi.html')


def recommendation(request):
    critiques = Critique.objects.all()
    return render(request, 'my_application/recommendation.html', {'critiques': critiques})


def annexe(request):
    return render(request, 'my_application/annexe.html')
