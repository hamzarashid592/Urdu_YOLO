import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np

# define the model options and run

options = {
    'model': 'cfg/tiny-yolo-voc-bayshosha.cfg',
    'load': -1,
    'threshold': 0.1
}

tfnet = TFNet(options)

# read the color image and covert to RGB

img = cv2.imread('Tester.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
result = tfnet.return_predict(img)
colors = [tuple(255 * np.random.rand(3)) for _ in range(len(result))]

# pull out some info from the results
print(len(result))
print (result)
tl=[]
br=[]
label=[]

for c,r in zip(colors,result):
    tl=(r['topleft']['x'], r['topleft']['y'])
    br=(r['bottomright']['x'], r['bottomright']['y'])
    label= r['label']
    # add the box and label and display it
    img = cv2.rectangle(img, tl, br, c, 5)
    # img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    plt.imshow(img)
    plt.show()
