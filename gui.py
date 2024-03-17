
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import numpy as np
from pathlib import Path
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\poste\Documents\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


from PIL import Image, ImageTk
from tkinter import filedialog

def load_image():
    global image, filename
    
    filename = filedialog.askopenfilename()
    
    if filename:
        img = Image.open(filename)
        img.thumbnail((620, 390), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(568, 254, anchor='center', image=img)
        canvas.image = img



def show_histogram():
    
    if filename:
        image = Image.open(filename)
        gray_image = image.convert('L')
        histogram = gray_image.histogram()
        hist_image = Image.new('RGB', (256, 257), color='white')
        draw = ImageDraw.Draw(hist_image)
        max_count = max(histogram)
        for i in range(256):
            count = int(histogram[i] * 200 / max_count)
            draw.line((i, 200, i, 200 - count), fill='blue')
        hist_photo = ImageTk.PhotoImage(hist_image)
        canvas.create_image(568, 254, anchor='center', image=hist_photo)
        canvas.image = hist_photo 

def grayscale():
    global image
    img = Image.open(filename)
    gray_image = img.convert('L')
    gray_image.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(gray_image)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image

def rotate_image():
    global image
    degree = 45
    pil_image = Image.open(filename)
    rotated_image = pil_image.rotate(degree)
    rotated_image.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(rotated_image)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image

def apply_noise():
    global image
    img = Image.open(filename)
    img_array = np.array(img)
    noise = np.random.normal(0, 30, img_array.shape)
    noisy_img_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    noisy_img = Image.fromarray(noisy_img_array)
    noisy_img.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(noisy_img)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image




def filter_image():
    global image
    img = Image.open(filename)
    filtered_image = img.filter(ImageFilter.MedianFilter(size=3))
    filtered_image.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(filtered_image)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image

def apply_threshold():
    global image
    threshold_value = 128
    img = Image.open(filename)
    thresholded_img = img.convert('L').point(lambda x: 255 * (x > threshold_value))
    image_th = thresholded_img.convert('RGB')
    image_th.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(image_th)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image


def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if file_path:
        image.save(file_path)


def apply_histogram_equalization():
    global image
    img = Image.open(filename)
    img_gray = img.convert('L')
    hist, bins = np.histogram(np.array(img_gray).flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    img_equalized = np.interp(np.array(img_gray).flatten(), bins[:-1], cdf_normalized).reshape(img_gray.size).astype('uint8')

    img_eq_pil = Image.fromarray(img_equalized)
    img_eq_pil.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(img_eq_pil)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image

def add_constant():
    global image
    c = 50  # set the constant value to 50
    img = Image.open(filename)
    img_array = np.array(img)
    img_array = img_array.astype('uint16')
    img_array += c
    img_array = np.clip(img_array, 0, 255)
    img_array = img_array.astype('uint8')
    img_const = Image.fromarray(img_array)
    img_const.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(img_const)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image

def negative_transform():
    global image
    img = Image.open(filename)
    img_array = np.array(img)
    img_array = 255 - img_array
    img_neg = Image.fromarray(img_array)
    img_neg.thumbnail((620, 390), Image.LANCZOS)
    image = ImageTk.PhotoImage(img_neg)
    canvas.create_image(568, 254, anchor='center', image=image)
    canvas.image = image



window = Tk()

window.geometry("973x658")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 658,
    width = 973,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    973.0,
    658.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    280.0,
    59.0,
    900.0,
    449.0,
    fill="#AFACAC",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=load_image,
    relief="flat"
)
button_1.place(
    x=61.0,
    y=181.0,
    width=132.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=quit,
    relief="flat"
)
button_2.place(
    x=61.0,
    y=303.0,
    width=132.0,
    height=47.0
)

canvas.create_text(
    415.0,
    0.0,
    anchor="nw",
    text="TIM GUI",
    fill="#000000",
    font=("Kavivanar Regular", 40 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=show_histogram,
    relief="flat"
)
button_3.place(
    x=51.0,
    y=473.0,
    width=132.0,
    height=47.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=apply_noise,
    relief="flat"
)
button_4.place(
    x=240.0,
    y=473.0,
    width=132.0,
    height=47.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=negative_transform,
    relief="flat"
)
button_5.place(
    x=49.0,
    y=548.0,
    width=132.0,
    height=47.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=apply_threshold,
    relief="flat"
)
button_6.place(
    x=807.0,
    y=473.0,
    width=132.0,
    height=47.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=apply_histogram_equalization,
    relief="flat"
)
button_7.place(
    x=807.0,
    y=548.0,
    width=132.0,
    height=47.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=add_constant,
    relief="flat"
)
button_8.place(
    x=618.0,
    y=548.0,
    width=132.0,
    height=47.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=rotate_image,
    relief="flat"
)
button_9.place(
    x=240.0,
    y=548.0,
    width=132.0,
    height=47.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=save_image,
    relief="flat"
)
button_10.place(
    x=430.0,
    y=548.0,
    width=132.0,
    height=47.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=filter_image,
    relief="flat"
)
button_11.place(
    x=429.0,
    y=473.0,
    width=132.0,
    height=47.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=grayscale,
    relief="flat"
)
button_12.place(
    x=618.0,
    y=473.0,
    width=132.0,
    height=47.0
)

canvas.create_text(
    782.0,
    622.0,
    anchor="nw",
    text="have a good day :)",
    fill="#000000",
    font=("Kavivanar Regular", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    127.0,
    87.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    938.0,
    137.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()