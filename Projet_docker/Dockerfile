# # Utilisez l'image de base Ubuntu
# FROM ubuntu:latest

# # Mettez à jour les paquets et installez les dépendances nécessaires
# RUN apt-get update && apt-get install -y curl wget python3 python3-pip

# # Téléchargez Mojo
# RUN curl -LO https://github.com/modular-systems/mojo/releases/download/1.0.0/mojo-linux-amd64-1.0.0.tar.gz

# # Décompressez le fichier téléchargé
# RUN tar -xf mojo-linux-amd64-1.0.0.tar.gz

# # Déplacez le fichier Mojo dans le répertoire bin
# RUN mv mojo-linux-amd64-1.0.0/mojo /usr/local/bin/mojo

# # Installez les bibliothèques Python nécessaires
# RUN pip3 install numpy pandas scikit-learn seaborn jupyter keras tensorflow

# # Définissez l'entrée par défaut pour exécuter Mojo
# ENTRYPOINT ["mojo"]

# Pour définir un notebook Jupyter comme point d’entrée dans votre Dockerfile, vous pouvez modifier la ligne ENTRYPOINT comme suit :

# ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# Cette commande démarre un serveur de notebook Jupyter à l’adresse IP 0.0.0.0 sur le port 8888, sans ouvrir de navigateur, et permet l’exécution en tant que root.
# pour exécuter Jupyter à l’intérieur d’un conteneur Docker déjà en cours d’exécution, vous pouvez utiliser la commande docker exec. Par exemple, pour démarrer un notebook Jupyter dans un conteneur en cours d’exécution, vous pouvez utiliser :

# docker exec -it <container_id> jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# # Remplacez <container_id> par l’ID de votre conteneur. Vous pouvez obtenir l’ID de votre conteneur en utilisant la commande docker ps.
# Veuillez noter que ces commandes démarreront Jupyter sans mot de passe ni token, ce qui peut présenter des problèmes de sécurité. Assurez-vous de sécuriser correctement votre serveur Jupyter si vous prévoyez de l’exposer sur Internet. Vous pouvez le faire en ajoutant un mot de passe ou un token à la commande de démarrage de Jupyter. Consultez la documentation de Jupyter pour plus d’informations sur la sécurisation de votre serveur Jupyter.

# Utilisez l'image de base Ubuntu
FROM ubuntu:20.04

# Mettez à jour les paquets et installez les dépendances nécessaires
RUN apt-get update && apt-get install -y curl wget python3 python3-pip

# Créez un répertoire pour l'environnement Jupyter
RUN mkdir /notebooks

# Téléchargez Mojo
RUN curl -LO https://github.com/modular-systems/mojo/releases/download/1.0.0/mojo-linux-amd64-1.0.0.tar.gz

# Décompressez le fichier téléchargé
RUN tar -xf mojo-linux-amd64-1.0.0.tar.gz

# Déplacez le fichier Mojo dans le répertoire bin
RUN mv mojo-linux-amd64-1.0.0/mojo /usr/local/bin/mojo

# Installez les bibliothèques Python nécessaires
RUN pip3 install numpy pandas scikit-learn seaborn
# Installez les bibliothèques jupyter
# RUN pip3 install  jupyter
# Installez les bibliothèques keras
# RUN pip3 install  keras
# Installez les bibliothèques tensorflow
# RUN pip3 install tensorflow

# # Définissez l'entrée par défaut pour exécuter Mojo
ENTRYPOINT ["mojo"]
# # Lancez Jupyter Notebook
# CMD ["jupyter", "notebook", "--notebook-dir=/notebooks"]

