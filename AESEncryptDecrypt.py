from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


if __name__ == "__main__":
    key = get_random_bytes(16)  # 16 bytes key for AES-128
    plaintext = b"Hello, AES encryption!"

    ciphertext = aes_encrypt(plaintext, key)
    decrypted_text = aes_decrypt(ciphertext, key)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)
