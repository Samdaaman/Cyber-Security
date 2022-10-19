from datetime import datetime
from multiprocessing.pool import Pool
from typing import Tuple
# from sage.all import *
from icecream import ic
from Crypto.Util.number import *
from progress.bar import Bar


def main():
    with open('output.txt') as fh:
        data = fh.read().strip().split(',')

    N = int(data[0])
    cts = eval(','.join(data[1:-1]))  # type: tuple[int]
    hint = int(data[-1])

    ic(N)
    ic(cts)
    ic(hint)

    primes = set()
    p = 1
    while True:
        p = Primes().next(p)
        if p > 2^10:
            break
        primes.add(p)
    ic(len(primes))
    crack_multi(N, cts, hint, primes)


def test():
    p, q = getPrime(1024), getPrime(1024)
    N = p*q
    e = 5
    m1 = b'HTB{FAKE_FLAG'
    m2 = b'_FOR_TESTING_'
    m3 = b'12345678910!}'
    pts = [bytes_to_long(i) for i in [m1, m2, m3]]
    ic(pts)
    cts = [pow(i,e,N) for i in pts]
    hint = sum(pts) # bcuz i don't want make chall unsolvable
    crack((N, cts, hint, e))


def test_multi():
    p, q = getPrime(1024), getPrime(1024)
    N = p*q
    e = 23
    m1 = b'HTB{FAKE_FLAG'
    m2 = b'_FOR_TESTING_'
    m3 = b'12345678910!}'
    pts = [bytes_to_long(i) for i in [m1, m2, m3]]
    cts = [pow(i,e,N) for i in pts]
    hint = sum(pts) # bcuz i don't want make chall unsolvable
    primes = [2,3,5,7,11,13,15,17,19,23]
    crack_multi(N, cts, hint, primes)


def crack_multi(N, cts, hint, primes):
    const = lambda x: [x] * len(primes)
    with open('results.txt', 'w') as fh:
        with Bar(max=len(primes)) as bar:
            with Pool() as pool:
                for result in pool.imap_unordered(crack, zip(const(N), const(cts), const(hint), primes), 1):
                    fh.write(f'[{datetime.now()}] {result}\n')
                    fh.flush()
                    bar.next()


def crack(args: Tuple[int, Tuple[int], int, int]):
    N, (c1, c2, c3), w, e = args

    Pall.<x1, x2, x3> = PolynomialRing(Integers(N))

    P0 = w - x1 - x2 - x3
    P1 = x1^e - c1
    P2 = x2^e - c2
    P3 = x3^e - c3
    I = ideal(P0, P1, P2, P3)
    B = I.groebner_basis()
    if len(B) == 1:
        return e, None

    m1_int = -int(B[0].coefficients()[1]) % N
    m2_int = -int(B[1].coefficients()[1]) % N
    m3_int = -int(B[2].coefficients()[1]) % N

    m = long_to_bytes(m1_int) + long_to_bytes(m2_int) + long_to_bytes(m3_int)
    # ic(m)
    return e, m


if __name__ == '__main__':
    # test()
    # test_multi()
    main()
