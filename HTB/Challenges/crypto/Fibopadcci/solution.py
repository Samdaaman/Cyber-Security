from pwn import *
import server


local = False
if not local:
    p = remote('138.68.188.223', 31306)

a_secret = b'HTB{th3_s3crt_A}'
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 121, 98, 219, 61]


def trial_decrypt(ct: bytes, b: bytes):
    if local:
        result = server.sendMessage(ct, a_secret, b)
    else:
        p.sendline('1')
        p.sendline(ct.hex())
        p.sendline(b.hex())
        p.recvuntil('Enter the B used during encryption in hex: ')
        res = p.recvline(False).decode()
        return res


    if result == "Message successfully sent!":
        return True
    elif result == "Error: Message padding incorrect, not sent.":
        return False
    else:
        raise Exception(result)


def crack_block(lb_pt: bytes, lb_ct: bytes, ct_block: bytes) -> bytes:
    # loop 1
    pt = b''
    dec = b''
    for j in range(16):
        # loop 2
        results = []
        for i in range(256):
            lb_ct_i = lb_ct[:15-j] + bytes([i]) + lb_ct[16-j:]
            results.append(trial_decrypt(ct_block, lb_ct_i))
            print(i)

        # crack
        if results.count(True) == 2:
            results[lb_ct[15-j]] = False
        assert results.count(True) == 1
        cracked_i = results.index(True)
        pt = bytes([cracked_i ^ 1 ^ lb_ct[15-j]]) + pt
        dec = bytes([cracked_i ^ 1]) + dec

        print(pt)

        if j < 15:
            pad = b''
            for i in range(j+1):
                pad = pad + bytes([fib[i+1]])
            lb_ct = lb_ct[:16-len(pad)] + server.xor(dec, pad)
    return pt


def main():
    if local:
        flag_ct, flag_a_hex, flag_b_hex = server.SuperSecureEncryption(server.key).encrypt(server.flag)
    else:
        p.sendline('0')
        p.readuntil('encrypted_flag: ')
        flag_ct = bytes.fromhex(p.recvline(False).decode())
        p.readuntil('a: ')
        flag_a_hex = p.recvline(False).decode()
        p.readuntil('b: ')
        flag_b_hex = p.recvline(False).decode()
    
    flag_a = server.unhex(flag_a_hex)
    flag_b = server.unhex(flag_b_hex)
    
    # Initial lb config
    lb_pt = flag_a
    lb_ct = flag_b

    # loop
    pt = b''
    ct_blocks = [flag_ct[i:i+16] for i in range(0, len(flag_ct), 16)]
    for ct_block in ct_blocks:
        # Fix so the different a's don't matter
        ct_block_fixed = server.xor(ct_block, server.xor(lb_pt, a_secret))
        
        lb_pt = crack_block(lb_pt, lb_ct, ct_block_fixed)
        lb_ct = ct_block
        pt += lb_pt

    print(pt)
    return


if __name__ == '__main__':
    main()