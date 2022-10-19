from operator import xor
from typing import List
from icecream import ic
from sage.crypto.sbox import SBox
from sage.crypto.sboxes import AES
from sage.all import *
from Crypto.Util.number import *
import os

KEY_SBOX = [170, 89, 81, 162, 65, 178, 186, 73, 97, 146, 154, 105, 138, 121, 113, 130, 33, 210, 218, 41, 202, 57, 49, 194, 234, 25, 17, 226, 1, 242, 250, 9, 161, 82, 90, 169, 74, 185, 177, 66, 106, 153, 145, 98, 129, 114, 122, 137, 42, 217, 209, 34, 193, 50, 58, 201, 225, 18, 26, 233, 10, 249, 241, 2, 188, 79, 71, 180, 87, 164, 172, 95, 119, 132, 140, 127, 156, 111, 103, 148, 55, 196, 204, 63, 220, 47, 39, 212, 252, 15, 7, 244, 23, 228, 236, 31, 183, 68, 76, 191, 92, 175, 167, 84, 124, 143, 135, 116, 151, 100, 108, 159, 60, 207, 199, 52, 215, 36, 44, 223, 247, 4, 12, 255, 28, 239, 231, 20, 134, 117, 125, 142, 109, 158, 150, 101, 77, 190, 182, 69, 166, 85, 93, 174, 13, 254, 246, 5, 230, 21, 29, 238, 198, 53, 61, 206, 45, 222, 214, 37, 141, 126, 118, 133, 102, 149, 157, 110, 70, 181, 189, 78, 173, 94, 86, 165, 6, 245, 253, 14, 237, 30, 22, 229, 205, 62, 54, 197, 38, 213, 221, 46, 144, 99, 107, 152, 123, 136, 128, 115, 91, 168, 160, 83, 176, 67, 75, 184, 27, 232, 224, 19, 240, 3, 11, 248, 208, 35, 43, 216, 59, 200, 192, 51, 155, 104, 96, 147, 112, 131, 139, 120, 80, 163, 171, 88, 187, 72, 64, 179, 16, 227, 235, 24, 251, 8, 0, 243, 219, 40, 32, 211, 48, 195, 203, 56]
PBOX = [59, 82, 101, 135, 189, 153, 105, 14, 179, 71, 167, 33, 160, 198, 218, 104, 66, 37, 216, 199, 132, 214, 217, 42, 231, 221, 236, 233, 203, 24, 220, 120, 158, 240, 84, 81, 152, 201, 57, 253, 249, 169, 79, 234, 136, 12, 40, 209, 29, 224, 17, 77, 60, 102, 195, 8, 212, 95, 147, 190, 138, 213, 98, 10, 4, 243, 1, 128, 145, 58, 241, 119, 88, 211, 110, 157, 3, 188, 19, 208, 44, 244, 122, 92, 109, 69, 134, 22, 90, 61, 202, 193, 141, 183, 133, 75, 144, 116, 191, 39, 207, 140, 192, 247, 83, 43, 121, 99, 254, 226, 177, 26, 9, 173, 78, 176, 223, 210, 156, 16, 227, 125, 93, 54, 76, 150, 5, 36, 185, 65, 72, 246, 131, 41, 106, 248, 151, 182, 204, 225, 229, 70, 7, 250, 115, 85, 163, 124, 184, 130, 239, 196, 15, 100, 252, 25, 171, 143, 0, 67, 222, 96, 165, 180, 46, 232, 117, 48, 38, 161, 50, 35, 73, 18, 154, 114, 175, 146, 148, 89, 80, 112, 228, 49, 172, 63, 123, 86, 149, 103, 230, 64, 28, 27, 166, 111, 170, 55, 47, 20, 51, 215, 32, 13, 118, 11, 53, 205, 238, 91, 6, 94, 200, 181, 162, 178, 194, 126, 164, 2, 255, 137, 242, 23, 74, 197, 142, 108, 52, 187, 129, 186, 155, 97, 107, 34, 245, 68, 56, 127, 21, 219, 159, 62, 113, 237, 206, 45, 251, 168, 87, 31, 30, 235, 174, 139]


def int_to_bits(value: int):
        return [int(i) for i in bin(value)[2:].rjust(8, '0')]

def bits_to_int(bits: List[int]):
    assert len(bits) == 8
    return sum([int(bits[i])*2^(7-i) for i in range(8)])

def block_to_bits(block: bytes):
    value = bytes_to_long(block)
    return [int(i) for i in bin(value)[2:].rjust(256, '0')]

def bits_to_block(bits: List[int]):
    assert len(bits) == 256
    value = sum([int(bits[i])*2^(255-i) for i in range(256)])
    return long_to_bytes(value).rjust(32, b'\x00')


def main():
    sbox = SBox(KEY_SBOX)

    F2.<w> = GF(2^8)
    poly_byte = sbox.interpolation_polynomial(F2)

    b, a = poly_byte.coefficients()
    ic(a, b)
    ic(a.integer_representation(), b.integer_representation())

    ic(poly_byte)

    

    F = GF(2)
    Am = matrix(F, 8)
    for i in range(8):
        bits = int_to_bits((a * w^(7-i)).integer_representation())
        for j in range(8):
            Am[j, i] = bits[j]
    Bm = vector(F, int_to_bits(b.integer_representation()))

    ic(Am)
    ic(Bm)

    for i in range(256):
        X = vector(F, int_to_bits(i))
        Y = Am*X + Bm
        y = bits_to_int(Y)
        assert y == KEY_SBOX[i]

    A = matrix(F, 256)
    for i in range(256):
        for j in range(256):
            if i // 8 == j // 8:
                A[i, j] = Am[i%8, j%8]

    B = vector(F, 256)
    for i in range(256):
        B[i] = Bm[i%8]

    x_bytes = os.urandom(32)
    X_test = vector(F, block_to_bits(x_bytes))

    Y_test = A * X_test + B
    Y_test_bytes = bits_to_block(Y_test)
    ic(Y_test_bytes.hex())
    ic(substitute(sbox, x_bytes).hex())

    sbox_d = SBox([xor(i, x_bytes[0]) for i in KEY_SBOX])
    K0 = matrix(F, 256)
    for i in range(256):
        K0[i, i%8] = 1
    Ad = A + K0
    Y_test = Ad * X_test + B
    Y_test_bytes = bits_to_block(Y_test)
    ic(Y_test_bytes.hex())
    ic(substitute(sbox_d, x_bytes).hex())

    P = matrix(F, 256)
    for i in range(256):
        # inbyte = i // 8
        # # inbit = 7 - (i % 8)
        # inbit = i % 8
        # outnum = PBOX[i]
        # outbyte = outnum // 8
        # # outbit = 7 - (outnum % 8)
        # outbit = outnum % 8
        # P[outbyte*8 + outbit, inbyte*8 + inbit] = 1
        P[PBOX[i], i] = 1

    Y_test = P * X_test
    Y_test_bytes = bits_to_block(Y_test)
    ic(Y_test_bytes.hex())
    ic(permute(x_bytes).hex())

    I = matrix.identity(F, 256)
    V = P*Ad + I
    W = P*B

    Y_test = V*X_test + W
    Y_test_bytes = bits_to_block(Y_test)
    ic(Y_test_bytes.hex())
    x_bytes_sub = substitute(sbox_d, x_bytes)
    x_bytes_per = permute(x_bytes_sub)
    y_bytes = xor_arr(x_bytes_per, x_bytes)
    ic(y_bytes.hex())


def xor_arr(a: bytes, b: bytes):
    return bytes([xor(i, j) for i, j in zip(a, b)])


def substitute(sbox: SBox, data):
    return bytes([sbox(b) for b in data])

def permute(data):
    out = [0]*32
    for num in range(256):
        outnum = PBOX[num]
        inbyte = num // 8
        inbit = 7 - (num % 8)
        outbyte = outnum // 8
        outbit = 7 - (outnum % 8)

        if data[inbyte] & (1 << inbit):
            out[outbyte] |= (1 << outbit)
    return bytes(out)


if __name__ == '__main__':
    main()