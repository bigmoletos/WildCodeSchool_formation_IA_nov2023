INSTALLATION DE MOJO AVEC UN CONTAINER DOCKER

Pour créer un Dockerfile pour faire fonctionner Mojo, vous pouvez suivre ces étapes :

1. **Créez un nouveau fichier** : Dans votre espace de travail VS Code, créez un nouveau fichier et nommez-le `Dockerfile` (sans extension de fichier).

2. **Ouvrez le Dockerfile** : Double-cliquez sur le Dockerfile pour l'ouvrir dans l'éditeur.

3. **Copiez et collez le contenu** : Copiez le contenu suivant et collez-le dans votre Dockerfile :

```dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl wget

RUN curl -LO https://github.com/modular-systems/mojo/releases/download/1.0.0/mojo-linux-amd64-1.0.0.tar.gz

RUN tar -xf mojo-linux-amd64-1.0.0.tar.gz

RUN mv mojo-linux-amd64-1.0.0/mojo /usr/local/bin/mojo

ENTRYPOINT ["mojo"]
```

4. **Enregistrez le Dockerfile** : Appuyez sur Ctrl+S pour enregistrer le Dockerfile.

5. **Construisez l'image Docker** : Ouvrez un terminal dans VS Code (Terminal > Nouveau terminal), puis exécutez la commande suivante pour construire l'image Docker :

```bash
docker build -t my-mojo-image .
```

6. **Exécutez le conteneur Docker** : Une fois l'image Docker construite, vous pouvez exécuter un conteneur à partir de cette image avec la commande suivante :

```bash
docker run -it --rm my-mojo-image
```

Cela devrait démarrer Mojo dans un conteneur Docker. Assurez-vous de remplacer `my-mojo-image` par le nom que vous souhaitez donner à votre image Docker.

Veuillez noter que vous devez avoir Docker installé et en cours d'exécution sur votre machine pour pouvoir construire et exécuter des images Docker.



Les corrections apportées sont les suivantes :
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
RUN pip3 install numpy pandas scikit-learn seaborn jupyter keras tensorflow

# Lancez Jupyter Notebook
CMD ["jupyter", "notebook", "--notebook-dir=/notebooks"]


L'image de base Ubuntu a été mise à jour à la version 20.04 pour garantir la compatibilité avec les bibliothèques Python les plus récentes.
Un répertoire a été créé pour l'environnement Jupyter pour y stocker les notebooks.
La commande CMD a été utilisée pour définir l'entrée par défaut pour exécuter Jupyter Notebook.
Avec ce Dockerfile, vous pouvez construire une image Docker qui contient tout ce dont vous avez besoin pour faire du machine learning avec le langage Mojo en utilisant un notebook Jupyter.

Voici les instructions pour construire l'image Docker :
```bash
docker build -t mojo_ia:latest .
```
Une fois l'image construite, vous pouvez l'exécuter en utilisant la commande suivante :
```bash
docker run -it -p 8888:8888 mojo_ia:latest
```
Cette commande va démarrer un conteneur Docker qui exécutera Jupyter Notebook sur le port 8888. Vous pouvez accéder à Jupyter Notebook en naviguant vers
```bash
http://localhost:8888
```
dans votre navigateur.

Pour plus d'informations sur l'utilisation de Jupyter Notebook, consultez la documentation officielle de Jupyter Notebook.