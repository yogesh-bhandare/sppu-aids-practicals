from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Signature import DSS
import base64


def generate_keys():
    """Generate ECC key pair"""
    key = ECC.generate(curve="P-256")
    return key.export_key(format="PEM"), key.public_key().export_key(format="PEM")


def encrypt(recipient_public_key, message):
    """Encrypt a message using recipient's public key"""
    # Import recipient's key and create ephemeral key
    recipient_key = ECC.import_key(recipient_public_key)
    ephemeral_key = ECC.generate(curve="P-256")

    # Generate shared secret via ECDH
    shared_point = ephemeral_key.d * recipient_key.pointQ

    # Convert the shared point x-coordinate to bytes
    shared_point_x = int(shared_point.x)
    shared_secret = shared_point_x.to_bytes(
        (shared_point_x.bit_length() + 7) // 8, byteorder="big"
    )

    # Generate a salt for HKDF
    salt = get_random_bytes(16)

    shared_key = HKDF(
        master=shared_secret,
        key_len=32,
        salt=salt,
        hashmod=SHA256,
        context=b"ECC-AES-Encryption",
    )

    # Encrypt with AES-GCM
    cipher = AES.new(shared_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode("utf-8"))

    # Package results
    return {
        "ephemeral_key": base64.b64encode(
            ephemeral_key.public_key().export_key(format="DER")
        ).decode(),
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "tag": base64.b64encode(tag).decode(),
        "salt": base64.b64encode(
            salt
        ).decode(),  # Include the salt in the encrypted data
    }


def decrypt(private_key, encrypted_data):
    """Decrypt message using private key"""
    key = ECC.import_key(private_key)
    ephemeral_key = ECC.import_key(base64.b64decode(encrypted_data["ephemeral_key"]))

    # Regenerate shared secret
    shared_point = key.d * ephemeral_key.pointQ

    # Convert the shared point x-coordinate to bytes
    shared_point_x = int(shared_point.x)
    shared_secret = shared_point_x.to_bytes(
        (shared_point_x.bit_length() + 7) // 8, byteorder="big"
    )

    # Use the same salt that was used for encryption
    salt = base64.b64decode(encrypted_data["salt"])

    shared_key = HKDF(
        master=shared_secret,
        key_len=32,
        salt=salt,
        hashmod=SHA256,
        context=b"ECC-AES-Encryption",
    )

    # Decrypt
    cipher = AES.new(
        shared_key, AES.MODE_GCM, nonce=base64.b64decode(encrypted_data["nonce"])
    )
    plaintext = cipher.decrypt_and_verify(
        base64.b64decode(encrypted_data["ciphertext"]),
        base64.b64decode(encrypted_data["tag"]),
    )
    return plaintext.decode("utf-8")


def sign(private_key, message):
    """Sign a message with ECDSA"""
    key = ECC.import_key(private_key)
    h = SHA256.new(message.encode("utf-8"))
    signature = DSS.new(key, "fips-186-3").sign(h)
    return base64.b64encode(signature).decode()


def verify(public_key, message, signature):
    """Verify an ECDSA signature"""
    key = ECC.import_key(public_key)
    h = SHA256.new(message.encode("utf-8"))
    try:
        DSS.new(key, "fips-186-3").verify(h, base64.b64decode(signature))
        return True
    except ValueError:
        return False


def main():
    # Generate keys
    private_key, public_key = generate_keys()
    print(f"Keys generated: {private_key.splitlines()[0]}...")

    # Test encryption/decryption
    message = "Hello, ECC encryption!"
    encrypted = encrypt(public_key, message)
    decrypted = decrypt(private_key, encrypted)
    print(f"Original: {message}\nDecrypted: {decrypted}")

    # Test signing/verification
    signature = sign(private_key, message)
    print(f"Signature valid: {verify(public_key, message, signature)}")
    print(
        f"Tampered message valid: {verify(public_key, message + 'tampered', signature)}"
    )


if __name__ == "__main__":
    main()
