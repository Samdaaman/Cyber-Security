# Setup
binary = '111111'
# End Setup

hex_unspaced = hex(int(binary, 2))
print(hex_unspaced[2:])

print()

hex_spaced = ''
for i in range(int(len(hex_unspaced)/2)):
    hex_chr = hex_unspaced[i * 2 : i * 2 + 2]
    hex_spaced += hex_chr
    hex_spaced += ' '
print(hex_spaced[3:-1])
