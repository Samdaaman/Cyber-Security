import wave


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')


wf = wave.open('audio.wav', 'rb')
CHUNK = 1024

buffer = wf.readframes(CHUNK)
c1 = []
for j in range(len(buffer)):
    i = buffer[j]
    if i > 1:
        break
    if j % 2 == 1:
        continue
    print(i)
    c1.append(i)

print(len(c1))

print(bitstring_to_bytes(''.join([str(i) for i in c1])))

