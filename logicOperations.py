import cv2
import numpy as np 


# Here it wont work because the size of the two images do not coincide
# Read the first two images
img1 = cv2.imread('watch.jpg')
img2 = cv2.imread('watchgray.jpg')

rows,cols,channels = img2.shape 
roi = img1[0:rows,0:cols]

# Now we want the grayish version of our image2
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

cv2.imshow('mask',mask)

# add = img1 + img2
# add = cv2.add(img1,img2)
# Associating weights to the image and 0 here i9s the gamma language
# weighted = cv2.addWeighted(img1,0.6,img2,0.4,0);
# Show them using the opencv
# cv2.imshow('add',add)
# cv2.imshow('weighted',weighted)
# Press any key will lead to successful termination
cv2.waitKey(0)
# Destroy all the windows
cv2.destroyAllWindows()