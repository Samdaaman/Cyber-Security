from hashlib import sha256
from pwn import *
from icecream import ic


# io = process('python3 debug.py', shell=True)
io = remote('138.68.148.72', 32159)

def verify(message: bytes, hash: bytes):
    io.sendlineafter(b'> ', b'2')
    io.sendlineafter(b': ', message)
    io.sendlineafter(b': ', hash.hex().encode())
    line = io.recvline()
    return b'Validated!' in line


def do_hash(message: bytes):
    io.sendlineafter(b'> ', b'1')
    io.sendlineafter(b': ', message)
    hash = bytes.fromhex(io.recvline(False).split(b'Hash: ')[1].decode())
    return hash


def step(prefix: bytes):
    hashes = [sha256(prefix + bytes([c])).digest() for c in range(256)]
    message = b'\0' * (len(prefix) + 1)
    # for i, hash in enumerate(hashes):
    #     if verify(message, hash):
    #         return prefix + bytes([i])
    hash = do_hash(message)
    try:
        i = hashes.index(hash)
    except ValueError:
        return None
    return prefix + bytes([i])
    

pt = b''
while True:
    test = step(pt)
    if test is None:
        break
    pt = test
    ic(pt)