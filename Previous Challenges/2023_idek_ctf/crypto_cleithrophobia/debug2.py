#!/usr/bin/env python3
#
# Polymero
#

# Imports
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import sys

# Local imports
with open('flag.txt', 'rb') as f:
    FLAG = f.read()
    f.close()

# Header
HDR = r"""|
|
|       __ _       ___ ____ ______ __ __ ____   ___  ____  __ __  ___  ____  ____  ____
|      /  ] |     /  _]    |      |  |  |    \ /   \|    \|  |  |/   \|    \|    |/    |
|     /  /| |    /  [_ |  ||      |  |  |  D  )     |  o  )  |  |     |  o  )|  ||  o  |
|    /  / | |___/    _]|  ||_|  |_|  _  |    /|  O  |   _/|  _  |  O  |     ||  ||     |
|   /   \_|     |   [_ |  |  |  | |  |  |    \|     |  |  |  |  |     |  O  ||  ||  _  |
|   \     |     |     ||  |  |  | |  |  |  .  \     |  |  |  |  |     |     ||  ||  |  |
|    \____|_____|_____|____| |__| |__|__|__|\_|\___/|__|  |__|__|\___/|_____|____|__|__|
|
|"""


# Server encryption function
def encrypt(msg, key):

    pad_msg = pad(msg, 16)
    blocks = [os.urandom(16)] + [pad_msg[i:i+16] for i in range(0,len(pad_msg),16)]
    print("\npt_blocks", file=sys.stderr)
    [print(block, file=sys.stderr) for block in blocks]

    itm = [blocks[0]]
    for i in range(len(blocks) - 1):
        tmp = AES.new(key, AES.MODE_ECB).encrypt(blocks[i+1])
        itm += [bytes(j^k for j,k in zip(tmp, blocks[i]))]
    print("\nm_blocks", file=sys.stderr)
    [print(block, file=sys.stderr) for block in itm]

    cip = [blocks[0]]
    for i in range(len(blocks) - 1):
        tmp = AES.new(key, AES.MODE_ECB).decrypt(itm[-(i+1)])
        cip += [bytes(j^k for j,k in zip(tmp, itm[-i]))]
    print("\nct_blocks", file=sys.stderr)
    [print(block, file=sys.stderr) for block in cip]

    return b"".join(cip[::-1])


# Server connection
KEY = os.urandom(32)

print(HDR)
print("|  ~ I trapped the flag using AES encryption and decryption layers, so good luck ~ ^w^")
print(f"|\n|    flag = {encrypt(FLAG, KEY).hex()}")

enc_0x10 = AES.new(KEY, AES.MODE_ECB).encrypt(b'\x10'*16)
enc_0x69 = AES.new(KEY, AES.MODE_ECB).encrypt(b'\x69'*16)
dec_0x69 = AES.new(KEY, AES.MODE_ECB).decrypt(b'\x69'*16)
print(f"enc_0x10={enc_0x10}", file=sys.stderr)
print(f"enc_0x69={enc_0x69}", file=sys.stderr)
print(f"dec_0x69={dec_0x69}", file=sys.stderr)

# Server loop
while True:

    try:

        print("|\n|  ~ Want to encrypt something?")
        msg = bytes.fromhex(input("|\n|    > (hex) "))

        enc = encrypt(msg, KEY)
        print(f"|\n|   {enc.hex()}")

    except KeyboardInterrupt:
        print('\n|\n|  ~ Well goodbye then ~\n|')
        break

    except:
        print('|\n|  ~ Erhm... Are you okay?\n|')
