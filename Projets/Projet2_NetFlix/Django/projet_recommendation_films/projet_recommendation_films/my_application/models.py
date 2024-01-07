from django.db import models


class Film(models.Model):
    app_label = 'my_application'
    titre = models.CharField(max_length=200)
    date_sortie = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Critique(models.Model):
    app_label = 'my_application'
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100)
    texte = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texte
