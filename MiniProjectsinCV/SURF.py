import cv2
import numpy as np 

# Read and decode the image
image = cv2.imread('input.jpg')
# Convert the read image to the grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Create the surf detector instance
surf = cv2.SURF()
# Only features whose hessian is larger than hessian threshold are retained by the detector
surf.hessianThreshold = 7500 
keypoints,descriptors = cv2.detectAndCompute(gray,None)
print("Number of keypoints detected : ",len(keypoints))

# Draw rich key points on the input image
image = cv2.drawKeypoints(image,keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - SURF'. image)
cv2.waitKey(0)
cv2.destroyAllWindows()

