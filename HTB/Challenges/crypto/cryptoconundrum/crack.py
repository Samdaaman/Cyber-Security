import json
import math
from icecream import ic


with open('output.txt') as fh:
    cts = fh.read().split('\n')


with open('frequencies.txt') as fh:
    freqs = json.load(fh) # type: dict[str, float]

freqs_non_zero = list(filter(lambda x: x != 0.0, freqs.values()))
ic(len(freqs_non_zero))
ic(len(set(freqs_non_zero)))

ic(len(cts))
ic(len(set(cts)))

freq_to_bigrams = {} # type: dict[float, list[str]]
for key, value in freqs.items():
    if value not in freq_to_bigrams:
        freq_to_bigrams[value] = []
    freq_to_bigrams[value].append(key)


pt_bigram_options = [] # type: list[list[str]]

for ct in cts:
    freq = math.floor(cts.count(ct) / len(cts) * 100000) / 100000
    pt_bigram_options.append(freq_to_bigrams[freq].copy())

while True:
    print('Removing')
    removed_some = False
    for i in range(len(pt_bigram_options) - 1):
        curr_bigrams = pt_bigram_options[i]
        next_bigrams = pt_bigram_options[i+1]
        
        for curr_bigram in curr_bigrams.copy():
            if not any(curr_bigram[1] == next_bigram[0] for next_bigram in next_bigrams):
                curr_bigrams.remove(curr_bigram)
                removed_some = True

        for next_bigram in next_bigrams.copy():
            if not any(next_bigram[0] == curr_bigram[1] for curr_bigram in curr_bigrams):
                next_bigrams.remove(next_bigram)
                removed_some = True

    if not removed_some:
        break

print('Done')
# print([len(bigrams) for bigrams in pt_bigram_options])

ct_to_bigram = {} # type: dict[str, str]
for i, pt_bigrams in enumerate(pt_bigram_options):
    if len(pt_bigrams) == 1:
        ct_to_bigram[cts[i]] = pt_bigrams[0]


pt = ''
for i in range(len(cts)):
    if cts[i] in ct_to_bigram:
        pt += ct_to_bigram[cts[i]][0]
    elif i < len(cts) - 1 and cts[i+1] in ct_to_bigram:
        pt += ct_to_bigram[cts[i+1]][1]
    else:
        pt += '?'
    
    if i == len(cts) - 1:
        pt += ct_to_bigram[cts[i]][1]

print(pt)