import stomp
import base64
import ssl

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

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        print('Mensagem recebida: %s' % frame.body)
        # Enviar ack para a fila
        self.conn.ack(frame.headers['message-id'], frame.headers['subscription'])

def receive_from_queue():
    conn = stomp.Connection([(STOMP_SERVER, STOMP_PORT)])
    conn.set_ssl(for_hosts=[(STOMP_SERVER, STOMP_PORT)], ssl_version=ssl.PROTOCOL_TLSv1_2)
    conn.set_listener('', MyListener(conn))
    conn.connect(STOMP_USER, STOMP_PASSWORD, wait=True)
    conn.subscribe(destination=QUEUE_ID, id=1, ack='client-individual')
    print('Aguardando mensagens...')
    try:
        while True:
            pass
    except KeyboardInterrupt:
        conn.disconnect()

if __name__ == '__main__':
    receive_from_queue()
