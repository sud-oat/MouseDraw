# MouseDraw

INSTALLATION:

Clone the repository

```
git clone https://github.com/CarlDragon5068/MouseDraw
cd MouseDraw
```

INSTALL REQUIREMENTS:

```
pip install autogui numpy pillow
```

USAGE:

Put the local path of the image you want to recreate in source_image variable in the form of a png or jpg file. You can modify pixel_size and drawing_speed in the function main(). Open paint and then run the program. You will have to modify pixel size to get the image to be of the size you want.

WARNING
this script is VERY simple and may take upto a minute to draw your image. be very careful that your cursor is actually in paint and not on anything else, as the program does not check for that.

HOW IT WORKS:

This program takes any coloured image and converts it to black and white by converting all pixels with values less than 128 to white and above 128 to black. Then the program would draw the image using the mouse, line by line, on a paint software.



