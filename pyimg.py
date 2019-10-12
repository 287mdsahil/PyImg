#!/usr/bin/env python3

from PIL import Image
import numpy as np
import sys


# Loading the image
def loadImage():
    img = Image.open(sys.argv[1])
    img.load()
    w = img.size[0]
    h = img.size[1]
    scale = 1
    if(w > h):
        scale = (100/w)
    else:
        scale = (100/h)
    w = int(w*scale)
    h = int(h*scale)
    print(w,h)
    img = img.resize((w, h), Image.ANTIALIAS)
    img = np.array(img)
    return img


##########################################################
img = loadImage()
print(img.shape)
