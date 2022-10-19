import string
h = 'E3B8287D4290F7233814D7A47A291DC0F71B2806D1A53B311CC4B97A0E1CC2B93B31068593332F10C6A3352F14D1B27A3514D6F7382F1AD0B0322955D1B83D3801CDB2287D05C0B82A311085A033291D85A3323855D6BC333119D6FB7A3C11C4A72E3C17CCBB33290C85B6343955CCBA3B3A1CCBB62E341ACBF72E3255CAA73F2F14D1B27A341B85A3323855D6BB333055C4A53F3C55C7B22E2A10C0B97A291DC0F73E3413C3BE392819D1F73B331185A3323855CCBA2A3206D6BE3831108B'
d = bytes.fromhex(h)

key_len = 5

key = [[] for _ in range(key_len)]

for i in range(key_len):
    for k in range(256):
        for j, c in enumerate(d):
            if j % key_len == i:
                if c ^ k > 128:
                    break
        else:
            key[i].append(k)

for k in key:
    print(f'=> {k}\n')

keys_and_score = []
for i in range(key_len):
    keys_and_score_for_offset = []
    for k in key[i]:
        score = 0
        for j, c in enumerate(d):
            if j % key_len == i:
                char = bytes([c ^ k]).decode()
                if char in string.printable:
                    score += 1
                    if char in string.ascii_letters:
                        score += 0.01
        keys_and_score_for_offset.append((bytes([k]).hex(), score))
    keys_and_score_for_offset = sorted(keys_and_score_for_offset, key=lambda x: -x[1])
    keys_and_score.append(keys_and_score_for_offset)

for key_and_score in keys_and_score:
    print(f'==> {key_and_score}')

