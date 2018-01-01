import cv2 
import numpy as np 

# init webcam 
cap = cv2.VideoCapture(0)
# Store the first frame 
ret, frame = cap.read()
# Create a float numpy array with frame values
average = np.float32(frame)

while True:
    ret, frame = cap.read()

    cv2.accumulateWeighted(frame,average, 0.01)

    # Scales, calculates absolute values and converts the result to
    # 8 bit 
    background = cv2.convertScaleAbs(average)

    cv2.imshow('input',frame)
    cv2.imshow('Disappearing Background', background)

    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
