from icecream import ic

def read_file(text_file):
    file = open(text_file, encoding="utf8").read().strip()
    return file

file = read_file("UTF-8.txt")

# h = 0
# i = 0
# b = 0 
# c = 0

ic((len(file) / 54109) ** (1/2)) # h range
ic(len(file) / 190783) # i range
ic(len(file) / 152054) # b range
ic(len(file) / 43339) # c range

for h in range(-4, 4):
    for i in range(-6, 6):
        for b in range(-8, 8):
            for c in range(-26, 26):
                d = h + b + c
                e = (d * 3) + (h * 4)
                g = c + 3
                a = h * h
                f = d + a
                indexes = [(54109 * a), (26461 * d), (41371 * b), (41371 * b), (190783 * i), (44827 * b), 421329, 886787, (43339 * c), (6990 * b), (161971 * b), (168118 * c), (190783 * i), (190783 * i), (44827 * b), (152054 * b), (28548 * d), 421287, 403001, (152054 * b), (6990 * b), 403001, (92781 * a), 657819, (33881 * b), 403001, 421287, 657819, 657819, 411523, 403001, 79837, (28548 * d), (41371 * b), 375470, 171564, 1027617, (33881 * b), (152054 * b), 657819, (28548 * d), 403001, (152054 * b), (33881 * b), 403001, (152054 * b), (6990 * b), 403001, (305633 * h), 403001, 1049683, (305633 * h), (6690 * 5), (33881 * b), 79837, 403001, 657819, (190783 * i), 403001, (9965 * (a + d)), (152054 * b), 903622, 79837, (225517 * h)]
                try:
                    chars = ''.join(file[index] for index in indexes)
                    print(f'{h} {i} {b} {c} {chars}')
                except IndexError:
                    pass

# ic(indexes)

