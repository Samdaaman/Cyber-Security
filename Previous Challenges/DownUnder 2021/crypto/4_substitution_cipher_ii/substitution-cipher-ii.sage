from string import ascii_lowercase, digits
from sage.all import *

CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
n = len(CHARSET)

def encrypt(msg, f):
    ct = ''
    for c in msg:
        ct += CHARSET[f.substitute(CHARSET.index(c))]
    return ct

# P.<x> = PolynomialRing(GF(n))
P = PolynomialRing(GF(n), names=('x',)); (x,) = P._first_ngens(1)
f = P.random_element(6)

FLAG = open('./flag.txt', 'r').read().strip()

enc = encrypt(FLAG, f)
print(enc)