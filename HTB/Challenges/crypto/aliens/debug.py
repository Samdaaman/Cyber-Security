from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
from icecream import ic

# from secret import FLAG
FLAG = 'HTB{FAKE_FLAG_FOR_TESTING}'

class AAES():
    def __init__(self):
        self.padding = "CryptoHackTheBox"

    def pad(self, plaintext):
        return plaintext + self.padding[:(-len(plaintext) % 16)] + self.padding

    def encrypt(self, plaintext):
        cipher = AES.new(os.urandom(16), AES.MODE_ECB)
        to_enc = pad(plaintext, 16)
        blocks = [to_enc[i:i+16] for i in range(0, len(to_enc), 16)]
        for i, block in enumerate(blocks):
            ic(i, block)
        # return to_enc
        return cipher.encrypt(to_enc)


def main():
    aaes = AAES()

    while True:
        message = input("Message for encryption: ")
        plaintext = aaes.pad(message) + aaes.pad(FLAG)
        print(aaes.encrypt(plaintext.encode()).hex())


if __name__ == "__main__":
    main()
