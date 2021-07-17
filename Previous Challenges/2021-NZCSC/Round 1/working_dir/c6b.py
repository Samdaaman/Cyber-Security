import hashlib
import itertools


def hash(k):
    hash_object = hashlib.sha1(b''.join(k))
    h = hash_object.hexdigest()
    return h

with open('gesture.key', 'rb') as fh:
    t = fh.read()

t = t.hex()

l = 2
while True:
    d = list(itertools.permutations([bytes([i]) for i in range(9)],l))
    print(f'{l}: {len(d)}')
    for k in d:
        if hash(k) == t:
            print(k)
            break
    l += 1
    if l > 10:
        break
