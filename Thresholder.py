# DESCRIPTION:
# The training images are thresholded to remove any backgrounf noise here.
import cv2
import os
import matplotlib.pyplot as plt
import time

IMDIR="E:\\NED\\FYP\\Jild 35"
OUTDIR="Thresholded"
if not os.path.isdir(OUTDIR):
    os.mkdir(OUTDIR)

for image in os.scandir(IMDIR):
    img = cv2.imread(os.path.join(IMDIR,image))
    _,img=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    NAME=str(time.time())
    cv2.imwrite(os.path.join(OUTDIR,"{}-thresholded.png".format(NAME)),img)
