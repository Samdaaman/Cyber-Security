from itertools import product
import math
from pwn import remote, process
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from icecream import ic
import lib

mix_col_lookup: dict[int, tuple[int, int]] = {}
mix_col_xor_options: list[set[int]] = [set() for _ in range(4)]
for i in range(4):
    for c in range(256):
        col = [0 for _ in range(4)]
        col[i] = c
        lib.mix_single_column(col)
        idx = sum(col[j] << (24 - 8*j) for j in range(4))
        mix_col_lookup[idx] = (c, i)
        for j in range(4):
            mix_col_xor_options[j].add(col[j])
ic([len(x) for x in mix_col_xor_options])

io = process('enc_fault2', stderr=None) # type: ignore

counter = 0
possible_lrnd_keys_all = [set(i for i in range(256)) for _ in range(16)]

while math.prod(len(x) for x in possible_lrnd_keys_all) > 256:
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

    for i in range(4):
        possible_lrnd_keys: set[int] = set()
        for pre_sbox_char in range(256):
            for xor in mix_col_xor_options[i]:
                pre_sbox_char_xord = pre_sbox_char ^ xor
                post_sbox_char = lib.sbox[pre_sbox_char]
                post_sbox_char_xord = lib.sbox[pre_sbox_char_xord]
                if post_sbox_char ^ post_sbox_char_xord == col_xor_result[i]:
                    possible_lrnd_keys.add(col_correct[i] ^ post_sbox_char)
        possible_lrnd_keys_all[i*4 + (col_num+i)%4].intersection_update(possible_lrnd_keys)

    counter += 1
    ic([len(x) for x in possible_lrnd_keys_all])
    ic(math.prod(len(x) for x in possible_lrnd_keys_all))
    ic(counter)

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
