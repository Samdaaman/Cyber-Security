from sage.all import *
from icecream import ic
import time
from typing import Callable
from pwn import *
from Crypto.Util.number import long_to_bytes

def turbonacci(n: int, p: int, b: int, c: int) -> int:
    if n < 2:
        return n

    return (b * turbonacci(n - 1, p, b, c) +
            c * turbonacci(n - 2, p, b, c)) % p


def fast_turbonacci(n: int, p: int, b: int, c: int) -> int:
    if n == 0:
        return 0

    F = GF(p)
    A = Matrix(F, [[0, 1], [c, b]])
    x = vector(F, [0, 1])
    y = (A ^ (n - 1)) * x
    ic(y)
    return y[1]


def fast_turbocrypt(pt: int, k: int, f: Callable[[int], int]) -> int:
    return f(pt) - f(k)


def test():
    for i in range(32):
        b, c, p = random_prime(512), random_prime(512), random_prime(512)

        now = time.perf_counter_ns()
        res1 = turbonacci(i, p, b, c)
        t1 = time.perf_counter_ns() - now
        now = time.perf_counter_ns()
        res2 = fast_turbonacci(i, p, b, c)
        t2 = time.perf_counter_ns() - now
        ic(t1)
        ic(t2)
        ic(i, res1, res2)
        assert res1 == res2


def main():
    context.terminal = 'xterm-256color'
    context.log_level = 'debug'
    proc = remote('209.97.133.57', int(31010))

    def recv_value(name: str) -> int:
        proc.recvuntil(f'{name} = '.encode())
        return int(proc.recvline(False).decode().split(' ')[0])

    p = recv_value('p')
    b = recv_value('b')
    c = recv_value('c')
    nonce = recv_value('nonce')

    ic(p, b, c, nonce)
    otp = fast_turbonacci(nonce, p, b, c)
    proc.sendline(f'{otp}'.encode())

    def option2(x: int):
        proc.sendlineafter(b'> ', b'2')
        proc.sendlineafter(b'pt = ', f'{x}'.encode())
        return recv_value('ct')

    F = GF(p)
    f_0 = F(option2(0))
    f_1 = F(option2(1))
    m = f_1 - f_0
    m_inv = m ^ -1
    k = - f_0 * m_inv

    proc.sendlineafter(b'> ', b'1')
    flag_enc = recv_value('ct')

    flag_int = (flag_enc + m*k) * m_inv
    print(long_to_bytes(flag_int))


if __name__ == '__main__':
   main()
