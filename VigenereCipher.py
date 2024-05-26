def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += char
    return plaintext


plaintext_vigenere = input("Enter the plaintext: ")
key_vigenere = input("Enter the key: ")

encrypted_text_vigenere = vigenere_encrypt(plaintext_vigenere, key_vigenere)
print("Encrypted ciphertext (Vigenere):", encrypted_text_vigenere)

decrypted_text_vigenere = vigenere_decrypt(encrypted_text_vigenere, key_vigenere)
print("Decrypted plaintext (Vigenere):", decrypted_text_vigenere)

