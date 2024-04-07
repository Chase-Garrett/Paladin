#!/usr/bin/env python3

import os


def extended_euclidean(x, y):
    if not y:
        return 1, 0
    a, b = extended_euclidean(y, x % y)
    return b, a - b * (x // y)


def pow_2_factor(n: int) -> (int, int):
    r = 0
    d = n
    while n > 0 and d % 2 == 0:
        d = d // 2
        r += 1
    return r, d


# check for primality
def primality_test(n: int, k: int) -> bool:
    r, d = pow_2_factor(n-1)
    for i in range(k):
        a = rand_bits(n.bit_length())
        while a not in range(2, n-2+1):
            a = rand_bits(n.bit_length())
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        n_1_found = False
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                n_1_found = True
                break
        if not n_1_found:
            return False
    return True


# generate random bits
rand_bits = lambda bit_length: int.from_bytes(os.urandom((bit_length + 7) // 8), 'big')


# Generate prime number
def prime_num_gen(prime_num_bit_length: int) -> int:
    l = pow(2, prime_num_bit_length - 1)
    h = pow(2, prime_num_bit_length) -1

    while True:
        prime = rand_bits(prime_num_bit_length)

        while prime not in range(l, h+1) or not prime % 2:
            prime = rand_bits(prime_num_bit_length)

        k = 64
        if primality_test(prime, k):
            return prime


def calculate_private_key(e: int, p: int, q: int) -> int:
    private_key, _ = extended_euclidean(e, (p-1)*(q-1))
    return private_key


# Main function for RSA encryption
def rsa_encrypt(plain_text: bytes, e: int, n: int) -> int:
    pt_int = int.from_bytes(plain_text, 'big')
    return pow(pt_int, e, n)


# Main function for RSA decryption
def rsa_decrypt(cipher_text: bytes, d: int, n: int) -> bytes:
    pt_int = pow(cipher_text, d, n)
    return pt_int.to_bytes((pt_int.bit_length() + 7) // 8, 'big')


# Calculate public key
# rsa_key_size = 2048
# prime_num_bit_length = rsa_key_size // 2
# p = prime_num_gen(prime_number_bit_length)
# q = prime_num_gen(prime_number_bit_length)
# n = p * q
#
# Private Key
# d = calculate_private_key(e, p, q)
