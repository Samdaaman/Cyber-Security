# Setup
input_file_path = "./tests/vingere.bin"
min_string_length = 1
max_string_length = 15
number_top_items = 10
# End setup


def run():
    # get the target file contents
    file_contents = get_cipher_text()
    # enumerate through the possible string lengths
    for cur_length in range(min_string_length, max_string_length + 1):
        get_common_strings_of_length(cur_length, file_contents)


def get_common_strings_of_length(str_length, file_contents):
    print("----- Length {} -----".format(str_length))
    counted_bytes_list = []
    freq_2d_list = []  # list of tuples ie [(freq, bytes)]

    for index in range(len(file_contents) + 1 - str_length):
        selected_bytes = file_contents[index : index + str_length]
        if selected_bytes not in counted_bytes_list:
            # prevent bytes from being double counted
            counted_bytes_list.append(selected_bytes)
            # build the 2d freq dictionary
            count = file_contents.count(selected_bytes)
            freq_2d_list.append((count, selected_bytes))

    freq_2d_list.sort(key=lambda pair: pair[0])
    freq_2d_list.reverse()

    print(len(freq_2d_list))
    print("{}".format(freq_2d_list))

    for top_item_index in range(number_top_items):
        tuple = freq_2d_list[top_item_index]
        print("    #{}: {}".format(top_item_index + 1, tuple))

    print("\n")
    return


def get_cipher_text():
    with open(input_file_path, 'rb') as file:
        file_contents = file.read()
    return file_contents


if __name__ == "__main__":
    run()
