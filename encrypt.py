from cryptography.fernet import Fernet

""""
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
"""
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)
f = Fernet(key)

with open('file_encrypted.txt', 'rb') as encrypted_file:
    original = encrypted_file.read()
encrypted = f.decrypt(original)

with open('file_encrypted.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
