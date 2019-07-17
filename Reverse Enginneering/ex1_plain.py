import base64

s = [[82, 87, 53, 48, 90, 88, 73, 103, 85, 71, 70, 122, 99, 51, 100, 118, 99, 109, 81, 54, 73, 65, 61, 61], [90, 109, 120, 104, 90, 122, 112, 117, 98, 51, 82, 48, 97, 71, 86, 109, 98, 71, 70, 110]]
g = [62, 95, 54, 17, 63, 62, 0, 25, 56, 123, 24, 94, 0, 42, 103, 28, 6, 0, 28, 2]
x = ':::::::::::::::::::::::::::::abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def c(l):
    c = ''.join([x[x.index(l[b]) + 17] for b in range(len(l))])
    z = [ ord(d) for d in base64.encodebytes(c.encode('utf-8')).decode('utf-8')[:-1] ]
    return (g == [ s[1][w] ^ z[w] for w in range(len(z))])

def o(a):
    for c in a:
        b(c)

def b(v):
    h = b''
    for i in range(len(v)):
        h += chr(v[i]).encode('utf-8')
    return base64.decodebytes(h).decode('utf-8')

def u(q):
    try:
        print(c(input(b(s[0]))))
    finally:
        return False

u('ok')