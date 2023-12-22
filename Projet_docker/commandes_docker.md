#  Voici les 20 commandes Docker les plus importantes à connaître :
#  Construit une image Docker à partir d'un Dockerfile.

# docker build**
docker build -t mojo:latest .
#  : Exécute un conteneur Docker.
# docker run**
docker run -it mojo:latest
# docker ps** : Liste les conteneurs Docker en cours d'exécution.
docker ps
# docker stop** : Met fin à un conteneur Docker en cours d'exécution.
docker stop my_container
# docker start** : Redémarre un conteneur Docker arrêté.
docker start my_container
# docker rm** : Supprime un conteneur Docker.
docker rm my_container
# docker images** : Liste les images Docker disponibles.
docker images
# docker pull** : Télécharge une image Docker depuis un référentiel distant.
docker pull ubuntu:latest
# docker push** : Publie une image Docker sur un référentiel distant.
docker push my_image
# docker login** : Connecte-vous à un référentiel Docker distant.
docker login
# docker tag** : Modifie l'étiquette d'une image Docker.
docker tag my_image my_new_image
# docker inspect** : Affiche les détails d'une image ou d'un conteneur Docker.
docker inspect my_container
# docker network** : Gère les réseaux Docker.
docker network create my_network
# docker volume** : Gère les volumes Docker.
docker volume create my_volume
# docker compose** : Gère les applications Docker complexes.
docker-compose up
# docker swarm** : Gère les clusters Docker.
docker swarm init


# exemples de code avec pour référentiel mon projet `mojo_ia` utilisé pour faire de l'IA et du machine learning :

# **docker build**

#docher file:
FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install numpy pandas scikit-learn

ENTRYPOINT ["python3"]
#

**docker run**

docker run -it -v $PWD:/data mojo_ia:latest
#
**docker ps**
docker ps
**docker stop**
docker stop my_container
**docker start**
docker start my_container
**docker rm**
docker rm my_container
**docker images**
docker images
**docker pull**
docker pull tensorflow/tensorflow:latest
**docker push**
docker push my_image
**docker login**
docker login
**docker tag**
docker tag my_image my_new_image
**docker inspect**
docker inspect my_container
**docker network**
docker network create my_network
**docker volume**
docker volume create my_volume
**docker compose**
version: '3.8'

services:
  my_app:
    image: mojo_ia:latest
    command: python3 my_app.py
#
**docker swarm**
docker swarm init
