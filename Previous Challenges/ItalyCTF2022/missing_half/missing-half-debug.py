#!/usr/bin/env python3

from typing import List
from Crypto.Util.number import *
import os
import random
from hashlib import md5
from icecream import ic
from progress.bar import Bar

FLAG = os.environ.get("FLAG", "flag{test}")


def a(x, y) -> int:
    return x ** y


def b(f: int, x: int) -> int:  # caller
    func = [random.seed, getPrime, isPrime, md5]
    if f == 3:
        return bytes_to_long(func[f](long_to_bytes(x)).digest())
    r = func[f](x)
    return int(r) if r else 0


def c(z: int, x: int, y: int) -> int:  # random
    if z:
        return random.randint(x ** 11, x ** 11 + y)
    x = long_to_bytes(x)
    y = long_to_bytes(y)
    while len(x) < len(y):
        x += x
    x = x[:len(y)]
    return bytes_to_long(xor(x, y))


def d(x: int) -> int:
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 24
    return (6 * d(x - 1) ** 2 * d(x - 3) - 8 * d(x - 1) * d(x - 2) ** 2) // (d(x - 2) * d(x - 3))


def fastd(n):
    n = n - 1
    temp = 1
    for i in range(1, n + 1):
        temp *= (2 ** i) - 1
    esp = 2 ** ((n ** 2 + n) // 2)
    return temp * esp


def e(msg: int) -> int:  # rsa
    n = 0x1702f4d2a98712defc05cb40b72a821479ccb9000a9bd698520082544b652bacfa721041f115da3a3cb8f4211a847706ae4dc9f048c7262a964e337bc47065de1059eccc87c19f662c21f9066805e5f75b3c62305395138d5eb71e9f9966297750ee17ccfcace1386abaf53434b264696744ae990bdebb17a4a56c4edc0cccfcf8da138fcf0c911f434d2d3e0b493b8fa9917f83f41273b4aaf7d631dabb66939f67fcb270e0a7156c7e66338027387e873c225991180fec96ea4fc0f9f88815010e5994d5f35ae21568d5641b00d44876762c392e9853045a5a92eb2354486f80946368f83469a7b37e621906f81f8005b126417fd716bcd79c84610dc093dd7575ebcf3af3d71a869830455d3ad6d68ad2254843320233e01f1cafdc73310f7ffb1deccb4df2fee6150a1a588867c5285c7049bf39e1a631badc81d61dda69e5d2e017235306ad46b0703e88a5c65807737a6a459231f5eb6bd6afd44fb46566c1
    e = 0x10001
    return pow(msg, e, n)


def xor(x, y):
    return bytes(a ^ b for a, b in zip(x, y))


def f(x: int, flag=FLAG.encode()) -> int:
    return bytes_to_long(xor(long_to_bytes(x), flag))


def Lukasiewicz_partial(password: str, stack: List[int]) -> int:
    func = {
        'a': (a, 2),
        'b': (b, 2),
        'c': (c, 3),
        'd': (fastd, 1),
        'e': (e, 1),
        'f': (f, 1)
    }

    bar = Bar('Progress', max=len(password))
    for t in password:
        if t.isdigit():
            stack.append(int(t))
        else:
            args = []
            for _ in range(func[t][1]):
                args.append(stack.pop())
            args.reverse()
            tmp = func[t][0](*args)
            stack.append(tmp)
        bar.next()
    bar.finish()
    return stack


# with open('missing-half-debug.py.out', 'w') as file:
# file.write('out:' + hex(Lukasiewicz(password)))
password = '08ae7eb31227acdb553aafec'

f_idx = password.index('f')
ic(len(password))
ic(f_idx)

# Up to the first "f" the stack is deterministic (independent of FLAG)
# deterministic_stack = Lukasiewicz_partial(password[:f_idx], [])
deterministic_stack = [
        0,
        160041365501716368448053427917678638214,
        2350988701644575015937473074444491355637331113544175043017503412556834518909454345703125
    ]


# ==============================================
# Overview of remaining steps
# ==============================================
# "f" step:
#   arg1: deterministic_stack[2] = 2350....125
#   return FLAG XOR'd with arg1


# "e" step:
#   arg1: output of above step
#   returns: arg1 encrypted with RSA


# "c" step:
#   arg1: deterministic_stack[0] = 0
#   arg2: deterministic_stack[1] = 160041365501716368448053427917678638214
#   arg3: output of previous step
#   returns: since arg1=0, it returns arg2 "sort-of" XOR'd with arg3 in a scuffed way that is reversible


# ==============================================
# Reverse order for cracking
# ==============================================
output4 = 0x69699507fd48efde364bab82106f89d23d22e463631a77941cfe29863229a40be8ba9ea548323b183bc37e4d7b151e8b60fac7d657185dfd1b75eebc2701c21bd3901f800145e76b1d48789428c7c3e8f7bc0aa11232ee076262d4f3c9b84b2a43e3da768e2f7622d645fa3bb94e65e64744b977f260ba1fd0956330c3cfc2fbddf350db366c2da5d72f91eb23905bc1b714b66460d726af257ff37d60897b33778d74c9a1e5dbf8c15390a5d65114c738f6812b39ec42afc00a873d866166411f2d4c9a69fce5aca631af87f4a6449282664e2a8ab79f5376486cf0f9fcb226e76b735dda222a024fda883352b8e24fee309f2057c7472a58a8aac886b9a1889e9b1f8d2306b493c4e16f3401a01263828a08e2070b4cdc6dd398bcac17d707847325064d4bf6dcfa9e683cee3c126eb4ad753997ae66792b71f83f835524ad6da5e25b3dabc21e541cd049bc038b7ced304c1012fe67919619c28f593940c5cb9c

# "c" step:
output3 = c(0, deterministic_stack[1], output4) # note this is actually c() inverse
# check it's right
output4_test = c(deterministic_stack[0], deterministic_stack[1], output3)
assert output4 == output4_test

# "e" step:
p = 101508832785985955552565353122121737721993273502298175210435222266367833577715998022894656354382850171462759222346590459054225243603686267128759721843436874152669720089862957418766772057931420195879446159380143921796986554177104777649965254024676644960176804859103133813804766266693420172934551827315872977254078260338793328596476945722634410151137268041424281547851223367780543620548301885832625481626226084395787868180619557254585495303587141192195620597534126355662587790632679436747378965477492157052992900323689771455598584904305855173463763288399527877718916799
q = 2911721007088133262675953106197241703556747554305425259320716892314498939605330257723180761563459946872506915178651543859508747846871417959638013334210124890497567604326390324762618539999256667220682352421111253679877478493941553844107359114872928940037671284003186268154810467080223359
n = 0x1702f4d2a98712defc05cb40b72a821479ccb9000a9bd698520082544b652bacfa721041f115da3a3cb8f4211a847706ae4dc9f048c7262a964e337bc47065de1059eccc87c19f662c21f9066805e5f75b3c62305395138d5eb71e9f9966297750ee17ccfcace1386abaf53434b264696744ae990bdebb17a4a56c4edc0cccfcf8da138fcf0c911f434d2d3e0b493b8fa9917f83f41273b4aaf7d631dabb66939f67fcb270e0a7156c7e66338027387e873c225991180fec96ea4fc0f9f88815010e5994d5f35ae21568d5641b00d44876762c392e9853045a5a92eb2354486f80946368f83469a7b37e621906f81f8005b126417fd716bcd79c84610dc093dd7575ebcf3af3d71a869830455d3ad6d68ad2254843320233e01f1cafdc73310f7ffb1deccb4df2fee6150a1a588867c5285c7049bf39e1a631badc81d61dda69e5d2e017235306ad46b0703e88a5c65807737a6a459231f5eb6bd6afd44fb46566c1
assert n == p*q
lam = (p-1)*(q-1)
d_priv = pow(0x10001, -1, lam)
output2 = pow(output3, d_priv, n)
# check its right
output3_test = e(output2)
assert output3 == output3_test

# "f" step:
output1 = bytes_to_long(xor(long_to_bytes(deterministic_stack[2]), long_to_bytes(output2)))
# check it's right
output2_test = f(deterministic_stack[2], long_to_bytes(output1))
assert output2 == output2_test

# Yay
print(long_to_bytes(output1))
