import math
data = []
for i in range(10):
    with open(f'secret.part{i+1}') as fi:
        data.append(fi.read())


def get(idx):
    g = idx % 10
    r = math.floor(idx/10)
    if r >= len(data[g]):
        return '?'
    else:
        return data[g][r]

s =''
for i in range(500):
    s += get(i)
print(s)
