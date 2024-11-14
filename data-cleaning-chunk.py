import pandas as pd
import numpy as np


def nettoyer_texte(texte):
    """_summary_

    Args:
        texte (_type_): _description_

    Returns:
        _type_: _description_
    """
    if isinstance(texte, str):
        return ''.join(char for char in texte if ord(char) < 128)
    else:
        return texte


def traiter_morceau(df_chunk):
    """_summary_

    Args:
        df_chunk (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Convertir toutes les colonnes en type 'object'
    df_chunk = df_chunk.astype(object)

    # Appliquer la fonction nettoyer_texte à toutes les colonnes
    for col in df_chunk.columns:
        df_chunk[col] = df_chunk[col].apply(nettoyer_texte)

    # Convertir les colonnes numériques en type 'float'
    colonnes_numeriques = ['Colonne_2', 'Colonne_4',
                           'Colonne_6', 'Colonne_8', 'Colonne_10']
    for col in colonnes_numeriques:
        df_chunk[col] = pd.to_numeric(df_chunk[col], errors='coerce')

    return df_chunk


# Paramètres pour le traitement par morceaux
chunksize = 10000  # Ajustez cette valeur selon votre mémoire disponible
fichier_entree = 'donnees_non_propres.csv'
fichier_sortie = 'donnees_nettoyees.csv'

# Initialiser un DataFrame vide pour stocker les résultats
df_resultat = pd.DataFrame()

# Lire et traiter le fichier par morceaux
for chunk in pd.read_csv(fichier_entree, chunksize=chunksize):
    # Traiter le morceau
    chunk_nettoye = traiter_morceau(chunk)

    # Ajouter le morceau traité au DataFrame résultat
    df_resultat = pd.concat([df_resultat, chunk_nettoye], ignore_index=True)

    # Afficher la progression
    print(f"Traité jusqu'à l'index {len(df_resultat)}")

# Trier le DataFrame final
print("Tri du DataFrame final...")
df_resultat = df_resultat.sort_values(by=['Colonne_1', 'Colonne_2'])

# Réinitialiser l'index
df_resultat = df_resultat.reset_index(drop=True)

# Enregistrer le DataFrame nettoyé
print("Enregistrement des données nettoyées...")
df_resultat.to_csv(fichier_sortie, index=False)

print(f"Nettoyage terminé. Les données ont été enregistrées dans 'donnees_nettoyees.csv'.")
