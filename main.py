# Entry point for Paladin

import os

from aes.aes import cbc_encrypt, cbc_decrypt
from rsa.rsa import rsa_encrypt, rsa_decrypt, prime_num_gen, calculate_private_key
from tkinter import *

d = None
n = None
iv = None

# create root window
root = Tk()

# root window title
root.title("Paladin")

# set dimension
root.geometry("1280x1000")

plain_txt_lbl = Label(root, text = "Plain text")
plain_txt_lbl.grid(column = 1, row = 0)

plain_txt_box = Text(root, width = 50, height = 25)
plain_txt_box.grid(column = 1, row = 1)

cipher_txt_lbl = Label(root, text = "Cipher text")
cipher_txt_lbl.grid(column = 1, row = 2)

cipher_txt_box = Text(root, width = 50, height = 25)
cipher_txt_box.grid(column = 1, row = 3)

key_lbl = Label(root, text = "Encrypted AES key")
key_lbl.grid(column = 2, row = 1)

key_box = Text(root, width = 50, height = 25)
key_box.grid(column = 2, row = 2)


def aes_256_click():
    global d, n, iv
    # generate AES-256 key
    aes_key = os.urandom(256 // 8)

    # generate 128 initial vector for CBC
    iv = os.urandom(128 // 8)


    # Calculate RSA public key
    p = prime_num_gen(1024)
    q = prime_num_gen(1024)
    n = p * q
    e = 65537

    # Calculate RSA private key
    d = calculate_private_key(e, p, q)

    plain_text = plain_txt_box.get("1.0", END)
    plain_text_bytes = plain_text.encode('utf-8')

    cipher_text = cbc_encrypt(plain_text_bytes, aes_key, iv)
    cipher_key = rsa_encrypt(aes_key, e, n)
    cipher_txt_box.insert("1.0", str(cipher_text))
    key_box.insert("1.0", str(cipher_key))


def aes_192_click():
    global d, n, iv
    # generate AES-256 key
    aes_key = os.urandom(192 // 8)

    # generate 128 initial vector for CBC
    iv = os.urandom(128 // 8)


    # Calculate RSA public key
    p = prime_num_gen(1024)
    q = prime_num_gen(1024)
    n = p * q
    e = 65537

    # Calculate RSA private key
    d = calculate_private_key(e, p, q)

    plain_text = plain_txt_box.get("1.0", END)
    plain_text_bytes = plain_text.encode('utf-8')

    cipher_text = cbc_encrypt(plain_text_bytes, aes_key, iv)
    cipher_key = rsa_encrypt(aes_key, e, n)
    cipher_txt_box.insert("1.0", str(cipher_text))
    key_box.insert("1.0", str(cipher_key))

def aes_128_click():
    global d, n, iv
    # generate AES-256 key
    aes_key = os.urandom(128 // 8)

    # generate 128 initial vector for CBC
    iv = os.urandom(128 // 8)


    # Calculate RSA public key
    p = prime_num_gen(1024)
    q = prime_num_gen(1024)
    n = p * q
    e = 65537

    # Calculate RSA private key
    d = calculate_private_key(e, p, q)

    plain_text = plain_txt_box.get("1.0", END)
    plain_text_bytes = plain_text.encode('utf-8')

    cipher_text = cbc_encrypt(plain_text_bytes, aes_key, iv)
    cipher_key = rsa_encrypt(aes_key, e, n)
    cipher_txt_box.insert("1.0", str(cipher_text))
    key_box.insert("1.0", str(cipher_key))


def decryption_click():
    global d, n, iv
    cipher_text = cipher_txt_box.get("1.0", END).strip()
    cipher_key = key_box.get("1.0", END).strip()

    cipher_text_bytes = eval(cipher_text)
    cipher_key = int(cipher_key)

    decrypt_key = rsa_decrypt(cipher_key, d, n)
    decrypt_text_bytes = cbc_decrypt(cipher_text_bytes, decrypt_key, iv)
    decrypt_text = decrypt_text_bytes.decode("utf-8")


    plain_txt_box.delete("1.0", END)
    plain_txt_box.insert("1.0", decrypt_text)

# Decryption
decryption_btn = Button(root, text = "Decrypt", fg = "black", command = decryption_click)
decryption_btn.grid(column = 2, row = 0)

# AES-256 key encryption
aes_256_btn = Button(root, text = "AES-256", fg = "black", command = aes_256_click)
aes_256_btn.grid(column = 0, row = 0)

# AES-192 key encryption
aes_192_btn = Button(root, text = "AES-192", fg = "black", command = aes_192_click)
aes_192_btn.grid(column = 0, row = 1)

# AES-128 key encryption
aes_128_btn = Button(root, text = "AES-128", fg = "black", command = aes_128_click)
aes_128_btn.grid(column = 0, row = 2)


root.mainloop()
