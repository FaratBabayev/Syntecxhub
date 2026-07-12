import socket
import threading
from crypto import encrypt_message, decrypt_message
from config import SECRET_KEY
def receive_messages():
    while True:
        data = client.recv(1024)
        if not data:
            break
        message = decrypt_message(data, SECRET_KEY)
        print("\nReceived:", message)
HOST = "127.0.0.1"
PORT = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
username = input("Username: ")
client.send(username.encode())
print("Connected to the server!")
receiver = threading.Thread(target=receive_messages)
receiver.start()
while True:
    message = input("You: ")
    full_message = f"{username}: {message}"
    encrypted = encrypt_message(full_message, SECRET_KEY)
    client.send(encrypted)
    if message.lower() == "exit":
        break
receiver.join()
client.close()