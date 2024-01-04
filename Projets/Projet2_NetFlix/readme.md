### PROJET2 prediction films

-les colonnes interessantes pour la suggestion de film sont:
acteur imdb film recommendation genre

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