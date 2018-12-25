import os

imdir = 'images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)
n = 0
folder="Splitted"
for imfile in os.scandir(folder):
    os.rename(imfile.path, os.path.join(imdir, '{:07}.png'.format(n)))
    #WARNING: The constant 07 above should not be changed as other python files depend on it.
    #Changing it may lead to chnage other files also.
    n += 1
