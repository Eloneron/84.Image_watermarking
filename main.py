"""
This is an image watermarking app.
Load an image, watermark and execute.

Release notes:
Initial release - 18.12.2021

No GUI
Fixed watermark file, size and position, alpha could be better as well
Fixed source image

Saves output file.

Copyright Robert Pralicz 2021
"""

# imports

from PIL import Image
import matplotlib.pyplot as plt

# to open the image
image = Image.open("sample.jpg")
# this open the photo viewer
# image.show()
# plt.imhsow(image)

# image watermark
size = (500, 100)
watermark = Image.open("watermark_no_bg.png")
# to keep the aspect ration in intact
watermark.thumbnail((200, 200), Image.ANTIALIAS)
# watermark = watermark.putalpha(10)

# add watermark
copied_image = image.copy()
# base image
copied_image.paste(watermark, (30, 500), watermark)
# pasted the crop image onto the base image
copied_image.show()
save = input("do you want to save the image? (y/n) ")
if save.lower() == 'y':
    name = input("Enter file name: ")
    name = name + '.jpg'
    copied_image.save(name)
