import pandas as pd
import numpy as np
import os

def nettoyer_texte(texte):
    """
    Nettoie le texte en supprimant les caractères non-ASCII.

    Args:
        texte (str ou autre): Le texte à nettoyer.

    Returns:
        str ou autre: Le texte nettoyé si c'était une chaîne, sinon la valeur originale.
    """
    if isinstance(texte, str):
        return ''.join(char for char in texte if ord(char) < 128)
    else:
        return texte

def traiter_morceau(df_chunk):
    """
    Traite un morceau du DataFrame en nettoyant le texte et en convertissant les types de données.

    Args:
        df_chunk (pd.DataFrame): Un morceau du DataFrame à traiter.

    Returns:
        pd.DataFrame: Le morceau de DataFrame traité.
    """
    # Convertir toutes les colonnes en type 'object'
    df_chunk = df_chunk.astype(object)

    # Appliquer la fonction nettoyer_texte à toutes les colonnes
    for col in df_chunk.columns:
        df_chunk[col] = df_chunk[col].apply(nettoyer_texte)

    # Convertir les colonnes numériques en type 'float'
    colonnes_numeriques = ['Colonne_2', 'Colonne_4', 'Colonne_6', 'Colonne_8', 'Colonne_10']
    for col in colonnes_numeriques:
        df_chunk[col] = pd.to_numeric(df_chunk[col], errors='coerce')

    return df_chunk

def main():
    """
    Fonction principale qui gère le processus de nettoyage des données.

    Cette fonction lit un fichier CSV volumineux par morceaux, nettoie les données,
    les trie et les enregistre dans un nouveau fichier CSV.
    """
    # Paramètres pour le traitement par morceaux
    chunksize = 10000  # Ajustez cette valeur selon votre mémoire disponible
    fichier_entree = 'donnees_non_propres.csv'
    fichier_sortie = 'donnees_nettoyees.csv'

    # Vérifier la taille du fichier d'entrée
    taille_fichier = os.path.getsize(fichier_entree)
    print(f"Taille du fichier d'entrée : {taille_fichier / (1024 * 1024):.2f} MB")

    total_lignes = sum(1 for _ in open(fichier_entree, 'r'))
    print(f"Nombre total de lignes dans le fichier : {total_lignes}")

    lignes_traitees = 0

    # Utiliser mode 'a' pour ajouter au fichier de sortie
    with open(fichier_sortie, 'w', newline='') as f_out:
        for chunk in pd.read_csv(fichier_entree, chunksize=chunksize):
            chunk_nettoye = traiter_morceau(chunk)
            
            # Écrire directement dans le fichier de sortie
            chunk_nettoye.to_csv(f_out, index=False, header=(lignes_traitees == 0))
            
            lignes_traitees += len(chunk)
            print(f"Traité {lignes_traitees} lignes sur {total_lignes}")

    print("Nettoyage terminé. Tri des données...")

    # Lire le fichier nettoyé, trier et réécrire
    df_final = pd.read_csv(fichier_sortie)
    df_final_trie = df_final.sort_values(by=['Colonne_1', 'Colonne_2'])
    df_final_trie.to_csv(fichier_sortie, index=False)

    print(f"Traitement terminé. Les données nettoyées et triées ont été enregistrées dans '{fichier_sortie}'.")
    print(f"Nombre total de lignes traitées : {len(df_final_trie)}")

if __name__ == "__main__":
    main()