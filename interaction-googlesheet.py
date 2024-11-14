# Pour interagir avec Google Sheets use gspread avec l'authentification OAuth2

mport gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

# Configurez les credentials (assurez-vous d'avoir un fichier JSON de clé de service)
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('chemin/vers/votre/fichier-cle.json', scopes=scope)
client = gspread.authorize(creds)

# Ouvrez le Google Sheet existant ou créez-en un nouveau
sheet = client.open('Nom_de_votre_feuille').worksheet('Nom_de_l_onglet')

# Exportez le DataFrame nettoyé
set_with_dataframe(sheet, df)