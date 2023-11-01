from itertools import product
import math
from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from icecream import ic
import lib

def h(x):
    return [hex(c)[2:].rjust(2, '0') for c in x]


# context.log_level = 'debug'
# io = process('./enc_fault2', stderr=None) # type: ignore
io = remote('209.97.140.29', 30260)

r11_options: list[list[list[int]]] = [list() for _ in range(4)]

while any(len(x) == 0 for x in r11_options) or math.prod(len(x) for x in r11_options) > 1:
    io.sendlineafter(b': ', b'y')
    correct = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    faulted = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
    if correct == faulted:
        continue

    correctT = lib.transpose4x4(correct)
    faultedT = lib.transpose4x4(faulted)

    xor_result = strxor(correct, faulted)
    xor_resultT = lib.transpose4x4(xor_result)

    col_num = 0
    for col_num in range(4):
        if xor_resultT[col_num] != 0:
            break
    
    col_correct = [correctT[i*4 + (col_num-i)%4] for i in range(4)]
    col_fault = [faultedT[i*4 + (col_num-i)%4] for i in range(4)]
    col_xor_result = [xor_resultT[i*4 + (col_num-i)%4] for i in range(4)]

    # for buf in [correctT, faultedT, xor_resultT]:
    #     for i in range(4):
    #         print(h(buf[i*4:(i+1)*4]))
    #     print()

    if len(r11_options[col_num]) == 0:
        for fault_val in range(256):
            for i in range(4):
                fault_arr = [0,0,0,0]
                fault_arr[i] = fault_val
                lib.mix_single_column(fault_arr)
                c_vals: list[list[int]] = [[] for _ in range(4)]
                for j in range(4):
                    for k in range(256):
                        if k ^ lib.inv_sbox[lib.sbox[k] ^ col_xor_result[j]] == fault_arr[j]:
                            c_vals[j].append(k)
                
                for c_val in product(*c_vals):
                    r11_option = [col_correct[i] ^ lib.sbox[c_val[i]] for i in range(4)]
                    r11_options[col_num].append(r11_option)

    else:
        for r11 in r11_options[col_num].copy():
            post_sr = [i^j for i,j in zip(col_correct, r11)]
            x_vect = [lib.inv_sbox[post_sr[i]] for i in range(4)]

            fault_vect = [x_vect[i] ^ lib.inv_sbox[lib.sbox[x_vect[i]] ^ col_xor_result[i]] for i in range(4)]
            lib.inv_single_column(fault_vect)
            if fault_vect.count(0) != 3:
                r11_options[col_num].remove(r11)

        assert len(r11_options[col_num]) > 0, 'dang!'
    
    ic(col_num, len(r11_options[col_num]))    

for r11_option in r11_options:
    ic(h(r11_option[0]))

r11: list[int] = []
for i in range(4):
    for j in range(4):
        r11.append(r11_options[(i+j)%4][0][j])

ic(h(r11))
aes_key = lib.get_key_from_last_rk(r11)

io.sendlineafter(b': ', b'n')
flag_enc = bytes.fromhex(io.recvline_contains(b': ').decode().split(':')[1])
aes = AES.new(aes_key, mode=AES.MODE_ECB)
pt = aes.decrypt(flag_enc)
if pt.startswith(b'HTB{'):
    print(pt.decode())
