# Comptez les valeurs manquantes par colonne
valeurs_manquantes = df.isnull().sum()

# Identifiez les lignes contenant des caractères non-ASCII
lignes_non_ascii = df.applymap(lambda x: not all(ord(c) < 128 for c in str(x))).any(axis=1)

# Comptez les erreurs de format pour les colonnes numériques
erreurs_format = {}
for col in ['Colonne_2', 'Colonne_4', 'Colonne_6', 'Colonne_8', 'Colonne_10']:
    erreurs_format[col] = df[col].apply(lambda x: not str(x).isdigit()).sum()

# Créez un DataFrame avec les statistiques d'erreurs
stats_erreurs = pd.DataFrame({
    'Valeurs manquantes': valeurs_manquantes,
    'Lignes avec caractères non-ASCII': lignes_non_ascii.sum(),
    'Erreurs de format (colonnes numériques)': pd.Series(erreurs_format)
})

# Exportez les statistiques d'erreurs vers une nouvelle feuille dans le même Google Sheet
feuille_stats = client.open('Nom_de_votre_feuille').add_worksheet(title='Statistiques_erreurs', rows=100, cols=20)
set_with_dataframe(feuille_stats, stats_erreurs)