
import sqlite3

# Se connecter à la base de données SQLite
connexion = sqlite3.connect(r"quêtes\Semaine3\quetes_sql\quete_movies_sql\movies.sqlite")

# Créer un objet curseur
curseur = connexion.cursor()

# Exécuter une requête SQL
requete_sql="""SELECT m.original_title, m.popularity
 FROM movies as m
 ORDER BY m.popularity DESC
 LIMIT 3;"""

curseur.execute(requete_sql)

# Récupérer tous les résultats
resultats = curseur.fetchall()

print(resultats)

# Fermer la connexion
connexion.close()
# #--------

# # ex de requete en python
# # csvsql --query "SELECT * FROM nom_de_la_table WHERE condition" mon_fichier.csv

# #-------------------------------------


# # 1 Le top 3 des films les plus populaires
#  SELECT m.original_title, m.popularity
#  FROM movies as m
#  ORDER BY m.popularity DESC
#  LIMIT 3;

# #-------------------------------------

#  #2 Le nombre de films par réalisateur
# SELECT d.name, COUNT(m.director_id) as nombre_de_films
# FROM directors d
# JOIN movies m ON d.id = m.director_id
# GROUP BY d.name
# ORDER BY nombre_de_films DESC;

# # autre solution avec une vue producteur_movies:
# # creation de la vue
# CREATE VIEW producteur_movies AS
# SELECT d.name as name, m.title as movie_title
# FROM directors d
# JOIN movies m ON d.id = m.director_id;

# # requete utilisant la vue
# SELECT pm.name, COUNT(pm.movie_title) as nombre_de_films
# FROM producteur_movies pm
# GROUP BY name
# ORDER BY nombre_de_films DESC;

# #-------------------------------------

# #3 --Le top 5 des réalisateurs ayant réalisé des bénéfices au cours de leur carrière.
# SELECT d.name, SUM(m.revenue) as profits
# FROM directors d
# JOIN movies m ON d.id = m.director_id
# GROUP BY d.name
# ORDER BY profits DESC
# LIMIT 5;

# # 4--Le nombre de films par réalisateur dont la popularité est
# # inférieure à 10.Puis, la moyenne des notes de ces films.
# SELECT
# d.name as directors_name,
# COUNT(m.popularity) as ranking ,
# AVG(m.vote_average) as Average_note
# FROM directors d
# JOIN movies m ON d.id = m.director_id
# WHERE m.popularity <10
# GROUP BY d.name
# ORDER BY ranking DESC;

# #-------------------------------------
# #5 --Tu vas maintenant créer une VIEW qui contient les réalisatrices,
# # --chacun de leur film ainsi que le nombre de votant par film.
# # --Enfin, à partir de cette vue, on veut le classement des réalisatrices
# # --en fonction du nombre de films, pour les films ayant plus de 1000 votants.

# # --création de la vue

# CREATE VIEW woman_directors_with_votes AS
# SELECT d.name, m.original_title, m.vote_count
# FROM movies m
# JOIN directors d ON d.id = m.director_id
# WHERE d.gender =1;

# # --création de la requete

# SELECT
# name as productrice_name,
# COUNT(original_title) as number_of_movies
# FROM woman_directors_with_votes
# WHERE vote_count  > 1000
# GROUP BY name
# ORDER BY number_of_movies DESC;

# #-------------------------------------

# # Fermer la connexion
# connexion.close()