import numpy as np
from PIL import Image

def load_image(image_path):
    img = Image.open(image_path).convert("L")
    width, height = img.size
    return np.array(img), width, height

array, width, height = load_image(r"image\m.png")
bit_image = [[None for x in range(width)] for y in range(height)] 

with open('image.txt', 'w') as file:
    for row_counter, row in enumerate(array):
        for pixel_counter, pixel in enumerate(row):
            if pixel>=128:
                bit_image[row_counter][pixel_counter] = 0
            else:
                bit_image[row_counter][pixel_counter] = 1

for row in bit_image:
    print(row)