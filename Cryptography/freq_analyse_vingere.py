## Setup
input_file_path = "test2.txt"
key_length = 1
known_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# known_chars = ''
## End setup

# initialise the summary list
summary_list = ["\nSummary:"]


def run():
    # get cipher text
    cipher_text = get_cipher_text()
    # split the cipher text into key_length number of parts
    cipher_text_list_of_split_lists = []
    for i in range(key_length):
        cipher_text_list_of_split_lists.append(split_cipher_text(i, cipher_text))
    # for each part that is split run frequency analysis on it
    for i in range(len(cipher_text_list_of_split_lists)):
        # configure summary
        summary_list.append("Offset {}".format(i))
        # run frequency analysis
        split_cipher_list = cipher_text_list_of_split_lists[i]
        freq_analyse(split_cipher_list)
    # print summary
    for row in summary_list:
        print(row)
    # Done
    print("Done")


def split_cipher_text(index, cipher_text):
    cipher_bytes_list = []
    for i in range(len(cipher_text)):
        cipher_byte_int = cipher_text[i]
        cipher_byte = chr(cipher_byte_int)
        if i % key_length == index:
            cipher_bytes_list.append(cipher_byte)
    return cipher_bytes_list


def get_cipher_text():
    with open(input_file_path, 'rb') as cipher_text_file:
        cipher_text = cipher_text_file.read()
    return cipher_text


def freq_analyse(cipher_list):
    # build freq_dict where the keys is ord(cipher_byte)
    # and the value is the count of cipher byte in text
    freq_dict = {}
    for cipher_byte in cipher_list:
        dict_key = ord(cipher_byte)
        # if the byte hasn't been counted, count it
        if dict_key not in freq_dict:
            count_of_byte = cipher_list.count(cipher_byte)
            freq_dict[dict_key] = count_of_byte
    # sort frequency dict
    sorted_freq_list_of_lists = sorted(freq_dict.items(), key=lambda x: x[1])
    sorted_freq_dict = {sorted_freq_list_of_lists[i][0] : sorted_freq_list_of_lists[i][1] for i in range(len(sorted_freq_list_of_lists))}

    # graph bar chart
    # get scale factor
    scale_factor = len(cipher_list)
    # counter to get the top three
    num_to_go = len(freq_dict)
    # for loop to iterate over dictionary
    for key in sorted_freq_dict:
        num_to_go -= 1
        byte_string = chr(key)
        if byte_string not in known_chars:
            byte_string = hex(key)
        # pad the byte name so it's nice
        while len(byte_string) < 5:
            byte_string += " "
        # get number of blocks
        byte_freq = sorted_freq_dict[key]
        num_blocks = round(100 * byte_freq / scale_factor)
        bar = "|"
        for i in range(num_blocks):
            bar += "█"
        # print a row of the barchart
        row = "{} {} {}".format(byte_string, bar, str(byte_freq))
        print(row)
        # if its one of the top 3, add to summary
        if num_to_go < 3:
            summary_list.append(row)


if __name__ == "__main__":
    run()
