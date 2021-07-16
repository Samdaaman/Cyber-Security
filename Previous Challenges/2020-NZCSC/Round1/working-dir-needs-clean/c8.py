import requests
import binascii

def get_hex(h):
    return binascii.hexlify(h)


def send(dh):
    data = bytearray.fromhex(dh)
    headers = {'User-Agent' : 'flog:GreenHerring'}
    r = requests.post('http://sushi.nzcsc.org.nz/c2', data=data, headers=headers, stream=True)
    print(f'{r.status_code} - {len(r.content)} - {get_hex(r.content)} {r.text}')


def main():
    send('b41f7cfa4106b508eebf762a3ae744bba1572b566e0446e8f581802245d04f91b5e322f2')
    send('6b65bc0f9817f7772f372ea772729d61f4b720b1acd2dc4f5f9bcd80f2a2ada0348d9ce2')
    send('6938a9d0ae7379610eff42d55849ebdd5a44f082f6f5869c39fafaff22ca64b5970df41b')
    # send('b41f7cfa4106b508eebf762a3ae744bba1572b566e0446e8f581802245d04f91b5e322f2')


if __name__ == '__main__':
    main()
