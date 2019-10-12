#!/usr/bin/env python3

from PIL import Image
import numpy as np
import sys


# Loading the image
def loadImage():
    maxdim = 300
    img = Image.open(sys.argv[1])
    img.load()
    w = img.size[0]
    h = img.size[1]
    scale = 1
    if(w > h):
        scale = (maxdim/w)
    else:
        scale = (maxdim/h)
    w = int(w*scale)
    h = int(h*scale)
    print(w,h)
    img = img.resize((w, h), Image.ANTIALIAS)
    img = np.array(img)
    return img

# function to convert rbg color sequence to ansi color code
def get_ansi_color_code(r, g, b):
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)

# function to print a pixel
def printPixel(r,g,b):
    colorCode = int(get_ansi_color_code(r,g,b))
    print(("\x1b[48;5;{}m  \x1b[0m".format(int(colorCode))),end="")

#function to print the image
def printImage(img):
    for x in img:
        for y in x:
            printPixel(y[0],y[1],y[2])
        print()

##########################################################
img = loadImage()
printImage(img)
