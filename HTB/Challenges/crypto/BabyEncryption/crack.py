with open('msg.enc') as fh:
    data = fh.read()
ct = bytearray.fromhex(data)

pt = []
for i in ct:
    for j in range(256):
        if (123 * j + 18) % 256 == i:
            pt.append(j)
            break

print(bytes(pt))