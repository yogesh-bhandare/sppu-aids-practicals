# Importing required libraries used
# to perform arithmetic operations
# on elliptic curves
from tinyec import registry
import secrets


# Function to calculate compress point
# of elliptic curves
def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]


# The elliptic curve which is used for the ECDH calculations
curve = registry.get_curve("brainpoolP256r1")

# Generation of secret key and public key
Ka = secrets.randbelow(curve.field.n)
X = Ka * curve.g
print("X:", compress(X))
Kb = secrets.randbelow(curve.field.n)
Y = Kb * curve.g
print("Y:", compress(Y))
print("Currently exchange the publickey (e.g. through Internet)")

# (A_SharedKey): represents user A
# (B_SharedKey): represents user B
A_SharedKey = Ka * Y
print("A shared key :", compress(A_SharedKey))
B_SharedKey = Kb * X
print("(B) shared key :", compress(B_SharedKey))
print("Equal shared keys:", A_SharedKey == B_SharedKey)
