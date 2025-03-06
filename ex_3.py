import pandas as pd

surveys_df = pd.read_csv("data/surveys.csv")

# Ne peut pas convertir les valeurs non finies (infini ou NaN) en entiers
try:
    surveys_df['weight'].astype('int64')
except BaseException as erreur:
    print(f'La raison : {erreur}')

# Convertir 'plot_id' en flottant
surveys_df['plot_id'] = surveys_df['plot_id'].astype('float')
print(surveys_df['plot_id'].dtype)

# Déterminer les valeurs non finies, renvoie un masque booléen
print(surveys_df.isna())

# Déterminer les lignes contenant au moins une valeur non finie
masque_nan = surveys_df.isna().any(axis='columns').head()
print(masque_nan)

# Afficher le nombre d'enregistrements par 'species_id' pour les lignes où la colonne 'weight' contient des valeurs non finies
une_selection = surveys_df[surveys_df['weight'].isna()]
print(une_selection.groupby('species_id')['record_id'].count())

# Afficher le nombre d'observation de la colonne 'weight' et sa moyenne 
print(surveys_df['weight'].count(), surveys_df['weight'].mean())

# Créer une copie pour ne pas modifier l'objet original
copie_surveys = surveys_df.copy()

# Remplacer les valeurs non finies par la moyenne
copie_surveys['weight'] = copie_surveys['weight'].fillna(
    copie_surveys['weight'].mean())

# Même moyenne mais toutes les valeurs sont finies
print(copie_surveys['weight'].count(), copie_surveys['weight'].mean())

# Puisqu'il n'y a plus de valeurs non finies, on peut convertir 'weight' en entier
copie_surveys['weight'] = copie_surveys['weight'].astype('int64')
print(copie_surveys['weight'])
print("Moyenne : ", copie_surveys['weight'].mean())

