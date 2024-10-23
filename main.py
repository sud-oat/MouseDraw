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
        print(row_bits)
    return bit_image


def draw_from_bits(bit_image, start_x, start_y, pixel_size=1, drawing_speed=0.001):
    pyautogui.PAUSE = drawing_speed #Amount of time between each action

    current_y = start_y

    for row in bit_image:
        current_x = start_x
        pyautogui.moveTo(current_x, current_y) #Move cursor to where we set the position of cursor

        streak_start = 0
        for i in range(len(row)):
            if i == len(row) - 1 or row[i] != row[i + 1]: #Check if the index value is the last value or if there is a difference in colour between current position and next
                streak_length = i - streak_start + 1

                if row[streak_start] == "1": #Calculates the length the image needs to draw and draws that length
                    pyautogui.mouseDown()
                    pyautogui.moveTo(
                        current_x + (streak_length * pixel_size), current_y
                    )
                    pyautogui.mouseUp()
                else: #Moves the cursor without drawing anything
                    pyautogui.moveTo(
                        current_x + (streak_length * pixel_size), current_y
                    )

                current_x += streak_length * pixel_size #Changes x coordinate to next line
                streak_start = i + 1

        current_y += pixel_size #Changes y coordinate to next line


def main():
    source_image = r"image/m.png"

    array = load_image(source_image)
    bit_image = process_image_to_bits(array)

    print("Starting in 3 seconds...")
    time.sleep(3)

    start_x, start_y = pyautogui.position() #set starting position to that of our cursor

    start_time = time.time()
    # draw_from_bits(bit_image, start_x, start_y, pixel_size=0.5, drawing_speed=0.001)
    print(f"Drawing completed in {time.time() - start_time:.2f} seconds")

    pyautogui.mouseUp()


if __name__ == "__main__":
    main()
0
