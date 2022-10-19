from pwn import *
from icecream import ic
from Crypto.Util.number import long_to_bytes, bytes_to_long
from sage.all import *


# p = process('python3 debug.py', shell=True)
p = remote('138.68.162.164', 31621)

def encrypt_own(msg: int):
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b': ', long_to_bytes(msg).hex().encode())
    return get_result()

def get_result():
    lines = [p.recvline(False).decode() for _ in range(64)]
    lines_parts = [line.split(', ') for line in lines]
    results = [(int(parts[0][1:]), int(parts[1][:-1])) for parts in lines_parts]
    return results


N = 2**1024

key_bits = [1] * 64

while sum(key_bits) > 32:
    zero_enc = encrypt_own(0)
    for i, (x, y) in enumerate(zero_enc):
        if x % 2 == 0 and y % 2 == 1:
            key_bits[-i-1] = 0
            key_s = ''.join(str(b) for b in key_bits)
            ic(sum(key_bits))

key = 0
for i, b in enumerate(key_bits[::-1]):
    key += b << i
ic(key)

# For testing
# key = 815912714321001519

p.sendlineafter(b'> ', b'1')
flag_enc = get_result()
x_arr = []
y_arr = []
for i in range(64):
    if key & 1 << i != 0:
        x_arr.append(flag_enc[i][0])
        y_arr.append(flag_enc[i][1])

R = IntegerModRing(N)
M = Matrix(R, [[pow(x, i, N) for i in range(32)] for x in x_arr])
b = vector(R, y_arr)
x = M.solve_right(b)

flag = long_to_bytes(x[0]).decode()
ic(flag)

p.close()