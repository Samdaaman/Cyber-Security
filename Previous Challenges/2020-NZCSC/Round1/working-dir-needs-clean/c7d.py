from try_flag import tf



alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ct = 'h2yv:94p6qrs7naeh'

keys = [
    'cryptographyfirstdisco'
    'cryptogram',
    'cryptograpic',
    'cyptogram',
    'cypto',
    'cyptology',
    'cyptoanalytical',
    'cyptographies',
    'cryptologists',
    'cryptological',
    'cryptography',
    'cryptanalyst',
    'cryptograph',
    'cryptologic',
    'cryptic',
    'crypt',
    'cryptograph',
    'cryptal',
    'cryptogram',
    'cypt'
    ]

for key in keys:
    keyl = [alphabet.index(c) for c in key]

    print(keyl)

    p = ''
    for i in range(len(ct)):
        c = ct[i]
        if c == ':':
            continue
        k = keyl[i % len(keyl)]
        p += alphabet[(alphabet.index(c) - k) % len(alphabet)]

    print(p)
    if 'flag' in p:
        tf(p.replace('flag', '').replace(':', ''))