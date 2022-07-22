from sage.all_cmdline import *
from Crypto.Util.number import getPrime, getRandomRange, isPrime, inverse, long_to_bytes, bytes_to_long
from icecream import ic


p = getPrime(16)
ic(p)
q = getPrime(16)
ic(q)
n = p*q
ic(n)
e = 65537

pt = bytes_to_long(b'sam')
ic(pt)

ct = pow(pt, e, n)

ic(ct)

l = (p-1)*(q-1)
ic(l)
d = pow(e, -1, l)
ic(d)

pt_test = pow(ct, d, n)
ic(pt_test)

test = crt(p, q, int(ct % p), int(ct % q))
ic(test)