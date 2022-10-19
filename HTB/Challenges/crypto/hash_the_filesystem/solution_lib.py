from struct import pack, unpack
from icecream import ic
from sage.all import *

uin64_mod = 18446744073709551616
x_prime_1 = 11400714785074694791
x_prime_2 = 14029467366897019727
x_prime_5 = 2870177450012600261
x_rotate = lambda x: ((x << 31) | (x >> 33)) % uin64_mod
x_rotate_inv = lambda x: ((x << 33) | (x >> 31)) % uin64_mod


def inv_mul(a, c):
    s = xgcd(a, uin64_mod)[1]
    return c * s % uin64_mod


def mock_hash_tuple(x):
    """Mocks builtin call to hash(tuple([x]))"""
    acc = x_prime_5
    acc += x * x_prime_2
    acc = x_rotate(acc)
    acc *= x_prime_1
    acc += 1 ^ (x_prime_5 ^ 3527539)
    acc %= uin64_mod
    acc_s = unpack('q', pack('Q', acc))[0]
    return acc_s


def inverse_hash(target_hash: int):
    """Inverts builtin call to hash(tuple([x])) and returns x for a given hash"""
    acc = unpack('Q', pack('q', target_hash))[0]
    acc -= 1 ^ (x_prime_5 ^ 3527539)
    acc = inv_mul(x_prime_1, acc)
    acc = x_rotate_inv(acc)
    acc -= x_prime_5
    return inv_mul(x_prime_2, acc)


if __name__ == '__main__':
    n = 123
    target_hash = hash(tuple([n]))
    ic(target_hash)
    ic(mock_hash_tuple(n))
    ic(inverse_hash(target_hash))


# #define _PyHASH_XXPRIME_1 ((Py_uhash_t)11400714785074694791ULL)
# #define _PyHASH_XXPRIME_2 ((Py_uhash_t)14029467366897019727ULL)
# #define _PyHASH_XXPRIME_5 ((Py_uhash_t)2870177450012600261ULL)
# #define _PyHASH_XXROTATE(x) ((x << 31) | (x >> 33))  /* Rotate left 31 bits */

# https://github.com/python/cpython/blob/v3.8.10/Objects/tupleobject.c#L368
# static Py_hash_t
# tuplehash(PyTupleObject *v)
# {
#     Py_ssize_t i, len = Py_SIZE(v);
#     PyObject **item = v->ob_item;
#
#     Py_uhash_t acc = _PyHASH_XXPRIME_5;
#     for (i = 0; i < len; i++) {
#         Py_uhash_t lane = PyObject_Hash(item[i]);
#         if (lane == (Py_uhash_t)-1) {
#             return -1;
#         }
#         acc += lane * _PyHASH_XXPRIME_2;
#         acc = _PyHASH_XXROTATE(acc);
#         acc *= _PyHASH_XXPRIME_1;
#     }
#
#     /* Add input length, mangled to keep the historical value of hash(()). */
#     acc += len ^ (_PyHASH_XXPRIME_5 ^ 3527539UL);
#
#     if (acc == (Py_uhash_t)-1) {
#         return 1546275796;
#     }
#     return acc;
# }