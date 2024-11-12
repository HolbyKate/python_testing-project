import pandas as pd
import numpy as np

# Chargement du fichier CSV
df = pd.read_csv('donnees_non_propres.csv', encoding='utf-8', low_memory=False)

# Affichage des premières lignes et des informations sur le DataFrame
print(df.head())
print(df.info())

