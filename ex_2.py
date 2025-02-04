import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
surveys_df = pd.read_csv("data/surveys.csv")

# Filtrer les données pour ne garder que certaines espèces
cond_especes = surveys_df['species_id'].isin(['AS', 'CQ','OX', 'UL'])

# Afficher les identifiants de sites uniques pour les espèces sélectionnées
surveys_df[cond_especes]['plot_id'].unique()

# Filtrer les données pour ne garder que les sexes 'F' et 'M' et les poids positifs
cond_sexe = surveys_df['sex'].isin(['F','M'])
cond_poids = surveys_df['weight'] > 0
colonnes = ['weight', 'plot_id', 'sex']

# Sélectionner les colonnes d'intérêt pour les données filtrées
selection = surveys_df[cond_sexe & cond_poids][colonnes]

# Calculer la moyenne des poids par site et par sexe
moy_par_site_sexe = selection.groupby(['plot_id', 'sex']).mean()

# Transformer le tableau pour avoir les sexes en colonnes
table_site_sex = moy_par_site_sexe.unstack()

# Supprimer le niveau supérieur des colonnes
table_site_sex.columns = table_site_sex.columns.droplevel()

# Créer un graphique en barres pour les poids moyens par site et par sexe
table_site_sex.plot(kind='bar')

# Filtrer les données pour ne garder que celles sans sexe spécifié
surveys_df[~cond_sexe]

# Ajouter des étiquettes et un titre au graphique
plt.xlabel('Site')
plt.ylabel('Poids')
plt.title('Moyenne des poids par site et par sexe')
plt.show()