import json
from sage.all import *
import gmpy2
from Crypto.Util.number import bytes_to_long, long_to_bytes
from server import TimeCapsule
from icecream import ic
from pwn import *


def crack(capsules):
    assert len(capsules) == 5
    # {"time_capsule": f"{m:X}", "pubkey": [f"{n:X}", f"{e:X}"]}
    pairs = [(
            bytes_to_long(bytes.fromhex(capsule['time_capsule'])),
            bytes_to_long(bytes.fromhex(capsule['pubkey'][0]))
        ) for capsule in capsules]

    m_pow5 = crt([p[0] for p in pairs], [p[1] for p in pairs])
    m = int(gmpy2.iroot(m_pow5, int(5))[0])
    return long_to_bytes(m)


def test():
    capsule = TimeCapsule(b'HTB{FAKE_FLAG}')
    capsules = [capsule.get_new_time_capsule() for _ in range(5)]
    m = crack(capsules)
    ic(m)


def main():
    # p = remote('localhost', 1337)
    p = remote('167.99.202.193', 32452)
    def get_new_time_capsule():
        p.sendlineafter(b'(Y/n) ', b'y')
        capsule_raw = p.recvline().decode().strip()
        return json.loads(capsule_raw)
    capsules = [get_new_time_capsule() for _ in range(5)]
    m = crack(capsules)
    ic(m)


if __name__ == '__main__':
    # test()
    main()
