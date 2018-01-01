import cv2 
import numpy as np 

image = cv2.imread('input.jpg')
# Convert the image to gray scale for efficient processing
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Create the ORB detector instance wherein we can specify the number of keypoints that are desired
orb = cv2.ORB(1000)

# Determine the number of keypoints
keypoints = orb.detect(gray, None)

# Obtain the descriptors
keypoints, descriptors = orb.compute(gray,keypoints)
print("Number of keypoints detected:", len(keypoints))

# Draw rich keypoints on the input image
image = cv2.drawKeypoints(image,keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - ORB', image)
cv2.waitKey()
cv2.destroyAllWindows()
