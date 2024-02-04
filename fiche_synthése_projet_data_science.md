# Étapes de réalisation d'un projet Data Science pro

1. **Déterminer si on fait de l'apprentissage supervisé ou non supervisé.**
2. **Déterminer si on fait de la régression ou de la classification.**
3. **EDA :**
    - Analyse descriptive des données : stats (tendance centrale, forme (kurtosis, skewness)...), nettoyage, valeurs manquantes (fillna, dropna, isna..), outliers (boxplot, écart interquartile, z-score).
    - Analyse exploratoire : corrélation linéaire (quanti-quanti), Chi2 (quali-quali), ANOVA (quanti-quali), heatmap, pairplot.
    - Tests statistiques : normalité, homoscédasticité, colinéarité, stationnarité, analyse de la p-value...
4. **Preprocessing :**
    - Encodage : dummies, one-hot...
    - Standardisation : min_max, centrage-réduction...
    - Réduction de dimension : ACP et analyse du cercle de corrélation.
5. **Les pré-requis des modèles à utiliser.**
6. **Modélisation :**
    - Choix d'une liste de modèles qu'on classe par complexité (du moins au plus).
    - Grid search.
    - Train_test split avec KFold (pour vérifier l'impact de la distribution des splits sur les résultats).
    - Choix des métriques d'évaluation des modèles.
    - Clustering sur les données pour un score plus adapté.
    - Pipeline pour automatiser les étapes précédentes.
7. **Monitoring du modèle :** évaluation au cours du temps de l'amélioration ou de la dégradation des performances, et potentiel changement de modèle.
8. **Intégration dans une application user-friendly.**
