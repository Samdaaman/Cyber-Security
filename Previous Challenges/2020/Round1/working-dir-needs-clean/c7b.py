
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ct = 'h2yv94p6qrs7naeh'

key = 'cryptograph'

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