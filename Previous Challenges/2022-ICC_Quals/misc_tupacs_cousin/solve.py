from icecream import ic

with open('message.txt') as fh:
    data = fh.read()

lines = data.split('\n')

binary = ''

for line in lines:
    if line == '':
        continue
    parts = line.split(',')
    parse = lambda x: '0' if float(x) < 0 else '1'
    binary += parse(parts[0])
    binary += parse(parts[1])

print(binary)

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

print(bitstring_to_bytes(binary))