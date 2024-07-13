import numpy as np

def encrypt(message, key):
    # Convert message to uppercase and remove spaces
    message = message.replace(" ", "").upper()

    # Pad the message with 'X' if its length is not a multiple of the key size
    while len(message) % len(key) != 0:
        message += 'X'

    # Convert characters to numbers (A=0, B=1, ..., Z=25)
    numbers = [ord(char) - ord('A') for char in message]

    # Reshape the numbers into a matrix
    matrix_size = int(len(key) ** 0.5)
    matrix = np.array(numbers).reshape(-1, matrix_size)

    # Multiply the matrix by the key matrix
    encrypted_matrix = np.dot(matrix, key) % 26

    # Convert the encrypted matrix back to a string
    encrypted_numbers = encrypted_matrix.flatten().tolist()
    encrypted_message = ''.join([chr(num + ord('A')) for num in encrypted_numbers])

    return encrypted_message

key_matrix = np.array([[9, 4], [5, 7]])

encrypted_message = encrypt("EXAM", key_matrix)
print("Encrypted message:", encrypted_message)
