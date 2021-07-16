from pwn import *

# p = remote('127.0.0.1', 1337)
p = remote('206.189.17.217', 30651)

def get_flag() -> bytes:
    p.recvuntil(b': ')
    p.sendline(b'1')
    return bytes(bytearray.fromhex(p.recvuntil(b'\n', True).decode()))

flag_len = len(get_flag())
options = [list(range(256)) for _ in range(flag_len)]

while True:
    flag = get_flag()
    assert len(flag) == flag_len
    options_remaining = 0
    
    for i in range(flag_len):
        options_remaining += len(options[i])
        if flag[i] in options[i]:
            options[i].remove(flag[i])

    print(f'options: {options_remaining}/{flag_len}')
    
    if options_remaining == flag_len:
        break

encrypted_halfway = bytes(map(lambda x: x[0], options))

def get_xor_stream() -> bytes:
    p.recvuntil(b': ')
    p.sendline(b'2')
    p.recvuntil(': ')
    p.sendline(b'0' * flag_len * 2)
    return bytes(bytearray.fromhex(p.recvuntil('\n', True).decode()))

options = [list(range(256)) for _ in range(flag_len)]

while True:
    xor_stream = get_xor_stream()
    assert len(xor_stream) == flag_len
    options_remaining = 0
    
    for i in range(flag_len):
        options_remaining += len(options[i])
        if xor_stream[i] in options[i]:
            options[i].remove(xor_stream[i])

    print(f'options: {options_remaining}/{flag_len}')
    
    if options_remaining == flag_len:
        break

xor_stream_decrypted = bytes(map(lambda x: x[0], options))

print(f'Halfway encrypted is {encrypted_halfway}')
print(encrypted_halfway.hex())

print(f'xor_stream_decrypted is {xor_stream_decrypted}')
print(xor_stream_decrypted.hex())

pt = b''
for i in range(flag_len):
    pt += bytes([encrypted_halfway[i] ^ xor_stream_decrypted[i]])

print(f'Decrypted pt is {pt}')

p.interactive()

p.shutdown()
