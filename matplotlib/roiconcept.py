# Sample Testing

import numpy as np 
import cv2 

# init web camera
cap = cv2.VideoCapture(0)

while True:
    # Read the first frame
    ret, frame = cap.read()
    # Convert the frame to grayscale
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    roi = gray[100:113,244:276]
    cv2.imshow('roi',roi)
    k = cv2.waitKey(0)
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()