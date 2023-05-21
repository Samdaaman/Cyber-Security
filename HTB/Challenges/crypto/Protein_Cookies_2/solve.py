from icecream import ic
import cryptoutil_debug as cryptoutil
from Crypto.Random import get_random_bytes

BLOCK_LEN = 32

original_data = 'user_id=guest&isLoggedIn=False'

SECRET = get_random_bytes(50)

def test():
    original_signature = cryptoutil.lj12_hash(SECRET + original_data.encode())
    forged_data, forged_signature = forge(original_signature)
    forged_signature_test = cryptoutil.lj12_hash(SECRET + forged_data.encode())
    ic(forged_signature, forged_signature_test)



def forge(signature_hex: str):
    to_append = '&isLoggedIn=True'
    forged = cryptoutil.pad(b'0' * 50 + original_data.encode()).decode()[50:] + to_append
    appended_block = pad(to_append.encode(), 50 + len(forged))
    ic(appended_block)
    forged_signature = cryptoutil.compression_function(appended_block, bytes.fromhex(signature_hex))

    return forged, forged_signature.hex()



def pad(data, original_len):
    if len(data) % BLOCK_LEN == 0:
        return data

    pad_byte = bytes([original_len % 256])
    pad_len = BLOCK_LEN - (len(data) % BLOCK_LEN)
    data += pad_byte * pad_len

    return data


if __name__ == '__main__':
    test()
    print('.'.join(forge('1188d286045737f469c69508bc99290e47954bee2a44fec0bf365b49893d53b1')))




# def scramble(enc: bytes):
#     enc = enc[::-1]
#     enc = enc[::2] + enc[1::2]
#     enc = enc[::3] + enc[2::3] + enc[1::3]
#     return enc

# def unscramble(enc: bytes):
#     enc2 = b''
#     i = 0
#     while i < len(enc) / 3:
#         enc2 += enc[i:i+1]
#         enc2 += enc[i+2*len(enc)//3:i+2*len(enc)//3+1]
#         if i < 10:
#             enc2 += enc[i+len(enc)//3+1:i+len(enc)//3+2]
#         i += 1
#     enc = enc2

#     enc2 = b''
#     i = 0
#     while i < len(enc) / 2:
#         enc2 += enc[i:i+1]
#         enc2 += enc[i+len(enc)//2:i+len(enc)//2+1]
#         i += 1
#     enc = enc2
    
#     enc = enc[::-1]
#     return enc


# def test():
#     ic(len(iv))
#     data = b'123456789AAAAAAAAAAAAAAAAAAAAAAA'

#     scrambled = scramble(data)
#     ic(scrambled)
#     unscrambled = unscramble(scrambled)
#     ic(unscrambled)
#     ic(len(unscrambled))