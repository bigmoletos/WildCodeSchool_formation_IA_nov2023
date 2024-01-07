### créer un projet Django nommé hello_world avec une page d’accueil.

Créez un nouveau projet Django avec la commande suivante :
`django-admin startproject hello_world`

Accédez au répertoire du projet :
`cd hello_world`

Créez une nouvelle application Django dans le projet :
`python manage.py startapp home`

Dans **home/views.py**, ajoutez une vue pour la page d’accueil :
Python

`from django.shortcuts import render`

`def home(request):`
`    return render(request, 'home.html')`


Créez un répertoire **templates** dans l’application **home** et créez un fichier **templates/home.html** dans ce répertoire.
Ajoutez le code HTML suivant à **home.html** :
HTML

<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Bienvenue sur la page d'accueil !</h1>
</body>
</html>

Dans **hello_world/urls.py**, ajoutez une URL pour la page d’accueil :
Python

`from django.urls import path`
`from home.views import home`

`urlpatterns = [`
`    path('', home, name='home'),`
`]`

Enfin, démarrez le serveur Django avec la commande suivante :
`python manage.py runserver`

Maintenant, si vous accédez à http://localhost:8000 dans votre navigateur, vous devriez voir la page d’accueil avec le message “Bienvenue sur la page d’accueil !”.