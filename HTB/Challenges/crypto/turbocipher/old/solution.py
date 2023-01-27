from pwn import *
from icecream import ic
import lib


proc = remote('142.93.37.215', 30169)

context.log_level = 'debug'

def recv_value(name: str) -> int:
    proc.recvuntil(f'{name} = '.encode())
    return int(proc.recvline(False).decode().split(' ')[0])

p = recv_value('p')
b = recv_value('b')
c = recv_value('c')
nonce = recv_value('nonce')

otp = lib.fast_turbonacci(nonce, p, b, c)
proc.sendline(str(otp).encode())

proc.interactive()
