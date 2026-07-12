import socket
import threading
import logging
from config import HOST, PORT
clients = {}
logging.basicConfig(
    filename="chat.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s")
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except OSError:
                clients.pop(client, None)
                client.close()
def handle_client(client_socket):
    username = client_socket.recv(1024).decode()
    clients[client_socket] = username
    print(f"{username} joined the chat.")
    logging.info(f"{username} joined the chat.")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        logging.info(f"Encrypted message ({len(data)} bytes)")
        print("Encrypted message received")
        broadcast(data, client_socket)
    logging.info(f"{username} left the chat.")
    clients.pop(client_socket, None)
    client_socket.close()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server is listening on {HOST}:{PORT}")
while True:
    client_socket, client_address = server.accept()
    print(f"Client connected from {client_address}")
    thread = threading.Thread(
    target=handle_client,
    args=(client_socket,))
    thread.start()