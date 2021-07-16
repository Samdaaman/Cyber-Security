import os
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes, inverse
from sympy import *
from icecream import ic


e = 0x69420
g = 0x69420

rsa_n = 0x16498bf7cc48a7465416e0f9ec8034f4030991e73aff9524ef74cc574228e36e6e1944c7686f69f0d1186a69b7aa77d7e954edc8a6932f006786f4648ecc8d4f4d3f6c03d9a1ee9fe61b28b6dd2791a63be581b8811a8ac90a387241ea68b7d36b4a274f64c7a721ad55cfcef23cd14c72542f576e4b507c11c4fa198e80021d484691b
ct1 = 0xa82b37d57b6476fa98f6ee7c278d934bd96c49aa1c5399552d25211230d76cb16ade049572bf631e3849903638d41c884957b9592d0aa072b2bdc3105fe0e3253284f85286ec613966f9cde77ae06e2053dc2254e44ca673b4c76879eff84e5fc32af976c1bfafe147a277d72aad674db749ed8f34d2ebe8189cf12afc9baa17764e4b

n_dh = 0xbe30ccaf896c16f53515e298df25df9158d0a95295c119f0444398b94fae26c0b4cf3a43b120cf0fb657069e0621eb1d2dd832eef3065e80ddbc35854dd4585cc41fd6a5b36339c0d9fcc066272be6818be6a624f75482bbb9c408010ac8c27b20397d870bfcb14e6318097b1601f99e391c9b68c5c586f8da561ff8507be9212713b910b748370ce692c11afa09b74ce80c5f5dd72046415aeed85e1ecedca14abe17ed19ab97729b859120699d9f80dd13f8483773df15b938b8399702a6e846b8728a70f1940d4c6e5835a06a89925eb1ec91a796f270e2d9be1a2c4bee5517109c161f04333d9c0d4034fbbd2dcf69fe734b759a89937f4d8ea0ee6b8385aae14a2cce361
ct2 = 0x65d57a564b8a8667a956705442063392b9b975b8ef869a6dbed04d6e585351f559fe6f5d96823f60b7306740fe2cf5aa81e4a12736d4f0a4826cbc8b4312643af19c75432b4ab222837031851f312df5d707b39bdf2d272f25c1947f3e2943f3592cb0519fee8f4b458021b6b8ee4eabeeae5127d412df4f6a88f66d7cc34c6bb77e0a1440737d0e167f9489f0c7fbfd7f6a5870b4b2865d29b91f6c2b375951e85b1b9f03887d4d3c4a6218111a95021ed1d554c57269e7830c3e7b8e17d13e1fb75ee9f305833d0cb6bfab738572cdbbc8b33b878ad25f78d47d7f449a6c348f5f9f1df3e09f924534a3669b4e69bd0411d154ec756b210691e2efc4a55aa664d938a868f4d

rsa_p = None
rsa_q = None
while True:
    rsa_p = 36209#getPrime(16)
    test = gcd(rsa_p, rsa_n - 1)
    if test > 1:
        rsa_p = test
        rsa_q = int(rsa_n / rsa_p)
        break

ic(rsa_p)
ic(rsa_q)

    