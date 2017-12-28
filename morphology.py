# erosion and dilation m t

import numpy as np
import cv2 

# Set up the video capture
cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	# Convert to hsv
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	# Keeping track of the cap
	lower_red = np.array([150,150,50])
	upper_red = np.array([180,255,150])

	# Perform masking on the frame
	mask = cv2.inRange(frame,lower_red,upper_red)
	res = cv2.bitwise_and(frame,frame,mask=mask)
	# Perform morphological transformations on the cap
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations=1)
	dilation = cv2.dilate(mask, kernel, iterations=1)
	# openings is for the false positives(noises in the background) and closings is for the false negative(noise in the cap)
	opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
	# For noise in the cap (false negatives) we use the closings
	closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)


	# Tophat is the difference between the image and the opening image
	# cv2.imshow('Tophat',tophat)
	# Blackhat is the difference between the image and the closing image
	# cv2.imshow('Blackhat',blackhat)
	cv2.imshow('frame',frame)
	cv2.imshow('res',res)
	cv2.imshow('erosion',erosion)
	cv2.imshow('dilation',dilation)
	cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)

	k = cv2.waitKey(5) & 0xFF
	if k==27:
			break
cv2.destroyAllWindows()
# Finally release the capture
cap.release()