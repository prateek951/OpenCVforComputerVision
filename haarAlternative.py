import cv2 
import numpy as np 

# Open the image classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load our image
image = cv2.imread('Trump.jpg')
# Convert to gray scale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray,1.3,5)

# When no faces detected,face classifier will return an empty tuple
if faces is ():
    print("No faces found")

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+h,y+k),(155,33,22),2)
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

