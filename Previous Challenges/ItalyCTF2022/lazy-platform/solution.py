from math import ceil
from pwn import *
from lib import getrandbytes, rand_bytes_to_ints
from MTRecover import MT19937Recover
from Crypto.Cipher import AES

# context.log_level = 'debug'
p = remote('lazy-platform.challs.teamitaly.eu', 15004)

def read_hex_value(prefix: str) -> bytes:
    line = p.recvline_contains(prefix.encode()).decode()
    return bytes.fromhex(line.split(prefix)[1].strip())

def dump_rand():
    p.sendlineafter(b'options', b'1')
    p.sendlineafter(b'encrypt: ', b'1')
    p.recvline()
    key = read_hex_value('Key: ')
    iv = read_hex_value('IV: ')
    return key + iv

iterations = ceil(625 / 12) # 12 because 32+16 is 48 bytes or 12 4-byte ints
outputs = []
with log.progress(f'Dumping {iterations} outputs', '0') as prog:
    for i in range(iterations):
        prog.status(f'{i}')
        rand_bytes = dump_rand()
        ints = rand_bytes_to_ints(rand_bytes)
        outputs += ints

# Crack
mtr = MT19937Recover()
r = mtr.go(outputs)

# Prediction
key = getrandbytes(32, r)
iv = getrandbytes(16, r)

# Decryption
p.sendlineafter(b'options', b'3')
ct = read_hex_value('Ciphertext: ')
pt = AES.new(key, AES.MODE_CBC, iv).decrypt(ct)
print(pt)