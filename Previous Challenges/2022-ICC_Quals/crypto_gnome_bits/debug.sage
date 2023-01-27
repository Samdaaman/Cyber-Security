from sage.all import *
from icecream import ic
import hashlib
import random

def randomise_prime(p):
    p_hat = p ^^ (int.from_bytes(random.randbytes(16), byteorder='big') >> 0x44)
    return next_prime(p_hat)

def encrypt(m, e, n):
    return pow(m, e, n)

p_pre = 13234103194443360542314003606061822952790304494137605794868717446846733612137338208297065257117670896243054116568306649642696655789989763579668452786195671
q_pre = 9392325738879221091161052241542958552908752788297182113252702566521782136989369043806317543485997663281228367799667934964580993161316000835769458928107171

p = randomise_prime(p_pre)
q = randomise_prime(q_pre)

print("p", p)
print("q", q)

N = p * q
print("N", N)

e = 0x10001

with open("output.csv", 'w') as outfile:
    with open("messages.txt", 'rb') as infile:
        outfile.write("count,encrypted\r\n")
        for i,M in enumerate(infile.readlines()):
            MNum = int.from_bytes(M.strip(), byteorder='big')
            outfile.write(f"{i},{encrypt(MNum, e, N)}\r\n")

    with open("flag.txt", 'rb') as flagfile:
        MNum = int.from_bytes(flagfile.read().strip(), byteorder='big')
        outfile.write(f"flag,{encrypt(MNum, e, N)}\r\n")