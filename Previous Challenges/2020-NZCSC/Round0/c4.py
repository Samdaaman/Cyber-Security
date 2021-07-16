#!/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(key, text):
    cipher = AES.new(bytes(key, "utf-8"), AES.MODE_ECB)

    text_as_bytes = bytes(text, "utf-8")
    text_as_padded_bytes = pad(text_as_bytes, 16)
    return cipher.encrypt(text_as_padded_bytes).hex()


def decrypt(key, text):
    cipher = AES.new(bytes(key, "utf-8"), AES.MODE_ECB)
    
    raw_bytes = bytes.fromhex(text)
    decrypted = cipher.decrypt(raw_bytes)
    return unpad(decrypted, 16).decode("utf-8")


def main():
    encrypted = [
        "3049cee6a95d539a8a6b335f018b14fd",
        "e70cb756ee16e9e1a45090264a597022",
        "ba79caba7b23a76052869a8df66e2919bcbe77aa5b6b0c13129e07285f7d54a5326aece8e7a3bd8b7f1746648ff4708a",
        "1216ec9e491b403b049cd768ba62690d613646a86bb096addc62d5d967967c061797e3802a33ea8c63318de7d8402f52b29975ec0f9986dd2120f6c171763323fce08d521f8d5166005276ddfc6f7a31",
        "854c6906332ffb3f78333aa7f2027a628bca48b2b2cbe8f2f01a448bb214d9b4",
        "c2d2b25b91cda61c69800c4c38a15dcf8bca48b2b2cbe8f2f01a448bb214d9b4",
        "d0935f7ee326ad6479afa51c055cb0369d050cfd1a697ac87e0b3130360dee3f",
        "bfa8ffd0e9d4b53b781caf8651943fa3"
    ]
    keys = [
        "flag:7245e1654e7"
    ]
    for key in keys:
        print(decrypt(key, encrypted[0]))

    for line in encrypted:
        print(decrypt(keys[0], line))


if __name__ == "__main__":
    main()
