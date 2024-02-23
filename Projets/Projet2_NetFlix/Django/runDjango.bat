@echo off
cd /d "\Projets\Projet2_NetFlix\Django"
.\django_env\Scripts\activate
cd /d ".\projet_recommandation_films\"
python manage.py runserver
pause
