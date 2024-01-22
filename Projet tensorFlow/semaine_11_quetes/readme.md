local_folder = '/Projet tensorFlow/semaine_11_quetes'

docker run -it --rm -v ${local_folder}:/tf/notebooks -p 8888:8888 tensorflow/tensorflow:latest-py3-jupyter


se mettre dans le repértoire où l'on souhaite lancer le container
docker run -it --rm -v ${PWD}:/tf/notebooks -p 8889:8888 tensorflow/tensorflow:latest-py3-jupyter

le notebook est accessible :http://localhost:8888
