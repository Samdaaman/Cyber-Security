from pwn import *
from Crypto.Util.number import bytes_to_long, getPrime, isPrime, long_to_bytes
import hashlib
import os

context.log_level = 'debug'

N_BITS = 2048
E_BITS = 13

primes = [2]
i = 3
while i < 2**E_BITS:
    if isPrime(i):
        primes.append(i)
    i += 2

print(f'num primes = {len(primes)}')

proc = process(['python3', 'server.py'])

def get_hex_value(name: str):
    line = proc.recvline_contains(f'{name} = '.encode()).decode()
    value_str = line.split(' = ')[1]
    return int(value_str, 16)

def encrypt(pt: bytes):
    proc.sendlineafter(b'> ', b'2')
    proc.sendlineafter(b'> ', pt)
    ct = get_hex_value('ciphertext')
    auth_code = get_hex_value('auth_code')
    return ct, auth_code

def decrypt(ct: bytes, auth_code: bytes):
    pass

n = get_hex_value('n')

for i in range(1):
    encrypt(b'0' * ((N_BITS // 8) - 6))

proc.interactive()