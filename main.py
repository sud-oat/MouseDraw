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


def draw_from_bits(bit_image, pixel_size=1):
    pyautogui.PAUSE = 0
    start_x, current_y = pyautogui.position()

    for row in bit_image:
        current_x = start_x
        pyautogui.moveTo(current_x, current_y)
        for streak, bit in row:
            current_x += streak * pixel_size
            if bit == 1:
                pyautogui.mouseDown()
                pyautogui.moveTo(current_x, current_y)
                pyautogui.mouseUp()
            else:
                pyautogui.moveTo(current_x, current_y)
        pyautogui.mouseUp()
        current_y += pixel_size


def main():
    source_image = r"image\pinguin.png"

    array = load_image(source_image)
    bit_image = process_image_to_bits(array)

    print("Starting in 3 seconds...")
    time.sleep(3)

    start_time = time.time()
    draw_from_bits(bit_image, pixel_size=1,)
    print(f"Drawing completed in {time.time() - start_time:.2f} seconds")

    pyautogui.mouseUp()


if __name__ == "__main__":
    main()
