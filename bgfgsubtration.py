# Gaussian Mixed based Background/Foreground Segmentation Algorithm
# You can use this on the background input as well
import numpy as np
import cv2

cap = cv2.VideoCapture('walking.avi')

# Initlaize background subtractor
foreground_background = cv2.BackgroundSubtractorMOG()

while True:
    
    ret, frame = cap.read()

    # Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)

    cv2.imshow('Output', foreground_mask)
    if cv2.waitKey(1) == 13: 
        break

cap.release()
cv2.destroyAllWindows()