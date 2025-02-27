# Projeto Python STOMP com Flask e OCI Queue

Este projeto demonstra como receber e enviar mensagens para OCI Queue usando o protocolo STOMP.

## Requisitos

- Python 3.x
- Flask
- stomp.py

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/python-stomp.git
    cd python-stomp
    ```

2. Crie um ambiente virtual e ative-o:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

## Configuração

Atualize as seguintes variáveis nos arquivos `msg_producer.py` e `msg_consumer.py` com suas informações:

- `STOMP_SERVER`
- `STOMP_USER`
- `OCI_TOKEN`
- `QUEUE_ID`

## Executando o Produtor

1. Inicie o servidor Flask:

    ```sh
    python msg_producer.py
    ```

2. Envie uma mensagem para o endpoint `/msg` usando o comando curl:

    ```sh
    curl  -X POST \
    '127.0.0.1:5000/msg' \
    --header 'Content-Type: application/json' \
    -d '{"Teste": "Queue"}'
    ```

## Executando o Consumidor

1. Inicie o consumidor:

    ```sh
    python msg_consumer.py
    ```

2. O consumidor ficará aguardando mensagens e imprimirá cada mensagem recebida no console.
