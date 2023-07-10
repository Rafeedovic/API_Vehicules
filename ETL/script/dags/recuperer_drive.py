from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authentification avec Google Drive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# ID du dossier sur Google Drive
folder_id = '1AAqT-4uRX7owVK6EUydxs_08srfN2VKh'  # Remplacez 'INSERT_FOLDER_ID_HERE' par l'ID réel de votre dossier A

# Chemin local du dossier de sortie
output_folder_path = 'output'

# Création du dossier de sortie s'il n'existe pas
import os
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Récupération des fichiers du dossier sur Google Drive
folder_query = f"'{folder_id}' in parents and trashed=false"
file_list = drive.ListFile({'q': folder_query}).GetList()

# Téléchargement des fichiers dans le dossier de sortie
for file in file_list:
    file_path = os.path.join(output_folder_path, file['title'])
    file.GetContentFile(file_path)
    print(f"Téléchargé : {file['title']}")
