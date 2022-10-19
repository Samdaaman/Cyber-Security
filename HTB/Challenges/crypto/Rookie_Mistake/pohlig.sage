from multiprocessing.pool import Pool
from sage.all import *

# adapted from 
# https://github.com/Chongsawad/Pohlig-Hellman/blob/master/pohlig.sage

def pohlig_hellman_PGH(p, g, h):
    # g must be small
    F = IntegerModRing(p)
    g = F(g)
    h = F(h)
    G = []
    H = []
    X = []
    c = []
    pfactors = factor(p-1)

    with Pool() as pool:
        const = lambda x: [x] * len(pfactors)
        c = pool.map(_pohlig_Hellman_PGH_work, zip(range(len(pfactors)), const(p), const(g), const(h), const(pfactors)))

    print("G=", G, "\n", "H=", H, "\n", "X=", X)

    # Using Chinese Remainder
    c.reverse()

    for i in range(len(c)):
        if len(c) < 2:
            break
        t1 = c.pop()
        t2 = c.pop()
        r = crt(t1[0], t2[0], t1[1], t2[1])
        m = t1[1]*t2[1]
        c.append((r, m))

    print("(x,p-1) =", c[0])



def _pohlig_Hellman_PGH_work(args):
    i, p, g, h, pfactors = args
    gi = (g ^ ((p-1)/(pfactors[i][0] ^ pfactors[i][1])))
    hi = (h ^ ((p-1)/(pfactors[i][0] ^ pfactors[i][1])))
    xi = (log(hi[i], gi[i]))
    ci = ((xi[i], (pfactors[i][0] ^ pfactors[i][1])))
    return ci