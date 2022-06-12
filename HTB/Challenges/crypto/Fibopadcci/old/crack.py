from icecream import ic
from pwn import *

a = b'HTB{th3_s3crt_A}' # My secret A! Only admins know it, and plus, other people won't be able to work out my key anyway!
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 121, 98, 219, 61]

# p = remote('127.0.0.1', 1337)
p = remote('206.189.17.217', 30183)

# find padding start
p.recvuntil(b'Your option: ')
p.sendline(b'0')
p.recvuntil(b': ')
flag_enc = [c for c in bytes.fromhex(p.recvuntil(b'\n').decode())]
p.recvuntil(b': ')
a_rnd = [c for c in bytes.fromhex(p.recvuntil(b'\n').decode())]
p.recvuntil(b': ')
b_rnd = [c for c in bytes.fromhex(p.recvuntil(b'\n').decode())]

# a_additional = [a[i] ^ a_rnd[i] for i in range(len(a))]
# flag_additionally_xored = [flag_enc[i] ^ a_additional[i] for i in range(16)] + flag_enc[16:]

def check_padding(ct, b):
    p.recvuntil(b'Your option: ')
    p.sendline(b'1')
    p.recvuntil(b': ')
    p.sendline(bytes(ct).hex().encode())
    p.recvuntil(b': ')
    p.sendline(bytes(b).hex().encode())
    test = p.recvuntil(b'sent')
    if b'success' in test:
        return True
    else:
        return False

c_0_dash = [flag_enc[i] ^ a[i] ^ a_rnd[i] for i in range(16)]
# m_0_test = [None]*16
# for i in range(16):
#     print(f'1.{i}')
#     b_rnd_test = b_rnd.copy()
#     k = 0
#     for j in range(16):
#         if m_0_test[j] is not None:
#             b_rnd_test[j] = m_0_test[j] ^ fib[k+1]
#             k += 1
        
#     for j in range(256):
#         if b_rnd[-i-1] == j:
#             continue
#         b_rnd_test[-i-1] = j
#         if check_padding(c_0_dash, b_rnd_test):
#             m_0_test[-i-1] = j ^ fib[0]
#             break
#     else:
#         m_0_test[-i-1] = b_rnd[-i-1] ^ fib[0]

# m_0 = [m_0_test[i] ^ b_rnd[i] for i in range(len(m_0_test))]
m_0 = b'HTB{cU5t0m_p4dd1'
print(bytes(m_0))

c_1_dash = [flag_enc[i] ^ a[i-16] ^ m_0[i-16] for i in range(16, 32)]
# m_1_test = [None]*16
# for i in range(16):
#     print(f'2.{i}')
#     b_rnd_test = c_0_dash.copy()
#     k = 0
#     for j in range(16):
#         if m_1_test[j] is not None:
#             b_rnd_test[j] = m_1_test[j] ^ fib[k+1]
#             k += 1
        
#     for j in range(256):
#         if c_0_dash[-i-1] == j:
#             continue
#         b_rnd_test[-i-1] = j
#         if check_padding(c_1_dash, b_rnd_test):
#             m_1_test[-i-1] = j ^ fib[0]
#             break
#     else:
#         m_1_test[-i-1] = c_0_dash[-i-1] ^ fib[0]

# m_1 = [m_1_test[i] ^ flag_enc[i] for i in range(len(m_1_test))]
m_1 = b'Ng_w0nT_s4v3_y0u'
print(bytes(m_1))

c_2_dash = [flag_enc[i] ^ a[i-32] ^ m_1[i-32] for i in range(32, 48)]
m_2_test = [None]*16
for i in range(16):
    print(f'3.{i}')
    b_rnd_test = c_1_dash.copy()
    k = 0
    for j in range(16):
        if m_2_test[j] is not None:
            b_rnd_test[j] = m_2_test[j] ^ fib[k+1]
            k += 1
        
    for j in range(256):
        if c_1_dash[-i-1] == j:
            continue
        b_rnd_test[-i-1] = j
        if check_padding(c_2_dash, b_rnd_test):
            m_2_test[-i-1] = j ^ fib[0]
            break
    else:
        m_2_test[-i-1] = c_1_dash[-i-1] ^ fib[0]

m_2 = [m_2_test[i] ^ flag_enc[i+16] for i in range(len(m_2_test))]
print(bytes(m_2))


print(bytes(m_0 + m_1 + m_2))

# ct_ext = b_rnd + flag_additionally_xored
# i = 1
# while True:
#     ct_ext_test = ct_ext.copy()
#     ct_ext_test[-i-16] = ct_ext_test[-i-16] + 1

#     if check_padding(ct_ext_test[16:], ct_ext_test[:16]):
#         break

#     i += 1

# print(f'number of padded bytes is {i}')


p.interactive()