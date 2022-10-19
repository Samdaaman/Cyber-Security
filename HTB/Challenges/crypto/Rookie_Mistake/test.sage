from sage.all import *
from icecream import ic
from Crypto.Util.number import getPrime
from random import randint
import itertools


def pohlig_hellman_old(p, g, h):
    factors = factor(p - 1)
    F = GF(p)
    g = F(g)
    h = F(h)
    ic(factors)
    residuals = []
    modului = []
    for pi, ki in factors:
        x_arr = []
        beta_arr = [h]
        for j in range(ki):
            if j > 0:
                divisor = g ^ (pi^(j-1) * x_arr[j-1])
                s = xgcd(divisor, h)[1]
                ic((pi^(j-1) * x_arr[j-1]), divisor, s, beta_arr[j-1] * s)
                beta_arr.append(beta_arr[j-1] * s)

            beta = beta_arr[j]
            lhs = beta ^ ((p-1) // pi^(j+1))
            rhs = g ^ ((p-1) // pi)
            x = discrete_log(lhs, rhs)
            x_arr.append(x)
            ic(pi, j, x)

        x = sum([pi^j * x_arr[j] for j in range(ki)])
        ic(pi, x)
        if x != 0:
            residuals.append(x)
            modului.append(pi ^ ki)

    ic(residuals)
    ic(modului)
    return crt(residuals, modului)


def pohlig_hellman(p, g, h):
    factors = factor(p - 1)
    F = GF(p)
    g = F(g)
    h = F(h)
    ic(factors)
    residuals_options = []
    modului = []
    for pi, ki in factors:
        lhs = h ^ ((p-1) // pi)
        rhs = g ^ ((p-1) // pi)
        x = discrete_log(lhs, rhs)
        ic(pi, x)
        if lhs == 1 and rhs == 1:
            residuals_options.append(list(range(pi)))
            print(f'Increasing result size by a {pi} times')
        else:
            residuals_options.append([x])
        modului.append(pi ^ ki)

    return set(crt(list(residuals), modului) for residuals in itertools.product(*residuals_options))


def gen_prime():
    while True:
        pm1 = 2 * getPrime(8) * getPrime(8) * getPrime(8)
        if is_prime(pm1 + 1) and not any(k > 1 for p, k in factor(pm1)):
            return pm1 + 1


def test1():
    while True:
        p = gen_prime()
        # p = getPrime(16)
        g = 3
        x = randint(0, p//2)
        h = pow(g, x, p)
        ic(h)
        ic(p)
        ic(x)
        t = pohlig_hellman(p, g, h)
        if x not in t:
            ic(t)
            break


def test2():
    p = getPrime(64)
    q = getPrime(64)
    n = p*q
    g = 0x69420
    x = 12345
    h = pow(g, x, n)
    cf = gcd(p-1, q-1)
    x_pm1 = pohlig_hellman(p, g, h)
    x_qm1 = pohlig_hellman(q, g, h, cf=cf)

    x_phi = crt(x_pm1, x_qm1, p-1, q-1)
    ic(x_phi)


def test3():
    p = 41
    g = 7
    h = 12
    x = pohlig_hellman(p, g, h)
    ic(x)
    ic(pow(g, x, p))


def test4():
    p = 8101
    g = 6
    h = 7531
    x = pohlig_hellman(p, g, h)
    ic(x)
    ic(pow(g, x, p))


def test5():
    h = 14082041
    p = 17985707
    g = 3
    x1 = 4052059
    x2 = pohlig_hellman(p, g, h)
    ic(pow(g, x1, p))


if __name__ == '__main__':
    test1()
