cipher = "aufzmenrtgzjrihm"
plain = ""

alphabet = "abcdefghijklmnopqrstuvwxyz"

def get_letter(n):
    return alphabet[(n % 26) - 1]

def get_n(letter):
    return alphabet.index(letter) + 1

j = 6
for i in range(len(cipher)):
    c = cipher[i]
    c_n = get_n(c)
    p_n = c_n + j
    p = get_letter(p_n)
    print(f'{c}={c_n} gets added {j} to get {p_n}={p}')
