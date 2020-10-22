import LoginToHTS


def get_string():
    content = LoginToHTS.login_and_get("https://www.hackthissite.org/missions/prog/12/")
    content_list = content.split("<b>")

    string_untrimmed = ""
    for i in range(len(content_list)):
        if "String: </b>" in content_list[i]:
            string_untrimmed = content_list[i]
            break

    string_trimmed = string_untrimmed[38:].split("\"")[0]
    return string_trimmed


def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return 1
    if num == 1 or num == 0:
        return 0
    return 2


def calc_answer(string):
    ints = []
    chars = []
    for char in string:
        try:
            test_int = int(char)
            ints.append(test_int)
        except ValueError:
            chars.append(char)

    primes = []
    compps = []
    for test_int in ints:
        if is_prime(test_int) == 1:
            primes.append(test_int)
        elif is_prime(test_int) == 2:
            compps.append(test_int)

    compps_tot = 0
    for compp in compps:
        compps_tot += compp

    primes_tot = 0
    for prime in primes:
        primes_tot += prime

    times_result = compps_tot * primes_tot

    shifted = ""
    for letter in chars:
        shifted = shifted + chr(ord(letter) + 1)

    return shifted[:25] + str(times_result)


def run():
    string_test = get_string()
    print(string_test)
    answer = calc_answer(string_test)
    print(answer)
    repsonse = LoginToHTS.post_data_with_headers('https://www.hackthissite.org/missions/prog/12/index.php', {'solution': answer, 'submitbutton': 'Submit (remaining time: 3 seconds)'}, {'Referer': 'https://www.hackthissite.org/missions/prog/12/'})
    print(repsonse.content.decode("utf-8"))
    print("Done")


if __name__ == "__main__":
    run()