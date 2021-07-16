ah = '6b65813f4fe991efe2042f79988a3b2f2559d358e55f2fa373e53b1965b5bb2b175cf039'
bh = 'fd034c32294bfa6ab44a28892e75c4f24d8e71b41cfb9a81a634b90e6238443a813a3d34'
ch = 'de328f76159108f7653a5883decb8dec06b0fd9bc8d0dd7dade1f04836b8a07da20bfe70'

# with open('test.bin', 'wb+') as fh:
#     fh.write(bytearray.fromhex(a+b+c))

a, b, c = [bytes(bytearray.fromhex(i)) for i in (ah, bh, ch)]

# for j in range(256):
#     p = ''
#     for i in range(len(a)):
#         p += chr(a[i] ^ j)
#     print([p])

# freq = {}
# for ct in [a,c]:
#     print(ct)

#     for i in ct:
#         freq[i] = freq.get(i, 0) + 1

# for key, value in freq.items():
#     print(f'{key}: {value}')

pt = ''
for i in range(len(a)):
    pt += chr(a[i] ^ b[i] ^ c[i])

print(pt)

    