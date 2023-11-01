import string
from debug import AAES
from icecream import ic
from pwn import *
import typing as t

aa = AAES()

# io = process('python3 -u debug.py', shell=True, stderr=None) # type: ignore
io = remote('157.245.43.189', 31118)

def encrypt(m: str):
    io.sendlineafter(b': ', m.encode())
    return bytes.fromhex(io.recvline(False).decode())

alphabet = string.ascii_letters + string.digits + '_{}'

pt = ''
shift = 1

while not pt.startswith('HTB{'):
    padding = 'CryptoHackTheBox'
    right = pt[:15]
    right += padding[:15 - len(right)]
    trial = right.rjust(16, 'X')
    ic(trial)

    blocks_oracle = [c + right for c in alphabet]
    m = ''.join(blocks_oracle) + ('\u00ff' * (shift % 16))

    ct = encrypt(m)

    blocks_enc = [ct[i:i+16] for i in range(0, len(ct), 16)]
    blocks_oracle_enc = blocks_enc[:len(blocks_oracle)]

    block_to_guess = blocks_enc[-2 - (shift // 16)]

    char_index = blocks_oracle_enc.index(block_to_guess)
    char = alphabet[char_index]
    ic(char, pt)

    pt = char + pt
    shift += 1
