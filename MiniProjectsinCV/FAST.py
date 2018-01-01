import cv2 
import numpy as np 

# Read and decode the image
image = cv2.imread('input.jpg')
# Convert the read image to the gray scale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Create FAST detector object 
fast = cv2.FastFeatureDetector()
# Obtain the keypoints by default non max suppression is On
# to turn off set fast.setBool('nonmaxSuppression',False) 
keypoints = fast.detect(gray,None)
print("Number of keypoints deteced: ",len(keypoints))

# Draw rich keypoints on input image
image = cv2.drawKeypoints(image,keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Feature method -FAST image
cv2.imshow('Feature Method - FAST', image)
cv2.waitKey()
# Destroy all the windows
cv2.destroyAllWindows()

