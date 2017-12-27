# Video analysis is similiar to the image analysis as video breaks down to frames

# Each frame is an image

import cv2 
import numpy as np 

# Turn on the video capture
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:

	# All analysis goes here
	 ret,frame = cap.read()
	 gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	 out.write(frame)
	 cv2.imshow('gray',gray)
	 cv2.imshow('frame',frame)
	 # when should the frame get killed
	 if cv2.waitKey(1) & 0xFF == ord('q'):
	 	break  
# Turn off the capture
cap.release()
out.release()
# Destroy all the windows
cap.destroyAllScreens()