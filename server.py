from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Configuration
PORT = os.getenv('PORT', 5000)
HOST = '0.0.0.0'

@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Message manquant'}), 400
    
    # Traitement du message reçu
    received_message = data['message']
    print(f"Message reçu: {received_message}")
    
    # Réponse
    return jsonify({
        'status': 'success',
        'received': received_message,
        'response': f'Message bien reçu: {received_message}'
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT) 