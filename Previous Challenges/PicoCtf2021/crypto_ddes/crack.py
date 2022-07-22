from re import L
import string
from Crypto.Cipher import DES
from icecream import ic

keys = []  # type: list[bytes]
for a in string.digits:
    for b in string.digits:
        for c in string.digits:
            for d in string.digits:
                for e in string.digits:
                    for f in string.digits:
                        keys.append(f'{a}{b}{c}{d}{e}{f}  '.encode())

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()


pt = bytes.fromhex('00').decode()
pt = pad(pt)
ct = bytes.fromhex('38c574a60f9c1183')
key_ct = bytes.fromhex('1b77b97452b7b91f0905cd3e232b4cac2bb8b2f19aeec56180c7dde44f20b189e938d42fc5419799')

middles = {}
for key1 in keys:
    cipher1 = DES.new(key1, DES.MODE_ECB)
    middle = cipher1.encrypt(pt)
    middles[middle] = key1

print('halfway')

for key2 in keys:
    cipher2 = DES.new(key2, DES.MODE_ECB)
    middle = cipher2.decrypt(ct)
    if middles.get(middle) is not None:
        key1 = middles[middle]
        ic(key1)
        ic(key2)
        break

cipher1 = DES.new(key1, DES.MODE_ECB)
cipher2 = DES.new(key2, DES.MODE_ECB)
middle = cipher2.decrypt(key_ct)
print(cipher1.decrypt(middle))
    
