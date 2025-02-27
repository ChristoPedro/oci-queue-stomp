from flask import Flask, request, jsonify
import stomp
import base64
import json
import ssl

app = Flask(__name__)

# Configurações do STOMP
# OCI Queue Message endpoing 
STOMP_SERVER = 'cell-1.queue.messaging.[Region].oci.oraclecloud.com'
STOMP_PORT = 61613
#Nome do usuário = "nome da tenancy/nome do usuário"
STOMP_USER = 'USERNAME'
# OCI Token Gerado na Tenancy
OCI_TOKEN = 'OCI_TOKEN'
# Token convertido para Base64
STOMP_PASSWORD = base64.b64encode(OCI_TOKEN.encode('utf-8')).decode('utf-8')
#OCID do OCI Queue
QUEUE_ID = 'Queue OCID'

# Função para enviar mensagem para a fila OCI
def send_to_queue(message):
    conn = stomp.Connection([(STOMP_SERVER, STOMP_PORT)])
    conn.set_ssl(
    for_hosts=[(STOMP_SERVER, STOMP_PORT)], ssl_version=ssl.PROTOCOL_TLSv1_2)
    conn.connect(STOMP_USER, STOMP_PASSWORD, wait=True)
    conn.send(body=message, destination=QUEUE_ID)
    conn.disconnect()

@app.route('/msg', methods=['POST'])
def receive_message():
    data = request.json
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
    send_to_queue(json.dumps(data))
    return jsonify({'status': 'Dados enviados com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)
