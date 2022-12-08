

# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_10 = Integer(10); _sage_const_1024 = Integer(1024); _sage_const_5 = Integer(5); _sage_const_23 = Integer(23); _sage_const_3 = Integer(3); _sage_const_7 = Integer(7); _sage_const_11 = Integer(11); _sage_const_13 = Integer(13); _sage_const_15 = Integer(15); _sage_const_17 = Integer(17); _sage_const_19 = Integer(19)
from datetime import datetime
from multiprocessing.pool import Pool
from typing import Tuple
from sage.all import *
from icecream import ic
from Crypto.Util.number import *
from progress.bar import Bar


def main():
    with open('output.txt') as fh:
        data = fh.read().strip().split(',')

    N = int(data[_sage_const_0 ])
    cts = eval(','.join(data[_sage_const_1 :-_sage_const_1 ]))  # type: tuple[int]
    hint = int(data[-_sage_const_1 ])

    ic(N)
    ic(cts)
    ic(hint)

    primes = set()
    p = _sage_const_1 
    while True:
        p = Primes().next(p)
        if p > _sage_const_2 **_sage_const_10 :
            break
        primes.add(p)
    ic(len(primes))
    crack_multi(N, cts, hint, primes)


def test():
    p, q = getPrime(_sage_const_1024 ), getPrime(_sage_const_1024 )
    N = p*q
    e = _sage_const_5 
    m1 = b'HTB{FAKE_FLAG'
    m2 = b'_FOR_TESTING_'
    m3 = b'12345678910!}'
    pts = [bytes_to_long(i) for i in [m1, m2, m3]]
    ic(pts)
    cts = [pow(i,e,N) for i in pts]
    hint = sum(pts) # bcuz i don't want make chall unsolvable
    crack((N, cts, hint, e))


def test_multi():
    p, q = getPrime(_sage_const_1024 ), getPrime(_sage_const_1024 )
    N = p*q
    e = _sage_const_23 
    m1 = b'HTB{FAKE_FLAG'
    m2 = b'_FOR_TESTING_'
    m3 = b'12345678910!}'
    pts = [bytes_to_long(i) for i in [m1, m2, m3]]
    cts = [pow(i,e,N) for i in pts]
    hint = sum(pts) # bcuz i don't want make chall unsolvable
    primes = [_sage_const_2 ,_sage_const_3 ,_sage_const_5 ,_sage_const_7 ,_sage_const_11 ,_sage_const_13 ,_sage_const_15 ,_sage_const_17 ,_sage_const_19 ,_sage_const_23 ]
    crack_multi(N, cts, hint, primes)


def crack_multi(N, cts, hint, primes):
    const = lambda x: [x] * len(primes)
    with open('results.txt', 'w') as fh:
        with Bar(max=len(primes)) as bar:
            with Pool() as pool:
                for result in pool.imap_unordered(crack, zip(const(N), const(cts), const(hint), primes), _sage_const_1 ):
                    fh.write(f'[{datetime.now()}] {result}\n')
                    fh.flush()
                    bar.next()


def crack(args: Tuple[int, Tuple[int], int, int]):
    N, (c1, c2, c3), w, e = args

    Pall = PolynomialRing(Integers(N), names=('x1', 'x2', 'x3',)); (x1, x2, x3,) = Pall._first_ngens(3)

    P0 = w - x1 - x2 - x3
    P1 = x1**e - c1
    P2 = x2**e - c2
    P3 = x3**e - c3
    I = ideal(P0, P1, P2, P3)
    B = I.groebner_basis()
    if len(B) == _sage_const_1 :
        return e, None

    m1_int = -int(B[_sage_const_0 ].coefficients()[_sage_const_1 ]) % N
    m2_int = -int(B[_sage_const_1 ].coefficients()[_sage_const_1 ]) % N
    m3_int = -int(B[_sage_const_2 ].coefficients()[_sage_const_1 ]) % N

    m = long_to_bytes(m1_int) + long_to_bytes(m2_int) + long_to_bytes(m3_int)
    # ic(m)
    return e, m


if __name__ == '__main__':
    # test()
    # test_multi()
    main()
