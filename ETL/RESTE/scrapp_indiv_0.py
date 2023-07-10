import pandas as pd
from bs4 import BeautifulSoup

# Ouvrir le fichier HTML
with open("index.html") as file:
    soup = BeautifulSoup(file, "lxml")

# Trouver toutes les tables de classe "A"
tables = soup.find_all("table", class_="listingTab")

# Créer une liste pour stocker les données extraites
data = []

# Parcourir les tables et extraire leur contenu
for table in tables:
    # Parcourir les lignes de la table
    rows = table.find_all("tr")
    for row in rows:
        # Parcourir les cellules de la ligne
        cells = row.find_all("td")
        row_data = []
        for cell in cells:
            # Extraire le contenu de la cellule
            content = cell.get_text()
            row_data.append(content)
        data.append(row_data)

# Créer un DataFrame à partir des données extraites
df = pd.DataFrame(data)

df.to_excel("output_indiv_0.xlsx", sheet_name='Sheet_name_1')  

# Afficher le DataFrame
print(df)
