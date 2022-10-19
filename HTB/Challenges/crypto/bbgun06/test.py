from hashlib import sha1
import re
from server import *
from icecream import ic
from Crypto.Util.number import long_to_bytes, bytes_to_long


asn1 = b"\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14"


def pad(message, target_length):
    max_message_length = target_length - 11
    message_length = len(message)

    if message_length > max_message_length:
        raise OverflowError(
            "%i bytes needed for message, but there is only"
            " space for %i" % (message_length, max_message_length))

    padding_length = target_length - message_length - 3

    return b"".join(
        [b"\x00\x01", padding_length * b"\xff", b"\x00", message])


def sign(message, d, n):
    hash_value = sha1(message).digest()

    keylength = len(long_to_bytes(n))
    cleartext = asn1 + hash_value
    padded = pad(cleartext, keylength)

    payload = bytes_to_long(padded)
    block = long_to_bytes(pow(payload, d, n))

    return block


def verify(message, signature, e, n):
    keylength = len(long_to_bytes(n))
    decrypted = pow(bytes_to_long(signature), e, n)
    clearsig = decrypted.to_bytes(keylength, "big")

    r = re.compile(b'\x00\x01\xff+?\x00(.{15})(.{20})', re.DOTALL)
    m = r.match(clearsig)

    if not m:
        print('failed step 1')
        return False
        # raise VerificationError('Verification failed')

    if m.group(1) != asn1:
        print('failed step 2')
        return False
        # raise VerificationError('Verification failed')

    if m.group(2) != sha1(message).digest():
        print('failed step 3')
        return False
        # raise VerificationError('Verification failed')

    return True

def hex2(num: int):
    return hex(num)[2:].rjust(512, '0')

# rsa = RSA(2048)
# ic(rsa.n)
# ic(rsa.d)
e = 3
n = 20004897981835739210283682852897387567400488824210846338863207592745454751190656483019241812511250034440711990846454498602577130796850902273292653028227823824572272819925111984528354369966250230234612775255748203963570808026156536118273022006328073005058404822136032105752361669924728089013013795126856931470001039465795146495530709788181880628730151351838300038484169764355195774883492821255203554482510602277134170655685893810015637537892807544495549240912790985744717757793109656684272423054845406556998351465777274954797939903638052003313016270122784645787065186176922977440795179573942976316301389604955969762603
d = 13336598654557159473522455235264925044933659216140564225908805061830303167460437655346161208340833356293807993897636332401718087197900601515528435352151882549714848546616741323018902913310833486823075183503832135975713872017437690745515348004218715336705603214757354737168241113283152059342009196751237954313142551176765540413406551515396569760601095780121715217469720514019257667287369218977580576285018471019818004474516189467957956799157172203328509583277279062802749897555155799387256808184559545746435551949216816662452186477403740318252027344360142322608920356891597332646021726681668262350060741592169007378747

user, data = parseEmail()
signature = sign(user, d, n)
ic(verify(user, signature, e, n))

ic(user)

sig = bytes_to_long(signature)
sig_enc = pow(sig, e, n)
ic(hex2(sig_enc))

sig2 = sig * ((n-1) ** 6)
sig2_enc = pow(sig2, 3, n)
ic(hex2(sig2_enc))

ic(sig == sig2 % n)

a_enc = 0x1ffff
a = pow(a_enc, d, n)
ic(a)

hash = b'\xdb\x7d\xdd\x3f\x79\x65\x41\xda\x4f\x80\x5d\x79\x48\x6f\xd3\x77\x07\x9c\x32\x70'
fake0 = b'\x00\x01\xff\x00' + asn1 + hash
fake1 = b'\x00\x01\xff\x00' + asn1 + hash + b'\x00'
fake2 = b'\x00\x01\xff\x00' + asn1 + hash + b'\x12\x34\x56'

def re_test(clearsig: bytes):
    r = re.compile(b'\x00\x01\xff+?\x00(.{15})(.{20})', re.DOTALL)
    m = r.match(clearsig)

    if not m:
        print('failed step 1')
        return False
        # raise VerificationError('Verification failed')

    if m.group(1) != asn1:
        print('failed step 2')
        return False
        # raise VerificationError('Verification failed')

    if m.group(2) != hash:
        print('failed step 3')
        return False
    
    return True

for fake in [fake0, fake1, fake2]:
    ic(re_test(fake))
# ic(len(fake) * 8)