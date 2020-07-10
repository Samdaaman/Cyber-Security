import math
import binascii

with open('c1_.lsb', 'rb') as fh:
    data = fh.read()

flip = False
p1 = []
for i in range(len(data)):
    c = data[i]
    if not flip:
        p1.append([c])
    else:
        p1[-1].append(c)
    flip = not flip

p2 = []
for i in p1:
    p2.append(i[0])

p3 = []
for i in range(math.floor(len(p2) / 8)):
    p3.append([
        p2[i*8],
        p2[i*8 + 1],
        p2[i*8 + 2],
        p2[i*8 + 3],
        p2[i*8 + 4],
        p2[i*8 + 5],
        p2[i*8 + 6],
        p2[i*8 + 7],
    ])

p4 = p3[0:58]
print('\n'.join([str(i) for i in p3]))

p5 = []
for i in p4:
    p5 += [str(j) for j in i]

n = int(f'0b{"".join(p5)}', 2)
print(binascii.unhexlify('%x' % n))
