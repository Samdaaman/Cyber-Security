# Setup
image_path = './tests/lsb_spongebob.png'
target_height = 28
# End Setup

from PIL import Image
from binascii import hexlify

# get the image
image = Image.open(image_path)
height = image.height
width = image.width
# get the image data as a series of tuples at a pixel access object
image_data = image.load()
print('Pixel Data mode is: {}\nSample: {}'.format(image.mode, image_data[0, 0]))

data_bin = ''
for x in range(width):
    pixel_value = image_data[x, target_height]

    red_lsb = bin(pixel_value[0])[-1]
    data_bin += red_lsb

    green_lsb = bin(pixel_value[1])[-1]
    data_bin += green_lsb

    blue_lsb = bin(pixel_value[2])[-1]
    data_bin += blue_lsb

print('Bits read: {}'.format(len(data_bin)))
data = b''
num_bytes = int(len(data_bin)/8)
print('Bytes to process: {} = {}'.format(len(data_bin)/8, num_bytes))

for byte_index in range(num_bytes):
    bit_list = data_bin[byte_index*8 : (byte_index+1)*8]  # eg [0, 0, 1, 0, 1, 1, 1, 0]
    eight_bits = ''.join(bit_list)  # eg 00101110
    byte_int = int(eight_bits, 2)  # eg 46
    byte = byte_int.to_bytes(1, 'big')  # eg b'.' ('.' is chr(46))
    data += byte

print('\nRaw:')
print(data)
print('\nHex:')
print(hexlify(data))
