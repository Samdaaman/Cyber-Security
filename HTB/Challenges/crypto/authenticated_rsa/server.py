from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
import hashlib
import os
# from secret import flag
flag = b'HTB{REDACTED}'

# HIDE FLAG auth_code and implement pyrandom
# 3 bytes padding minimum - e can be anywhere in first 1000 primes ???

N_BITS = 2048
E_BITS = 13
MAX_REQUESTS = 1000

def random_no_zeros(size: int):
    output = b''
    for _ in range(size):
        byte = b'\x00'
        while byte == b'\x00':
            byte = os.urandom(1)
        output += byte
    return output


def get_auth_code(data: bytes):
    return hashlib.sha256(data).digest()


def encrypt(e: int, n: int, pt: bytes):
    if len(pt) + 6 > N_BITS // 8:
        raise Exception('Too long plaintext')
    
    padding = b'\x02' + random_no_zeros((N_BITS // 8) - 3 - len(pt)) + b'\x00'
    pt_padded = padding + pt
    pt_padded_int = bytes_to_long(pt_padded)
    ct_int = pow(pt_padded_int, e, n)
    ct = long_to_bytes(ct_int)
    auth_code = get_auth_code(padding)
    return ct, auth_code


def decrypt(d: int, n: int, ct: bytes, auth_code: bytes):
    ct_int = bytes_to_long(ct)
    pt_padded_int = pow(ct_int, d, n)
    pt_padded = long_to_bytes(pt_padded_int)
    
    if not pt_padded.startswith(b'\x02'):
        return None # invalid padding
    
    padding, _, pt = pt_padded.partition(b'\x00')
    padding += b'\x00'
    if auth_code != get_auth_code(padding):
        return None # invalid auth code

    return pt


def main():
    while True:
        p = getPrime(N_BITS // 2)
        q = getPrime(N_BITS // 2)
        n = p * q
        phi = (p - 1) * (q - 1)
        try:
            e = getPrime(E_BITS)
            d = pow(e, -1, phi)
            break
        except ValueError:
            pass

    print(
f'''
======================================================================
Welcome to the Very Super Secure Authenticated RSA Encryption terminal
Security measures require authentication codes and PKCS#1 v1.5 padding

Authentication allows messages to only be decrypted by trusted persons
======================================================================

Your randomised public key
e = <SECRET>
n = {long_to_bytes(n).hex()}''')

    try:
        num_requests = 0

        while True:
            print(
'''
Options:                  
1) Get encrypted flag
2) Authenticated encryption
3) Authenticated decyption''')

            option = int(input('Enter choice > '))

            num_requests += 1
            if num_requests> MAX_REQUESTS:
                raise Exception('Too many requests')

            if option == 1:
                flag_enc, flag_auth_code = encrypt(e, n, flag)

                print(f'flag_enc = {flag_enc.hex()}')
                print(f'flag_auth_code = {flag_auth_code.hex()}')

            elif option == 2:
                pt = input('Enter pt > ').encode()
                ct, auth_code = encrypt(e, n, pt)
                print(f'ciphertext = {ct.hex()}')
                print(f'auth_code = {auth_code.hex()}')

            elif option == 3:
                ct = bytes.fromhex(input('ciphertext (hex) > '))
                auth_code = bytes.fromhex(input('auth_code (hex) > '))
                pt = decrypt(d, n, ct, auth_code)
                if pt is None:
                    print('Decryption failed - invalid padding or auth code')
                elif pt == flag:
                    print('Only admins can decrypt the flag')
                else:
                    print(f'decrypted = {pt.decode(errors="ignore")}')
            
            else:
                print('Unknown option')

    except KeyboardInterrupt:
        print()

    except Exception as ex:
        print(f'Exception {ex}')


if __name__ == '__main__':
    main()
