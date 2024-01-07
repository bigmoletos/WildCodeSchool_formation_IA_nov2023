### PROJET2 prediction films
-limiter la quantité et ne prendre moins 5000 films, ne pas prendre les series, faire le choix en fonction de l'imdb score et en fonction des genres les plus regardés, voir les stat des netflix et youtube pour connaitre les gouts des francais

-ne prendre que le francais
-les colonnes interessantes pour la suggestion de film sont:
acteur imdb film recommandation genre

-encoder les colonnes numerique
-trouver les plus proches voisins
-partir sur les 15 plus proches voisins puis trier par l'imdb puis trier par le genre

-faire juste un knn plus proche voisins pas les autres type knn

-pour les genre on aura beauoup de colonnes
-faire avant un clustering
-faire une prediction sur le meme cluster

-faire de l'ACP

-trouver la pertinence de la prediction  il faut donc trouver une metrique pertinente

-pour travailler sur du bigdata il faut prendre un échantillon des datasets
df.samples(n=20000, random_state=1)


#### info chatGpt
5 critères pertinents pour choisir un film :

**Genre** : Le genre d’un film (comédie, drame, action, etc.) peut grandement influencer sa popularité. Certains genres peuvent être plus populaires que d’autres en fonction du public cible5.
**Acteurs** : Les acteurs jouant dans le film peuvent avoir un impact significatif sur sa popularité. Les films avec des acteurs bien connus et appréciés ont tendance à attirer plus de spectateurs5.
**Réalisateur** : Le réalisateur d’un film peut également influencer sa popularité. Les films réalisés par des réalisateurs renommés sont souvent très attendus et bien reçus5.
**Critiques** : Les critiques de films peuvent influencer la décision des spectateurs de voir un film. Les films avec de bonnes critiques ont tendance à attirer plus de spectateurs6.
**Durée** : La durée d’un film peut également être un facteur important. Certains spectateurs préfèrent les films plus courts, tandis que d’autres préfèrent les films plus longs5.

#### info Bard

Voici quelques statistiques d'Allociné, YouTube et Netflix sur les films les plus regardés :

**Genre** : les films les plus regardés sont généralement des films d'action, de comédie, de science-fiction et de fantasy.
**Type** : les films les plus regardés sont généralement des films originaux, des suites et des préquelles.
**Durée** : les films les plus regardés ont généralement une durée de **2h à 2h30.**
**Producteur** : les films les plus regardés sont généralement produits par des studios hollywoodiens tels que Disney, Warner Bros. et Universal Pictures.
**Acteur** : les acteurs les plus populaires sont généralement ceux qui ont joué dans des films à succès tels que Tom Cruise, Scarlett Johansson et Robert Downey Jr.

**Les cinq critères** les plus pertinents pour faire un choix de films pour une salle de cinéma sont les suivants :

La **popularité du film** : il est important de choisir des films qui sont susceptibles d'attirer un large public.
La **qualité du film** : il est important de choisir des films qui ont reçu de bonnes critiques et qui sont susceptibles de plaire au public.
La **date de sortie du film** : il est important de choisir des films qui sont sortis récemment ou qui vont sortir prochainement.
Le **budget du film** : il est important de choisir des films qui ont un budget suffisant pour garantir une qualité de production élevée.
Les **restrictions d'âge** : il est important de choisir des films qui sont adaptés à la tranche d'âge de la clientèle de la salle de cinéma.
