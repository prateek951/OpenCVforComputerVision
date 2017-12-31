import cv2
import numpy as np 
# Using the mog background reduction algorithm

# This algorithm works by finding the changes the ones that 
# are changing is the foreground and the one which is not changing 
# is the background as compared from the previus frames

# Capture the video scene
cap = cv2.VideoCapture('bgrSample.mp4')
# Createa an instance for the background reduction
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    # Read a frame
    ret,frame = cap.read()
    # Apply the bg reduction mask on the frame
    fgmask = fgbg.apply(frame)

    # Display the original frame and the background-reduced version of it
    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    # Waiting for the process to end 
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the capture
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
    