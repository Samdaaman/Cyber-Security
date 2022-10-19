#include <stdio.h>


// https://github.com/python/cpython/blob/v3.8.10/Objects/tupleobject.c#L368
#define _PyHASH_XXPRIME_1 ((Py_uhash_t)11400714785074694791ULL)
#define _PyHASH_XXPRIME_2 ((Py_uhash_t)14029467366897019727ULL)
#define _PyHASH_XXPRIME_5 ((Py_uhash_t)2870177450012600261ULL)
#define _PyHASH_XXROTATE(x) ((x << 31) | (x >> 33))  /* Rotate left 31 bits */

typedef unsigned long long Py_uhash_t;
typedef long long Py_ssize_t;
typedef long long Py_hash_t;

Py_hash_t test()
{
    int i = 0;
    Py_ssize_t len = 1;
    Py_uhash_t acc = _PyHASH_XXPRIME_5;
    printf("%i) %llu\n", ++i, acc);
    Py_uhash_t lane = 1;
    if (lane == (Py_uhash_t)-1) {
        return -1;
    }
    acc += lane * _PyHASH_XXPRIME_2;
    printf("%i) %llu\n", ++i, acc);
    acc = _PyHASH_XXROTATE(acc);
    printf("%i) %llu\n", ++i, acc);
    acc *= _PyHASH_XXPRIME_1;
    printf("%i) %llu\n", ++i, acc);
    /* Add input length, mangled to keep the historical value of hash(()). */
    acc += len ^ (_PyHASH_XXPRIME_5 ^ 3527539UL);
    printf("%i) %llu\n", ++i, acc);
    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}

int main()
{
    Py_hash_t hash = test();
    printf("%lld\n", hash);
}

// 1) 2870177450012600261
// 2) 16899644816909619988
// 3) 2239882801824648374
// 4) 8932352168822476794
// 5) 11802529618835948721
// -6644214454873602895