from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
def encrypt_message(message, key):
    cipher = AESGCM(key)
    nonce = os.urandom(12)
    message = message.encode()
    ciphertext = cipher.encrypt(
    nonce,
    message,
    None)
    return nonce + ciphertext
def decrypt_message(data, key):
    cipher = AESGCM(key)
    nonce = data[:12]
    ciphertext = data[12:]
    message = cipher.decrypt(
        nonce,
        ciphertext,
        None)
    return message.decode()