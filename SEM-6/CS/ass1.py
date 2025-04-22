# Permutation tables
# These tables define how bits should be rearranged at various stages

# P10 permutation table for the initial key permutation (10 bits -> 10 bits)
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

# P8 permutation table for generating subkeys (10 bits -> 8 bits)
P8 = [6, 3, 7, 4, 8, 5, 10, 9]

# Initial Permutation (IP) table for the plaintext (8 bits -> 8 bits)
IP = [2, 6, 3, 1, 4, 8, 5, 7]

# Inverse Initial Permutation (IP_INV) table for the final step (8 bits -> 8 bits)
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

# Expansion/Permutation (EP) table used in the Feistel function (4 bits -> 8 bits)
EP = [4, 1, 2, 3, 2, 3, 4, 1]

# P4 permutation table used after S-boxes (4 bits -> 4 bits)
P4 = [2, 4, 3, 1]

# S-boxes (Substitution boxes) for non-linear transformations
# S0 box (4 bits -> 2 bits)
S0 = [
    [1, 0, 3, 2],  # Row 0
    [3, 2, 1, 0],  # Row 1
    [0, 2, 1, 3],  # Row 2
    [3, 1, 0, 2],  # Row 3
]

# S1 box (4 bits -> 2 bits)
S1 = [
    [0, 1, 2, 3],  # Row 0
    [2, 3, 1, 0],  # Row 1
    [3, 0, 1, 2],  # Row 2
    [2, 1, 0, 3],  # Row 3
]


def permute(block, permutation):
    """Apply permutation to the block
    Args:
        block: list of bits to permute
        permutation: list defining the new bit positions
    Returns:
        New list of bits after permutation
    """
    return [
        block[i - 1] for i in permutation
    ]  # -1 because Python uses 0-based indexing


def left_shift(bits, n):
    """Perform circular left shift on first and second halves
    Args:
        bits: list of bits to shift
        n: number of positions to shift
    Returns:
        Shifted bits with both halves shifted separately
    """
    half = len(bits) // 2  # Split into two halves
    left = bits[:half]
    right = bits[half:]
    # Perform circular shift on each half and combine
    return left[n:] + left[:n] + right[n:] + right[:n]


def generate_keys(key):
    """Generate K1 and K2 from the 10-bit key
    Args:
        key: 10-bit master key as list
    Returns:
        Tuple of (K1, K2) subkeys
    """
    # Step 1: Apply P10 permutation to the key
    p10_key = permute(key, P10)

    # Step 2: Left shift each 5-bit half by 1 position
    shifted = left_shift(p10_key, 1)

    # Step 3: Generate K1 by applying P8 permutation
    k1 = permute(shifted, P8)

    # Step 4: Left shift each 5-bit half by 2 positions (total of 3 shifts from original)
    shifted = left_shift(shifted, 2)

    # Step 5: Generate K2 by applying P8 permutation
    k2 = permute(shifted, P8)

    return k1, k2


def xor(bits1, bits2):
    """Perform XOR operation on two bit arrays
    Args:
        bits1: first bit array
        bits2: second bit array
    Returns:
        Bitwise XOR result
    """
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]


def s_box_lookup(bits, s_box):
    """Perform S-box substitution
    Args:
        bits: 4-bit input
        s_box: which S-box to use (S0 or S1)
    Returns:
        2-bit output from S-box
    """
    # Calculate row index (first and fourth bits)
    row = bits[0] * 2 + bits[3]
    # Calculate column index (middle two bits)
    col = bits[1] * 2 + bits[2]
    # Get value from S-box
    val = s_box[row][col]
    # Convert value to 2 bits (binary representation)
    return [val >> 1 & 1, val & 1]


def feistel_function(right, subkey):
    """The F function used in each round
    Args:
        right: right half of data (4 bits)
        subkey: round subkey (8 bits)
    Returns:
        4-bit output of Feistel function
    """
    # Step 1: Expansion/Permutation (4 bits -> 8 bits)
    expanded = permute(right, EP)

    # Step 2: XOR with subkey
    xored = xor(expanded, subkey)

    # Step 3: Split into two 4-bit halves for S-boxes
    left_half = xored[:4]
    right_half = xored[4:]

    # Step 4: Apply S-box substitutions
    s0_out = s_box_lookup(left_half, S0)  # First half goes through S0
    s1_out = s_box_lookup(right_half, S1)  # Second half goes through S1

    # Step 5: Combine results and apply P4 permutation
    combined = s0_out + s1_out
    return permute(combined, P4)


def encrypt_block(block, k1, k2):
    """Encrypt an 8-bit block using S-DES
    Args:
        block: 8-bit plaintext
        k1: first subkey
        k2: second subkey
    Returns:
        8-bit ciphertext
    """
    # Step 1: Initial permutation
    permuted = permute(block, IP)

    # Round 1
    left = permuted[:4]  # First 4 bits
    right = permuted[4:]  # Last 4 bits
    f_out = feistel_function(right, k1)  # Apply Feistel function with K1
    new_left = xor(left, f_out)  # XOR with left half

    # Switch function (swap halves)
    switched = right + new_left

    # Round 2
    left = switched[:4]
    right = switched[4:]
    f_out = feistel_function(right, k2)  # Apply Feistel function with K2
    new_left = xor(left, f_out)  # XOR with left half

    # Final permutation (don't swap after last round)
    output = new_left + right
    ciphertext = permute(output, IP_INV)

    return ciphertext


def decrypt_block(block, k1, k2):
    """Decrypt an 8-bit block using S-DES
    Args:
        block: 8-bit ciphertextx1
        k1: first subkey
        k2: second subkey
    Returns:
        8-bit plaintext
    Note: Decryption is same as encryption but with reversed key order
    """
    return encrypt_block(block, k2, k1)


# Example usage
if __name__ == "__main__":
    # Example 10-bit key
    key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]

    # Example 8-bit plaintext
    plaintext = [0, 1, 0, 1, 0, 1, 0, 1]

    # Generate subkeys
    k1, k2 = generate_keys(key)
    print("Subkey K1:", k1)
    print("Subkey K2:", k2)

    # Encrypt
    ciphertext = encrypt_block(plaintext, k1, k2)
    print("\nPlaintext: ", plaintext)
    print("Ciphertext:", ciphertext)

    # Decrypt
    decrypted = decrypt_block(ciphertext, k1, k2)
    print("\nDecrypted: ", decrypted)

    # Verify decryption matches original plaintext
    print("\nSuccess:", decrypted == plaintext)
