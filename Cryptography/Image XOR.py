from PIL import Image


def open_image(path):
    image = Image.open(path)
    pxl_data = list(image.getdata())
    return pxl_data


def save_image(pxl_data, width, height):
    image = Image.new('RGB', (width, height))
    image.putdata(pxl_data)
    image.show()


img1 = open_image("tests/c8a.png")
img2 = open_image("tests/c8b.png")
print(img1)
print(img2)

img3 = []
for i in range(len(img1)):
    pxl_list1 = img1[i]
    pxl_list2 = img2[i]
    pxl_tuple3 = ()
    for j in range(3):
        pxl_value1 = pxl_list1[j]
        pxl_value2 = pxl_list2[j]
        pxl_value3 = pxl_value1 ^ pxl_value2
        pxl_tuple3 = pxl_tuple3 + (pxl_value3, )
    img3.append(pxl_tuple3)
save_image(img3, 144, 103)
