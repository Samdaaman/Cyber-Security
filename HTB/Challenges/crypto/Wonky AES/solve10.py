from itertools import product
import math
import multiprocessing
from pwn import remote, process
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from icecream import ic
import lib

io = process('enc_fault2', stderr=None) # type: ignore

counter = 0
r11_options: list[list[list[int]]] = [list() for _ in range(4)]

def do_work(args: tuple[int, list[int], list[int]]):
    c0, col_correct, col_xor_result = args
    r11_options: list[list[int]] = []
    test_val = [c0 ^ lib.inv_sbox[lib.sbox[c0] ^ col_xor_result[0]], 0, 0, 0]
    print(f'{c0=}', flush=True)
    for c1 in range(256):
        test_val[1] = c1 ^ lib.inv_sbox[lib.sbox[c1] ^ col_xor_result[1]]
        for c2 in range(256):
            test_val[2] = c2 ^ lib.inv_sbox[lib.sbox[c2] ^ col_xor_result[2]]
            for c3 in range(256):
                test_val[3] = c3 ^ lib.inv_sbox[lib.sbox[c3] ^ col_xor_result[3]]
                lib.inv_single_column(test_val)
                if test_val.count(0) == 3:
                    r11_option = [col_correct[i] ^ lib.sbox[[c0,c1,c2,c3][i]] for i in range(4)]
                    r11_options.append(r11_option)
    return r11_options

while any(len(x) == 0 for x in r11_options) or math.prod(len(x) for x in r11_options) > 1:
    io.sendlineafter(b': ', b'y')
    correct = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    faulted = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    if correct == faulted:
        continue

    xor_result = strxor(correct, faulted)

    col_num = 0
    for col_num in range(4):
        if xor_result[col_num] != 0:
            break

    col_correct = [correct[i*4 + (col_num-i)%4] for i in range(4)]
    col_fault = [faulted[i*4 + (col_num-i)%4] for i in range(4)]
    col_xor_result = [xor_result[i*4 + (col_num-i)%4] for i in range(4)]
    ic([hex(c) for c in col_xor_result])

    if len(r11_options[col_num]) == 0:
        with multiprocessing.Pool() as pool:
            for result in pool.imap_unordered(do_work, [(i, col_correct, col_xor_result) for i in range(256)]):
                r11_options[col_num] += result
        ic(len(r11_options[col_num]))

        with open('r11_options.txt', 'w') as fh:
            fh.write(str(r11_options))
        break            

    counter += 1

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
