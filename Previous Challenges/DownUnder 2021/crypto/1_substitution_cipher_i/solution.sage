from sage.all import *

def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P = PolynomialRing(ZZ, names=('x',)); (x,) = P._first_ngens(1)
f = 13*x^2 + 3*x + 7

ct = open('./output.txt', 'r').read().strip()

subs = []
for i in range(256):
    subs.append(encrypt(bytes([i]), f))

pt = ''
for c in ct:
    pt += chr(subs.index(c))

print(pt)