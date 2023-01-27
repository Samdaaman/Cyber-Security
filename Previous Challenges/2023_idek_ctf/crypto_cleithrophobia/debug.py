#!/usr/bin/env python3
#
# Polymero
#

# Imports
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor
import os
from icecream import ic

# Local imports
with open('flag.txt', 'rb') as f:
    FLAG = f.read()
    f.close()

# Server connection
KEY = os.urandom(32)

# Server encryption function
def encrypt(msg, key, iv):
    pad_msg = pad(msg, 16)
    blocks = [iv] + [pad_msg[i:i+16] for i in range(0,len(pad_msg),16)]

    itm = [blocks[0]]
    for i in range(len(blocks) - 1):
        tmp = AES.new(key, AES.MODE_ECB).encrypt(blocks[i+1])
        itm += [bytes(j^k for j,k in zip(tmp, blocks[i]))]

    cip = [blocks[0]]
    for i in range(len(blocks) - 1):
        tmp = AES.new(key, AES.MODE_ECB).decrypt(itm[-(i+1)])
        cip += [bytes(j^k for j,k in zip(tmp, itm[-i]))]

    return b"".join(cip[::-1])


def encrypt2(msg: bytes, key: bytes, iv: bytes):
    ic(len(msg), msg)
    pad_msg = pad(msg, 16)
    ic(len(pad_msg), pad_msg)

    pt_blocks = [pad_msg[i:i+16] for i in range(0,len(pad_msg),16)]
    ic(pt_blocks)

    m_blocks = []
    for i, pt_block in enumerate(pt_blocks):
        pt_block_enc = AES.new(key, AES.MODE_ECB).encrypt(pt_block)
        if i == 0:
            xor_input = iv
        else:
            xor_input = pt_blocks[i-1] # previous pt_block
        m_block = strxor(pt_block_enc, xor_input)
        m_blocks.append(m_block)

    ic(m_blocks)

    ct_blocks = []
    for i, m_block in enumerate(m_blocks[::-1]):
        m_block_dec = AES.new(key, AES.MODE_ECB).decrypt(m_block)
        if i == 0:
            xor_input = iv
        else:
            xor_input = m_blocks[-i] # previous m_block
        ct_block = strxor(m_block_dec, xor_input)
        ct_blocks.append(ct_block)

    return b''.join(ct_blocks[::-1] + [iv])

def main():
    pt = b'idek{FAKE_FAKE_FOR_TESTING12345678}'
    iv = os.urandom(16)
    # ct = encrypt(pt, KEY, iv)
    # ct2 = encrypt2(pt, KEY, iv)
    # ic(ct)
    # ic(ct2)
    # ic(ct == ct2)

    ic(encrypt(b'\x00' * 64, KEY, os.urandom(16)))
    ic(encrypt(b'', KEY, os.urandom(16)))


    # h_blocks = []
    # ct_blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    # for i, ct_block in enumerate(ct_blocks):
    #     if i > 0:
    #         h_blocks.append

if __name__ == '__main__':
    main()

# print(HDR)
# print("|  ~ I trapped the flag using AES encryption and decryption layers, so good luck ~ ^w^")
# print(f"|\n|    flag = {encrypt(FLAG, KEY).hex()}")



# # Server loop
# while True:

#     try:

#         print("|\n|  ~ Want to encrypt something?")
#         msg = bytes.fromhex(input("|\n|    > (hex) "))

#         iv = os.urandom(16)
#         enc = encrypt(msg, KEY, iv)
#         ic(enc)
#         enc2 = encrypt2(msg, KEY, iv)
#         ic(enc2)
#         print(f"|\n|   {enc.hex()}")

#     except KeyboardInterrupt:
#         print('\n|\n|  ~ Well goodbye then ~\n|')
#         break

#     except:
#         print('|\n|  ~ Erhm... Are you okay?\n|')
