import os
import math
from Crypto.Util.number import *
from cryptography.hazmat.primitives.asymmetric import rsa
from icecream import ic

# https://shainer.github.io/crypto/matasano/2017/10/14/rsa-padding-oracle-attack.html
# https://cryptopals.com/sets/6/challenges/48


def get_length(pt):
    'Returns number of bytes to make pt as a number, forced to be ceiling even'
    res = 0
    if (len(bin(pt)) - 2) % 8 != 0:
        res += 1
    res += (len(bin(pt)) - 2) // 8
    return res

def ceil(a, b):
    return -(-a // b)

class RSA:
    def __init__(self, size):
        
        self.e = 0x10001
        self.size = size

        priv = rsa.generate_private_key(
         public_exponent=self.e,
         key_size=size
        )
        pub = priv.public_key()
        
        self.n = pub.public_numbers().n
        
        self.d = priv.private_numbers().d
        self.n_size = ceil(self.size, 8)
        self.B = 2**((self.n_size-1)*8)   # 2^(127*8)

        ic(self.size)
        ic(self.n)
        ic(self.d)
        ic(self.n_size)
        ic(self.B)
    
    def pad(self, pt):
        res = 0x02 << 8 * (self.n_size - 2)  # 2**(126*8+1)
        ic(bin(res)[2:].rjust(128*8, '0'))
        random_pad = os.urandom(self.n_size - 3 - get_length(pt))
        ic(random_pad)
        ic(len(random_pad))
        for idx, val in enumerate(random_pad):
            if val == 0:
                val = 1
            res += val << (len(random_pad) - idx + get_length(pt)) * 8
            ic(val)
            ic(bin(res)[2:].rjust(128*8, '0'))
        ic(res)
        res += pt
        ic(res)
        return res

    def encrypt(self,pt):
        pt = bytes_to_long(pt)
        padded_pt = self.pad(pt)
        ct = pow(padded_pt, self.e, self.n)
        return long_to_bytes(ct).hex()

    def decrypt(self,ct):
        ct = bytes_to_long(ct)
        pt = pow(ct, self.d, self.n)
        return pt


def main():
    FLAG = b'HTB{dummyflag}'
    size = 1024
    tmp = RSA(size)
    flag = tmp.encrypt(FLAG)
    while True:
        try:
            print('Please choose:\n'+\
                        '1. Get public key.\n'+\
                        '2. Get encrypted flag.\n'+\
                        '3. Get length.\n'+\
                        '> ')
            opt = input()
            
            if opt == '1':
                pub_key = (hex(tmp.n)[2:], hex(tmp.e)[2:])
                print('(n,e): ' + str(pub_key) + '\n')
            elif opt == '2':
                print('Encrypted text: ' + flag + '\n')
            elif opt == '3':
                print('Provide a ciphertext:\n'+\
                            '> ')
                ct = input()
                ct = bytes.fromhex(ct)
                pt = tmp.decrypt(ct)
                length = get_length(pt)
                print('Length: ' + str(length) + '\n')
            else:
                print('Wrong option!\n')
                exit(1)
        except Exception as e:
            print(e)
            print('Invalid Input. Exit!')
            exit(1)

    

if __name__ == "__main__":
    main()