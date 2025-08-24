#!/usr/bin/python
"""This module encrypts and decrypts files."""

from cryptography.fernet import Fernet
from os.path import exists

key_path = 'keyfile.key'
if not exists(key_path):
    key = Fernet.generate_key()
    with open(key_path, 'wb') as keyfile:
        keyfile.write(key)

with open(key_path, 'rb') as keyfile:
    key = keyfile.read()


def encrypt(file_path: str):
    """Encrypt the file."""
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt(file_path: str):
    """Decrypt the file."""
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

