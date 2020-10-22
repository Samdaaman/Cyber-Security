import requests


def get_crack_and_send():
    # setup cookie and username
    phpsid = input("Enter PHPSID: ")
    cookie = {'PHPSESSID': phpsid}
    username = "5amthehacker"

    print("Getting Text from HTS")
    urllevel = 'https://www.hackthissite.org/missions/prog/11/'
    urlsubmit = urllevel + 'index.php'

    with requests.Session() as session:

        response = session.get(urllevel, cookies=cookie)

        content = bytes(response.content).decode("utf-8")

        # check if login was sucessful
        if username in content:
            print("Login Sucessful")

        else:
            print("Login Unsucessful")
            print(content)
            return

        print("Got data")

        content_list = content.split("/>")
        cipher_untrimmed = ""
        shift_untrimmed = ""
        for item in content_list:
            if "Generated String:" in item:
                cipher_untrimmed = item
            if "Shift:" in item:
                shift_untrimmed = item

        cipher = cipher_untrimmed[:len(cipher_untrimmed) - 4]
        shift = shift_untrimmed[:len(shift_untrimmed) - 4]

        print(cipher)
        print(shift)
        print("Decrypting")

        plain = process_and_crack([cipher, shift])
        print(plain)

        print("Sending")
        response_submit = session.post(urlsubmit, data={"solution": plain}, cookies=cookie, headers={'referer': urllevel})

        print(response_submit.content.decode("utf-8"))




def process_and_crack(cipher_list):
    untrimmmed_cipher_text = cipher_list[0]
    cipher_text = untrimmmed_cipher_text.replace("Generated String: ", "")

    # calculate the character to split the string with
    split_character = ""
    for char in cipher_text:
        try:
            int(char)
        except ValueError:
            split_character = char
            break

    cipher_ints = []
    for cipher_int in cipher_text.split(split_character):
        if cipher_int != '':
            cipher_ints.append(int(cipher_int))
    
    shift_text = cipher_list[1].replace("Shift: ", "")
    shift_int = int(shift_text)
    
    return crack(cipher_ints, shift_int)


def crack(cipher_ints, shift):

    plain_ints = []
    for cipher_int in cipher_ints:
        plain_int = cipher_int - shift
        plain_ints.append(plain_int)

    # get the plain text from the plain ints
    plain_text = ""
    for plain_int in plain_ints:
        plain_text = plain_text + chr(plain_int)

    return plain_text


def run():
    # # text for testing
    # test_list = ["Generated String: 45/57/42/92/67/40/54/48/49/54/", "Shift: 4"]
    # # test cracking algorithm
    # test_plain = process_and_crack(test_list)
    # print(test_plain)

    print("Starting")
    get_crack_and_send()
    print("Done")


if __name__ == '__main__':
    run()