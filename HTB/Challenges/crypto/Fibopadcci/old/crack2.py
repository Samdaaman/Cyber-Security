from icecream import ic
from pwn import *
from queue import Queue

a = b'HTB{th3_s3crt_A}' # My secret A! Only admins know it, and plus, other people won't be able to work out my key anyway!
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 121, 98, 219, 61]

# ps = [remote('127.0.0.1', 1337) for _ in range(8)]
ps = [remote('206.189.17.217', 31864) for _ in range(8)]

# find padding start
ps[0].recvuntil(b'Your option: ')
ps[0].sendline(b'0')
ps[0].recvuntil(b': ')
flag_enc = [c for c in bytes.fromhex(ps[0].recvuntil(b'\n').decode())]
ps[0].recvuntil(b': ')
a_rnd = [c for c in bytes.fromhex(ps[0].recvuntil(b'\n').decode())]
ps[0].recvuntil(b': ')
b_rnd = [c for c in bytes.fromhex(ps[0].recvuntil(b'\n').decode())]

# a_additional = [a[i] ^ a_rnd[i] for i in range(len(a))]
# flag_additionally_xored = [flag_enc[i] ^ a_additional[i] for i in range(16)] + flag_enc[16:]

def check_padding(ct, b, p):
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


def decrypt_block(c_i_dash, b_rnd_or_c_dash_before):
    m_i_test = [None] * 16
    print('------------')
    for i in range(16):
        print(f'{i} ', end='')
        b_rnd_test = b_rnd_or_c_dash_before.copy()
        k = 0
        for j in range(16):
            if m_i_test[j] is not None:
                b_rnd_test[j] = m_i_test[j] ^ fib[k+1]
                k += 1
            
        worker_results = Queue()
        for j in range(2):
            def do_work():
                results = []
                b_rnd_test_local = b_rnd_test.copy()
                for k in range(32):
                    guess = j*32 + k
                    b_rnd_test_local[-i-1] = j
                    if b_rnd_or_c_dash_before[-i-1] == guess:
                        results.append((guess, False))
                    elif check_padding(c_i_dash, b_rnd_test_local, ps[j]):
                        results.append((guess, True))
                    else:
                        results.append((guess, False))
                    print(f'{j}:{k}')
                worker_results.put(results)
            Thread(target=do_work, daemon=True).start()
            time.sleep(10)

        results = [None] * 256
        for j in range(8):
            print(f'worker done{j}')
            for index, value in worker_results.get():
                results[index] = value
            print(results)
        
        input()

        for j in range(256):
            if b_rnd_or_c_dash_before[-i-1] == j:
                continue
            b_rnd_test[-i-1] = j
            if check_padding(c_i_dash, b_rnd_test):
                m_i_test[-i-1] = j ^ fib[0]
                break
        else:
            m_i_test[-i-1] = b_rnd[-i-1] ^ fib[0]
    print()
    return m_i_test

c_0_dash = [flag_enc[i] ^ a[i] ^ a_rnd[i] for i in range(16)]
m_0_test = decrypt_block(c_0_dash, b_rnd)
m_0 = [m_0_test[i] ^ b_rnd[i] for i in range(16)]
print(bytes(m_0))

c_1_dash = [flag_enc[i] ^ a[i-16] ^ m_0[i-16] for i in range(16, 32)]
m_1_test = decrypt_block(c_1_dash, c_0_dash)
m_1 = [m_1_test[i] ^ flag_enc[i] for i in range(16)]
print(bytes(m_1))

c_2_dash = [flag_enc[i] ^ a[i-32] ^ m_1[i-32] for i in range(32, 48)]
m_2_test = decrypt_block(c_2_dash, c_1_dash)
m_2 = [m_2_test[i] ^ flag_enc[i+16] for i in range(16)]
print(bytes(m_2))

print(bytes(m_0 + m_1 + m_2))

ps[0].interactive()