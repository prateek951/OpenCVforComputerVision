import cv2 
import numpy as np 
# init webcam
cap = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# Create the knn background subtractor 
fgbg = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)

    cv2.imshow('frame', fgmask)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
