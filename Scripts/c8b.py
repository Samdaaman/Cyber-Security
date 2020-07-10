from cryptography.hazmat.primitives.ciphers.aead import AESGCM

plain = b'0' * 4
# key = AESGCM.generate_key(bit_length=128)
# key = bytearray.fromhex('495e27ba7f7f7f7fb5e9ebfa6ba835c5')
key = bytearray.fromhex('7f7f7f7fba275e49c535a86bfaebe9b5')
# nouce = b'0' * 12
nouce = bytearray.fromhex('6938a9d0ae7379610eff42d55849ebdd')
aesgcm = AESGCM(key)
ct = aesgcm.encrypt(nouce, plain, None)
data = nouce + ct
print(len(data))
print(''.join(['{:02x}'.format(i) for i in data]))
print(aesgcm.decrypt(nouce, ct, None))
