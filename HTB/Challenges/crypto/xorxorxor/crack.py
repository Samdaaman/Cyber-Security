import itertools

with open('output.txt') as fh:
    ct_hex = fh.read().split(': ')[1].strip()
    ct = bytearray.fromhex(ct_hex)

KEY_LEN = 4

shreded = []
for i in range(KEY_LEN):
    shreded.append([])
    for j in range(len(ct) // KEY_LEN):
        shreded[i].append(ct[j*KEY_LEN + i])

def get_keys(shred: list):
    keys = []
    for i in range(255):
        for j in shred:
            p = j ^ i
            # if p > 127 or p < 32:
            if p not in b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}':
                break
        else:
            keys.append(i)
    return keys

print(shreded)

keys = list(map(get_keys, shreded))
print(keys)

class XOR:
    def __init__(self):
        self.key = b'[\x1e\xb4\x9a'
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def pp(l):
    print(','.join([str(c).rjust(4) for c in l]))

for key in itertools.product(*keys):
    xored = b''
    for i in range(len(ct)):
        xored += bytes([ct[i] ^ key[i % len(key)]])
    print(xored)

pp(ct)
pp(XOR().decrypt(ct))
print(XOR().decrypt(ct))