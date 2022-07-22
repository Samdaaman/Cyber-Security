from debug import *
from icecream import ic


def twistedColumnarDecrypt(ct: str, key: str):
    derived_key = deriveKey(key)

    width = len(key)

    num_cols = len(ct) // width
    num_rows = width

    matrix1 = [[None for _ in range(num_cols)] for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            matrix1[i][j] = ct[i * num_cols + j]
    ic(matrix1)

    matrix2 = [matrix1[k-1][::-1] for k in derived_key]
    ic(matrix2)

    matrix3 = transpose(matrix2)
    ic(matrix3)
    pt = ''.join(''.join(row) for row in matrix3)

    return pt


def test():
    key = str(int.from_bytes(os.urandom(4), 'big')).rjust(10, '0')
    ic(key)
    pt = 'sam is cool abcdefgh'
    ct = twistedColumnarEncrypt(pt, key)
    ic(ct)
    pt_test = twistedColumnarDecrypt(ct, key)
    ic(pt_test)
    assert pt == pt_test


def main():
    with open('encrypted_messages.txt') as fh:
        ct_array = [line.strip() for line in fh.readlines()]
    
    pt_out = ''

    for ct in ct_array:
        key = str(148823505998502)
        pt = twistedColumnarDecrypt(ct, key)
        ic(pt)
        pt_out += pt + '\n'

    print(pt_out)

#    HTB{THISRNGISNOTSAFEFORGENETINGOUTPUTS} 



if __name__ == '__main__':
    main()
    # test()