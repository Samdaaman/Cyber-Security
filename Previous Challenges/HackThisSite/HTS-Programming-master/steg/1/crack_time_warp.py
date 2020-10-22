import base64
import os
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def crack_with_password(password, message):
    salt = b'os.urandom(16)'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)
    try:
        decrypted = f.decrypt(message)
    except:
        return
    print(decrypted)


with open("./enc_1") as f:
    message = f.read().encode()

for i in range(10000):
    crack_with_password(str(i + 25961040).encode(), message)
