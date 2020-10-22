from PIL import Image


def pixeldata():
    # image = Image.open("./PNG.png")
    image = Image.open("./Mission 2 test.bmp")
    pxldata = list(image.getdata())
    return pxldata


def run():
    # get pixel offsets from each other and set to pixellocations
    pxldata = pixeldata()
    lastpixel = 0
    pixellocations = []
    for i in range(len(pxldata)):
        # 1 for PNG and 255
        if pxldata[i] == 1 or pxldata[i] == 255:
            pixellocations.append(i - lastpixel)
            lastpixel = i

    # convert pixellocations to morse
    morselist = []
    for location in pixellocations:
        morselist.append(chr(location))
    morsestring = ""
    for morsechr in morselist:
        morsestring = morsestring + morsechr
    morseletters = morsestring.split(' ')

    morsealphabet = {".-" : "a",
                     "-..." : "b",
                     "-.-." : "c",
                     "-.." : "d",
                     "." : "e",
                     "..-." : "f",
                     "--." : "g",
                     "...." : "h",
                     ".." : "i",
                     ".---" : "j",
                     "-.-" : "k",
                     ".-.." : "l",
                     "--": "m",
                     "-." : "n",
                     "---" : "o",
                     ".--." : "p",
                     "--.-" : "q",
                     ".-." : "r",
                     "..." : "s",
                     "-" : "t",
                     "..-" : "u",
                     "...-" : "v",
                     ".--" : "w",
                     "-..-" : "x",
                     "-.--" : "y",
                     "--.." : "z",
                     ".----" : "1",
                     "..---" : "2",
                     "...--" : "3",
                     "....-" : "4",
                     "....." : "5",
                     "-...." : "6",
                     "--..." : "7",
                     "---.." : "8",
                     "----." : "9",
                     "-----" : "0"}

    # convert the morse to english
    convertedstring = ""
    for morseletter in morseletters:
        if not morseletter == '':
            convertedletter = morsealphabet[morseletter]
            convertedstring = convertedstring + convertedletter
    print(convertedstring)


if __name__ == '__main__':
    run()
