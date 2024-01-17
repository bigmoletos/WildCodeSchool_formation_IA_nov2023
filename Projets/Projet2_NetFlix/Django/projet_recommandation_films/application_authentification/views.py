from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


def connexion(request):
    #return HttpResponse("Hello !")
    message = "hello sur la page de connexion"
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

#  option
# def connexion(request):
#     message = "hello sur la page de connexion"  # This message will be overwritten by an error message if login fails.
#     if request.method == "POST":
#         pseudo = request.POST.get("pseudo")
#         motdepasse = request.POST.get("motdepasse")
#         user = authenticate(username=pseudo, password=motdepasse)
#         if user is not None:
#             login(request, user)
#             return redirect("accueil")
#         else:
#             message = "Identifiant incorrect : T'es qui toi ?! 🤨🧐"
#     # If we get here, it's either a GET request, or the login has failed.
#     return render(request, "application_authentification/connexion.html", {"message": message})
