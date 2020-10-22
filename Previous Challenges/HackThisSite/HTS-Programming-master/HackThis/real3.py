test = ""
tes1 = "http://www.######.com"
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghij"



def crack_shifts(test, tes1):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghij"
    shifts = ""
    for i in range(len(test)):
        plain_chr = test[i]
        cipher_chr = tes1[i]
        if plain_chr in alpha:
            if cipher_chr != "#":
                shifts += str(alpha.index(plain_chr) - alpha.index(cipher_chr))
            else:
                shifts += "?"
        else:
            shifts += plain_chr

    print(shifts)


def crack_cipher(test, shift_list):
    plain = ""
    cnt = 0
    for i in range(len(test)):
        cipher_chr = test[i]
        if cipher_chr in alpha:
            shift = shift_list[cnt % len(shift_list)]
            plain += alpha[alpha.index(cipher_chr) - shift]
            cnt += 1
        else:
            plain += cipher_chr
    print(plain)


print("")

crack_shifts("/oiAguA/ykdp/8?rF=xhyvAttm", "/levels/real/3############")
crack_shifts("kxyr://FED.mrslnn.kvs", "http://www.######.com")
crack_shifts("/ohCeux/rlho/6?ww=wjwzohhw", "/levels/real/3############")

print("")

crack_cipher("/oiAguA/ykdp/8?rF=xhyvAttm", [3, 4, 5, 2, 9, 8, 7, 6])
crack_cipher("kxyr://FED.mrslnn.kvs", [3, 4, 5, 2, 9, 8, 7, 6])
crack_cipher("/ohCeux/rlho/6?ww=wjwzohhw", [3, 3, 7, 0, 9, 5, 0, 7, 7])
