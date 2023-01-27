from pwn import *
from icecream import ic
from itertools import product
from typing import List

context.log_level = 'error'
p = remote('austiccquals.cyber.uq.edu.au', 3005)

def make_guess(guess: str):
    ic(guess)
    p.sendlineafter(b'> ', guess.encode())
    p.recvline()
    p.recvline()
    result = p.recvline(keepends=False).decode().split(' ')
    ic(result)
    return result

def play_once():
    first5 = make_guess('01234')
    second5 = make_guess('56789')

    chars = []
    for i, r in enumerate(first5 + second5):
        if r != '-':
            chars.append(str(i))
    ic(chars)

    possiblities = [''.join(x) for x in product(chars, chars, chars, chars, chars)]
    ic(len(possiblities))
    for possibility in possiblities.copy():
        for c in chars:
            if c not in possibility:
                if possibility in possiblities:
                    possiblities.remove(possibility)
    ic(len(possiblities))
    correct_spots = [None for _ in range(5)]
    incorrect_spots = [set() for _ in range(5)]

    def cull_possibilities(guess: str, result: List[str]):
        for i, (g, r) in enumerate(zip(list(guess), result)):
            if r == '=':
                correct_spots[i] = g
            else:
                incorrect_spots[i].add(g)

        ic(incorrect_spots)
        ic(correct_spots)

        for possibility in possiblities.copy():
            for i, c in enumerate(possibility):
                if correct_spots[i] is not None:
                    if c != correct_spots[i] and possibility in possiblities:
                        possiblities.remove(possibility)
                if c in incorrect_spots[i] and possibility in possiblities:
                    possiblities.remove(possibility)

        ic(len(possiblities))

    cull_possibilities('01234', first5)
    cull_possibilities('56789', second5)

    for i in range(3):
        if len(possiblities) == 0:
            make_guess('00000')
            continue
        guess = possiblities[0]
        result = make_guess(guess)
        cull_possibilities(guess, result)
        if len(possiblities) == 1:
            break


def main():
    for i in range(5):
        play_once()
    print(p.recvall())


if __name__ == '__main__':
    main()
