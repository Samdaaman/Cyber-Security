from hashlib import sha256
from typing import List, Tuple
from icecream import ic
from sage.all import *
from pwn import *
import json
from random import seed, randint
from Crypto.Cipher import AES

# context.log_level = 'debug'

tube = remote('142.93.39.188', 30311)
# tube = remote('localhost', 1337)

p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
a = 0
b = 7
private_key_max = 8748541127929402731638

def get_public_key(base_x, base_y) -> Tuple[int, int]:
    tube.sendlineafter(b'\n> ', b'1')
    tube.sendlineafter(b':', f'{base_x},{base_y}'.encode())
    point_raw = tube.recvline_contains(b'Public Key: ', False)
    return tuple(json.loads(point_raw.decode().split(': ')[1]))


def low_prime_factors(n: int):
    factors = []  # type: List[int]
    if n % 2 == 0:
        factors.append(2)
    for i in Primes():
        if n % i == 0:
            factors.append(i)
        if i > 1000000:
            break
    return factors


# Part 1: invalid curve attack: https://meowmeowxw.gitlab.io/ctf/de1-2020-ecdh/
def get_private_key():
    banned_factors = [2, 3, 7, 13, 199] # idek why these don't work

    residuals = []
    moduli = []
    b_fake = 1
    while b_fake < 10:
        ECFAKE = EllipticCurve(GF(p), [a, b_fake])
        ic(b_fake)
        for prime_factor in low_prime_factors(ECFAKE.order()):
            if prime_factor not in banned_factors and prime_factor not in moduli:
                ic(prime_factor)

                base = ECFAKE.gen(0) * (ECFAKE.order() // prime_factor)
                public_keys = [tuple(base * i)[:2] for i in range(prime_factor)]
                
                public_key = get_public_key(base[0], base[1])
                assert public_key in public_keys

                residual = public_keys.index(public_key)
                residuals.append(residual)
                moduli.append(prime_factor)

                moduli_product = 1
                for modulus in moduli:
                    moduli_product *= modulus
                
                ic(moduli_product)
                ic(residuals)
                ic(moduli)
                
                if moduli_product > private_key_max:
                    # We never get here as we run out of factors :(
                    ic(residuals)
                    ic(moduli)
                    return crt(residuals, moduli)

        b_fake += 1

    # Since we ran out of factors bruteforce the remaining crt options
    moduli_product = 1
    for modulus in moduli:
        moduli_product *= modulus

    private_key_option = crt(residuals, moduli)
    private_key_options = []
    while private_key_option < private_key_max:
        private_key_options.append(private_key_option)
        private_key_option +=  moduli_product
    ic(len(private_key_options))

    ECREAL = EllipticCurve(GF(p), [a, b])
    G = [
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    ]
    public_1 = get_public_key(G[0], G[1])
    ic(public_1)
    for private_key_option in private_key_options:
        check = ECREAL(G[0], G[1]) * private_key_option
        if (tuple(check)[:2] == public_1):
            return private_key_option # yay found the right private key
        
private_key = int(get_private_key())
# private_key = 3262827136301000405966  # remote
# private_key = 1234567890000000000000  # local
ic(private_key)


# Part 2
seed(private_key)

def randomBasisLetter():
    r = randint(0, 1)
    return "Z" if r else "X"

basises = [randomBasisLetter() for _ in range(256)]

tube.sendlineafter(b'\n> ', b'2')
tube.sendlineafter(b'KEP: ', ''.join(basises).encode())
user_key = bytes.fromhex(tube.recvline_startswith(b'The Quantum key: ').split(b'The Quantum key: ')[1].decode())
flag_encrypted = bytes.fromhex(tube.recvline_startswith(b'Flag Encrypted: ').split(b'Flag Encrypted: ')[1].decode())

user_key_bitflipped = bytes([i ^ 255 for i in user_key])
server_key = sha256(user_key_bitflipped).digest()
cipher = AES.new(server_key, AES.MODE_ECB)
flag = cipher.decrypt(flag_encrypted)
print(flag)

tube.close()