from math import ceil
from MTRecover import MT19937Recover
import random
from typing import List


# https://github.com/eboda/mersenne-twister-recover
NUM_INPUTS = 625 # number needed to crack "Given at least 624 outputs of a Mersenne Twister we can restore its internal state"


def test1():
    r1 = random.Random(31337)
    outputs = [r1.getrandbits(32) for _ in range(625)]
    
    mtr = MT19937Recover()
    r2 = mtr.go(outputs)
    
    assert r1.getrandbits(32) == r2.getrandbits(32)


def getrandbytes(n: int, r: random.Random = random) -> bytes:
    return r.getrandbits(n * 8).to_bytes(n, "little")


def rand_bytes_to_ints(rand_bytes: bytes) -> List[int]:
    num_ints = len(rand_bytes) // 4
    ints = []
    for i in range(num_ints):
        int_bytes = rand_bytes[i*4: i*4+4]
        ints.append(int.from_bytes(int_bytes, 'little'))
    return ints


def test2():
    seed = 12345
    length = 48 # must be divisible by 4
    r1 = random.Random(seed)
    a1 = r1.getrandbits(length * 8).to_bytes(length, 'little')

    r2 = random.Random(seed)
    a2_array = [r2.getrandbits(32) for _ in range(length // 4)]

    a1_test = rand_bytes_to_ints(a1)
    assert len(a1_test) == len(a2_array)
    assert all([i == j for i, j in zip(a1_test, a2_array)])

 
def test3():
    iterations = ceil(625 / 12) # 12 because 32+16 is 48 bytes or 12 4-byte ints
    outputs = []
    for _ in range(iterations):
        # known
        key = getrandbytes(32)
        iv = getrandbytes(16)

        # calculated
        rand_bytes = key + iv
        ints = rand_bytes_to_ints(rand_bytes)
        outputs += ints

    # Crack
    mtr = MT19937Recover()
    r = mtr.go(outputs)
    
    # Prediction time
    key = getrandbytes(32)
    iv = getrandbytes(16)
    key_test = getrandbytes(32, r)
    iv_test = getrandbytes(16, r)

    print(key)
    print(key_test)
    print(iv)
    print(iv_test)


def main():
    test3()


if __name__ == '__main__':
    main()