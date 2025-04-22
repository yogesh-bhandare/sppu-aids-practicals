from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64


def generate_ecc_keypair():
    """Generate an ECC key pair using the P-256 curve"""
    # Generate a new ECC key (default is the NIST P-256 curve)
    key = ECC.generate(curve="P-256")

    # Extract the private key
    private_key = key.export_key(format="PEM")

    # Extract the public key
    public_key = key.public_key().export_key(format="PEM")

    return private_key, public_key


def ecc_encrypt(recipient_public_key, message):
    """
    Hybrid encryption using ECC for key exchange and AES for data encryption
    """
    # Import the recipient's public key
    recipient_key = ECC.import_key(recipient_public_key)

    # Generate an ephemeral ECC key pair
    ephemeral_key = ECC.generate(curve="P-256")

    # Perform ECDH key agreement
    shared_point = ephemeral_key.d * recipient_key.pointQ

    # Derive a symmetric encryption key from the shared point
    shared_key = HKDF(
        master=shared_point.x.to_bytes(
            (shared_point.x.bit_length() + 7) // 8, byteorder="big"
        ),
        key_len=32,
        salt=get_random_bytes(16),
        hashmod=SHA256,
        context=b"ECC-AES-Encryption",
    )

    # Encrypt the message using AES-GCM
    cipher = AES.new(shared_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode("utf-8"))

    # Export the ephemeral public key
    ephemeral_public_key = ephemeral_key.public_key().export_key(format="DER")

    # Package everything together
    encrypted_data = {
        "ephemeral_public_key": base64.b64encode(ephemeral_public_key).decode("utf-8"),
        "nonce": base64.b64encode(cipher.nonce).decode("utf-8"),
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8"),
        "tag": base64.b64encode(tag).decode("utf-8"),
    }

    return encrypted_data


def ecc_decrypt(private_key, encrypted_data):
    """
    Decrypt a message using the private key and the encrypted data
    """
    # Import the private key
    key = ECC.import_key(private_key)

    # Import the ephemeral public key
    ephemeral_public_key_bytes = base64.b64decode(
        encrypted_data["ephemeral_public_key"]
    )
    ephemeral_public_key = ECC.import_key(ephemeral_public_key_bytes)

    # Perform ECDH key agreement
    shared_point = key.d * ephemeral_public_key.pointQ

    # Derive the same symmetric encryption key
    shared_key = HKDF(
        master=shared_point.x.to_bytes(
            (shared_point.x.bit_length() + 7) // 8, byteorder="big"
        ),
        key_len=32,
        salt=get_random_bytes(
            16
        ),  # Note: In production, this salt should be communicated alongside the ciphertext
        hashmod=SHA256,
        context=b"ECC-AES-Encryption",
    )

    # Decrypt the message
    nonce = base64.b64decode(encrypted_data["nonce"])
    ciphertext = base64.b64decode(encrypted_data["ciphertext"])
    tag = base64.b64decode(encrypted_data["tag"])

    cipher = AES.new(shared_key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext.decode("utf-8")


def ecdsa_sign(private_key, message):
    """
    Sign a message using ECDSA
    """
    from Crypto.Signature import DSS
    from Crypto.Hash import SHA256

    # Import the private key
    key = ECC.import_key(private_key)

    # Create a signature object
    signer = DSS.new(key, "fips-186-3")

    # Hash the message
    h = SHA256.new(message.encode("utf-8"))

    # Sign the hash
    signature = signer.sign(h)

    return base64.b64encode(signature).decode("utf-8")


def ecdsa_verify(public_key, message, signature):
    """
    Verify a signature using ECDSA
    """
    from Crypto.Signature import DSS
    from Crypto.Hash import SHA256

    # Import the public key
    key = ECC.import_key(public_key)

    # Create a verification object
    verifier = DSS.new(key, "fips-186-3")

    # Hash the message
    h = SHA256.new(message.encode("utf-8"))

    # Verify the signature
    try:
        verifier.verify(h, base64.b64decode(signature))
        return True
    except ValueError:
        return False


def main():
    # Generate ECC key pair
    private_key, public_key = generate_ecc_keypair()
    print("ECC Key Pair Generated:")
    print(f"Private Key: {private_key.splitlines()[0]}...")
    print(f"Public Key: {public_key.splitlines()[0]}...")

    # Test encryption and decryption
    message = "Hello, ECC with PyCryptodome!"
    print(f"\nOriginal Message: {message}")

    encrypted = ecc_encrypt(public_key, message)
    print("\nEncrypted Data:")
    for key, value in encrypted.items():
        if key == "ciphertext":
            print(f"{key}: {value[:20]}...")
        else:
            print(f"{key}: {value[:20]}...")

    decrypted = ecc_decrypt(private_key, encrypted)
    print(f"\nDecrypted Message: {decrypted}")

    # Test ECDSA signing and verification
    print("\nTesting ECDSA:")
    signature = ecdsa_sign(private_key, message)
    print(f"Signature: {signature[:20]}...")

    verified = ecdsa_verify(public_key, message, signature)
    print(f"Signature Verification: {'Success' if verified else 'Failed'}")

    # Test with tampered message
    tampered_message = message + " Tampered!"
    tampered_verified = ecdsa_verify(public_key, tampered_message, signature)
    print(
        f"Tampered Message Verification: {'Success' if tampered_verified else 'Failed'}"
    )


if __name__ == "__main__":
    main()
