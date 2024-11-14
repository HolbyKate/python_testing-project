import pandas as pd
import numpy as np

# Charger les données
df = pd.read_csv('donnees_non_propres.csv')

# Afficher les premières lignes et les informations du DataFrame
print(df.head())
print(df.info())


def nettoyer_texte(texte):
    if isinstance(texte, str):
        return ''.join(char for char in texte if ord(char) < 128)
    else:
        return texte


# Convertir toutes les colonnes en type 'object'
df = df.astype(object)

# Appliquer la fonction nettoyer_texte à toutes les colonnes
for col in df.columns:
    df[col] = df[col].apply(nettoyer_texte)

# Convertir les colonnes numériques en type 'float'
colonnes_numeriques = ['Colonne_2', 'Colonne_4',
                       'Colonne_6', 'Colonne_8', 'Colonne_10']
for col in colonnes_numeriques:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Trier le DataFrame
df = df.sort_values(by=['Colonne_1', 'Colonne_2'])

# Réinitialiser l'index
df = df.reset_index(drop=True)

# Enregistrer le DataFrame nettoyé
df.to_csv('donnees_nettoyees.csv', index=False)

print("Nettoyage terminé. Les données ont été enregistrées dans 'donnees_nettoyees.csv'.")
