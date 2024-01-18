from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def accueil(request):
    nom = request.user.username
    return render(request, "accueil.html", {"nom" : nom})
