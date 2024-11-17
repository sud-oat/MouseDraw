import numpy as np
from PIL import Image
import pyautogui
import time

def load_image(image_path):
    return np.array(Image.open(image_path).convert("L"))

def get_streaks(row, threshold):
    binary = (row < threshold).astype(int)
    change_points = np.where(np.diff(binary))[0]
    
    streaks = []
    start = 0
    current_val = binary[0]
    
    for point in change_points:
        streaks.append([point - start + 1, current_val])
        start = point + 1
        current_val = 1 - current_val
    
    streaks.append([len(binary) - start, current_val])
    return streaks

def process_image_to_bits(array, threshold):
    return [get_streaks(row, threshold) for row in array]

def draw_from_bits(bit_image, pixel_size, delay):
    pyautogui.PAUSE = delay
    start_x, current_y = pyautogui.position()
    
    for row in bit_image:
        current_x = start_x
        for streak, bit in row:
            if bit:
                pyautogui.moveTo(current_x, current_y)
                pyautogui.dragTo(current_x + streak * pixel_size, current_y, duration=0)
            current_x += streak * pixel_size
        current_y += pixel_size

def main():
    source_image = r"image\pinguin.png"
    pixel_size = 1
    delay = 0
    image_average = True

    start_processing_time = time.time()
    
    image_array = load_image(source_image)
    threshold = np.mean(image_array) if image_average else 128
    print(threshold)
    
    bit_image = process_image_to_bits(image_array, threshold)

    end_processing_time = time.time()

    
    print("starting in 3...")
    time.sleep(3)
    
    start_time = time.time()
    draw_from_bits(bit_image, pixel_size, delay)
    print(f"Drawing image completed in {time.time() - start_time:.2f} seconds, with a processing time of {end_processing_time-start_processing_time:.2f}")

if __name__ == "__main__":
    main()