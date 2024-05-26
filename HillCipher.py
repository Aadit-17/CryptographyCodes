def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def matrix_inverse(matrix, modulus):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det %= modulus
    det_inverse = mod_inverse(det, modulus)

    if det_inverse is None:
        raise ValueError("Matrix isn't invertible.")

    adjugate = [[matrix[1][1], -matrix[0][1]],
                [-matrix[1][0], matrix[0][0]]]

    inverse = [[(det_inverse * adjugate[i][j]) % modulus for j in range(2)] for i in range(2)]

    return inverse


def matrix_multiply(matrix1, matrix2, modulus):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                result[i][j] %= modulus
    return result


def hill_cipher_encrypt(plain_text, key_matrix, modulus):
    plain_numbers = [ord(char) - ord('A') for char in plain_text]

    while len(plain_numbers) % len(key_matrix) != 0:
        plain_numbers.append(0)

    plain_matrix = [[plain_numbers[i] for i in range(j, j + len(key_matrix))] for j in
                    range(0, len(plain_numbers), len(key_matrix))]

    encrypted_matrix = [[0, 0] for _ in range(len(plain_matrix))]
    for i in range(len(plain_matrix)):
        encrypted_matrix[i] = [sum(plain_matrix[i][k] * key_matrix[k][j] for k in range(len(key_matrix))) % modulus for
                               j in range(len(key_matrix))]

    encrypted_numbers = [number for sublist in encrypted_matrix for number in sublist]
    encrypted_text = ''.join([chr(number + ord('A')) for number in encrypted_numbers])

    return encrypted_text


def hill_cipher_decrypt(encrypted_text, key_matrix, modulus):
    encrypted_numbers = [ord(char) - ord('A') for char in encrypted_text]

    encrypted_matrix = [[encrypted_numbers[i] for i in range(j, j + len(key_matrix))] for j in
                        range(0, len(encrypted_numbers), len(key_matrix))]

    key_matrix_inverse = matrix_inverse(key_matrix, modulus)

    decrypted_matrix = [[0, 0] for _ in range(len(encrypted_matrix))]
    for i in range(len(encrypted_matrix)):
        decrypted_matrix[i] = [
            sum(encrypted_matrix[i][k] * key_matrix_inverse[k][j] for k in range(len(key_matrix))) % modulus for j in
            range(len(key_matrix))]

    decrypted_numbers = [number for sublist in decrypted_matrix for number in sublist]

    decrypted_numbers = [num for num in decrypted_numbers if num != 0]

    decrypted_text = ''.join([chr(number + ord('A')) for number in decrypted_numbers])

    return decrypted_text


print("Enter key matrix (4 integers, row by row):")
key_matrix = [[int(input()) for _ in range(2)] for _ in range(2)]
modulus = 26
plain_text = input("Enter plain text: ")
encrypted_text = hill_cipher_encrypt(plain_text, key_matrix, modulus)
decrypted_text = hill_cipher_decrypt(encrypted_text, key_matrix, modulus)

print("\nKey Matrix:\n", key_matrix)
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
