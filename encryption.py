from Crypto.Cipher import AES
import base64
import os

key = os.environ.get("AES_SECRET_KEY",).encode('utf-8')  # 32 bytes

def pad(data):
    return data + (16 - len(data) % 16) * chr(16 - len(data) % 16)

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data).encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')
