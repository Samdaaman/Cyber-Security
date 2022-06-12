from Crypto.Cipher import AES
import os
from icecream import ic

from oracle_cracker import OracleCracker

fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 121, 98, 219, 61]


def xor(a, b):
    return bytes([_a ^ _b for _a, _b in zip(a, b)])


def pad(data): #Custom padding, should be fine!
    c = 0
    while len(data) % 16:
        pad = str(hex(fib[c] % 255))[2:]
        data += bytes.fromhex(pad.rjust(2, '0'))
        c += 1
    return data

def checkpad(data):
    if len(data) % 16 != 0:
        return 0
    char = data[-1]

    try:
        start = fib.index(char)
    except ValueError:
        return 0
    
    newfib = fib[:start][::-1]

    for i in range(len(newfib)):
        char = data[-(i+2)]
        if char != newfib[i]:
            return 0
    return 1


class SuperSecureEncryption: # This should be unbreakable!
    def __init__(self, key):
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, data: bytes):
        data = pad(data)
        iv = os.urandom(16).replace(b'\x00', b'\xff') 

        lb_cipher = iv
        output = b''

        data  = [data[i:i+16] for i in range(0, len(data), 16)]

        for block in data:
            enc = self.cipher.encrypt(xor(lb_cipher, block))  # type: bytes
            output += enc
            lb_cipher = enc
        return output, iv

    def decrypt(self, data: bytes, iv: bytes):
        lb_cipher = iv
        output = b''
        data = [data[i:i+16] for i in range(0, len(data), 16)]
        for block in data:
            dec = self.cipher.decrypt(block)  # type: bytes
            dec = xor(dec, lb_cipher)
            output += dec
            lb_cipher = block
        if checkpad(output):
            return output
        else:
            return None


class TestCracker(OracleCracker):
    def __init__(self):
        super().__init__(16)
        self.cipher = SuperSecureEncryption(b'abcdefgh12345678')

    def call_oracle(self, ct_block: bytes, iv: bytes) -> bool:
        return self.cipher.decrypt(ct_block, iv) is not None

    def get_pad_byte(self, padding_index: int, padding_len: int) -> int:
        return fib[padding_index]


def main():
    cracker = TestCracker()
    pt = b'Sam is cool, 123456789-abcdefghijklmnopqrstuvwxyz'
    ct, iv = cracker.cipher.encrypt(pt)
    pt = cracker.crack(ct, iv)
    print(pt)


if __name__ == '__main__':
    main()
