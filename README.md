# MouseDraw

### INSTALLATION:

Clone the repository
```
git clone https://github.com/CarlDragon5068/MouseDraw
cd MouseDraw
```

### INSTALL REQUIREMENTS:

```
pip install pyautogui numpy pillow
```

### USAGE:

Put the local path of the image you want to recreate in `source_image` variable in the form of a png or jpg file. You can modify:
- `pixel_size` (this is the size of the image relative to its dimensions. `1` means one to one, `2` means twice the size, `0.5` is half size, etc.)
- `delay` (leave this on zero unless the speed is too fast, otherwise, the higher it is, the slower the program will draw)
- `image_average` (to control whether the program considers the darkness of the image or just whether it uses `128`[the median for brightness]. It's recommended to check out both versions, as it usually depends on your preference in aesthetics)

In the function `main()`, open paint, select the pencil tool, run the program, and place your cursor on the top left side of the image in paint.

### WARNING

This script is **VERY simple and crude**. It does **NOT** have any built-in failsafe apart from the `pyautogui` check if the mouse is on the edges. If the program exceeds the limits of the paint screen, it **WILL** start clicking on your taskbar. **IT DOES NOT CARE**. Be **VERY careful** that this does not happen. It may take up to a minute to draw your image. Be very careful that your cursor is actually in paint and not on anything else, as the program does not check for that.

### HOW IT WORKS:

The program processes an image by converting it to grayscale and then into a series of "streaks" based on brightness levels. These streaks represent segments of each row in the image that share the same brightness classification (either dark or light). The script uses the streaks to recreate the image in a drawing program like MS Paint by moving the mouse and dragging lines corresponding to the dark streaks. This process is repeated for each row of the image until the entire drawing is completed.