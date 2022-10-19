

def crack_old(N: int, cts: Tuple[int], hint: int, e: int):
    c1, c2, c3 = cts
    w = hint

    # P.<xi, yi> = PolynomialRing(Integers(N))
    P = PolynomialRing(Integers(N), names=('xi', 'yi',)); (xi, yi,) = P._first_ngens(2)
    P1 = xi^e - c1
    P2 = xi^e - c2
    P3 = xi^e - c3
    R1 = P1
    S2 = P3.subs(w - yi)
    S1 = S2.subs(yi + xi).polynomial(xi).resultant(P2.subs(xi).polynomial(xi))

    ic(S1)
    ic(R1)

    ic(gcd(S1, R1))