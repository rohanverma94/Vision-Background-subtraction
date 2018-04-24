import matplotlib.pyplot as plt
import numpy as np
import cv2

# Read in the image
image = cv2.imread('stop_sign.jpg')
# Convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# ---------------------------------------------------------- #


Define the color selection criteria
lower_red = np.array([0,0,0]) 
upper_red = np.array([255,89,80])

# Mask the image 
masked_image = np.copy(image)
mask = cv2.inRange(masked_image, lower_red, upper_red)

#Apply the mask to masked_image

masked_image[mask!=0] = (0,0,0)

#plt.imshow(mask)
plt.imshow(masked_image)
