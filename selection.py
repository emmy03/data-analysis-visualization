# Charger le module pandas
import pandas as pd

# Charger les données
surveys_df = pd.read_csv("data/surveys.csv")

# Sélectionner la colonne 'species_id'
id_especes = surveys_df['species_id']

# Obtenir les dimensions de la colonne
id_especes.shape

# Sélectionner plusieurs colonnes (avec une liste)
colonnes = ['year', 'month', 'day']
surveys_df[colonnes]

# Afficher les valeurs de la première ligne pour les colonnes 'species_id', 'plot_id', 'weight'
print(surveys_df.loc[0, ['species_id', 'plot_id', 'weight']])

# Afficher les valeurs des lignes 0 et 10 pour toutes les colonnes
print(surveys_df.loc[[0,10], :])

# Essayer d'afficher les valeurs des lignes 0, 10 et 35549 pour toutes les colonnes
try:
    print(surveys_df.loc[[0,10,35549], :])
except BaseException as erreur:
    # Afficher le message d'erreur si une exception est levée
    print(f'Le problème : {erreur}')

# Essayer d'afficher les valeurs des lignes 0 à 4 et des colonnes 1 à 4
try:
    print(surveys_df.loc[0:4,1:4])
except BaseException as erreur:
    # Afficher le message d'erreur si une exception est levée
    print(f'Le problème : {erreur}')

# Filtrer les lignes où l'année est supérieure ou égale à 2001
cond_annees = (surveys_df['year'] >= 2001)

# Filtrer les lignes où le poids est inférieur ou égal à 8
cond_poids = (surveys_df['weight'] <= 8)

# Afficher les lignes qui satisfont les deux conditions
print(surveys_df[cond_annees & cond_poids])