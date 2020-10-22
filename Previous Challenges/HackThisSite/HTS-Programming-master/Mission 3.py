import hashlib
from binascii import hexlify, unhexlify
import itertools


def getmd5(string):
    return hashlib.md5(string.encode("utf-8")).hexdigest()


def evalcrosstotal(strmd5):
    inttotal = 0
    arrmd5chars = []
    for md5char in strmd5:
        arrmd5chars.append(md5char)
    for value in arrmd5chars:
        addon = int(value, 16)
        inttotal += addon
    return inttotal


# test serial 99Z-KH5-OEM-240-1.1\n
def encryptstring(string, password):
    passwordmd5hex = getmd5(password)
    intmd5total = evalcrosstotal(passwordmd5hex)

    encrypted_values = []
    strlength = len(string)

    for i in range(strlength):
        int1 = ord(string[i:i+1])
        int2 = int(passwordmd5hex[i % 32:(i % 32)+1], 16)
        int3 = intmd5total
        encrypted_values.append(ord(string[i:i+1]) + int(passwordmd5hex[i % 32:(i % 32)+1], 16) - intmd5total)
        intmd5total = evalcrosstotal(getmd5(string[:i+1])[:16] + getmd5(intmd5total.__str__())[:16])

    cipher_text = ""
    for encrypted_value in encrypted_values:
        cipher_text = cipher_text + " " + encrypted_value.__str__()

    return cipher_text[1:]


def get_cipherchars(cipher_text):
    cipher_chars = [char for char in cipher_text.split(" ")]
    return cipher_chars


def known_values(index):
    remainder = index % 20
    if remainder == 3 or remainder == 7 or remainder == 11 or remainder == 15:
        return "-"
    if remainder == 16 or remainder == 18:
        return "1"
    if remainder == 17:
        return "."
    if remainder == 8:
        return "O"
    if remainder == 9:
        return "E"
    if remainder == 10:
        return "M"
    if remainder == 19:
        return "\n"
    return ""


def crackold(cipher_text):
    cipher_chars = get_cipherchars(cipher_text)
    cipher_ints = [int(cipher_char) for cipher_char in cipher_chars]
    for starting_md5_total in range(480):
        for password0 in range(16):
            plain0 = get_possible_plain_char(password0, cipher_ints[0], starting_md5_total, 0)
            if plain0:
                int_md5_total1 = evalcrosstotal(getmd5(plain0)[:16] + getmd5(starting_md5_total.__str__())[:16])
                for password1 in range(16):
                    plain1 = get_possible_plain_char(password1, cipher_ints[1], int_md5_total1, 1)
                    if plain1:
                        int_md5_total2 = evalcrosstotal((getmd5(plain0 + plain1))[:16] + getmd5(int_md5_total1.__str__())[:16])
                        for password2 in range(16):
                            plain2 = get_possible_plain_char(password2, cipher_ints[2], int_md5_total2, 2)
                            if plain2:
                                int_md5_total3 = evalcrosstotal((getmd5(plain0 + plain1 + plain2))[:16] + getmd5(int_md5_total2.__str__())[:16])
                                for password3 in range(16):
                                    plain3 = get_possible_plain_char(password3, cipher_ints[3], int_md5_total3, 3)
                                    if plain3 != known_values(3):
                                        continue
                                    else:
                                        print(plain0 + plain1 + plain2 + plain3)


def crack(cipher_text):
    cipher_chars = get_cipherchars(cipher_text)
    cipher_ints = [int(cipher_char) for cipher_char in cipher_chars]
    plain_chars = []
    password_hex_ints = []
    md5_total_ints = []

    # for each possible starting md5total value
    for test_starting_md5_total in range(480):
        # make lists of 100
        md5_total_ints = [0 for i in range(100)]
        plain_chars = ["" for i in range(100)]

        # -1 represents unset and password list is only 32 long
        password_hex_ints = [-1 for i in range(32)]

        # set the starting md5total
        md5_total_ints[0] = test_starting_md5_total

        # start the brute force
        brute_step_setup(plain_chars, 0, password_hex_ints, cipher_ints, md5_total_ints)


def brute_step_setup(plain_chars, char_index, password_hex_ints, cipher_ints, md5_total_ints):
    # only go 100 layers deep in the dream
    if char_index == 100:
        plain_text = ""
        for char in plain_chars:
            plain_text = plain_text + char
        print(plain_text)
        return

    # check if hex password char has already be bruteforced and if it has don't re bruteforce it
    if password_hex_ints[char_index % 32] == -1:
        for test_password_hex_int in range(16):
            brute_step(plain_chars, char_index, password_hex_ints, cipher_ints, md5_total_ints, test_password_hex_int)
    else:
        brute_step(plain_chars, char_index, password_hex_ints, cipher_ints, md5_total_ints, password_hex_ints[char_index % 32])


def brute_step(plain_chars, char_index, password_hex_ints, cipher_ints, md5_total_ints, password_hex_int):
    password_hex_ints[char_index % 32] = password_hex_int
    test_plain_char = get_possible_plain_char(password_hex_int, cipher_ints[char_index], md5_total_ints[char_index], char_index)
    if test_plain_char:
        # we are in bois
        plain_chars[char_index] = test_plain_char

        # get current plain text
        current_plain = ""
        for plain_char in plain_chars:
            current_plain = current_plain + plain_char

        # disregard/clear past attmepts
        current_plain = current_plain[:char_index + 1]
        for index in range(32 - (char_index + 1)):
            password_hex_ints[index + char_index + 1] = -1

        # set next intmd5total if not at the end
        if char_index < 99:
            md5_total_ints[char_index + 1] = evalcrosstotal(getmd5(current_plain)[:16] + getmd5(md5_total_ints[char_index].__str__())[:16])

        # go one layer deeper
        brute_step_setup(plain_chars, char_index + 1, password_hex_ints, cipher_ints, md5_total_ints)


def get_possible_plain_char(nth_password_int, cipherint, intmd5total, index):
    test_char_int = cipherint - nth_password_int + intmd5total
    # 49 = "1", 45 = "-", 46 = ".", 65-90 = "A-Z", 48-57 = "0-9"
    if 0 <= test_char_int <= 127:
        # test if its a know value
        if known_values(index):
            if known_values(index) == chr(test_char_int):
                return chr(test_char_int)
        else:
            if 65 <= test_char_int <= 90 or 48 <= test_char_int <= 57:
                return chr(test_char_int)
    return ""


def run():
    # # test result -146 -208 -188 -215 (ABC-, abc)
    # print(encryptstring("ABC-ABC-OEM-230-1.1\n", "abc"))

    test_cipher_text = "-207 -131 -167 -171 -179 -144 -113 -151 -143 -168 -89 -216 -169 -200 -113 -152 -240 -158 -216 -192 -163 -163 -170 -193 -152 -136 -142 -152 -162 -138 -144 -197 -170 -137 -142 -174 -119 -202 -190 -220 -159 -109 -140 -166 -167 -155 -175 -176 -191 -162 -151 -239 -85 -153 -181 -213 -156 -222 -184 -215 -195 -207 -169 -195 -157 -142 -186 -155 -157 -158 -113 -232 -146 -140 -145 -218 -152 -161 -170 -238 -139 -162 -176 -172 -139 -71 -163 -184 -132 -155 -109 -172 -139 -158 -147 -199 -137 -240 -171 -233"
    # print(get_cipherchars(test_cipher_text))

    print("\n\nStarting Crack:\n")
    crack(test_cipher_text)
    print("done")


if __name__ == '__main__':
    run()
