import cv2 
import numpy as np 

# Setting up the video capture
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    # at this stage we are having the frame 
    # We want the laplacian gradient for the frame
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    
    # Apply the canny edge detector on the frame that we obtained
    edges = cv2.Canny(frame,100,200)

    # Display the images
    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
    

# destroy all the windows
cv2.destroyAllWindows()
# Release the capture
cap.release()