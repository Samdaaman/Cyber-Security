import zipfile
import math

passwords = []


def gen_passwords(max_length, all_lengths):
    global passwords
    keysABC = [chr(i + 65) for i in range(26)]
    keysabc = [chr(i + 97) for i in range(26)]
    keys123 = [chr(i + 48) for i in range(10)]
    keyshexletters = [chr(i + 65) for i in range(6)]

    key_list = keys123 + keysABC + keysabc
    key_list_length = len(key_list)

    # for length in range(max_length):
    #     passwords += step(length, key_list)

    if (max_length >= 1 and all_lengths) or max_length == 1:
        for key1 in key_list:
            passwords.append(key1)

    if (max_length >= 2 and all_lengths) or max_length == 2:
        for key1 in key_list:
            for key2 in key_list:
                passwords.append(key1 + key2)

    if (max_length >= 3 and all_lengths) or max_length == 3:
        for key1 in key_list:
            for key2 in key_list:
                for key3 in key_list:
                    passwords.append(key1 + key2 + key3)

    if (max_length >= 4 and all_lengths) or max_length == 4:
        for key1 in key_list:
            for key2 in key_list:
                for key3 in key_list:
                    for key4 in key_list:
                        passwords.append(key1 + key2 + key3 + key4)

    if (max_length >= 5 and all_lengths) or max_length == 5:
        for key1 in key_list:
            for key2 in key_list:
                for key3 in key_list:
                    for key4 in key_list:
                        for key5 in key_list:
                            passwords.append(key1 + key2 + key3 + key4 + key5)

    if (max_length >= 6 and all_lengths) or max_length == 6:
        for key1 in key_list:
            for key2 in key_list:
                for key3 in key_list:
                    for key4 in key_list:
                        for key5 in key_list:
                            for key6 in key_list:
                                passwords.append(key1 + key2 + key3 + key4 + key5 + key6)

    if (max_length >= 7 and all_lengths) or max_length == 7:
        for key1 in key_list:
            for key2 in key_list:
                for key3 in key_list:
                    for key4 in key_list:
                        for key5 in key_list:
                            for key6 in key_list:
                                for key7 in key_list:
                                    passwords.append(key1 + key2 + key3 + key4 + key5 + key6 + key7)


def step(index, key_list):
    step_passwords = []
    for key in key_list:
        if index == 0:
            step_passwords.append(key)
        else:
            for i in range(len(key_list) ** index):
                step_passwords.append(key + step(index - 1, key_list)[i])
    return step_passwords


def get_test_pass(n):
    return passwords[n]


def crack(zip_file):
    for i in range(len(passwords)):
        trydecypt(zip_file, get_test_pass(i))
    print("Done Cracking")


def trydecypt(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode("utf-8"))
        print("Sucess password is {}".format(password))
    except:
        pass


def run():
    print("Generating Passwords")
    gen_passwords(4, True)
    print("Done Generating Passwords")
    zip_file = zipfile.ZipFile('./steg/inner.zip')
    crack(zip_file)


if __name__ == "__main__":
    run()