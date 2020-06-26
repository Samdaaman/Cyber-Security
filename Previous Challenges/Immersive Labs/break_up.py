with open('b64.txt') as fh:
    data = fh.readlines()[0]

i = 0
buffer = 130000
while True:
    chunk = data[i*buffer: (i+1)*buffer]
    if chunk == '':
        break
    with open(f'out_{i}.txt', 'w') as fh:
        fh.write(chunk)
    i += 1