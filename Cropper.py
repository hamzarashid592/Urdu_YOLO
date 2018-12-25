# DESCRIPTION:
# The training images are cropped a little here..
import cv2
import os
import matplotlib.pyplot as plt
import time
import pdb

startX=190
endX=3020
startY=140
endY=2320

IMDIR="Thresholded"
OUTDIR="Cropped"
if not os.path.isdir(OUTDIR):
    os.mkdir(OUTDIR)

for image in os.listdir(IMDIR):
    img = cv2.imread(os.path.join(IMDIR,image))
    img=img[startY:endY,startX:endX]
    NAME=str(time.time())
    cv2.imwrite(os.path.join(OUTDIR,"{}-cropped.png".format(NAME)),img)
