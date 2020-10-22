from PIL import Image


def pixeldata():
    # image = Image.open("./PNG.png")
    image = Image.open("./haroldv2_basic.png")
    pxldata = list(image.getdata())
    return pxldata


pxl_data = pixeldata()

for y in range(736):
    pxl_row = pxl_data[y * 500: (y+1) * 500]
    row_str = ""
    for x in range(500):
        list_test_values = []

        # test left
        if x != 0:
            left = [pxl_row[x][i]-pxl_row[x - 1][i] for i in range(3)]
            list_test_values.append(left)

        # test right
        if x != 499:
            right = [pxl_row[x][i] - pxl_row[x + 1][i] for i in range(3)]
            list_test_values.append(right)

        # test up
        if y != 0:
            up = [pxl_row[x][i] - pxl_data[(y-1) * 500][i] for i in range(3)]
            list_test_values.append(up)

        # test down
        if y != 735:
            down = [pxl_row[x][i] - pxl_data[(y + 1) * 500][i] for i in range(3)]
            list_test_values.append(down)

        canidate = False
        for test_values in list_test_values:
            for test_value in test_values:
                if test_value == -1 or test_value == 1:
                    canidate = True
                    break
            if canidate:
                break
        if canidate:
            row_str += "M"
        else:
            row_str += " "

    print(row_str)
