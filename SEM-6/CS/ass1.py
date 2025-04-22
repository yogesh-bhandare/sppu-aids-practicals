# Implementation of S-DES

# pip install pycryptodomex

import binascii
from Cryptodome.Cipher import DES


def pad(data):
    padding_length = 8 - (len(data) % 8)  # Calculate required padding
    return data + (b" " * padding_length)  # Use spaces instead of null bytes


def des_encrypt(key, data):
    data = pad(data)  # Ensure data is a multiple of 8 bytes
    iv = b"00000000"  # Initialization Vector (8 bytes)
    des = DES.new(key, DES.MODE_CBC, iv)  # Create DES cipher object
    return des.encrypt(data)  # Encrypt and return ciphertext


def des_decrypt(key, ciphertext):
    iv = b"00000000"  # Same IV used for decryption
    des = DES.new(key, DES.MODE_CBC, iv)
    decrypted_data = des.decrypt(ciphertext)  # Decrypt data
    return decrypted_data.rstrip()  # Remove extra spaces from padding


key = b"sec__key"
plaintext = b"Yogesh Bhandare"

# Encrypt the plaintext
ciphertext = des_encrypt(key, plaintext)
print("Ciphertext:", binascii.hexlify(ciphertext))

# Decrypt the ciphertext
decrypted_text = des_decrypt(key, ciphertext)
print("Decrypted Text:", decrypted_text.decode())
