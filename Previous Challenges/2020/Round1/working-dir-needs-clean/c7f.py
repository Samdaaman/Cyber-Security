from try_flag import tf, names



alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ct = '94p6qrs7naeh'

keys = names

for key in keys:
    if ' ' in key:
        continue
    key = key.lower()
    ctl = [alphabet.index(c) for c in ct]
    keyl = [alphabet.index(c) for c in key]

    print(ctl)
    print(keyl)

    p = ''
    for i in range(len(ctl)):
        c = ctl[i]
        k = keyl[i % len(keyl)]
        p += alphabet[(c - k) % len(alphabet)]

    print(p)
    tf(p)
    # if 'flag' in p:
    #     tf(p.replace('flag', '').replace(':', ''))