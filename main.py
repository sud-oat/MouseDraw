import numpy as np
from PIL import Image

def load_image(image_path):
    return np.array(Image.open(image_path).convert("L"))

array = load_image(r"image\pinguin.png")


with open('image.txt', 'w') as file:
    for row in array:
        for pixel in row:
            print("Lol")

        file.write("\n")

