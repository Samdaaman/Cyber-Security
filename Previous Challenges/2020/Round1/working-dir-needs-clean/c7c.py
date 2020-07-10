
alphabet = 'khnumotepi'
for c in 'abcdefghijklmnopqrstuvwxyz0123456789':
    if c not in alphabet:
        alphabet += c
ct = 'h2yv94p6qrs7naeh'

key = 'flag'

ctl = [alphabet.index(c) for c in ct]
keyl = [alphabet.index(c) for c in key]

print(ctl)
print(keyl)

for j in range(len(alphabet)):
    p = ''
    for i in range(len(ctl)):
        c = ctl[i]
        p += alphabet[(c - j) % len(alphabet)]

    print(p)