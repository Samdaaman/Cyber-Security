from pwn import *
from icecream import ic
from Crypto.Util.strxor import strxor
import sys

# p = process(['python3', 'debug2.py'], stderr=sys.stdout)
p = remote('cleithrophobia.chal.idek.team', 1337)

p.recvuntil(b'flag = ')
flag_hex = p.recvline(keepends=False).decode()
flag = bytes.fromhex(flag_hex)

ic(flag_hex)

def encrypt(to_enc: bytes):
    p.sendlineafter(b'> (hex) ', to_enc.hex().encode())
    p.recvline()
    p.recvuntil(b'|   ')
    return bytes.fromhex(p.recvline(keepends=False).decode())


result1 = encrypt(b'\x10'*16*2)  # padding=b'\x10'*16
result1_iv = result1[-16:]
result1_c1 = result1[16:16*2]
result1_c2 = result1[16*2:16*3]
result1_c2_d = strxor(result1_iv, result1_c2)
result1_m2 = strxor(result1_c1, result1_c2_d) # encrypting all 0x10 bytes (same as padding byte)
enc_0x10 = strxor(result1_m2, b'\x10'*16)

ic(enc_0x10)

def decrypt_block(block: bytes):
    assert len(block) == 16
    to_enc = strxor(block, enc_0x10) # padding=b'\x10'*16
    result2 = encrypt(to_enc)
    result2_iv = result2[-16:]
    result2_c1 = result2[16:16*2]
    return strxor(result2_iv, result2_c1)

def encrypt_block(block: bytes):
    assert len(block) == 16
    to_enc = b'\x10'*16 + block
    result3 = encrypt(to_enc)
    result3_iv = result3[-16:]
    result3_c0_d = decrypt_block(strxor(result3_iv, enc_0x10))
    result3_c0 = result3[:16]
    result3_m1 = strxor(result3_c0, result3_c0_d)
    return strxor(result3_m1, b'\x10'*16)

ic(encrypt_block(b'\x69'*16))
ic(decrypt_block(b'\x69'*16))

ic(len(flag))
flag_iv = flag[-16:]
flag_blocks = [flag[i:i+16] for i in range(0, len(flag)-16, 16)]
ic(flag_iv)
ic(flag_blocks)
m_blocks = []
for i, block in enumerate(flag_blocks[::-1]):
    if i == 0:
        xor_arg = flag_iv
    else:
        xor_arg = m_blocks[i-1]
    block = strxor(block, xor_arg)
    m_blocks.append(encrypt_block(block))
m_blocks = m_blocks[::-1]

pt_blocks = []
for i, block in enumerate(m_blocks):
    if i == 0:
        xor_arg = flag_iv
    else:
        xor_arg = pt_blocks[i-1]
    block = strxor(block, xor_arg)
    pt_blocks.append(decrypt_block(block))

print(pt_blocks)
pt = b"".join(pt_blocks)

print(pt)
p.close()