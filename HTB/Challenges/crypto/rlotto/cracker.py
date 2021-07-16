from pwn import *
import time
import random

# p = remote('127.0.0.1', 1337)
p = remote('206.189.17.217', 30323)

start = int(time.time())

data = p.recvuntil('Guess')
p.recv()
data = data.decode().split('EXTRACTION: ')[-1].split(' \r')[0]
numbers = [int(c) for c in data.split(' ')]
print(f'Numbers are {numbers}')

times = [start]
for i in range(1, 10):
    times.append(start + i)
    times.append(start - i)

print(times)

for time_i in times:
    random.seed(time_i)
    extracted = []
    
    while len(extracted) < 10:
        r = random.randint(1, 90)
        if r not in extracted:
            if len(extracted) < 5 and numbers[len(extracted)] != r:
                break
            extracted.append(r)

    if len(extracted) == 10:
        print(f'Found {extracted}')
        p.send(' '.join([str(i) for i in extracted[5:]]))

p.interactive()
