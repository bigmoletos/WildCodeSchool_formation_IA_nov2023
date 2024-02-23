
## DataFrame : name_basics
- **Shape** : `(13144850, 6)`
- **Liste des colonnes** : `['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']`
- **Liste des colonnes numériques** : `[]`
- **Liste des colonnes non numériques** : `['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']`
- **Colonnes avec des NA** :
```
nconst                     0
primaryName                7
birthYear                  0
deathYear                  0
primaryProfession    2630039
knownForTitles             0
dtype: int64
```
- **Noms des colonnes avec au moins une valeur NA** : `['primaryName', 'primaryProfession']`
- **Nombre de lignes avec au moins une valeur NA** : `2630045`
- **head** :
```
nconst | primaryName | birthYear | deathYear | primaryProfession | knownForTitles
nm0000001 | Fred Astaire | 1899 | 1987 | soundtrack,actor,miscellaneous | tt0072308,tt0053137,tt0050419,tt0031983
nm0000002 | Lauren Bacall | 1924 | 2014 | actress,soundtrack | tt0037382,tt0117057,tt0038355,tt0075213
```

## DataFrame : title_akas
- **Shape** : `(38349425, 8)`
- **Liste des colonnes** : `['titleId', 'ordering', 'title', 'region', 'language', 'types', 'attributes', 'isOriginalTitle']`
- **Liste des colonnes numériques** : `['ordering']`
- **Liste des colonnes non numériques** : `['titleId', 'title', 'region', 'language', 'types', 'attributes', 'isOriginalTitle']`
- **Colonnes avec des NA** :
```
titleId              0
ordering             0
title               18
region             117
language             0
types                0
attributes           0
isOriginalTitle      0
dtype: int64
```
- **Noms des colonnes avec au moins une valeur NA** : `['title', 'region']`
- **Nombre de lignes avec au moins une valeur NA** : `135`
- **head** :
```
titleId | ordering | title | region | language | types | attributes | isOriginalTitle
tt0000001 | 1 | Карменсіта | UA | \N | imdbDisplay | \N | 0
tt0000001 | 2 | Carmencita | DE | \N | \N | literal title | 0
```

## DataFrame : title_basics
- **Shape** : `(10450471, 9)`
- **Liste des colonnes** : `['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']`
- **Liste des colonnes numériques** : `[]`
- **Liste des colonnes non numériques** : `['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']`
- **Colonnes avec des NA** :
```
tconst             0
titleType          0
primaryTitle      17
originalTitle     17
isAdult            0
startYear          0
endYear            0
runtimeMinutes     0
genres            18
dtype: int64
```
- **Noms des colonnes avec au moins une valeur NA** : `['primaryTitle', 'originalTitle', 'genres']`
- **Nombre de lignes avec au moins une valeur NA** : `35`
- **head** :
```
tconst | titleType | primaryTitle | originalTitle | isAdult | startYear | endYear | runtimeMinutes | genres
tt0000001 | short | Carmencita | Carmencita | 0 | 1894 | \N | 1 | Documentary,Short
tt0000002 | short | Le clown et ses chiens | Le clown et ses chiens | 0 | 1892 | \N | 5 | Animation,Short
```

## DataFrame : title_crew
- **Shape** : `(10450471, 3)`
- **Liste des colonnes** : `['tconst', 'directors', 'writers']`
- **Liste des colonnes numériques** : `[]`
- **Liste des colonnes non numériques** : `['tconst', 'directors', 'writers']`
- **Colonnes avec des NA** :
```
tconst       0
directors    0
writers      0
dtype: int64
```
- **Noms des colonnes avec au moins une valeur NA** : `[]`
- **Nombre de lignes avec au moins une valeur NA** : `0`
- **head** :
```
tconst | directors | writers
tt0000001 | nm0005690 | \N
tt0000002 | nm0721526 | \N
```

## DataFrame : title_episode
- **Shape** : `(7984745, 4)`
- **Liste des colonnes** : `['tconst', 'parentTconst', 'seasonNumber', 'episodeNumber']`
- **Liste des colonnes numériques** : `[]`
- **Liste des colonnes non numériques** : `['tconst', 'parentTconst', 'seasonNumber', 'episodeNumber']`
- **Colonnes avec des NA** :
```
tconst           0
parentTconst     0
seasonNumber     0
episodeNumber    0
dtype: int64
```
- **Noms des colonnes avec au moins une valeur NA** : `[]`
- **Nombre de lignes avec au moins une valeur NA** : `0`
- **head** :
```
tconst | parentTconst | seasonNumber | episodeNumber
tt0041951 | tt0041038 | 1 | 9
tt0042816 | tt0989125 | 1 | 17
```

## DataFrame : title_principals
- **Shape** : `(59896759, 6)`
- **Liste des colonnes** : `['tconst', 'ordering', 'nconst', 'category', 'job', 'characters']`
- **Liste des colonnes numériques** : `['ordering']`
- **Liste des colonnes non numériques** : `['tconst', 'nconst', 'category', 'job', 'characters']`
- **Colonnes avec des NA** :
```
tconst        0
ordering      0
nconst        0
category      0
job           0
characters    0
dtype: int64
```
- **Noms des colonnes avec au moins une valeur NA** : `[]`
- **Nombre de lignes avec au moins une valeur NA** : `0`
- **head** :
```
tconst | ordering | nconst | category | job | characters
tt0000001 | 1 | nm1588970 | self | \N | ["Self"]
tt0000001 | 2 | nm0005690 | director | \N | \N
```

## DataFrame : title_ratings
- **Shape** : `(1386077, 3)`
- **Liste des colonnes** : `['tconst', 'averageRating', 'numVotes']`
- **Liste des colonnes numériques** : `['averageRating', 'numVotes']`
- **Liste des colonnes non numériques** : `['tconst']`
- **Colonnes avec des NA** :
```
tconst           0
averageRating    0
numVotes         0
dtype: int64
```
- **Noms des colonnes avec au moins une valeur NA** : `[]`
- **Nombre de lignes avec au moins une valeur NA** : `0`
- **head** :
```
tconst | averageRating | numVotes
tt0000001 | 5.7 | 2014
tt0000002 | 5.7 | 272
```
