from PIL import Image
from collections import defaultdict

def Converter(image):
    file_name = image
    im = Image.open(file_name)
    by_color = defaultdict(int)
    for pixel in im.getdata():
        by_color[pixel] += 1

    sort_orders = sorted(by_color.items(), key=lambda x: x[1], reverse=True)

    n = 0
    color_list = []
    new_color_list = []
    for i in sort_orders:
        color_list.append(i[0])
        n += 1
        if n == 10:
            break

    for color in color_list:
        color = '#%02x%02x%02x' % color
        new_color_list.append(color)

    return new_color_list
