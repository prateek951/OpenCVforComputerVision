import cv2 
import numpy as np

# Create our body classifier
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Invoke the VideoCapture Instance to begin with live shooting
cap = cv2.VideoCapture('walking.avi')
# Check for whether the camera is shooting or not
while cap.isOpened():
    # Read the first frame
    ret, frame = cap.read()
    # Our focus is on the first frame
    # Resize the grabbed frame
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    # Convert the frame to the grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our cascade classifier
    bodies = body_classifier.detectMultiScale(gray,1.3,5)

    # Out of all the bodies identified create the bounding box
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('Pedestrians', frame)
    if cv2.waitKey(1) == 13:
        pass
cap.release()
cv2.destroyAllWindows()