import numpy as np
from PIL import Image
import pyautogui #pyautogui controls the mouse of the system
import time

#Return the image as an array
def load_image(image_path):
    img = Image.open(image_path).convert("L")
    return np.array(img)

#Sets the pixels tending towards black to black and those tending towards white to white
def process_image_to_bits(array):
    bit_image = []

    for row in array:
        row_bits = ""
        for pixel in row:
            row_bits += "0" if pixel >= 128 else "1"
        streak_start = 0
        row_container = []  # Initialize row_container for each row

        for i in range(len(row_bits)):
            if i == len(row_bits) - 1 or row_bits[i] != row_bits[i + 1]:
                streak_length = i - streak_start + 1
                if row_bits[streak_start] == "1": 
                    container = [streak_length, 1]
                else:
                    container = [streak_length, 0]
                row_container.append(container)  # Append the container to row_container
                streak_start = i + 1
        
        bit_image.append(row_container)  # Append the completed row_container to bit_image
    return bit_image


def draw_from_bits(bit_image, pixel_size=1, drawing_speed=0.001):
    pyautogui.PAUSE = drawing_speed
    current_x, current_y = pyautogui.position
    pyautogui.move(current_x,current_y)

    for row in bit_image:
        for streak, bit in row:
            #logic goes here
        current_y += pixel_size


def main():
    source_image = r"image/m.png"

    array = load_image(source_image)
    bit_image = process_image_to_bits(array)

    print("Starting in 3 seconds...")
    time.sleep(3)

    start_time = time.time()
    draw_from_bits(bit_image, pixel_size=0.5, drawing_speed=0.001)
    print(f"Drawing completed in {time.time() - start_time:.2f} seconds")

    pyautogui.mouseUp()


if __name__ == "__main__":
    main()
0
