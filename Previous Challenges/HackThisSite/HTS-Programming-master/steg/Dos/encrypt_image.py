from PIL import Image
from binascii import hexlify, unhexlify
import numpy


def getdata():
    with Image.open('./no_data.png') as image:
        pxl_data = list(image.getdata())
    return pxl_data


def encrypt_hex(pxl_data, plain_hex_str, password_hex_str):
    height = 256
    width = 393
    alpha_offset = 254 - 15  # 254 is the max alpha value we can detect, and 15 is the max password_int value

    # check length
    if len(plain_hex_str) > width * 2:
        print("Error too long plain")
        return

    # pad password with 0s
    if len(password_hex_str) * 2 < len(plain_hex_str):
        password_hex_padded = password_hex_str
        while len(password_hex_padded) * 2 < len(plain_hex_str):
            password_hex_padded += "0"
    elif len(password_hex_str) * 2 == len(plain_hex_str):
        password_hex_padded = password_hex_str
    else:
        print("Error password string to long")
        return

    plain_ints = []

    # get plain ints
    for double_index in range(int(len(plain_hex_str) / 2)):
        byte_plain = unhexlify(plain_hex_str[double_index * 2: double_index * 2 + 2])
        plain_int = int.from_bytes(byte_plain, byteorder='big')
        plain_ints.append(plain_int)

    # get password ints
    password_ints = []
    for index in range(len(password_hex_padded)):
        pass_char = password_hex_padded[index]
        pass_int = int(pass_char, 16) + alpha_offset
        password_ints.append(pass_int)

    # start encryption
    enc_pxl_data = pxl_data.copy()

    for x in range(len(plain_ints)):
        coloumn_list = []
        for y in range(height):
            pxl_values = list(pxl_data[x + y * width])
            coloumn_list.append(pxl_values)
        plain_int = plain_ints[x]
        coloumn_list[plain_int][3] = password_ints[x]

        for y in range(height):
            enc_pxl_data[x + y * width] = coloumn_list[y]

    enc_array = numpy.zeros([height, width, 4], dtype=numpy.uint8)
    for y in range(height):
        row = enc_pxl_data[y * width: (y+1) * width]
        for x in range(width):
            pxl_values = row[x]
            pxl_values_array = numpy.array(pxl_values)
            enc_array[y, x] = pxl_values_array.copy()

    return enc_array


def save(pxl_data, filename):
    image = Image.fromarray(pxl_data, mode='RGBA')
    image.save(filename)


hex_plain = '504B03040A000900000067ACAE4E7396B406370000002B00000008000000666C61672E747874BAA5001A8A517DA3689DEC1874BD3E3922DB7C9100FB6C3DD82667CB1FE754BE161FCF7A80E7CB8FB777F2E55415CB72A0361168752575504B07087396B406370000002B000000504B03040A0009000000C8BCAE4EF6786200160000000A0000000B00000070616464696E672E7478747B7C34E00715FDA8DA700FA803420B6FF8874F08358A504B0708F6786200160000000A000000504B01021F000A000900000067ACAE4E7396B406370000002B000000080024000000000000002000000000000000666C61672E7478740A0020000000000001001800A9ACE755380AD501E8DFC3E2350AD501E8DFC3E2350AD501504B01021F000A0009000000C8BCAE4EF6786200160000000A0000000B002400000000000000200000006D00000070616464696E672E7478740A00200000000000010018002E639085490AD5012B736E5E380AD5012B736E5E380AD501504B05060000000002000200B7000000BC0000000000'
old_pxl_data = getdata()
new_pxl_data = encrypt_hex(old_pxl_data, hex_plain, "1ACD4E060CD91EF7121487F3F9C6BEE6")
save(new_pxl_data, './test.png')
