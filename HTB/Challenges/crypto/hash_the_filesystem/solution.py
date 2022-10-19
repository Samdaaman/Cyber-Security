import json
from pwn import *
from icecream import ic
from solution_lib import inverse_hash

contents_set = set()

while True:
    # p = remote('localhost', 1337)
    p = remote('64.227.43.207', 31079)

    p.sendlineafter(b'Who are you:\n> ', b'admio')
    p.recvuntil(b'Your token is: ')
    token_hex = p.recvline(False).decode()
    token = bytes.fromhex(token_hex)
    forged_token = token
    forge_index = len('{"username": "admi')
    forged_token = token[:forge_index] + bytes([token[forge_index] ^ 1]) + token[forge_index+1:]

    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'Submit your token.\n',
        f'{{"token":"{forged_token.hex()}"}}'.encode())
    p.recvuntil(b'{"files": ')
    files_raw = p.recvuntil(b']')
    filenames = json.loads(files_raw.decode())  # type: list[str]

    for filename in filenames:
        if filename.startswith('ff'):
            target_hash = -int(filename[2:], 16)
        else:
            target_hash = int(filename, 16)

        x = inverse_hash(target_hash)
        test_hash = hex(hash(tuple([x]))).replace('0x', '').replace('-', 'ff')
        if test_hash != filename:
            continue # inverse_hash only seems to work for x <= signed max - just do a loop 

        p.sendlineafter(b'> ', b'3')
        p.sendlineafter(b'Submit your token and passphrase.\n',
            f'{{"token":"{forged_token.hex()}","passphrase":[{x}]}}'.encode())
        p.recvuntil(b'"content": "')
        contents = p.recvuntil(b'"', True).decode()
        contents_set.add(contents)
        ic(contents)
        ic(len(contents_set))

    p.close()

    if len(contents_set) == len(filenames):
        break
    
for contents in contents_set:
    print(bytes.fromhex(contents))