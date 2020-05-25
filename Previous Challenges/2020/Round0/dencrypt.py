#!/bin/env python3
import sys
import os

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    print("Run `pip3 install --user pycryptodome` first")
    sys.exit(2)

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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {os.path.basename(sys.argv[0])} <e|d> <key> <text>")
        sys.exit(1)

    if sys.argv[1] == "e":
        print(encrypt(sys.argv[2], sys.argv[3]))
    elif sys.argv[1] == "d":
        print(decrypt(sys.argv[2], sys.argv[3]))
    else:
        print("Unrecognised function. Expected e or d")
        sys.exit(1)
