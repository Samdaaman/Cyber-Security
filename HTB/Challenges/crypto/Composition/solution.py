from hashlib import md5
from pwn import *
from icecream import ic
import gmpy2
from sage.all import *
from Crypto.Util.number import isPrime
from Crypto.Cipher import AES


proc = remote('134.122.104.208', 31802)
# proc = process('python3 debug.py', shell=True)


def recv_value(start: str):
    return proc.recvline_contains(start.encode(), False).decode().split(start)[1]

def recv_point():
    P_raw = recv_value('Point(')
    Px = int(P_raw.split('x=')[1].split(', ')[0])
    Py = int(P_raw.split('y=')[1].split(')')[0])
    return Px, Py


# print(proc.recvuntil(b'DEBUG_END').decode())

ct = bytes.fromhex(recv_value('Encrypted flag: '))
iv = bytes.fromhex(recv_value('IV: '))
N = int(recv_value('N: '))
Ax, Ay = recv_point()
proc.sendline()
Bx, By = recv_point()
proc.close()

ic(ct.hex())
ic(iv.hex())
ic(N)
ic(Ax, Ay)
ic(Bx, By)

n_root = int(gmpy2.iroot(N, int(2))[0])

if n_root % 2 == 0:
    n_root -= 1

p = 0
q = 0
while True:
    if gcd(n_root, N) > 1:
        p = n_root
        q = N // n_root
        break
    n_root -= 2

assert p*q == N

ic(p)
ic(q)

def next_prime(num):
    if num % 2 == 0:
        num += 1
    else:
        num += 2
    while not isPrime(num):
        num += 2
    return num

e = next_prime(p >> (512 // 4))
ic(e)

a = ((Ay**2 - Ax**3 - By**2 + Bx**3) * pow(Ax - Bx, -1, N)) % N
b = (Ay**2 - Ax**3 - a*Ax) % N
ic(a)
ic(b)

EC_p = EllipticCurve(GF(p), [a, b])
A_p = EC_p(Ax % p, Ay % p)
e_inv_p = int(pow(e, -1, A_p.order()))
G_p = e_inv_p * A_p
ic(G_p)
ic(A_p)
ic(e * G_p)
Gx_p = int(G_p.xy()[0])

ec_q = EllipticCurve(GF(q), [a, b])
A_q = ec_q(Ax % q, Ay % q)
e_inv_q = int(pow(e, -1, A_q.order()))
G_q = e_inv_q * A_q
ic(G_q)
ic(A_q)
ic(e * G_q)
Gx_q = int(G_q.xy()[0])

Gx = crt(Gx_p, Gx_q, p, q)

key = md5(str(Gx).encode()).digest()
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)
ic(pt)