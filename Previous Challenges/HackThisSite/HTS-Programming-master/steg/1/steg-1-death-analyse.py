import base64
from binascii import hexlify


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


with open("./death.txt", 'r') as file:
    data = file.read()

data = "UEsDBBQAAgAIABqjrE40rAkTaAMAANUDAAAIABwAZ29vZGx1Y2tVVAkAA6Me2FwdH9hcdXgLAAEE6AMAAAToAwAA8/dmZhFhYGDgYGBdtMbvPGN/RwUjA8NyJgYGbgYZhpLM3NTwxKICvYLK0BBOBuZZMjdilgJxaQU3AyPLC2YGBjDRG+jrzWwoYGu+X2nddJbpW67tYk/kr1No4mhyFzxptvnuhbsqKUHef7+eu3VXa1ECn3OaUf692dMfL37J9njLpjyud73tsVl7krdx26nFZbYkGabJHY/eJLvB6lef/mM9lf1dVibWV19891MPfflUao6jXYn0iq/LfNc7/81P6Ni2+eS+g4y3MnIY/jcHZAevDgic0//g+Orfs2//vHv46Vd95qwOvks3qn7PNDzW5HbnV0bFSUPXxFihv5tW8Tv5dc+cwnXnkvQpiVdmgcnPAnMXlR0rf7RlgqSyYMi/ReK7Yn9mBF+e+rv1yuW7T//sETDKP7g2KHje2c91ETfb76h1WEW+32Az96u6/BztegvNJSnZNwSv/1vs4dq9q+36qggepepwHpcij57Vgh25njzfGeecyLrtpLbTLS5+gyd7RxWryaYwwS2Za5lFPlV+W3SCXzrjtef+O/cMHN+EKKy7F2Uwf4Oi8GGNquXxRZ3yu248kbYN3Twn/fbkvWwKvMIB0UXcRxgVb7L7wyOPGxh5e68/vqAFjLwUIGYGRl5qXjI40pYBI2wbZqSJHrw7zcmBgeGB+iuZ/08XcRtFHElxKb0smaZ2aJaHsP/+9P3vE/9u1j4a92uxmUalw3w/i/Ibr9YFXxNJWcv+4ITkrskdX+9YCBl+f/ZBpuRmb/xHm0CukBI/L4mCWedyjr59Fz0pbmGCUdFEz30PXyx/YKNfNzkzK2rH37Pvd7yvZW9ueSB1baPonrMa8QvDOG6qLHlgc2cW2yNTIeXa3w7ar1Os3SeaCN7SXDvZ+X+W/x8xcxnrb2L935ZNn+d++eXMxJL9a5Mu+c80OCL3PfWPmLhbC7ex4MM78To6R643C0mZbr248dfFjdvTtvIsb9p0u1pG68YqxUrVrLaX/c/l2Co6fxxcWZ6pevR29+Wq5bFdTZE7V5hOn7m60enrdc4d69gjomzmnVx2Nrbj3YqVJm8rOo7U/WcP8GZkkmPGlUskGEAAyGX42whioeQZVkieQQt6ZAMxYw5h4JbGvUAKHI+skHjEMIiVDaSYCQhnAWkVZhCPCwBQSwMECgACAAAALaSsTsPKAqcXAAAAFwAAAAQAHABsaW5rVVQJAAOlINhc7CDYXHV4CwABBOgDAAAE6AMAAGh0dHBzOi8vYml0Lmx5LzJ2VXB3TkQKUEsBAh4DFAACAAgAGqOsTjSsCRNoAwAA1QMAAAgAGAAAAAAAAAAAALSBAAAAAGdvb2RsdWNrVVQFAAOjHthcdXgLAAEE6AMAAAToAwAAUEsBAh4DCgACAAAALaSsTsPKAqcXAAAAFwAAAAQAGAAAAAAAAQAAALSBqgMAAGxpbmtVVAUAA6Ug2Fx1eAsAAQToAwAABOgDAABQSwUGAAAAAAIAAgCYAAAA/wMAAAAA"
print(hexlify(base64.b64decode(data)))
length = 1
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
