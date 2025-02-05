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

SERVER_URL = f"https://{POD_ID}-8080.proxy.runpod.net"

print(f"Tentative de connexion à : {SERVER_URL}")

try:
    # Test de l'endpoint de santé d'abord
    health_response = requests.get(f"{SERVER_URL}/api/health")
    print(f"Health check status: {health_response.status_code}")
    print(f"Health check response: {health_response.text}")
    
    if health_response.ok:
        # Si le health check est ok, on teste l'envoi de message
        response = requests.post(
            f"{SERVER_URL}/api/message",
            json={"message": "Test depuis ma machine locale"}
        )
        
        print(f"Message status code: {response.status_code}")
        print(f"Message response: {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"Erreur de connexion: {e}") 