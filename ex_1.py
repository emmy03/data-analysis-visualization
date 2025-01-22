import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
especes_df = pd.read_csv("data/species.csv")
surveys_df = pd.read_csv("data/surveys.csv")

# Obtenir la liste des différents taxons
taxons_uniques = especes_df['taxa'].unique()
print("\nListe des différents taxons : ", taxons_uniques)

# Obtenir le nombre de taxons uniques
nombre_taxons = especes_df['taxa'].nunique()
print("\nNombre de différents taxons : ", nombre_taxons)

# Grouper les données par sexe et obtenit le nombre de femelles et de mâles
par_sex = surveys_df.groupby('sex')
count_sex = par_sex['record_id'].count()
print("\nNombre de femelles et de mâles : \n", count_sex)

# Grouper les données par deux colonnes et obtenir la moyenne
par_site_sex = surveys_df.groupby(['plot_id', 'sex'])
moyenne_par_site_sex = par_site_sex.mean(numeric_only=True)
print("\nMoyenne des variables par site et sexe : \n", moyenne_par_site_sex)

# Obtenir les statistiques descriptives des poids par site
par_site = surveys_df.groupby('plot_id')
stats_poids = par_site['weight'].describe()
print("\nStatistiques descriptives des poids par site : \n", stats_poids)

# Créer un graphique pour le poids médian par mois
par_mois = surveys_df.groupby('month')
medianes = par_mois['weight'].median()

# Tracer le graphique
medianes.plot(kind='line')
plt.xlabel('Mois')
plt.ylabel('Poids médian')
plt.title('Poids médian par mois')
plt.show()