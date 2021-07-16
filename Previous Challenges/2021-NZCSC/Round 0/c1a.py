from Crypto.Cipher import DES
from hashlib import md5
from base64 import b64decode

def des_encrypt(key, plain_text):
    # encrypt using DES
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plain_text)


def des_decrypt(key, cipher_text):
    # decrypt using DES
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(cipher_text)


def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)

def nth_key(index):
    # Code from https://github.com/thomwiggers
    """Gets the nth key with respect to parity bits"""
    keystring = []

    for i in range(8):
        key_byte = index & 127  # 127 == int('1111111', 2)
        hamming_weight = bin(key_byte).count('1')
        if hamming_weight % 2 == 0:
            keystring.append(((key_byte << 1) + 1))
        else:
            keystring.append((key_byte << 1))

        index >>= 7

    return bytes(keystring[::-1])  # reverse order

def main():
    # with open('c1_enc.bin', 'rb') as fh:
    #     cipher = fh.read()

    data = b64decode('V+QQEMfkRgUXVy8d8aI93UfMI9auuIGkco2Zm7Gs2bc+pFS1hgR7+ppKqHgyn3XeLGpUggbuAMU=')
    key = data[-8:]
    cipher = data[:-8]

    # plain = b'YEEEET'
    # for i in range(2**56):
    #     key = nth_key(i)
    #     plain = des_decrypt(key, cipher)
    #     if b'flag' in plain:
    #         print(plain)
    #         print(i)
    #         exit(0)

    plain = des_decrypt(key, cipher)
    print(plain)
    print(len(plain))


main()

# from Crypto.Cipher import DES
# from binascii import unhexlify, hexlify
# from random import randint




# def mtm_attack(plain_text, cipher_text, numbits):

#     # status
#     print("There are {} keys and MTM texts to generate".format(2 ** numbits))

#     # key generation
#     keys_list = []
#     for i in range(2 ** numbits):
#         key = nth_key(i)
#         # print(hexlify(key).decode("utf-8"))
#         keys_list.append(key)
#     print("Generated {} keys".format(len(keys_list)))

#     # mtm texts (single DES cipher text) generation
#     mtm_texts = []
#     for key in keys_list:
#         mtm_texts.append(des_encrypt(key, plain_text))
#     print("Generated {} MTM Texts".format(len(mtm_texts)))

#     # see if mtm texts cross over with any decrypted cipher texts
#     for key_decrypt in keys_list:
#         test_mtm_text = des_decrypt(key_decrypt, cipher_text)
#         if test_mtm_text in mtm_texts:
#             # found a mtm text
#             print("Found MTM Key")
#             return keys_list[mtm_texts.index(test_mtm_text)], key_decrypt
#     # fail couldn't find a key
#     print("Couldn't find a key")
#     return


# if __name__ == '__main__':
#     run()