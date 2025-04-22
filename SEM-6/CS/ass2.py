# S-AES Implementation

# S-Box and Inverse S-Box
s_box = [0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5, 0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7]


# Key Expansion
def expand_key(key):
    def g(w, rcon):
        # Rotate nibbles
        rotated = ((w << 4) | (w >> 4)) & 0xFF
        # Substitute nibbles
        n0 = s_box[(rotated >> 4) & 0xF]
        n1 = s_box[rotated & 0xF]
        return ((n0 << 4) | n1) ^ rcon

    w0 = (key >> 8) & 0xFF
    w1 = key & 0xFF
    # Round 1 constants
    w2 = w0 ^ g(w1, 0x80)
    w3 = w2 ^ w1
    # Round 2 constants
    w4 = w2 ^ g(w3, 0x30)
    w5 = w4 ^ w3

    return [(w0 << 8) | w1, (w2 << 8) | w3, (w4 << 8) | w5]


# SubNibbles
def sub_nibbles(state):
    return (
        s_box[(state >> 12) & 0xF] << 12
        | s_box[(state >> 8) & 0xF] << 8
        | s_box[(state >> 4) & 0xF] << 4
        | s_box[state & 0xF]
    )


# ShiftRows
def shift_rows(state):
    return (
        (state & 0xF000)
        | ((state & 0x0F00) >> 4)
        | ((state & 0x00F0) << 4)
        | (state & 0x000F)
    )


# MixColumns
def gf_mult(a, b):
    product = 0
    for _ in range(4):
        if b & 1:
            product ^= a
        a <<= 1
        if a & 0x10:
            a ^= 0b10011  # x^4 + x + 1
        b >>= 1
    return product & 0xF


def mix_columns(state):
    s0 = (state >> 12) & 0xF
    s1 = (state >> 8) & 0xF
    s2 = (state >> 4) & 0xF
    s3 = state & 0xF

    ns0 = gf_mult(1, s0) ^ gf_mult(4, s2)
    ns1 = gf_mult(1, s1) ^ gf_mult(4, s3)
    ns2 = gf_mult(4, s0) ^ gf_mult(1, s2)
    ns3 = gf_mult(4, s1) ^ gf_mult(1, s3)

    return (ns0 << 12) | (ns1 << 8) | (ns2 << 4) | ns3


# Encryption
def encrypt(plaintext, key):
    round_keys = expand_key(key)
    state = plaintext ^ round_keys[0]  # Initial AddRoundKey

    # Round 1
    state = sub_nibbles(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state ^= round_keys[1]

    # Round 2
    state = sub_nibbles(state)
    state = shift_rows(state)
    state ^= round_keys[2]

    return state


plaintext = 0x1234
key = 0x5678
ciphertext = encrypt(plaintext, key)
print(f"Plaintext: 0x{plaintext:04x}")
print(f"Ciphertext: 0x{ciphertext:04x}")
