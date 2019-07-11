from Crypto.Cipher import DES
from binascii import unhexlify, hexlify
from random import randint


def des_encrypt(key, plain_text):
    # encrypt using DES
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plain_text)


def des_decrypt(key, cipher_text):
    # decrypt using DES
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(cipher_text)


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


def run():
    # test plain text
    plain_text = b'abcdefgh'

    # tmax = 1 for testing max cracking time otherwise tmax = 0
    tmax = 0

    # key size to crack
    numbits = 14

    test_mtm_attack(plain_text, numbits, tmax)


def test_mtm_attack(plain_text, numbits, tmax):

    # code if 1 or if 0 which can test the maximum time for cracking else random cracking time
    if tmax:
        keynum1 = 2 ** numbits - 1
        keynum2 = 2 ** numbits - 1
    else:
        # key number generation
        keynum1 = randint(0, 2 ** numbits - 1)
        keynum2 = randint(0, 2 ** numbits - 1)

    # Test MTM Attack
    print("Testing MTM Attack with key numbers {} and {}\nwith key length {} bits".format(keynum1, keynum2, numbits))

    # Generate Cipher Text
    print("Generating Cipher Text from {}".format(plain_text))
    key1 = nth_key(keynum1)
    key2 = nth_key(keynum2)
    cipher_text = des_encrypt(key2, des_encrypt(key1, plain_text))
    print("Key1 is: {}\nKey2 is: {}\n".format(hexlify(key1).decode("utf-8"), hexlify(key2).decode("utf-8")))

    print("Executing MTM Attack")
    mtm_keys = mtm_attack(plain_text, cipher_text, numbits)
    if len(mtm_keys) == 2:
        mtm_key1 = mtm_keys[0]
        mtm_key2 = mtm_keys[1]
        print("\nMTM Keys are\nKey1 is: {}\nKey2 is: {}".format(hexlify(mtm_key1).decode("utf-8"), hexlify(mtm_key2).decode("utf-8")))


def mtm_attack(plain_text, cipher_text, numbits):

    # status
    print("There are {} keys and MTM texts to generate".format(2 ** numbits))

    # key generation
    keys_list = []
    for i in range(2 ** numbits):
        key = nth_key(i)
        # print(hexlify(key).decode("utf-8"))
        keys_list.append(key)
    print("Generated {} keys".format(len(keys_list)))

    # mtm texts (single DES cipher text) generation
    mtm_texts = []
    for key in keys_list:
        mtm_texts.append(des_encrypt(key, plain_text))
    print("Generated {} MTM Texts".format(len(mtm_texts)))

    # see if mtm texts cross over with any decrypted cipher texts
    for key_decrypt in keys_list:
        test_mtm_text = des_decrypt(key_decrypt, cipher_text)
        if test_mtm_text in mtm_texts:
            # found a mtm text
            print("Found MTM Key")
            return keys_list[mtm_texts.index(test_mtm_text)], key_decrypt
    # fail couldn't find a key
    print("Couldn't find a key")
    return


if __name__ == '__main__':
    run()