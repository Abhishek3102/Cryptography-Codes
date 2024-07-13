ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'
ALPHABETS_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message, k1, k2):
    if not is_valid_key(k1, k2):
        raise ValueError("Invalid keys. Make sure gcd(k1, 26) is 1, k1 is between 1 and 25 inclusive, and k2 is between 0 and 25 inclusive.")

    result = ''
    for letter in message:
        if letter in ALPHABETS:
            index = (k1 * ALPHABETS.index(letter) + k2) % len(ALPHABETS)
            result += ALPHABETS[index]
        elif letter in ALPHABETS_UPPER:
            index = (k1 * ALPHABETS_UPPER.index(letter) + k2) % len(ALPHABETS_UPPER)
            result += ALPHABETS_UPPER[index]
        else:
            result += letter

    return result

def decrypt(message, k1, k2):
    if not is_valid_key(k1, k2):
        raise ValueError("Invalid keys. Make sure gcd(k1, 26) is 1, k1 is between 1 and 25 inclusive, and k2 is between 0 and 25 inclusive.")

    result = ''
    for letter in message:
        if letter in ALPHABETS:
            index = ((ALPHABETS.index(letter) - k2) * inverse(k1)) % len(ALPHABETS)
            result += ALPHABETS[index]
        elif letter in ALPHABETS_UPPER:
            index = ((ALPHABETS_UPPER.index(letter) - k2) * inverse(k1)) % len(ALPHABETS_UPPER)
            result += ALPHABETS_UPPER[index]
        else:
            result += letter

    return result

def inverse(k1):
    i = 0
    while (k1 * i) % 26 != 1:
        i += 1
    return i

def is_valid_key(k1, k2):
    return 1 <= k1 <= 25 and 0 <= k2 <= 25 and gcd(k1, 26) == 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            k1 = int(input("Enter the first key (k1): "))
            k2 = int(input("Enter the second key (k2): "))

            if is_valid_key(k1, k2):
                plaintext = input("Enter the message to encrypt: ")
                print("Encrypted message:", encrypt(plaintext, k1, k2))
            else:
                print("Invalid keys. Make sure gcd(k1, 26) is 1, k1 is between 1 and 25 inclusive, and k2 is between 0 and 25 inclusive.")

        elif choice == '2':
            k1 = int(input("Enter the first key (k1): "))
            k2 = int(input("Enter the second key (k2): "))

            if is_valid_key(k1, k2):
                ciphertext = input("Enter the message to decrypt: ")
                print("Decrypted message:", decrypt(ciphertext, k1, k2))
            else:
                print("Invalid keys. Make sure gcd(k1, 26) is 1, k1 is between 1 and 25 inclusive, and k2 is between 0 and 25 inclusive.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
