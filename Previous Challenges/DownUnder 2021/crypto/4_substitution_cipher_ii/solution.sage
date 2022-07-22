from string import ascii_lowercase, digits
from sage.all import *
from icecream import ic


CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
# enc = open('./output.txt', 'r').read().strip()

n = len(CHARSET)
ic(n)

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

ic(f)

b = CHARSET.index(enc[0])
a = (CHARSET.index(enc[1]) - b) % n

ic(a)
ic(b)


# known = 'DUCTF{}'
# known_enc = enc[:6] + enc[-1]

# assert len(known) == len(known_enc)

# while True:
#     f = P.random_element(4) * x^2 + a*x + b
#     enc_test = encrypt(known, f)

#     if enc_test == known_enc:
#         break

# print(f)


