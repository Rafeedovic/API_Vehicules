import json

def json_load(df):
    json_data = df.to_json(orient='records')
    json_file_path = './Output/data.json'
    with open(json_file_path, 'w',encoding='utf-8') as file:
        file.write(json_data)
  
    print("Les données ont été écrites dans le fichier JSON.")
    
    with open(json_file_path, 'r',encoding='utf-8') as file:
        try:
            json_data = json.load(file)
            repaired_json = json.dumps(json_data, indent=4,ensure_ascii=False)  # Répare le JSON en ajoutant l'indentation
            with open(json_file_path, 'w',encoding='utf-8') as file:
                file.write(repaired_json)
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON : {str(e)}")
    
    return None
