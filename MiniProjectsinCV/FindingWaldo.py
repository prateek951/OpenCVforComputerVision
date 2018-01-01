import cv2
import numpy as np 

# Load the input image and convert to gray scale 
image = cv2.imread('WaldoBeach.jpg')
cv2.imshow('Where is Waldo?', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Load the template image in gray scale
template = cv2.imread('waldo.jpg',0)

# We slide the template image over the source image from left to right
# and top to bottom, one pixel at a time.Then for each of these locations,
# we compute the correlation coefficient to determine how good or bad the match is

# High CC can be considered as the good matchers for finding waldo
result = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF)
# cv2.minMaxLoc finds where our good matches are
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Create the bounding box
top_left = max_loc 
bottom_right = (top_left[0] + 50,top_left[1] + 50)
cv2.rectangle(image,top_left,bottom_right,(0,0,255),5)

cv2.imshow('Where is Waldo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()