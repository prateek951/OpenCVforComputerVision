# Import the necessary libraries

# Implementation of Color Threshold

import numpy as np 
import matplotlib.pyplot as plt 
import cv2 

# Read in and display the image 
image = cv2.imread('images/pizza_bluescreen.jpg')
# gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
# print(gray_image)

# Print out the type of the image data and its dimensions 

print('the image is',type(image),'the dimensions of the image',image.shape)

%matplotlib inline 

# The color of the image comes out to be red in background
# whereas the image that we gave it had a blue background
# This is because OpenCV reads the image in the BGR format.
# So what should be blue it shows that as red and vice versa.

# plt.imshow(image)

# Make a copy of the image 
image_copy = np.copy(image)

# Perform a color transformation on this copy 
image_copy = cv2.cvtColor(image_copy,cv2.COLOR_BGR2RGB)

# Display the image 
plt.imshow(image_copy)


# Define the color threshold 

# Define our color selection boundaries in RGB values 
lower_blue = np.array([0,0,220])
upper_blue = np.array([50,70,255])

# Create a mask 

# Define the masked area 
mask = cv2.inRange(image_copy,lower_blue,upper_blue)

plt.imshow(mask)

# Mask the image to let the pizza show through
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0,0,0]

# 0 represents black and mask != 0 represents the region white now 
# This white region was initially what was blue and that is what we want to change 

# Display the image 
plt.imshow(masked_image)

# Mask and add a background image 

background_image = cv2.imread('images/space_background.jpg')
background_image = cv2.cvtColor(background_image,cv2.COLOR_BGR2RGB)

# Crop this loaded image so that it is of the same size 
# as the pizza image
background_cropped_image = background_image[0:514,0:816]

background_cropped_image[mask == 0] = [0,0,0]

# Display the background 
plt.imshow(background_cropped_image)

# Add the two images together 
complete_image = background_cropped_image + masked_image

# Display the complete image 
plt.imshow(complete_image)
