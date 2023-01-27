import os
import random
import sys
import time

if False:
    # for testing
    SECRET_OFFSET = 0
    start = round((time.time() + SECRET_OFFSET) * 1000)
else:
    # for real
    SECRET_OFFSET = -67198624
    # start = 1673647500 # 11:05am January 14th (NZ time)
    start = 1673651100 # 11:05am January 14th (NZ time)
    start += SECRET_OFFSET
    start *= 1000

# notes
# random.seed(round((time.time() + SECRET_OFFSET) * 1000))
# os.environ["SECRET_KEY"] = "".join([hex(random.randint(0, 15)) for x in range(32)]).replace("0x", "")



j = 0
BLOCK_SIZE = 10000
while True:
    for i in range(BLOCK_SIZE):
        seed = start - i - (j*BLOCK_SIZE)
        random.seed(seed)
        # print(f'{seed} : ', end='') # for testing
        print("".join([hex(random.randint(0, 15)) for x in range(32)]).replace("0x", ""))
    j += 1
    print(f'Generated {j*BLOCK_SIZE} keys ({j * BLOCK_SIZE / (1000 * 60)} min worth)', file=sys.stderr)