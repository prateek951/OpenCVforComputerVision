# CAMSHIFT ALGORITHM
# Continuous Adaptive MeanShift  for continuos adaptive window

# Applies MS till it converges
# Calculates the size of the window
# Calculates the orientation by using the best fitting eclipse

import numpy as np 
import cv2 
# init webcam 
cap = cv2.VideoCapture(0)
# Take the first frame
ret, frame = cap.read()

# Setup the default location of the tracking window
r,h,c,w = 240,100,400,160
track_window = (c,r,w,h)

# Define the ROI
roi = frame[r:r+h,c:c+w]
# Convert the roi to the hsv
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

# Create a mask between the HSV bounds
lower_purple = np.array([125,0,0])
upper_purple = np.array([175,255,255])
mask = cv2.inRange(hsv_roi, lower_purple, upper_purple)

# Obtain the color histogram of the ROI
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])

# Setup the termination criteria
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT,10,1)

while True:
    # Slice on another frame
    ret, frame = cap.read()
    if ret == True:
        # Convert the frame to hsv
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # Calculate the back projection for the histogram
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply camshift algorithm to get the new location
        ret, track_window = cv2.CamShift(dst,track_window,term_criteria)

        # Draw an adaptive box on the image using polylines
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True,255,2)

        cv2.imshow('Camshift Tracking', img2)

        if cv2.waitKey(1) == 13:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()