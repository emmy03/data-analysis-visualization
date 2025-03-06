# Importer la bibliothèque "pandas"
import pandas as pd

# Charger les données
surveys_df = pd.read_csv("data/surveys.csv")

# Afficher les types de données des colonnes
print(surveys_df.dtypes)

# Convertir le type de données
surveys_df['month'] = surveys_df['month'].astype('str')
print(surveys_df['month'].dtype)

print(surveys_df['month'].describe())