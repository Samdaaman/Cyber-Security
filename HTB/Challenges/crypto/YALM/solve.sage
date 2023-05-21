from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from icecream import ic
from sage.all import *


def main():
    proc = remote('138.68.155.111', int(32154))
    # proc = process(['python3', 'debug.py'], stderr=None)

    if False: # set to True to find n
        def test_enc(x: int):
            proc.sendlineafter(b'Option: ', f'2'.encode())
            proc.sendlineafter(b'Plaintext: ', f'{long_to_bytes(x).hex()}'.encode())
            line = proc.recvline(False)
            return line == b'Thanks for the message!'


        i = 1
        while test_enc(1 << i):
            ic(i)
            i *= 2

        # Just check n is of the len 2**i bits (and not a weird number)
        assert not test_enc(1 << i) 
        assert test_enc(1 << (i-1))

        n_bits = i
        ic(n_bits)

        n = 0
        while i > 0:
            if test_enc(n + (1 << i)):
                n += 1 << i
            i -= 1
            print(f'Brute forcing n: {i} / {n_bits}')

        n += 1
    else:
        # From the above
        n = 21749248918759683544337447272671509713087570396847392696977994631698960045317596819865693333334493624370502448636831584145988028711233567234243060258534971464669149620614565032099403467041715388472573566028628032216786420721029298628718338901002634257184379911607586178908031583767930607042050327867387826322057745659825383472535093247656847914770054940932586227870658228788851350227826766531278231302804798812982333973499725242482126946725617567342220811180425286455535934049795118021253184879329685587581988120903375604417828886611483991738931048802648869100685999118954373198032024067740799452410209559772440413103
    
    ic(n)

    proc.sendlineafter(b'Option: ', f'1'.encode())
    ct1 = int(proc.recvline(False).split(b'Ciphertext: ')[1].decode(), 16)
    pt2 = bytes_to_long(b'Hey! This is my secret... it is secure because RSA is extremely strong and very hard to break... Here you go: HTB{')
    while True:
        ct2 = int(pow(pt2, 3, n))

        # https://en.wikipedia.org/wiki/Coppersmith%27s_attack#Coppersmith%E2%80%99s_short-pad_attack
        # https://github.com/ValarDragon/CTF-Crypto/blob/master/RSA/FranklinReiter.sage
        e = 3
        P.<x,y> = PolynomialRing(ZZ)
        ZmodN = Zmod(n)
        g1 = x^e - ct1
        g2 = (x+y)^e - ct2
        res = g1.resultant(g2)
        P.<y> = PolynomialRing(ZmodN)
        # Convert Multivariate Polynomial Ring to Univariate Polynomial Ring
        rres = 0
        for i in range(len(res.coefficients())):
            rres += res.coefficients()[i]*(y^(res.exponents()[i][1]))
        eps=1/40
        diff_array = rres.small_roots(epsilon=eps)
        if len(diff_array) == 0:
            pt2 = pt2 << 8
            ic(len(long_to_bytes(pt2)))
            continue
        else:
            break

    diff = int(diff_array[0])
    if diff > n // 2:
        diff = diff - n
    ic(diff)
    ic(long_to_bytes(pt2 - diff))


if __name__ == '__main__':
    main()
