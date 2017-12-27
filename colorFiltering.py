import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

# For a video we will be requiring the while loop

while True:
	_,frame = cap.read()
	# Frame conversion to hsv
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	# Frame is now in hsv
	# Hue Saturation Value
	lower_red = np.array([150,150,150])
	upper_red = np.array([255,255,150])

	mask = cv2.inRange(hsv,lower_red,upper_red)
	res = cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	k = cv2.waitKey(5)
	if k == 27:
		break
cv2.destroyAllWindows()
cv2.release()