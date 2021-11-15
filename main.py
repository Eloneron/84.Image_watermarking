"""
This is an image watermarking app.
Load an image, watermark and execute.

Release notes:
Initial release - xx.08.2021

Copyright Robert Pralicz 2021
"""

from tkinter import Tk, Canvas, PhotoImage, Button
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


BGCOLOR = "#B2B1B9"
BUTTON = "#141E61"
FONT = "#252a34"

image, watermark = None, None

def get_file():
    global image
    file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    PILimage = Image.open(file)
    if PILimage.width > 800:
        PILimage.resize(100,200)
    image = ImageTk.PhotoImage(PILimage)

    return image

def load_img():
    image = get_file()
    # file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    canvas.itemconfig(image_id, image=image)


window = Tk()
window.title("Image Watermarking App")
window.wm_minsize(800, 600)
window.config(bg=BGCOLOR, padx=10, pady=10)

my_button = Button(text="Load Photo", command=load_img, bg=BGCOLOR, highlightthickness=0)
my_button.config(padx=10, pady=10)
my_button.grid(row=2, column=2, columnspan=1)

canvas = Canvas(width=790, height=590, bg=BGCOLOR, highlightthickness=0, )  # highlight... - no border visible
original_img = PhotoImage(file="sample.png")
image_id = canvas.create_image(0, 0, anchor='nw', image=original_img)
canvas.grid(row=1, column=0, columnspan=3)

window.mainloop()
