# This code picks out the images based on the annotation generated and stores them in a separate folder.
import os
import cv2
import pdb

imdir = 'images'
finaldir='Training_Images_FINAL'
if not os.path.isdir(finaldir):
    os.mkdir(finaldir)

n = 0
m=0
annotationdir="annotations"
ann_array=[]
im_array=[]

for annfile in os.listdir(annotationdir):#   Gathering contents of the annotations folder
    ann_array.append(annfile[:-4])

for imfile in os.listdir(imdir):#Gathering contents of the Images folder
    im_array.append(imfile[:-4])
mask=[]
# pdb.set_trace()
while(m<len(ann_array)):#Comparing the two lists and making a mask array.
    if(im_array[n]==ann_array[m]):
        mask.append(1)
        n+=1
        m+=1
    else:
        mask.append(0)
        n+=1
n=0
for ma in mask:
    if ma==1:
        img=cv2.imread(os.path.join(imdir,'{}.png'.format(im_array[n])))
        cv2.imwrite(os.path.join(finaldir, '{}.png'.format(im_array[n])),img)
        n+=1
    else:
        n+=1
