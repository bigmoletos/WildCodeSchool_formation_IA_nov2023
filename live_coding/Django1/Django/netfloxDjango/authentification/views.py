from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

def connexion(request):
    #return HttpResponse("Hello !")
    message = ""
    if request.method == "POST": # Si un formulaire a été validé
        pseudo = request.POST["pseudo"]
        motdepasse = request.POST["motdepasse"]
        verification = authenticate(
            username = pseudo,
            password = motdepasse)
        if verification: # Si y a bien une correspondance dans la base de données
            login(request, verification)
            return redirect("accueil")
        else:
            message = "Identifiant incorrect : T'es qui toi ?! 🤨🧐"
            return render(request, "connexion.html",
                      context={"message" : message})
    else: # Pas de formulaire validé, on vient d'arriver sur la page
        return render(request, "connexion.html",
                      context={"message" : message})
    
def deconnexion(request):
    logout(request)
    return redirect("")    
