while True:
    i = input("Enter string to transform:\n")
    print("CONCAT(CHAR(" + "),CHAR(".join(str(ord(c)) for c in i) + "))")
