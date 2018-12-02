import numpy as np 
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import cv2 # the computer vision library 

%matplotlib qt 

# Read in and display the image 
image = mpimg.imread('images/waymo_car.jpg')
# Print out the image dimensions 
print('Image dimensions :',image.shape)

# Change from color to grayscale 

gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Display the grayscale image 
plt.imshow(gray_image,cmap='gray')

x=190
y=375
pixel_val = gray_image[y,x]
print(pixel_val)
