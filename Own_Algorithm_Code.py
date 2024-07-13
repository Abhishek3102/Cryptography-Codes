import hashlib

def generate_key(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    key = int(hashed_password, 16) % 26
    return key

def substitution_encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        encrypted_char = chr((ord(char) + key - 32) % 94 + 32)
        encrypted_text += encrypted_char
    return encrypted_text

def substitution_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_char = chr((ord(char) - key - 32) % 94 + 32)
        decrypted_text += decrypted_char
    return decrypted_text

def transposition_encrypt(plaintext):
    columns = [''] * 2
    for i, char in enumerate(plaintext):
        columns[i % 2] += char
    transposed_text = columns[0] + columns[1]
    return transposed_text

def transposition_decrypt(transposed_text):
    mid = len(transposed_text) // 2
    plaintext = ''.join(transposed_text[i % 2 * mid + i // 2] for i in range(len(transposed_text)))
    return plaintext

def encrypt(plaintext, password):
    key = generate_key(password)
    print("Generated Key:", key)

    substitution_encrypted = substitution_encrypt(plaintext, key)
    print("Substitution Encrypted:", substitution_encrypted)

    transposition_encrypted = transposition_encrypt(substitution_encrypted)
    print("Transposition Encrypted:", transposition_encrypted)

    return transposition_encrypted

def decrypt(encrypted_text, password):
    key = generate_key(password)
    print("Generated Key:", key)

    transposition_decrypted = transposition_decrypt(encrypted_text)
    print("Transposition Decrypted:", transposition_decrypted)

    substitution_decrypted = substitution_decrypt(transposition_decrypted, key)
    print("Substitution Decrypted:", substitution_decrypted)

    return substitution_decrypted

plaintext = input("Please enter the plain-text:")
password = input("Please enter the password:")
print("Plaintext:", plaintext)


print("\nEncryption Process:")
encrypted_text = encrypt(plaintext, password)
print("\nEncrypted Text:", encrypted_text)


print("\nDecryption Process:")
decrypted_text = decrypt(encrypted_text, password)
print("\nDecrypted Text:", decrypted_text)