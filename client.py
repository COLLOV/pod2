import requests
import os
import time

# Configuration
# Utilisation du proxy RunPod
# Format: https://POD_ID-PORT.proxy.runpod.net
# Exemple pour le port 80: https://abc123-80.proxy.runpod.net
SERVER_URL = os.getenv('SERVER_URL', 'https://POD_ID-80.proxy.runpod.net')

def send_message(message):
    try:
        response = requests.post(
            f"{SERVER_URL}/api/message",
            json={"message": message},
            timeout=5
        )
        
        if response.status_code == 200:
            print(f"Réponse du serveur: {response.json()}")
            return response.json()
        else:
            print(f"Erreur: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion: {e}")
        return None

def check_server_health():
    try:
        response = requests.get(f"{SERVER_URL}/api/health", timeout=5)
        return response.status_code == 200
    except:
        return False

if __name__ == '__main__':
    # Attente que le serveur soit prêt
    while not check_server_health():
        print("En attente du serveur...")
        time.sleep(5)
    
    # Exemple d'utilisation
    message = "Bonjour depuis le pod client!"
    send_message(message) 