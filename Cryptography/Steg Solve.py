from PIL import Image
# Make sure that pillow is installed
# Setup
img_path = 'tests/test.png'
out_path = 'tests/steg solve/'
# End Setup


def get_image(path):
    image = Image.open(path)
    return image


def save_image(image, path):
    image.save(path)
    # image.show()


def get_plane(img, channel_index, plane_number):
    width = img.width
    height = img.height
    # get the pixel data
    pxl_data = img.load()
    # get the plane
    print('Getting Plane {}'.format(plane_number))
    new_img = Image.new('1', [width, height])
    new_img_pxl_values = new_img.load()
    # go over each pixel in the image
    for x in range(width):
        for y in range(height):
            pixel_value_colour = pxl_data[x, y]
            pixel_value_channel = pixel_value_colour[channel_index]
            pixel_value_channel_bin = bin(pixel_value_channel)[2:].zfill(8)
            pixel_value_plane = pixel_value_channel_bin[7 - plane_number]
            new_img_pxl_values[x, y] = 255 * int(pixel_value_plane),
    # save the image
    save_image(new_img, out_path + '{}_{}.png'.format(img.mode[channel_index], plane_number))


def get_overall_channel(img, channel_index):
    width = img.width
    height = img.height
    # get the pixel data
    pxl_data = img.load()
    new_img = Image.new('L', [width, height])
    new_img_pxl_values = new_img.load()
    # go over each pixel
    for x in range(width):
        for y in range(height):
            pixel_value_colour = pxl_data[x, y]
            pixel_value_channel = pixel_value_colour[channel_index]
            new_img_pxl_values[x, y] = int(pixel_value_channel)
    # save the image
    save_image(new_img, out_path + '{}_Overall.png'.format(img.mode[channel_index]))


# open the image
img_orig = get_image(img_path)

# perform steg on each channel
for cur_channel in img_orig.mode:
    print('\nChannel: {}'.format(cur_channel))
    cur_channel_index = img_orig.mode.index(cur_channel)
    # for each plane on a certain channel
    for cur_plane_number in range(8):
        get_plane(img_orig, cur_channel_index, cur_plane_number)
    # get the overall channel image
    print('Getting Overall Channel for: {}'.format(cur_channel))
    get_overall_channel(img_orig, cur_channel_index)
