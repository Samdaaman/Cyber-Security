from string import ascii_letters, ascii_lowercase


with open('challenge.txt') as fh:
    ct = fh.read()

alphabet = ascii_lowercase

pt = ''
for i, c in enumerate(ct):
    c_lower = c.lower()
    if c_lower in alphabet:
        idx = alphabet.index(c_lower)
        idx = (idx - i) % len(alphabet)
        p = alphabet[idx] if c_lower == c else alphabet[idx].upper()
        pt += p
    else:
        pt += c
print(pt)