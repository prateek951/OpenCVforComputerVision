import cv2 
import numpy as np 

# Capture yourself or to any sample video
cap = cv2.VideoCapture(0)
# init bg subtractor
foreground_background = cv2.BackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    # Apply bg subtractor to get the foreground mask 
    foreground_mask = foreground_background.apply(frame)

    cv2.imshow('Output',foreground_mask)

    if cv2.waitKey(1) == 13:
        break 
cap.release()
cv2.destroyAllWindows()