# We can make use of smoothing and blurring to get rid of the noise

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	hsv  = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	# frame converted to hsv model

	lower_red = np.array([150,150,50])
	upper_red = np.array([180,255,150])

	mask = cv2.inRange(hsv,lower_red,upper_red)
	res = cv2.bitwise_and(frame,frame,mask=mask)

	# For averaging so as to remove noise due to blurring and smoothing
	kernel= np.ones((15,15),np.float32)/225
	smoothed = cv2.filter2D(res,-1,kernel)

	#appying gaussian blur to our result
	blur = cv2.GaussianBlur(res,(15,15),0)

	# apply median blur on the result
	median = cv2.medianBlur(res,15)
	# apply bilateral blur on the result
	bilateralBlur = cv2.bilateralFilter(res,15,75,75)

	cv2.imshow('frame',frame)
	# cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	cv2.imshow('smoothed',smoothed)
	cv2.imshow('blur',blur)
	cv2.imshow('median',median)
	cv2.imshow('bilateralBlur',bilateralBlur)

	k = cv2.waitKey(5)

	if k==27:
		break
cv2.destroyAllWindows()
cap.release()		