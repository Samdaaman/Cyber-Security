from typing import Tuple
from icecream import ic
from Crypto.Util.number import bytes_to_long, getPrime, getRandomRange
import lib
import sys
from decimal import *


def main():
    ic(lib.dec_power(5.5, 3, 100))


    # sys.setrecursionlimit(100000)
    bits = 10
    p = getPrime(bits)
    b = getPrime(bits)
    c = getPrime(bits)
    # find_periods(p, b, c)
    getcontext().prec = 10000

    n = getRandomRange(0, p)
    ic(p, b, c, n)
    ic(lib.fast_turbonacci(n, p, b, c))
    ic(lib.fast_turbonacci_old(n, p, b, c))




def find_periods(p: int, b: int, c: int):
    ic(p, b, c)
    f_pm1 = lib.fast_turbonacci_old(p-1, p, b, c)
    f_p = lib.fast_turbonacci_old(p, p, b, c)
    ic(f_pm1, f_p)
    i = 2
    first_zero = 0
    while True:
        f = lib.fast_turbonacci_old(i, p, b, c)
        if f == 0:
            print(f'Found first zero at {i}')
            first_zero = i
            break
        i += 1
    return

    i = first_zero
    while True:
        print(f'test = {lib.fast_turbonacci_old(i, p, b, c)}')
        if lib.fast_turbonacci_old(i+1, p, b, c) == 1:
            print(f'Found repeat at {i+1}')
            break
        i += first_zero

    # common_factor = gcd((b-1, c-1))
    # print(f'test2 = {(p-1) // common_factor}')


# def decimal_test(p: int, b: int, c: int):


if __name__ == '__main__':
    main()
