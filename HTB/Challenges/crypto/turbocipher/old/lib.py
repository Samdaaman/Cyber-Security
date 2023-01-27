from decimal import Decimal, getcontext
from typing import Callable
from Crypto.Util.number import bytes_to_long, getPrime, getRandomRange
from gmpy2 import mpz
from sage.all import factor
from icecream import ic


def turbonacci(n: int, p: int, b: int, c: int) -> int:
    if n < 2:
        return n

    return (b * turbonacci(n - 1, p, b, c) +
            c * turbonacci(n - 2, p, b, c)) % p


def lcg(x: int, m: int, n: int, p: int) -> int:
    return (m * x + n) % p


def turbocrypt(pt: int, k: int, f: Callable[[int], int]) -> int:
    return sum((f(i + 1) - f(i)) for i in range(k, pt))


cache = {}
def fast_turbonacci_old(n: int, p: int, b: int, c: int) -> int:
    if n < 2:
        return n

    if p not in cache:
        cache[p] = {}

    if n in cache[p]:
        return cache[p][n]

    f = (b*fast_turbonacci_old(n-1, p, b, c) + c*fast_turbonacci_old(n-2, p, b, c)) % p
    cache[p][n] = f

    return f


def dec_power(num, n, p):
    total = 1
    while n > 0:
        ic(n)
        if n % 2 == 1:
            total *= num
            total %= p
        num = (num**2) % p
        n = n >> 1
    return total


def fast_turbonacci(n: int, p: int, b: int, c: int) -> int:
    getcontext().prec = 500
    b_dec = Decimal(b)
    c_dec = Decimal(c)
    denominator = (b_dec**2 + 4*c_dec)**Decimal(1/2)
    ic(denominator)
    f_n = dec_power((b_dec + (b_dec**2 + 4*c_dec)**Decimal(1/2)) / 2, n, (round(p*10000))) / denominator
    return round(f_n) % p
    

def fast_turbocrypt(pt: int, k: int, f: Callable[[int], int]) -> int:
    return f(pt) - f(k)


def test():
    for i in range(30):
        b, c, p = getPrime(512), getPrime(512), getPrime(512)

        assert turbonacci(i, p, b, c) == fast_turbonacci_old(i, p, b, c)
        assert turbocrypt(i, -1, int) == fast_turbocrypt(i, -1, int)


if __name__ == '__main__':
    test()
