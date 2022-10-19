from pwn import *
from icecream import ic
from Crypto.Util.strxor import strxor

# context.log_level = 'debug'
pt = b''

p = process('python3 server.py', shell=True)
p.recvline()
flag_enc = bytes.fromhex(p.recvline().decode().split(': ')[1])
p.sendline()
p.recvline()
p.sendline(flag_enc[:16].hex())
first_block = bytes.fromhex(p.recvline().decode().split(': ')[1])
pt += first_block
p.wait()

def get_block():
    global pt
    i = len(pt) // 16
    p = process('python3 server.py', shell=True)
    p.recvline()
    flag_ct = bytes.fromhex(p.recvline().decode().split(': ')[1])
    p.sendline((b'\x10'*16).hex())
    enc = bytes.fromhex(p.recvline().decode().split(': ')[1])
    iv = enc[16:]
    c_i = flag_ct[i*16:(i+1)*16]
    b_i = strxor(c_i, iv)
    prev_c_i = flag_ct[(i-1)*16:i*16]
    prev_b_i = strxor(prev_c_i, iv)
    a_i = strxor(b_i, prev_b_i)
    to_dec = strxor(a_i, iv)
    p.sendline(to_dec.hex())
    pt += bytes.fromhex(p.recvline().decode().split(': ')[1])
    p.wait()
    ic(pt)

get_block()
get_block()
get_block()
get_block()
get_block()