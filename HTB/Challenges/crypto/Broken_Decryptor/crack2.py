from pwn import *
from queue import Queue

NUM_THREADS = 70
# IP = '127.0.0.1'; PORT = 1337
IP = '206.189.17.217'; PORT = 30651

p_global = remote(IP, PORT)

def get_flag(p) -> bytes:
    p.recvuntil(b': ')
    p.sendline(b'1')
    return bytes(bytearray.fromhex(p.recvuntil(b'\n', True).decode()))

flag_len = len(get_flag(p_global))
options = [list(range(256)) for _ in range(flag_len)]

getting_flags = True
def get_flags():
    p = remote(IP, PORT)
    while getting_flags:
        flag_queue.put(get_flag(p))

flag_queue = Queue()
for _ in range(NUM_THREADS):
    Thread(target=get_flags, daemon=True).start() 

while True:
    flag = flag_queue.get()
    assert len(flag) == flag_len
    options_remaining = 0
    
    for i in range(flag_len):
        options_remaining += len(options[i])
        if flag[i] in options[i]:
            options[i].remove(flag[i])

    print(f'options: {options_remaining}/{flag_len}')
    
    if options_remaining == flag_len:
        break

getting_flags = False
encrypted_halfway = bytes(map(lambda x: x[0], options))

def get_xor_stream(p) -> bytes:
    p.recvuntil(b': ')
    p.sendline(b'2')
    p.recvuntil(b': ')
    p.sendline(b'0' * flag_len * 2)
    return bytes(bytearray.fromhex(p.recvuntil('\n', True).decode()))

options = [list(range(256)) for _ in range(flag_len)]

xor_stream_queue = Queue()
getting_xor_streams = True
def get_xor_streams():
    p = remote(IP, PORT)
    while getting_xor_streams:
        xor_stream_queue.put(get_xor_stream(p))

for _ in range(NUM_THREADS):
    Thread(target=get_xor_streams, daemon=True).start() 

while True:
    xor_stream = xor_stream_queue.get()
    assert len(xor_stream) == flag_len
    options_remaining = 0
    
    for i in range(flag_len):
        options_remaining += len(options[i])
        if xor_stream[i] in options[i]:
            options[i].remove(xor_stream[i])

    print(f'options: {options_remaining}/{flag_len}')
    
    if options_remaining == flag_len:
        break

getting_xor_streams = False
xor_stream_decrypted = bytes(map(lambda x: x[0], options))

print(f'Halfway encrypted is {encrypted_halfway}')
print(encrypted_halfway.hex())

print(f'xor_stream_decrypted is {xor_stream_decrypted}')
print(xor_stream_decrypted.hex())

pt = b''
for i in range(flag_len):
    pt += bytes([encrypted_halfway[i] ^ xor_stream_decrypted[i]])

print(f'Decrypted pt is {pt}')