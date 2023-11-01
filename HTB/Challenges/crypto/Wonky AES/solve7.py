from itertools import product
import math
from pwn import remote, process
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from icecream import ic
import lib

mix_col_lookup: dict[int, dict[int, dict[int, dict[int, list[tuple[int, int]]]]]] = {}
for i in range(4):
    for c in range(256):
        col = [0 for _ in range(4)]
        col[i] = c
        lib.mix_single_column(col)
        if col[0] not in mix_col_lookup:
            mix_col_lookup[col[0]] = {}
        if col[1] not in mix_col_lookup[col[0]]:
            mix_col_lookup[col[0]][col[1]] = {}
        if col[2] not in mix_col_lookup[col[0]][col[1]]:
            mix_col_lookup[col[0]][col[1]][col[2]] = {}
        if col[3] not in mix_col_lookup[col[0]][col[1]][col[2]]:
            mix_col_lookup[col[0]][col[1]][col[2]][col[3]] = []
        mix_col_lookup[col[0]][col[1]][col[2]][col[3]].append((c, i))

post_sbox_lookup: dict[int, dict[int, list[int]]] = { i: {} for i in range(256) }
for post_xor in range(256):
    for post_sbox in range(256):
        post_sbox_xord = post_sbox ^ post_xor
        pre_sbox = lib.inv_sbox[post_sbox]
        pre_sbox_xord = lib.inv_sbox[post_sbox_xord]
        pre_xor = pre_sbox ^ pre_sbox_xord
        if pre_xor not in post_sbox_lookup[post_xor]:
            post_sbox_lookup[post_xor][pre_xor] = []
        post_sbox_lookup[post_xor][pre_xor].append(post_sbox)

io = process('enc_fault2', stderr=None) # type: ignore

counter = 0

while True:
    io.sendlineafter(b': ', b'y')
    correct = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    faulted = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    xor_result = strxor(correct, faulted)

    col_num = 0
    for col_num in range(4):
        if xor_result[col_num] != 0:
            break

    col_correct = [correct[i*4 + (col_num-i)%4] for i in range(4)]
    col_fault = [faulted[i*4 + (col_num-i)%4] for i in range(4)]
    col_xor_result = [xor_result[i*4 + (col_num-i)%4] for i in range(4)]
    ic([hex(c) for c in col_xor_result])

    possible_post_sbox_chars: list[list[int]] = [[0 for _ in range(256)] for _ in range(4)]

    for c0, d0 in mix_col_lookup.items():
        for c1, d1 in d0.items():
            for c2, d2 in d1.items():
                for c3, d3 in d2.items():
                    for i in range(4):
                        pre_xor = [c0, c1, c2, c3][i]
                        if pre_xor in post_sbox_lookup[col_xor_result[i]]:
                            for post_sbox in post_sbox_lookup[col_xor_result[i]][pre_xor]:
                                possible_post_sbox_chars[i][post_sbox] += 1

    counter += 1
    ic(counter)
    possible_post_sbox_chars_lens = [len(x) for x in possible_post_sbox_chars]
    ic(possible_post_sbox_chars_lens)
    break

# io.sendlineafter(b': ', b'n')
# flag_enc = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
# print(flag_enc.hex())

# rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

# with open('rkeys.txt', 'w') as fh:
#     fh.write('[\n')
#     for rk in product(*possible_lrnd_keys_all):
#         fh.write(f'    {list(rk)},\n')
#     fh.write(']\n')

# for last_rk in product(*possible_lrnd_keys_all):
#     last_rk = last_rk[:4] + last_rk[7:8] + last_rk[4:7] + last_rk[10:12] + last_rk[8:10] + last_rk[13:16] + last_rk[12:13]
#     aes_key = lib.get_key_from_last_rk(last_rk)
#     aes = AES.new(aes_key, mode=AES.MODE_ECB)
#     pt = aes.decrypt(flag_enc)
#     if pt.startswith(b'HTB{'):
#         print(pt.decode())
#         break
