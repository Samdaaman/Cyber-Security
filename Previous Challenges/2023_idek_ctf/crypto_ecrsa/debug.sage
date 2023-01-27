from sage.all import *
from icecream import ic


def crack(d: int, M3, T3):
    e = 3
    lam = (e * d - 1) // 2
    ic(lam)
    m, ym = M3[:2]
    t = ZZ(int.from_bytes(b"ECRSA offers added security by elliptic entropy.", 'big'))
    yt = 2
    # t, yt = T3[:2]
    a, b = matrix([[m, 1], [t, 1]]).solve_right(vector([ym^2 - m^3, yt^2 - t^3]))
    ic(a, b)


def chall():
    p, q = [random_prime(2^512, lbound = 2^511) for _ in range(2)]
    e = 3

    while gcd(p - 1, e) != 1: p = next_prime(p)
    while gcd(q - 1, e) != 1: q = next_prime(q)

    n = p*q
    d = inverse_mod(e, (p-1)*(q-1))

    # d stands for debug. You don't even know n, so I don't risk anything.
    # print('d =', d)
    ic(d)
    ic(p)
    ic(q)
    ic((p-1)*(q-1))

    m = ZZ(int.from_bytes(b"It is UNBREAKABLE, I tell you!! I'll even bet a flag on it, here it is: idek{REDACTED}", 'big'))
    t = ZZ(int.from_bytes(b"ECRSA offers added security by elliptic entropy.", 'big'))
    ym = randint(1, n)
    yt = 2

    # I like it when my points lie on my curve.
    a, b = matrix([[m, 1], [t, 1]]).solve_right(vector([ym^2 - m^3, yt^2 - t^3]))
    ic(a,b)
    E = EllipticCurve(Zmod(n), [a, b])
    M = E(m, ym)
    T = E(t, yt)

    E.base_field = E.base_ring # fix multiplication over rings (might not work depending on sage version!)
    # print('Encrypted flag:', M*e)
    # print('Encrypted test:', T*e)

    M3, T3 = M*e, T*e
    M3 = [int(x) for x in M3]
    T3 = [int(x) for x in T3]

    ic(a * m + b - ym^2 + m^3)
    ic((a * M3[0] + b - M3[1]**2 + M3[0]**3))
    ic((a * M3[0] + b - M3[1]**2 + M3[0]**3) % n)
    ic((a * T3[0] + b - T3[1]**2 + T3[0]**3))
    ic((a * T3[0] + b - T3[1]**2 + T3[0]**3) % n)

    return d, M3, T3


def main():
    crack(*chall())


if __name__ == '__main__':
    main()
