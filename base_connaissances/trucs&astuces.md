## voir https://github.com/MachineLearnia/Python-Machine-Learning/blob/master/27%20-%20Exploratory%20Data%20Analysis.ipynb
### pour avoir un affichage plus clair le :-<50
for col in df.select_dtypes(include=['float64','int64']):
    print(f"Moyenne col: {col:-<50}  {df[col].mean()} ")

Moyenne col: PassengerId---------------------------------------  446.0
Moyenne col: Survived------------------------------------------  0.3838383838383838
Moyenne col: Pclass--------------------------------------------  2.308641975308642
Moyenne col: Sex-----------------------------------------------  0.35241301907968575
Moyenne col: Age-----------------------------------------------  29.69911764705882
Moyenne col: SibSp---------------------------------------------  0.5230078563411896
Moyenne col: Parch---------------------------------------------  0.38159371492704824
Moyenne col: Fare----------------------------------------------  32.204207968574636


#### lzq graphiques à connaitrre pour l'EDA avec la correlation .corr()
plt.figure(figsize =(20,10))
sns.histplot(df[['Age','Sex','Survived']].dropna().corr())
sns.displot(df[['Age','Sex','Survived']], label='Survived')
sns.clustermap(df[['Age','Sex','Survived']].dropna().corr())
sns.countplot(df[['Age','Sex','Survived']].dropna().corr())
sns.lmplot(x='Age', y=col, hue='Survived', data=df)
plt.show()

pd.crosstab(index=[df['Age'], df['Sex'], df['Survived']], columns=df[col])

####  Correlation
df.select_dtypes(include=['float64','int64']).corr()["Survived"].sort_values(ascending=False)

####  Distribution des survivants en fonction du sexe
pd.crosstab(df["Survived"], df["Sex"])
