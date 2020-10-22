import itertools


# generate serials took too long
def generate_serials():
    for i in range(36 ^ 9):
        generate_nth_serial(i)


# generate nth serial ran out of memory
def generate_nth_serial(n):
    # define character range
    chr_range = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    chr_range_list = []
    for char in chr_range:
        chr_range_list.append(char)

    # serial number consists of 9 characters
    nine_list = list(itertools.product(chr_range_list, repeat=9))
    nine = nine_list[n]

    nine_string = ""
    for i in range(3):
        for j in range(3):
            nine_string = nine[i * 3 + j]
        nine_string = nine_string + "-"

    serial = nine_string + "1.1\n"

    return serial


def run():
    print("hello")


if __name__ == '__main__':
    run()
