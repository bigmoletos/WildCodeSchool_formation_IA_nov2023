from django.urls import path
from .views import AccueilView, IrisView, TitanicView

urlpatterns = [
    path('accueil/', AccueilView.as_view(), name='accueil'),
    path('iris/', IrisView.as_view(), name='iris'),
    path('titanic/', TitanicView.as_view(), name='titanic'),
]
