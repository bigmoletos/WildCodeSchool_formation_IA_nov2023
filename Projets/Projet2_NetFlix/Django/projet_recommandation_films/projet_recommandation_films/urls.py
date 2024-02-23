"""
URL configuration for projet_recommandation_films project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from my_application.views import accueil, kpi, annexe, actor_view, contact, graphiques,etudes,analyse,autocomplete_view, recommandation_view
from application_authentification.views import connexion, deconnexion
# from my_application.views import FilmAutocomplete.as_view

urlpatterns = [
    # path('', accueil, name='accueil'),
    path('accueil/', accueil, name="accueil"),
    path('connexion', connexion, name="connexion"),
    path('deconnexion', deconnexion, name='deconnexion'),
    path("", connexion, name=""),
    path('kpi/', kpi, name='kpi'),
    path('admin/', admin.site.urls),
    # path('kpi/<str:acteur>/', kpi, name='kpi'),
    path('kpi/<str:acteur>/', kpi, name='kpi_acteur'),
    path('recommandation/', recommandation_view, name='recommandation'),
    path('annexe/', annexe, name='annexe'),
    path('contact/', contact, name='contact'),
    path('graphe/', graphiques, name="graphe"),
    path('etude/', etudes, name="etude"),
    path('actor_view/', actor_view, name='actor_view'),
    path('analyse/', analyse, name='analyse'),
    path('autocomplete', autocomplete_view, name='autocomplete-url'),
    path("select2/", include("django_select2.urls")),
    # path('api/film-autocomplete/', FilmAutocomplete.as_view),
]
    # path("admin/", admin.site.urls),
    # path("", connexion, name=""),
    # path("deconnexion", deconnexion, name="deconnexion"),
    # path("accueil", accueil, name="accueil"),