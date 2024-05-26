def generate_playfair_key_table(key):
    key = key.upper().replace("J", "I")
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_table = [list(key)]
    for char in alphabet:
        if char not in key_set:
            key_table[-1].append(char)
            if len(key_table[-1]) == 5:
                key_table.append([])
    return key_table


def find_char_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)


def playfair_encrypt(plaintext, key):
    key_table = generate_playfair_key_table(key)
    ciphertext = ""
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = [char for char in plaintext if char.isalpha()]
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        row1, col1 = find_char_position(key_table, char1)
        row2, col2 = find_char_position(key_table, char2)
        if row1 == row2:
            ciphertext += key_table[row1][(col1 + 1) % 5] + key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_table[(row1 + 1) % 5][col1] + key_table[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_table[row1][col2] + key_table[row2][col1]
    return ciphertext


def playfair_decrypt(ciphertext, key):
    key_table = generate_playfair_key_table(key)
    plaintext = ""
    ciphertext = ciphertext.upper().replace("J", "I")
    ciphertext = [char for char in ciphertext if char.isalpha()]
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1] if i + 1 < len(ciphertext) else 'X'
        row1, col1 = find_char_position(key_table, char1)
        row2, col2 = find_char_position(key_table, char2)
        if row1 == row2:
            plaintext += key_table[row1][(col1 - 1) % 5] + key_table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_table[(row1 - 1) % 5][col1] + key_table[(row2 - 1) % 5][col2]
        else:
            plaintext += key_table[row1][col2] + key_table[row2][col1]
    return plaintext


plaintext_playfair = input("Enter the plaintext: ")
key_playfair = input("Enter the key(String): ")

encrypted_text_playfair = playfair_encrypt(plaintext_playfair, key_playfair)
print("Encrypted ciphertext (Playfair):", encrypted_text_playfair)

decrypted_text_playfair = playfair_decrypt(encrypted_text_playfair, key_playfair)
print("Decrypted plaintext (Playfair):", decrypted_text_playfair)

