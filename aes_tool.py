import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from utils import derive_key

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    with open(file_path, 'rb') as f:
        data = f.read()

    padded_data = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path + ".enc", 'wb') as f:
        f.write(salt + iv + encrypted)

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        content = f.read()

    salt = content[:16]
    iv = content[16:32]
    encrypted_data = content[32:]

    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted) + unpadder.finalize()

    output_file = file_path.replace('.enc', '.dec')
    with open(output_file, 'wb') as f:
        f.write(data)
