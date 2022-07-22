from base64 import b64decode
import challenge
from icecream import ic
from Crypto.Cipher import AES


def call(msg: str) -> bytes:
    pt = challenge.flag + str.encode(msg)
    ct_b64 = challenge.enc(pt)
    return b64decode(ct_b64.encode())


def test_lengths():
    print('calculating initial pt length')
    control_len = len(call(''))
    ic(control_len)
    i = 0
    while len(call(' ' * i)) == control_len:
        i += 1
    pt_len = control_len - i + 1
    ic(pt_len)

    test = call('0' * 48)
    for i in range(0, len(test), 16):
        ic(test[i: i+16])


def main():
    key = ''
    for i in range(16):
        target_block_enc = call((i+1)*'0')[-16:]

        for j in range(256):
            test_block = (chr(j) + key).ljust(16, '0')
            test_block_enc = call(test_block)[32: 48]
            if target_block_enc == test_block_enc:
                key = chr(j) + key
                break

        else:
            raise Exception('dang')
    
        ic(key)

    cipher = AES.new(key.encode(), AES.MODE_ECB)
    flag = cipher.decrypt(call(''))
    ic(flag)


if __name__ == '__main__':
    test_lengths()
    main()
