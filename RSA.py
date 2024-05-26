def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def totient(p, q):
    return (p - 1) * (q - 1)


def random_e(lambda_n):
    for i in range(2, lambda_n):
        if gcd(i, lambda_n) == 1:
            return i
    return -1


def private_key(e, lambda_n):
    for i in range(1, lambda_n):
        if (i * e) % lambda_n == 1:
            return i
    return -1


def mod_pow(a, b, m):
    x = 1
    y = a % m
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % m
        y = (y * y) % m
        b //= 2
    return x % m


def encrypt(message, e, n):
    cipher = [mod_pow(ord(char), e, n) for char in message]
    return cipher


def decrypt(cipher, d, n):
    message = [chr(mod_pow(char, d, n)) for char in cipher]
    return ''.join(message)


p = int(input("Enter the value of p(prime): "))
q = int(input("Enter the value of q(prime>q): "))

if is_prime(p) and is_prime(q) and p > 1 and q > 1:
    n = p * q
    lambda_n = totient(p, q)
    e = random_e(lambda_n)
    d = private_key(e, lambda_n)

    print("\nn is", n)
    print("lambda N is", lambda_n)
    print("e is", e)
    print("d is", d)

    message = input("Enter plaintext(number): ")
    cipher = encrypt(message, e, n)

    print("\nencrypted text:")
    print(''.join(map(str, cipher)))

    decrypted_message = decrypt(cipher, d, n)
    print("\ndecrypted text:", decrypted_message)
else:
    print("\nThe value of p and q should be prime and greater than 1.")
