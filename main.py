import numpy as np
from PIL import Image

def load_image(image_path):
    return np.array(Image.open(image_path).convert("L"))

print(load_image(r"image\pinguin.png"))