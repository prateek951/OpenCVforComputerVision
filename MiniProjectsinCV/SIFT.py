# USING SIFT,SURF,FAST,BRIEF AND ORB
# Create a detector
# Input image into the detector
# Obtain the keypoints
# Draw the keypoints

import cv2
import numpy as np 

# Read and decode the input image
image = cv2.imread('input.jpg')
# Convert the image to the gray scale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Input the image to the detector 
sift = cv2.SIFT()
keypoints = sift.detect(gray, None)
print("Number of Keypoints detected :", len(keypoints))

# Draw rich keypoints on the input image
image = cv2.drawKeypoints(image,keypoints,flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - SIFT', image)
cv2.waitKey(0)
cv2.destroyAllWindows()