import binascii
from Cryptodome.Cipher import AES


def pad(data):
    padding_length = 16 - (len(data) % 16)
    return data + (b" " * padding_length)


def unpad(data):
    return data.rstrip(b" ")


def aes_encrypt(key, data):
    iv = b"0000000000000000"  # 16-byte IV for AES
    aes = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data)
    return aes.encrypt(padded_data)


def aes_decrypt(key, ciphertext):
    iv = b"0000000000000000"
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = aes.decrypt(ciphertext)
    return unpad(decrypted_data)


# Define a 16-byte key
key = b"1234567891234567"
plaintext = b"ABCDEF"

# Encrypt the plaintext
ciphertext = aes_encrypt(key, plaintext)
print("Ciphertext:", binascii.hexlify(ciphertext))

# Decrypt the ciphertext
decrypted_text = aes_decrypt(key, ciphertext)
print("Decrypted Text:", decrypted_text.decode())
