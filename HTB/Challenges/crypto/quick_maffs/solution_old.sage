from multiprocessing.pool import Pool
from typing import List, Tuple
from sage.all import *
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
    e = 13
    m1 = b'HTB{FAKE_FLAG'
    m2 = b'_FOR_TESTING_'
    m3 = b'12345678910!}'
    pts = [bytes_to_long(i) for i in [m1, m2, m3]]
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
                    fh.write(f'{result}\n')
                    fh.flush()
                    bar.next()


def crack(args: Tuple[int, Tuple[int], int, int]):
    N, (c1, c2, c3), w, e = args

    Pall.<x1, x2, x3> = PolynomialRing(Integers(N))

    P0 = x1 + x2 + x3 - w
    Q0 = P0
    ic(Q0)
    ic(parent(Q0))

    P1 = x1^e - c1
    Q1 = Q0.polynomial(x1).resultant(P1.polynomial(x1))
    x2, x3 = parent(Q1).gens()
    ic(parent(Q1))

    P2 = x2^e - c2
    Q2 = Q1.polynomial(x2).resultant(P2.polynomial(x2))
    x3, = parent(Q2).gens()

    P3 = x3^e - c3

    gcd3 = xgcd_integer_mod_univariate_poly(Q2, P3)[0]
    m3_int = -gcd3.coefficients()[0]
    m3 = long_to_bytes(m3_int)
    ic(m3)

    Q1 = Q1.subs({x3: m3_int})
    gcd2 = xgcd_integer_mod_univariate_poly(Q1, P2)[0]
    ic(gcd2)
    ic(gcd2.coefficients())
    coeff_a = gcd2.coefficients()[0]
    m2_int = pow(-coeff_a, -1, N)
    m2 = long_to_bytes(m2_int)
    ic(m2)

    m1_int = w - m2_int - m3_int
    m1 = long_to_bytes(m1_int)
    ic(m1)
    return e, m1 + m2 + m3


def xgcd_integer_mod_univariate_poly(a, b):
    # view-source:https://mathsci2.appstate.edu/~cookwj/sage/algebra/Euclidean_algorithm-poly.html 
    tmp = a.quo_rem(b) 
    r=[a, b, tmp[1]]
    q=[0, 0, tmp[0]]

    i=2
    # While we have yet to reach a zero remainder continue divisions tacking on the new
    # quotient and remainder to our lists q and r.
    while r[i] != 0:
        i=i+1
        tmp = r[i-2].quo_rem(r[i-1]) 
        q.append(tmp[0])
        r.append(tmp[1])

    # coefficients grabs the coefficients of r[i-1] (the last nonzero remainder = gcd). 
    # The "[-1]" grabs the final coefficient (i.e. the leading coefficient). 
    # gcd's for PIDs are defined up to a unit multiple. For polynomial rings it is customary
    # to make "the" gcd a monic polynomial. Thus we should divide by the leading coefficient.
    lc = r[i-1].coefficients()[-1]    
        
    # This reverses the Euclidean algorithm to find A and B so that Aa+Bb=gcd.
    # Notice the for loop is stepping down by -1 from i-2 to 2.
    # 
    # Also, notice that we divide by lc throughout so that the gcd is monic.
    A = 1
    B = -q[i-1]
    for j in reversed(range(2,i-1)):
        tmp = B
        B = A-q[j]*B
        A = tmp


    g = r[i-1]/lc
    s = A/lc
    t = B/lc
    return (g, s, t)


if __name__ == '__main__':
    # test_multi()
    main()
