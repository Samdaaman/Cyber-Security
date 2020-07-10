from PIL import Image

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')


i = Image.open('c7g.png')
di = i.load()

d = ''
b = ''
for y in range(i.height):
    print(y)
    p = di[0, y]

    for pi in p[0:3]:
        if pi != 0:
            d+='1'
        else:
            d+='0'

print(d)
#f = bitstring_to_bytes(''.join(d))
print(bytes(int(d[i : i + 8], 2) for i in range(0, len(d), 8)))
print(f)

