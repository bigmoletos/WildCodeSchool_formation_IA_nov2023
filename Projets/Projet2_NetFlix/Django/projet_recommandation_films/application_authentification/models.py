from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import random
import string


class Utilisateur(AbstractUser):  # Une classe du model == table dans une BDD
    # champ1 =
    # champ2 =
    # champ3 =
    pass



# # Créer un utilisateur
# user = User.objects.create_user('root', 'lennon@thebeatles.com', '123')

# # Initialiser le mot de passe
# user.set_password('newpassword')
# # option mot depasse aléatoire
# # password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
# # user.set_password(password)
# user.save()