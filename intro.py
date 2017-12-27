# Loading the image

# Using cv2 you can analyse the video frame as a still frame

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# plot the images using the matplotlib

# How to handle an image in opencv image or video

# Read the image

# here we are reading the image by specifying a filter
# as GRAYSCALE which is the simplified image form
# if the second parameter is left behind it will read the image
# as rgb image 
# In the grayscale we will remove the degree of opaqueness which kicks out alpha

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

# IMREAD_COLOR - 1
# IMREAD_UNCHANGED - (-1)

# cv2.imshow('image',img)

# # On pressing 0 the view will vanish
# cv2.waitKey(0);
# cv2.destroyAllWindows();

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

# Even on videos we will be using the imread

# For saving the image we will be using the imwrite
cv2.imwrite('watchgray.png',img)



