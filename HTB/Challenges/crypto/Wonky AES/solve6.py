from itertools import product
import math
from pwn import remote, process
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from icecream import ic
import lib

# mix_col_lookup: dict[int, tuple[int, int]] = {}
mix_col_lookup: dict[int, dict[int, dict[int, dict[int, tuple[int, int]]]]] = {}
mix_col_lookup_l1: dict[int, dict[int, list[tuple[int, int, int, int]]]] = { i: { j: [] for j in range(256) } for i in range(256) }
mix_col_xor_options: list[list[int]] = [[0 for _ in range(256)] for _ in range(4)]
for i in range(4):
    for c in range(256):
        col = [0 for _ in range(4)]
        col[i] = c
        lib.mix_single_column(col)
        # idx = sum(col[j] << (24 - 8*j) for j in range(4))
        # mix_col_lookup[idx] = (c, i)
        mix_col_lookup_l1[col[0]][col[1]].append((col[2], col[3], c, i))

        if col[0] not in mix_col_lookup:
            mix_col_lookup[col[0]] = {}
        if col[1] not in mix_col_lookup[col[0]]:
            mix_col_lookup[col[0]][col[1]] = {}
        if col[2] not in mix_col_lookup[col[0]][col[1]]:
            mix_col_lookup[col[0]][col[1]][col[2]] = {}
        mix_col_lookup[col[0]][col[1]][col[2]][col[3]] = (c, i)

        for j in range(4):
            mix_col_xor_options[j][col[j]] += 1

post_sbox_lookup: dict[int, set[int]] = { i: set() for i in range(256) }
for post_xor in range(256):
    for post_sbox in range(256):
        post_sbox_xord = post_sbox ^ post_xor
        pre_sbox = lib.inv_sbox[post_sbox]
        pre_sbox_xord = lib.inv_sbox[post_sbox_xord]
        pre_xor = pre_sbox ^ pre_sbox_xord
        post_sbox_lookup[post_xor].add(pre_xor)
        # if pre_xor not in post_sbox_lookup[post_xor]:
        #     post_sbox_lookup[post_xor][pre_xor] = []
        # post_sbox_lookup[post_xor][pre_xor].append(post_sbox)

io = process('enc_fault2', stderr=None) # type: ignore

counter = 0
possible_lrnd_keys_all: list[set[int]] = [None for _ in range(4)] # type: ignore
possible_lrnd_options_l2: list[set[int]] = [None for _ in range(4)] # type: ignore

while True:
    io.sendlineafter(b': ', b'y')
    correct = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    faulted = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    xor_result = strxor(correct, faulted)

    # for buf in [correct, faulted, xor_result]:
    #     for i in range(4):
    #         print(buf[i*4:(i+1)*4].hex())
    #     print()

    col_num = 0
    for col_num in range(4):
        if xor_result[col_num] != 0:
            break

    col_correct = [correct[i*4 + (col_num-i)%4] for i in range(4)]
    col_fault = [faulted[i*4 + (col_num-i)%4] for i in range(4)]
    col_xor_result = [xor_result[i*4 + (col_num-i)%4] for i in range(4)]
    ic([hex(c) for c in col_xor_result])

    test1 = 0
    test2 = 0

    # def restep(lookup: dict[int, dict | list], lrnd_key_mask: int, level: int, options: set[int]):
    #     for xor, lookup_child in mix_col_lookup.items():
    #         if level < 3:
    #             ic(xor, len(lookup_child.keys()))
    #         for pre_sbox_char in range(256):
    #                 pre_sbox_char_xord = pre_sbox_char ^ xor
    #                 post_sbox_char = lib.sbox[pre_sbox_char]
    #                 post_sbox_char_xord = lib.sbox[pre_sbox_char_xord]
    #                 if post_sbox_char ^ post_sbox_char_xord == col_xor_result[0]:
    #                     lrnd_key_mask_next = lrnd_key_mask | (xor << (24 - level*8))
    #                     if level < 3:
    #                         restep(lookup_child, lrnd_key_mask_next, level + 1, options) # type: ignore
    #                     else:
    #                         options.add(lrnd_key_mask_next)

    def restep(lrnd_key_mask: int, level: int, pre_lrnd_options_l2: None | set[int], lrnd_options_l2: set[int], options: set[int]):
        for i, pre_xor in enumerate(post_sbox_lookup[col_xor_result[level]]):
            if level == 0:
                ic(i, pre_xor)
            
            lrnd_key_mask_next = lrnd_key_mask | (pre_xor << (24 - level*8))
            if level == 1:
                if pre_lrnd_options_l2 is not None and lrnd_key_mask_next not in pre_lrnd_options_l2:
                    continue

            lrnd_options_l2.add(lrnd_key_mask)
            if level < 3:
                restep(lrnd_key_mask_next, level + 1, pre_lrnd_options_l2, lrnd_options_l2, options) # type: ignore
            else:
                options.add(lrnd_key_mask_next)

    lrnd_options = set()
    lrnd_options_l2 = set()
    restep(0, 0, possible_lrnd_options_l2[col_num], lrnd_options_l2, lrnd_options)
    ic(len(lrnd_options))
    ic(len(lrnd_options_l2))
   
    if possible_lrnd_keys_all[col_num] is None:
        possible_lrnd_keys_all[col_num] = lrnd_options
        possible_lrnd_options_l2[col_num] = lrnd_options_l2
    else:
        possible_lrnd_keys_all[col_num].intersection_update(lrnd_options)
        possible_lrnd_options_l2[col_num].intersection_update(lrnd_options_l2)

    ic(len(possible_lrnd_keys_all[col_num]))
    ic(len(possible_lrnd_options_l2[col_num]))

    counter += 1
    ic(counter)
    possible_lrnd_keys_all_lens = [len(x) if x is not None else None for x in possible_lrnd_keys_all]
    if all(x is not None for x in possible_lrnd_keys_all):
        ic(math.prod(len(x) for x in possible_lrnd_keys_all))

        if math.prod(len(x) for x in possible_lrnd_keys_all) <= 256:
            break

io.sendlineafter(b': ', b'n')
flag_enc = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
print(flag_enc.hex())

rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

with open('rkeys.txt', 'w') as fh:
    fh.write('[\n')
    for rk in product(*possible_lrnd_keys_all):
        fh.write(f'    {list(rk)},\n')
    fh.write(']\n')

for last_rk in product(*possible_lrnd_keys_all):
    last_rk = last_rk[:4] + last_rk[7:8] + last_rk[4:7] + last_rk[10:12] + last_rk[8:10] + last_rk[13:16] + last_rk[12:13]
    aes_key = lib.get_key_from_last_rk(last_rk)
    aes = AES.new(aes_key, mode=AES.MODE_ECB)
    pt = aes.decrypt(flag_enc)
    if pt.startswith(b'HTB{'):
        print(pt.decode())
        break
