import numpy as np
from PIL import Image
import pyautogui  # pyautogui controls the mouse of the system
import time


# Return the image as an array
def load_image(image_path):
    img = Image.open(image_path).convert("L")
    return np.array(img)


def average_image(array):
    return int(np.mean(array))


# Sets the pixels tending towards black to black and those tending towards white to white
def process_image_to_bits(array, average):
    bit_image = []

    for row in array:
        row_bits = ""
        for pixel in row:
            row_bits += "0" if pixel >= average else "1"
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

        bit_image.append(
            row_container
        )  # Append the completed row_container to bit_image
    return bit_image


def draw_from_bits(bit_image, pixel_size, delay):
    pyautogui.PAUSE = delay
    start_x, current_y = pyautogui.position()

    for row in bit_image:
        current_x = start_x
        for streak, bit in row:
            if bit == 1:
                pyautogui.moveTo(current_x, current_y)
                current_x += streak * pixel_size
                pyautogui.mouseDown()
                pyautogui.moveTo(current_x, current_y)
                pyautogui.mouseUp()
            else:
                current_x += streak * pixel_size
        current_y += pixel_size


def main():
    source_image = r"image\images.png"
    pixel_size = 1
    delay = 0
    use_image_average = True

    image_array = load_image(source_image)

    average = average_image(image_array) if use_image_average else 128

    bit_image = process_image_to_bits(image_array, average)

    print("Starting in 3 seconds...")
    time.sleep(3)

    start_time = time.time()
    draw_from_bits(bit_image, pixel_size, delay)
    print(f"Drawing completed in {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
