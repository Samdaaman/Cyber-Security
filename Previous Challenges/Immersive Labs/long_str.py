long_str = '0'
try:
    while True:
        long_str += f'-{len(long_str)}'
        print(len(long_str))
        if len(long_str) > 1000000:
            raise Exception()
except:
    with open('out.txt', 'w') as fh:
        fh.writelines([long_str])