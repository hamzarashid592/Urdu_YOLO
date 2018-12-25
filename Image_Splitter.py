# DESCRIPTION:
# This code actually is acting as the main generator of image data. It splits the pages of urdu text to small images
# and stores them in a folder.
import cv2
import os
import matplotlib.pyplot as plt
import time
import numpy
import pdb

IMDIR='Cropped'
OUTDIR="Splitted"
if not os.path.isdir(OUTDIR):
    os.mkdir(OUTDIR)
iterations=0
for image in os.scandir(IMDIR):
    img = cv2.imread(image.path)

    img2 = img

    height, width, channels = img.shape
    # Number of pieces Horizontally
    CROP_W_SIZE  = 2
    # Number of pieces Vertically to each Horizontal
    CROP_H_SIZE = 25

    for ih in range(CROP_H_SIZE ):
        for iw in range(CROP_W_SIZE ):
            x = int(width/CROP_W_SIZE * iw)
            y = int(height/CROP_H_SIZE * ih)
            h = int(height / CROP_H_SIZE)
            w = int(width / CROP_W_SIZE )
            print(x,y,h,w)
            img = img[y:y+h, x:x+w]

            NAME = str(time.time())
            cv2.imwrite(os.path.join(OUTDIR,"{}-splitted.png".format(NAME)),img)
            img = img2
    iterations+=1
    if iterations>=1:
        break
# pdb.set_trace()
