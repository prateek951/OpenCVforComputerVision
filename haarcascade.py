# This algorithm is used to detect the object in the a video using the haar cascade 
# object detection algorithm

import cv2
import numpy as np 

# Haar cascades are massive xml files with lot of feature sets.These feature
# sets might correspond to a specific type of object

# Load in our two cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load in the web camera
cap = cv2.VideoCapture(0)

while True:
    # Grab,decode the next frame
    ret, image = cap.read()
    # Convert the grabbed frame into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Here 1.3 is the scaling factor and 5 is the minNeighbours
    # First we gonna find all the faces and we gonna draw a rectangle over the faces
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        # For the grabbed face, draw a rectangle on the face
        cv2.rectangle(image,(x,y),(x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = image[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('image',image)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break 

#  Close video file or the capturing device
cap.release()
# Destroy all the HighGUI windows
cv2.destroyAllWindows()