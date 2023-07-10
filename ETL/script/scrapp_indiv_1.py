import pandas as pd
from bs4 import BeautifulSoup
import unicodedata

def scrapping_index_html(filepath):
    # Ouvrir le fichier HTML
    print(filepath)
    with open(filepath) as file:
        soup = BeautifulSoup(file, "lxml")

    # Trouver toutes les tables dont le tbody est "JScaracCarac1", "JScaracCarac2" ou "JScaracCarac3"
    tables = soup.find_all("tbody", class_= ["JScaracCarac1", "JScaracCarac2", "JScaracCarac3", "JScaracCarac4", "JScaracCarac5", "JScaracCarac6"])

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
                row_data.append(unicodedata.normalize('NFKD', content).encode('ascii', 'ignore').decode('utf-8'))
            data.append(row_data)

    # Créer un DataFrame à partir des données extraites
    #df = pd.DataFrame(data)
    return data

#scrapping_index_html(index.html)

#df.T.to_excel("output_indiv_1.xlsx", sheet_name='Sheet_name_1')  

# Afficher le DataFrame
#print(df)
