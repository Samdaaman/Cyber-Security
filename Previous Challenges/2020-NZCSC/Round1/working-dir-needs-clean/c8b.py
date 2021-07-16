from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import requests
import binascii


def get_hex(h):
    return binascii.hexlify(h)


key = bytearray.fromhex('7f7f7f7fba275e49c535a86bfaebe9b5')


def get_data(plain: bytes):
    nouce = bytearray.fromhex('00000000000000000000000000000000')
    aesgcm = AESGCM(key)
    ct = aesgcm.encrypt(nouce, plain, None)
    return nouce + ct


def send(d: bytearray):
    headers = {'User-Agent': 'flog:GreenHerring'}
    r = requests.post('http://sushi.nzcsc.org.nz/c2', data=d, headers=headers, stream=True)
    # print(f'{r.status_code} - {len(r.content)} - {get_hex(r.content)} {r.text}')
    print(f'{r.status_code} - {len(r.content)}')
    return r.content


def rec(res: bytes):
    nouce = res[0:16]
    ct = res[16:]
    aesgcm = AESGCM(key)
    plain = aesgcm.decrypt(nouce, ct, None)
    print(get_hex(plain))
    return plain


def main():
    plain = bytes.fromhex('00000000')
    data = get_data(plain)
    print(get_hex(data))
    res = send(data)
    print(get_hex(res))
    pl = rec(res)
    print(pl)
    # rec(bytes.fromhex('b41f7cfa4106b508eebf762a3ae744bba1572b566e0446e8f581802245d04f91b5e322f2'))
    t = bytes(a ^ b for a, b in zip(res, pl*9))
    print(t)


if __name__ == '__main__':
    main()
