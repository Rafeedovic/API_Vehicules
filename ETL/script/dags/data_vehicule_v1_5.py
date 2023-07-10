import os
import pandas as pd
from sqlalchemy import create_engine
from scrapp_indiv_1 import *
from json_repair import * 

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
    i=0
    for root, dirs, files in os.walk(folder_path):
        if len(dirs) == 0 and len(files) == 1 and files[0] == "index.html":
            while (i<10):
                file_path = os.path.join(root, files[0])
                caracteristiques = scrapping_index_html(filepath=file_path)
                i+=1
                print(i)
                file_path = file_path.replace("fiches-techniques\\modele--", "")
                index_html_files.append([file_path,caracteristiques])
    return index_html_files

def nom_colonnes_except_marque_modele_annee_config(row):
    return [case[0] for case in row]

def distribute_caracteristiques(row):
    list_val = [data for col, data in row]
    return list_val

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

def vider_dossier(dossier):
    for fichier in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, fichier)
        if os.path.isfile(chemin_fichier):
            os.remove(chemin_fichier)
        
def main_etl():
    #vider_dossier('.\\Output\\')
    # Exemple d'utilisation
    dossier_principal = "fiches-techniques\\"
    resultat = find_index_html_files(dossier_principal)
    #print(len(resultat))
    # Créer une DataFrame à partir des chemins de fichiers
    df = pd.DataFrame(resultat, columns=["Chemin","Caractéristiques"])
    print(df["Caractéristiques"][0])
    liste_nom_colonnes_except_marque_modele_annee_config = nom_colonnes_except_marque_modele_annee_config(df["Caractéristiques"][0])
    # Extraire les informations spécifiques et les stocker dans les colonnes appropriées
    df[["Marque", "Modèle", "Année", "Config"]] = df["Chemin"].apply(extract_file_info).apply(pd.Series)
    df[liste_nom_colonnes_except_marque_modele_annee_config] = df["Caractéristiques"].apply(distribute_caracteristiques).apply(pd.Series)

    # Supprimer les lignes avec des informations manquantes
    df.dropna(inplace=True)

    df = df.drop([df.columns[0],df.columns[1]], axis=1)
    #df = df.drop(df.columns[0], axis=1)

    # Réinitialiser l'index de la DataFrame
    #df.reset_index(drop=True, inplace=True)

    #Loading
    print("LOADING IN EXCEL FILE ...... ")
    #print(df)
    df.to_excel("./Output/output.xlsx", sheet_name='Sheet_name_1')  
    print("LOADING IN DATABASE   ...... ")
    loading_db(df)

    print("LOADING IN JSON   ...... ")
    json_load(df)


main_etl()