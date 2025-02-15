# -*- coding: utf-8 -*-

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.fernet import Fernet

# Caminho para o arquivo da chave privada
private_key_file = "/home/kali/Desktop/Ransomware/private_key.pem"
encrypted_file_path = "C:\\Users\\hp\\OneDrive\\Ambiente de Trabalho\\Этический хакер\\scripts\\cryptography\\EncryptedFile.txt"
decrypted_file_path = "C:\\Users\\hp\\OneDrive\\Ambiente de Trabalho\\Этический хакер\\scripts\\cryptography\\DecryptedFile.txt"

# Carregar a chave privada do arquivo PEM
with open(private_key_file, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Carregar a chave simétrica criptografada
with open("encrypted_symmetric_key.key", "rb") as key_file:
    encrypted_symmetric_key = key_file.read()

# Descriptografar a chave simétrica usando a chave privada
decrypted_symmetric_key = private_key.decrypt(
    encrypted_symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Criar uma instância de Fernet com a chave simétrica descriptografada
fernet_instance = Fernet(decrypted_symmetric_key)

# Descriptografar o arquivo criptografado
with open(encrypted_file_path, "rb") as file:
    encrypted_data = file.read()
    decrypted_data = fernet_instance.decrypt(encrypted_data)

# Salvar o arquivo descriptografado
with open(decrypted_file_path, "wb") as file:
    file.write(decrypted_data)
