p = int(input("Enter the prime modulus (p): "))
a = int(input("Enter the coefficient of x^2 (a): "))
b = int(input("Enter the coefficient of x^3 (b): "))

x_G = int(input("Enter the x-coordinate of the generator point G: "))
y_G = int(input("Enter the y-coordinate of the generator point G: "))
G = (x_G, y_G)


def add_points(P, Q):
    if P == Q:
        lam = (3 * P[0]**2 + a) * pow(2 * P[1], p - 2, p) % p
    else:
        lam = (Q[1] - P[1]) * pow(Q[0] - P[0], p - 2, p) % p
    x = (lam**2 - P[0] - Q[0]) % p
    y = (lam * (P[0] - x) - P[1]) % p
    return (x, y)


private_key = int(input("Enter your private key (an integer): "))


def multiply_point(P, k):
    result = G
    for bit in bin(k)[2:]:
        result = add_points(result, result)
        if bit == '1':
            result = add_points(result, P)
    return result


public_key = multiply_point(G, private_key)
print(f"Your public key (Q) is: {public_key}")

x_message = int(input("Enter the x-coordinate of the plaintext message: "))
y_message = int(input("Enter the y-coordinate of the plaintext message: "))
message = (x_message, y_message)

ephemeral_key = int(input("Enter the ephemeral key (an integer): "))
ephemeral_point = multiply_point(G, ephemeral_key)

C1 = ephemeral_point
C2 = add_points(message, multiply_point(public_key, ephemeral_key))
print(f"Ciphertext (C1, C2) is: ({C1}, {C2})")


def negate_point(P):
    x, y = P
    return x, -y


shared_secret = multiply_point(C1, private_key)

plaintext = add_points(C2, negate_point(shared_secret))
print(f"Decrypted plaintext message is: {plaintext}")
