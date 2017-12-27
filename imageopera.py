import numpy as np 
import cv2 

# Reading the image and store it in a variable
img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

# img[55,55] = [255,255,255]
# px = img[55,55]

# print(px)

# ROI of the image Region of interest for the image

# roi = img[100:150,100:150]
# print(roi)


# Here we have converted the region of interest to a white square
img[100:150,100:150] = [255,255,255]


watch_face = img[37:111,107:194]

img[0:74,0:87] = watch_face


# Show the image
cv2.imshow('image',img)
cv2.waitKey(0)
# Destroy all the windows
cv2.destroyAllWindows()

