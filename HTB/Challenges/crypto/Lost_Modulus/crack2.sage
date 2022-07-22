from Crypto.Util.number import getPrime, long_to_bytes, inverse
from sage.all_cmdline import *   # import sage library


class RSA:
    def __init__(self):
        self.p = getPrime(512)
        self.q = getPrime(512)
        self.e = 3
        self.n = self.p * self.q
        self.d = inverse(self.e, (self.p-1)*(self.q-1))
    def encrypt(self, data: bytes) -> bytes:
        pt = int(data.hex(), 16)
        ct = pow(pt, self.e, self.n)
        return long_to_bytes(ct)
    def decrypt(self, data: bytes) -> bytes:
        ct = int(data.hex(), 16)
        pt = pow(ct, self.d, self.n)
        return long_to_bytes(pt)

with open('output.txt') as fh:
    ct = bytearray.fromhex(fh.read().strip().split(': ')[1])

pt = int(ct.hex(), 16) ** (1/3)
print(pt)
print(int(ct.hex(), 16))
print(long_to_bytes(int(pt)))