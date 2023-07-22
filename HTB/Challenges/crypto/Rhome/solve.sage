import os
os.environ['TERM'] = 'xterm-256color'

from pwn import *
from icecream import ic
from sage.all import *
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from hashlib import sha256
from icecream import ic


# io = process('python3 debug.py', shell=True, stderr=None)
io = remote('206.189.120.31', int(30892))

io.sendlineafter(b'> ', b'2')
io.sendlineafter(b'> ', b'1')

p = int(io.recvline().split(b'= ')[1])
g = int(io.recvline().split(b'= ')[1])
A = int(io.recvline().split(b'= ')[1])
B = int(io.recvline().split(b'= ')[1])

factors_pm1 = list(factor(p - 1))
factors_pm1.sort()
q = factors_pm1[1][0]
r = factors_pm1[2][0]
ic(q, r)

F = GF(p)
F_B = F(B)
b = discrete_log(F_B, F(g))
ic(b)

ss = pow(A, int(b), p)

io.sendlineafter(b'> ', b'3')
flag_enc = bytes.fromhex(io.recvline(False).decode().split('= ')[1])

key = sha256(long_to_bytes(ss)).digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)
pt = cipher.decrypt(flag_enc)
print(pt)