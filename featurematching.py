import cv2
import numpy as np 
import matplotlib.pyplot as plt
# This is not like template matching wherein the transformations are preserved
# and where the template image was a spliced portion of the source image

# In this algorithm we have two images one is the source image
# SOURCE IMAGE - with different lightnening,different angle of rotations
# TEMPLATE IMAGE -- same applies for this image as well

# BRUTE FORCE MATCHING

img2 = cv2.imread('feature-source.jpg',0)
img1 = cv2.imread('feature-template.jpg',0)

orb = cv2.ORB_create()

# Keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# Find the keypoints using the ORB detector

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Find the matches and sort them on the basis of confidence
matches = bf.match(des1,des2)
matches = sorted(matches,key= lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
plt.imshow(img3)
plt.show()