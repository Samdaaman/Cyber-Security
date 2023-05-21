from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes

BITS = 2048

# while True:
#     p = getPrime(BITS // 2)
#     q = getPrime(BITS // 2)
#     n = p * q
#     e = 65537
#     phi = (p - 1) * (q - 1)
#     try:
#         d = pow(e, -1, phi)
#         break
#     except ValueError:
#         pass

# for i in range(100):
#     pt1 = bytes_to_long(f'TEST 123 {"a" * i}'.encode())
#     ct1 = pow(pt1, e, n)
#     print(ct1.bit_length())

#     ct1_mod = (ct1 << (8*e)) % n
#     print(ct1_mod)
#     pt1_mod = pow(ct1_mod, d, n)
#     print(long_to_bytes(pt1_mod))


# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.Cipher import PKCS1_v1_5
# from Crypto.PublicKey import RSA

# e = 3

# key = RSA.generate(BITS, e=e)
# key.n
# ct = PKCS1_v1_5.new(key).encrypt(b'TEST 12345')
# pt1 = PKCS1_v1_5.new(key).decrypt(ct, b'')
# print(pt1)
# pt2 = PKCS1_v1_5.new(key).decrypt(long_to_bytes((bytes_to_long(ct) << (8*e)) % key.n), b'')
# print(pt2)
# pt3 = long_to_bytes(pow(bytes_to_long(ct), key.d, key.n))
# print(pt3)

e = 74021
n = 27114403558047827885860902137422935551922831894282402014363488778491049206663940188497093716956184312992754792613175453456062920747428927593559879350655099115211560554675427348445904948929622556769356100988257267697841028497669171434029597387544085558916216954592695136260355827272552355671393193550416467319842519081803203955107518213165001535092215363690159714177734763674443761116636811136246319199535135193659409140810029188708641592297348189433172457219489981783111654803948264511525272269959686041053991865953970889690674874131137949980854458200362626861364268178363521199093843346412884082723905647831676007921
ct = bytes_to_long(bytes.fromhex('c0aaa7c0e1c2026987f99209db20b00110e0506bb788054ce0b72c689614e0b49c1c5dc65777e10dadc2d318dd1def1a12683646b6e01a50cdbe83899e844631744767e822f3f6d43a914dece8457fc653bb5360dfc4c888fc5ffdf18eb2dc3a169bb30727e98dcba8ea13ae0c8e5f5b17bfb2512ababc9b54a82ee4b073637fe8a2c3d69c74cf9955071a153d5d1cef378980581a80f498662d6823707d482d69eb66be590376ce8d057a676f594f3e7ef0813a90b68b0d476b6336b2e7d100a49addce61887cf1ad1b9a8e1c747bd87663506d3dc2cfa01b5c18e633df5bcc94cc69c06119266e7f98b495d1c8c6c2a9129f30c432e0b17eb1341e40f4ec4a'))
print(ct.bit_length())

ct1_mod = (ct << (8*e)) % n
print(long_to_bytes(ct1_mod).hex())