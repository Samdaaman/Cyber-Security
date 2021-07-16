from try_flag import names

for name in names:
    # print(f'steghide extract -sf steg2.bmp -p "{name}"')
    print(f'java -jar ./openstego.jar extract -sf challenge.png -p "{name}"')