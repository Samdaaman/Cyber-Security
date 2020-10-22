from PIL import Image


def pixeldata():
    # image = Image.open("./PNG.png")
    image = Image.open("./test-steg.png")
    pxldata = list(image.getdata())
    return pxldata


def run():
    # get pixel offsets from each other and set to pixellocations
    pxl_data = pixeldata()

    # for each row
    for i in range(120):
        pxl_row = (pxl_data[i * 220: i * 220 + 220])
        str_row = ""
        # for each list of 4 pixel values (RGBA) in the row
        for pxl_values in pxl_row:
            # isolate the alpha value
            alpha_value = pxl_values[3]
            if alpha_value == 255:
                str_row += " "
            elif alpha_value == 254:
                str_row += "$"
            else:
                print("Error")
                print("{}\n{}".format(pxl_row, pxl_values))
                return
        print(str_row)


if __name__ == '__main__':
    run()
