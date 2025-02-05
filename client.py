import requests
import os
import time

# Configuration
# Utilisation du DNS interne de RunPod
# Remplacer POD_ID par l'ID du pod serveur (ex: 'abc123.runpod.internal')
SERVER_URL = os.getenv('SERVER_URL', 'http://POD_ID.runpod.internal:80')

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