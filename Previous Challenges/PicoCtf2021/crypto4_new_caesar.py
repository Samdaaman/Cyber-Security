from collections import Counter
from re import L
import string
from itertools import *
from icecream import ic

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(data):
	plain = ""
	for i in range(len(data) // 2):
		a = ALPHABET.find(data[i*2])
		b = ALPHABET.find(data[i*2+1])
		plain += chr((a << 4) + b)
	return plain


def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]


ct = 'lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil'
for key in ALPHABET:
	unshifted = ''
	for i, c in enumerate(ct):
		unshifted += unshift(c, key[i % len(key)])

	print(b16_decode(unshifted))

ic(ALPHABET[0], ALPHABET[-1])


def challenge():
	flag = "redacted"
	key = "redacted"

	assert all([k in ALPHABET for k in key])
	assert len(key) == 1

	b16 = b16_encode(flag)
	enc = ""
	for i, c in enumerate(b16):
		enc += shift(c, key[i % len(key)])
	print(enc)
