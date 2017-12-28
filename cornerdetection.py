# Used in character recognition motion tracking or any form of
# object tracking

import cv2
import numpy as np 

# Aim is to detect the corners in an image

# Read the image 
img = cv2.imread('cornerdetection.jpg')

# Convert to the grayscale the image that we got
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
# Apply img the method aagainst the grayscale image
# 100 implies that we want 100 of them to be finded
# 0.01 represents the quality
#10 represents the minimum distance between the corners
corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners = np.int0(corners)

# Loop over all the corners and mark them
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)

# Now we have got all the corners display the final image
cv2.imshow('Corner',img)
cv2.waitKey(0)
