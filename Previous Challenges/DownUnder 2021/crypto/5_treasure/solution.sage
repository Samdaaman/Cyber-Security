from pwn import *
from sage.all import *

FAKE_COORDS = 5754622710042474278449745314387128858128432138153608237186776198754180710586599008803960884
p = 13318541149847924181059947781626944578116183244453569385428199356433634355570023190293317369383937332224209312035684840187128538690152423242800697049469987

# context.log_level = 'debug'
io = process('python3 treasure.py', shell=True, raw=False)

def receive_int(prefix: str):
    line = io.recvline_contains(prefix.encode()).decode().strip().split(prefix)[1]
    return int(line)

def cuberoot(a, p):
    if p == 2:
        return a
    if p == 3:
        return a
    if (p%3) == 2:
        return pow(a,(2*p - 1)/3, p)
    if (p%9) == 4:
        root = pow(a,(2*p + 1)/9, p)
        if pow(root,3,p) == a%p:
            return root
        else:
            return None
    if (p%9) == 7:
        root = pow(a,(p + 2)/9, p)
        if pow(root,3,p) == a%p:
            return root
        else:
            return None
    else:
        print("Not implemented yet. See the second paper")

s1 = receive_int('Your share is: ')
io.sendline(b'1')
r = receive_int('The secret is revealed: ')

secret = (s1**3 * r) % p
secret_inv = pow(secret, -1, p)
r1_r2 = (s1 * secret_inv) % p
F = GF(p)
FAKE_COORDS_cuberoot = F(FAKE_COORDS).nth_root(3)
secret_inv_cuberoot = F(secret_inv).nth_root(3)
s1_fake = (FAKE_COORDS_cuberoot * secret_inv_cuberoot * s1) % p

io.sendline(f'{s1_fake}'.encode())
io.sendline(f'{secret}'.encode())

print(io.recvall().decode())