def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primitive_root(p):
    """Find a primitive root modulo p"""
    if not is_prime(p):
        return None

    # Find factors of p-1
    phi = p - 1
    factors = set()
    n = phi
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)

    # Check numbers to find a primitive root
    for g in range(2, p):
        is_primitive = True
        for factor in factors:
            if pow(g, phi // factor, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return g
    return None


class DiffieHellman:
    def __init__(self, p=None, g=None):
        """Initialize with prime p and primitive root g"""
        # Default values if none provided
        self.p = p if p else 23
        self.g = g if g else 5

        # Validate or find parameters
        if not is_prime(self.p):
            raise ValueError("p must be prime")
        if not g:
            self.g = find_primitive_root(self.p)
        if self.g is None or self.g >= self.p:
            raise ValueError("Invalid primitive root")

    def generate_private_key(self):
        """Generate a private key (random number < p)"""
        import random

        return random.randint(2, self.p - 2)

    def generate_public_key(self, private_key):
        """Generate public key: g^(private_key) mod p"""
        return pow(self.g, private_key, self.p)

    def generate_shared_secret(self, private_key, other_public_key):
        """Generate shared secret: public_key^(private_key) mod p"""
        return pow(other_public_key, private_key, self.p)


# Example usage
def demonstrate_diffie_hellman():
    # Initialize with common parameters
    p = int(input("Enter value of p: "))
    g = int(input("Enter value of g: "))
    dh = DiffieHellman(p=p, g=g)

    # Alice's keys
    alice_private = dh.generate_private_key()
    alice_public = dh.generate_public_key(alice_private)

    # Bob's keys
    bob_private = dh.generate_private_key()
    bob_public = dh.generate_public_key(bob_private)

    # Shared secrets
    alice_shared = dh.generate_shared_secret(alice_private, bob_public)
    bob_shared = dh.generate_shared_secret(bob_private, alice_public)

    # Display results
    print(f"Prime (p): {dh.p}")
    print(f"Primitive root (g): {dh.g}")
    print(f"Alice's private key: {alice_private}")
    print(f"Alice's public key: {alice_public}")
    print(f"Bob's private key: {bob_private}")
    print(f"Bob's public key: {bob_public}")
    print(f"Alice's shared secret: {alice_shared}")
    print(f"Bob's shared secret: {bob_shared}")
    print(f"Keys match: {alice_shared == bob_shared}")


if __name__ == "__main__":
    demonstrate_diffie_hellman()
