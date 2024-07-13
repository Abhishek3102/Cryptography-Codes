import numpy as np

def text_to_matrix(text, block_size):
    matrix = []
    for char in text:
        matrix.append(ord(char) - ord('A'))
    while len(matrix) % block_size != 0:
        matrix.append(23)  # padding with 'X' (ASCII 88)
    return np.array(matrix).reshape(-1, block_size)

def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        for value in row:
            text += chr(value % 26 + ord('A'))
    return text

def hill_encrypt(plaintext, key):
    block_size = len(key)
    plaintext_matrix = text_to_matrix(plaintext, block_size)
    ciphertext_matrix = np.dot(plaintext_matrix, key) % 26
    return matrix_to_text(ciphertext_matrix)

# Input plaintext and key from the user
plaintext = input("Enter plaintext: ").upper().replace(" ", "")
key_str = input("Enter key (e.g., '6 24 1 13 16 10 20 17 15' for a 3x3 matrix): ")
key_values = list(map(int, key_str.split()))

# Convert key to a 2D numpy array
key_size = int(len(key_values) ** 0.5)
key = np.array(key_values).reshape(key_size, key_size)

# Encrypt the plaintext
ciphertext = hill_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
