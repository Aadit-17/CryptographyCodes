def caesar_encrypt(plaintxt, key):
    ciphertxt = ""
    for char in plaintxt:
        if char.isalpha():
            if char.isupper():
                ciphertxt += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                ciphertxt += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            ciphertxt += char
    return ciphertxt


def caesar_decrypt(ciphertxt, key):
    plaintxt = ""
    for char in ciphertxt:
        if char.isalpha():
            if char.isupper():
                plaintxt += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                plaintxt += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            plaintxt += char
    return plaintxt


plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (0-25): "))

encrypted_text = caesar_encrypt(plaintext, key)
print("Encrypted ciphertext:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, key)
print("Decrypted plaintext:", decrypted_text)
