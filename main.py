# Entry point for Paladin

import os

from aes.aes import cbc_encrypt, cbc_decrypt
from rsa.rsa import rsa_encrypt, rsa_decrypt, prime_num_gen, calculate_private_key


def main():
    while True:
        # Generate AES key
        aes_key = os.urandom(256 // 8)

        # Generate 128 initial vector for CBC
        iv = os.urandom(128 // 8)

        # Calculate RSA public key
        p = prime_num_gen(1024)
        q = prime_num_gen(1024)
        n = p * q
        e = 65537

        # Calculate RSA private key
        d = calculate_private_key(e, p, q)

        plain_text = input('Enter plaintext to encrypt: ')
        plain_text_bytes = plain_text.encode('utf-8')

        cipher_text = cbc_encrypt(plain_text_bytes, aes_key, iv)
        cipher_key = rsa_encrypt(aes_key, e, n)
        decrypt_key = rsa_decrypt(cipher_key, d, n)
        decrypt_text = cbc_decrypt(cipher_text, decrypt_key, iv)

        print('Decrypted text: ', decrypt_text.decode('utf-8'))


if __name__ == '__main__':
    main()
