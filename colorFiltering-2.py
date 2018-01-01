import cv2 
import numpy as np 

# init webcam
cap = cv2.VideoCapture(0)

# define the range of blue color in hsv
# numpy array taking the hue sation values
# hue will vary from 0 to 180
lower_purple = np.array([125,0,0])
upper_purple = np.array([175,255,255])

while True:
    # Slice the video into a number of frames
    # Read the first frame
    ret, frame = cap.read()
    # Convert the frame into hsv
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # Capture the values only between the lower and upper_purple
    mask = cv2.inRange(frame,lower_purple,upper_purple)
    result = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Filtered Color Only', result)
    if cv2.waitKey(1) == 13:
        break
# Release the capture
# Destroy all the MULTI GUI windows
cap.release()
cv2.destroyAllWindows()