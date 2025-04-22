def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """Calculate the modular multiplicative inverse of a mod m"""

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    _, x, _ = extended_gcd(a, m)
    return (x % m + m) % m


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class RSA:
    def __init__(self, p=61, q=53):
        """Initialize RSA with two prime numbers"""
        if not (is_prime(p) and is_prime(q)):
            raise ValueError("Both p and q must be prime")
        if p == q:
            raise ValueError("p and q must be different")

        self.n = p * q
        self.phi = (p - 1) * (q - 1)

        # Choose e (public exponent)
        self.e = 17  # Common choice, must be coprime with phi
        if gcd(self.e, self.phi) != 1:
            raise ValueError("e must be coprime with phi(n)")

        # Calculate d (private exponent)
        self.d = mod_inverse(self.e, self.phi)

    def encrypt(self, plaintext):
        """Encrypt plaintext (integer < n)"""
        if not 0 <= plaintext < self.n:
            raise ValueError(f"Plaintext must be between 0 and {self.n - 1}")
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        """Decrypt ciphertext"""
        if not 0 <= ciphertext < self.n:
            raise ValueError(f"Ciphertext must be between 0 and {self.n - 1}")
        return pow(ciphertext, self.d, self.n)


def demonstrate_rsa():
    # Create RSA instance with default primes
    rsa = RSA()

    # Example message (must be < n)
    message = 42
    print(f"Original message: {message}")

    # Encrypt
    ciphertext = rsa.encrypt(message)
    print(f"Public key (e, n): ({rsa.e}, {rsa.n})")
    print(f"Ciphertext: {ciphertext}")

    # Decrypt
    plaintext = rsa.decrypt(ciphertext)
    print(f"Private key (d, n): ({rsa.d}, {rsa.n})")
    print(f"Decrypted message: {plaintext}")

    # Verify
    print(f"Decryption successful: {plaintext == message}")


if __name__ == "__main__":
    demonstrate_rsa()
