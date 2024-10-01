import numpy as np
from PIL import Image

def load_image(image_path):
    return np.array(Image.open(image_path).convert("L"))

array = load_image(r"image\pinguin.png")


with open('image.txt', 'w') as file:
    for row in array:
        for pixel in row:
            divider = 255/2
            if pixel>=divider:
                file.write("1")
            else:
                file.write("0")

        file.write("\n")

