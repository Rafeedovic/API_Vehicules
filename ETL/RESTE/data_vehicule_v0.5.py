import os
import pandas as pd
from sqlalchemy import create_engine

def extract_file_info(file_path):
    # Supprimer l'extension et diviser le chemin en segments
    file_path = file_path.replace("\\", "/")  # Remplacer les barres obliques inverses par des barres obliques
    segments = file_path.split("/")
    
    # Vérifier si le chemin correspond au format attendu
    if len(segments) < 2 or segments[-1] != "index.html":
        return ""
    
    # Supprimer la partie du chemin que vous souhaitez exclure
    segments = segments[:-1]
    
    # Extraire les informations spécifiques de chaque segment
    marque = ""
    modele = ""
    annee = ""
    config = ""
    
    if len(segments) >= 1:
        marque_full = segments[0].split("-")
        marque = marque_full[0]
        modele = ' '.join(marque_full[1:])

    if len(segments) >= 2:
        annee = segments[1]
    if len(segments) >= 3:
        config = segments[2]
        config = config.replace("+"," ")
    
    return [marque, modele, annee, config]

def find_index_html_files(folder_path):
    index_html_files = []
    for root, dirs, files in os.walk(folder_path):
        if len(dirs) == 0 and len(files) == 1 and files[0] == "index.html":
            file_path = os.path.join(root, files[0])
            file_path = file_path.replace("C:\\My Web Sites\\v7\\www.caradisiac.com\\fiches-techniques\\modele--", "")
            index_html_files.append(file_path)
    return index_html_files

def loading_db(df):
    # Nom de la table cible dans la base de données
    table_name = 'data'

    try:
        # Établir une connexion à la base de données MySQL
        engine = create_engine('mysql://root:@localhost/prjet_transport')
        
        # Insérer le dataframe dans la base de données
        df.to_sql(table_name, con=engine, if_exists='replace', index=True)
        
        # Fermer la connexion à la base de données
        engine.dispose()
        print("Insertion réussie dans la base de données.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'insertion des données :", str(e))

def main():
    # Exemple d'utilisation
    dossier_principal = "C:\\My Web Sites\\v7\\www.caradisiac.com\\fiches-techniques\\"
    resultat = find_index_html_files(dossier_principal)


    # Créer une DataFrame à partir des chemins de fichiers
    df = pd.DataFrame(resultat, columns=["Chemin"])

    # Extraire les informations spécifiques et les stocker dans les colonnes appropriées
    df[["Marque", "Modèle", "Année", "Config"]] = df["Chemin"].apply(extract_file_info).apply(pd.Series)


    # Supprimer les lignes avec des informations manquantes
    df.dropna(inplace=True)

    #df = df.drop(df.columns[0], axis=1)

    # Réinitialiser l'index de la DataFrame
    #df.reset_index(drop=True, inplace=True)

    #Loading
    print("LOADING IN EXCEL FILE ...... ")
    df.to_excel("output.xlsx", sheet_name='Sheet_name_1')  
    print("LOADING IN DATABASE   ...... ")
    loading_db(df)

if __name__=="__main__":
    main()