import requests
import os

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

# Test d'envoi de message
response = requests.post(
    f"{SERVER_URL}/api/message",
    json={"message": "Test depuis ma machine locale"}
)

print(f"Réponse: {response.json()}") 