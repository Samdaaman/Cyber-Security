import base64
from PIL import Image

image = Image.open("tests/lsb_spongebob_isolated.png")

extracted = ''

pixels = image.load()
# Iterate over pixels of the first row
for x in range(0,image.width):
    r,g,b = pixels[x,0]
    # Store LSB of each color of each pixel
    extracted += bin(255 ^ r)[-1]
    extracted += bin(255 ^ g)[-1]
    extracted += bin(255 ^ b)[-1]

chars = []
for i in range(round(len(extracted)/8)):
    byte = extracted[i*8:(i+1)*8]
    chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))

flag = base64.b64decode(''.join(chars))
print(flag)
