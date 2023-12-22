import pandas  as pd

df=pd.read_csv("G:\\programmation\\WildCodeSchool\\Formation_IA_DATA_nov2023\\quêtes\\Semaine3\\live_coding\\Base_de_données_et_SQL\\Data_Immo.csv", sep=";", header=1,encoding='ISO-8859-1')
# header=1 pour indiquer que la deuxiéme ligne contient les entetes
#  sep=";"pour indiquer que le séparateur est un ; et non  ,
#  pour eviter l'erreur d'encodage encoding='ISO-8859-1'

df.head()  # Affiche les 5 premières lignes du DataFrame
df.info()  # Affiche un résumé concis du DataFrame
df.describe()  # Affiche des statistiques descriptives du DataFrame
