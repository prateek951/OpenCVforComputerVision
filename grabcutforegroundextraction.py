import cv2
import numpy as np 
import matplotlib.pyplot as plt 

# GRAB CUT FOREGROUND EXTRACTION
# specify the image
img = cv2.imread('watch.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

# Defining the background model
bgdModel = np.zeros((1,65),np.float64)
# Defining the foreground model
fgdModel = np.zeros((1,65),np.float64)

rect  = (50,50,300,500)

# Now grabcut the region of interest
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()