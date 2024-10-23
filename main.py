import numpy as np
from PIL import Image
import pyautogui
import time

def load_image(image_path):
    img = Image.open(image_path).convert("L")
    return np.array(img)


def process_image_to_bits(array):
    bit_image = []

    for row in array:
        row_bits = ""
        for pixel in row:
            row_bits += "0" if pixel >= 128 else "1"
        bit_image.append(row_bits)
    return bit_image


def draw_from_bits(bit_image, start_x, start_y, pixel_size=1, drawing_speed=0.001):
    pyautogui.PAUSE = drawing_speed

    current_y = start_y
    for row in bit_image:
        current_x = start_x
        pyautogui.moveTo(current_x, current_y)

        streak_start = 0
        for i in range(len(row)):
            if i == len(row) - 1 or row[i] != row[i + 1]:
                streak_length = i - streak_start + 1

                if row[streak_start] == "1":
                    pyautogui.mouseDown()
                    pyautogui.moveTo(
                        current_x + (streak_length * pixel_size), current_y
                    )
                    pyautogui.mouseUp()
                else:
                    pyautogui.moveTo(
                        current_x + (streak_length * pixel_size), current_y
                    )

                current_x += streak_length * pixel_size
                streak_start = i + 1

        current_y += pixel_size


def main():
    source_image = r""

    array = load_image(source_image)
    bit_image = process_image_to_bits(array)

    print("Starting in 3 seconds...")
    time.sleep(3)

    start_x, start_y = pyautogui.position()

    start_time = time.time()
    draw_from_bits(bit_image, start_x, start_y, pixel_size=1, drawing_speed=0.001)
    print(f"Drawing completed in {time.time() - start_time:.2f} seconds")

    pyautogui.mouseUp()


if __name__ == "__main__":
    main()
0
