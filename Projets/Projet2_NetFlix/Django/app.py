from django.urls import path
from .views import AccueilView, IrisView, TitanicView

urlpatterns = [
    path('accueil/', AccueilView.as_view(), name='accueil'),
    path('kpi/', IrisView.as_view(), name='kpi'),
    path('recommendation/', TitanicView.as_view(), name='recommendation'),
]
