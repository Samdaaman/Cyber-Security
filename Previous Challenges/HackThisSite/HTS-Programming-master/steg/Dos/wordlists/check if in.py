max_to_read = 10 ** 2
offset = 10 ** 7

md5s_list = []
with open('md5s.txt', errors='ignore') as md5s_file:
    md5s_file.seek(offset)
    for i in range(max_to_read):
        md5s_list.append(md5s_file.readline().strip('\n'))

with open('rockyou.txt', mode='r', errors='ignore') as rockyou_file:
    rockyou_list = rockyou_file.readlines()

print("Opened fils")
for index in range(max_to_read):
    md5 = md5s_list[index]
    # print(md5)
    # if not md5:
    #     continue
    # if md5[0] != "s":
    #     continue
    if md5 not in rockyou_list:
        print("\"{}\" not in rockyou".format(md5))
