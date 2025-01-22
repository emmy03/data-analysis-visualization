# Importer la bibliothèque "pandas"
import pandas as pd

#Importer la bibliothèque "matplotlib"
import matplotlib.pyplot as plt

# Chargement des données du fichier "data/surveys.csv"
surveys_df = pd.read_csv("data/surveys.csv")

# Afficher les quelques premières enregisrements
surveys_df.head()

# Obtenir les dimensions du DataFrame
surveys_df.shape

# Obtenir la liste des noms de colonnes
surveys_df.columns

# Une colonne est un objet de type "Series"
surveys_df['weight'].describe()

# Calculer des statistiques descriptives par colonne
print("Valeurs non nulles : ", surveys_df['weight'].count())
print("Moyenne des valeurs : ", surveys_df['weight'].mean())
print("Deviation standard : ", surveys_df['weight'].std())
print("Valeur minimale : ", surveys_df['weight'].min())
print("Valeur maximale : ", surveys_df['weight'].max())

# Créer une nouvelle colonne
surveys_df['poids_kg'] = surveys_df['weight'] / 1000

# Afficher les dernières lignes
print(surveys_df.tail())

# Grouper les données par sexe
par_sex = surveys_df.groupby('sex')
print(par_sex)

# Obtenir des statistiques pour toutes les variables numériques
print(par_sex.describe())

# Obtenir unisuement la moyenne de chaque colonne
print(par_sex.mean(numeric_only=True))

# Obtenir la taille de population de l'espèce 'AB'
par_espece = surveys_df.groupby('species_id')
print(par_espece.head())
print(par_espece['record_id'].count()['AB'])

# Créer des graphiques à partir de Pandas
par_site = surveys_df.groupby(['plot_id'])
par_site['record_id'].count().plot(kind='bar')

plt.show()