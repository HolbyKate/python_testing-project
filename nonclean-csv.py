import csv
import random
import string


def generate_messy_data():
    # Générer une chaîne aléatoire avec des caractères spéciaux
    return ''.join(random.choice(string.ascii_letters + string.digits + 'éèàùâêîôûç /\\') for _ in range(10))


def generate_messy_number():
    # Générer un nombre aléatoire, parfois avec des erreurs
    if random.random() < 0.1:  # 10% de chance d'avoir une erreur
        return random.choice(['', 'N/A', 'error', str(random.randint(0, 100000))])
    return str(random.randint(0, 100000))


# Création du fichier CSV
with open('donnees_non_propres.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # En-têtes
    headers = [f'Colonne_{i+1}' for i in range(10)]
    writer.writerow(headers)

    # Générer 1000 lignes de données
    for _ in range(1000):
        row = []
        for i in range(10):
            if i % 2 == 0:
                row.append(generate_messy_data())
            else:
                row.append(generate_messy_number())
        writer.writerow(row)

print("Le fichier 'donnees_non_propres.csv' a été créé avec succès.")
