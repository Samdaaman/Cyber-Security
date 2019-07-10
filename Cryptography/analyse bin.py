def trynumberAs(data):
    index = 0
    while index < len(data):
        if data[index] == "A":
            count = 1
            while data[index + count] == "A":
                count += 1
                if index + count == len(data):
                    break
            print(count)
        index += 1


with open("./tests/vingere.bin", 'r') as file:
    data = file.read()

length = 5
common_strings_unsorted = {}
for index in range(len(data) - length):
    string_to_count = ""
    for i in range(length):
        string_to_count += data[index + i]
    try:
        common_strings_unsorted[string_to_count]
    except KeyError:
        count = data.count(string_to_count)
        common_strings_unsorted[string_to_count] = count

common_strings_list = sorted(common_strings_unsorted, key=lambda k: common_strings_unsorted[k])

keysABC = [chr(i + 65) for i in range(26)]
keysabc = [chr(i + 97) for i in range(26)]
keys123 = [chr(i + 48) for i in range(10)]

keys = keysABC + keysabc + keys123

for letter in keys:
    if letter in common_strings_unsorted:
        keys.remove(letter)

for key in keys:
    print(key)

for common_string in common_strings_list:
    print("{} : {}".format(common_string, str(common_strings_unsorted[common_string])))
