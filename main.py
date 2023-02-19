#!/usr/bin/env python3

from PIL import Image 
import sys
import os
import time

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image: Image.Image, new_width=100):
    w, h = image.size 
    ratio = h / w
    new_h = int(new_width * ratio)
    return image.resize((new_width, new_h))

def grayify(image: Image.Image):
    return image.convert("L")

def pixels_to_ascii(image: Image.Image):
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])


def to_ascii(filepath: str, new_w=100):
    """
    Convert a black and white png file to an numpy array
    """
    im = Image.open(filepath)
    return pixels_to_ascii(grayify(resize_image(im, new_w)))

def main(n_w: str="65"):
    """
    BAD APPLE
    =========
    """
    BASE_DIR = os.path.dirname(__file__)
    FRAMES_DIR = os.path.join(BASE_DIR, "frames")
    if not os.path.exists(FRAMES_DIR): exit(1)
    frames = 0
    for _ in os.listdir(FRAMES_DIR) : frames += 1 
    os.system("clear")
    new_width = int(n_w)
    for i in range(1, frames+1):
        data = to_ascii(os.path.join(FRAMES_DIR, f"{i:0>4}.png"), new_width)
        pixel_count = len(data)
        ascii_img = "\n".join(data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
        print(ascii_img, end="\r")
        time.sleep(0.01)


if __name__ == "__main__":
    import sys
    if "-h" in sys.argv:
        print("Usage: main.py\n\t-s\t\tSpecify the width of to display\n\t-h\t\tShow this thing call 'help'\n")
        
    else:
        main(sys.argv[2]) if len(sys.argv) > 1 and sys.argv[1] == "-s" else main()
