from Crypto.Cipher import AES
from Crypto.Hash import SHA256


key = SHA256.new('$encryptedBytes'.encode()).digest()
print([b for b in key])

with open('enc.bin', 'rb') as fh:
    data = fh.read()

aes = AES.new(key, mode=AES.MODE_CBC, iv=data[:16])

decrypted = aes.decrypt(data[16:])

with open('dec.bin', 'wb') as fh:
    fh.write(decrypted)
