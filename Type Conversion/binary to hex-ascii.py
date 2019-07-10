# Setup
binary = '011100110110000101101101001000000110100101110011001000000110001101101111011011110110110000100001'
# End Setup

print('{} bits, {} hex values and {} bytes'.format(len(binary), len(binary)/4, len(binary)/8))

if len(binary) % 4 == 0:
    hex_unspaced = hex(int(binary, 2))
    print(hex_unspaced)

    hex_spaced = ''
    for i in range(int(len(hex_unspaced)/2)):
        hex_chr = hex_unspaced[i * 2 : i * 2 + 2]
        hex_spaced += hex_chr
        hex_spaced += ' '
    print(hex_spaced[3:-1])
else:
    print('Binary must be a multiple of 4 to be converted to hex')

if len(binary) % 8 == 0:
    data = b''
    num_bytes = int(len(binary) / 8)
    for byte_index in range(num_bytes):
        eight_bits = binary[byte_index*8 : (byte_index+1)*8]  # eg 00101110
        byte_int = int(eight_bits, 2)  # eg 46
        byte = byte_int.to_bytes(1, 'big')  # eg b'.' ('.' is chr(46))
        data += byte
    print(data)
else:
    print('Binary must be multiple of 8 to be converted to ASCII')