import requests
import os
import json

def load_env():
    with open('.env') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Charger les variables d'environnement depuis .env
load_env()

# Récupérer le POD_ID depuis les variables d'environnement
POD_ID = os.getenv('POD_ID')
if not POD_ID:
    raise ValueError("POD_ID n'est pas défini dans le fichier .env")

SERVER_URL = f"https://{POD_ID}-80.proxy.runpod.net"

print(f"Tentative de connexion à : {SERVER_URL}")

try:
    # Test d'envoi de message
    response = requests.post(
        f"{SERVER_URL}/api/message",
        json={"message": "Test depuis ma machine locale"}
    )
    
    print(f"Status code: {response.status_code}")
    print(f"Réponse brute: {response.text}")
    
    if response.ok:  # Si status_code est 200-299
        try:
            print(f"Réponse JSON: {response.json()}")
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON: {e}")
    else:
        print(f"Erreur HTTP: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Erreur de connexion: {e}") 