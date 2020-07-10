



def main():
    c = 'h2yv94p6qrs7naeh'
    k = 'flagaaaaaaaaaaaaa'
    #k = 'inwhichtombdidcryptography' * 5
    #k = 'khnumhotep' *2
    #k = 'cryptokhnumhotepa'
    #k = 'cryptokhnumhotep'
    #k = 'cryptographyfirst'
    k = 'cryptkhnumhotep2'
    a = 'abcdefghijklmnopqrstuvwxyz'
    A = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
    o1 = '0123456789'
    o2 = '1234567890'

    al = [
        'abcdefghijklmnopqrstuvwxyz0123456789',
        '0123456789abcdefghijklmnopqrstuvwxyz',
        a + o2,
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789',
        'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWYXZ',
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ',
        'ABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789abcdefghijklmnopqrstuvwxyz',
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789abcdefghijklmnopqrstuvwxyz'
        ]
    al = [
        a+o1,
        o1+a,
        a+A+o1,
        a+o1+A,
        A+a+o1,
        A+o1+a,
        o1+A+a,
        o1+a+A,
        a+o2,
        o2+a,
        a+A+o2,
        a+o2+A,
        A+a+o2,
        A+o2+a,
        o2+A+a,
        o2+a+A
    ]
    s=[]
    for a in al:
        j = 0
        p = ''
        for i in range(len(c)):
            ci = c[i]
            ki = k[i]
            if ci != ':':
                p += a[(a.index(ci) - a.index(ki)) % len(a)]
                j += 1
            else:
                p += ':'
        s.append(p)

    for a in []:
        j = 0
        p = ''
        for i in range(len(c)):
            ci = c[i]
            ki = k[j]
            if ci != ':':
                p += a[(a.index(ci) - a.index(ki)) % len(a)]
                j += 1
            else:
                p += ':'
        s.append(p)
    for a in al:
        j = 0
        p = ''
        for i in range(len(c)):
            ci = c[i]
            ki = k[i]
            if ci != ':':
                p += a[(a.index(ci) ^ a.index(ki)) % len(a)]
                j += 1
            else:
                p += ':'
        s.append(p)

    for a in al:
        j = 0
        p = ''
        for i in range(len(c)):
            ci = c[i]
            ki = k[j]
            if ci != ':':
                p += a[(a.index(ci) ^ a.index(ki)) % len(a)]
                j += 1
            else:
                p += ':'
        s.append(p)

    for f in s:
        print(f) if 'flag' or 1 in f else 0


if __name__ == "__main__":
    main()
