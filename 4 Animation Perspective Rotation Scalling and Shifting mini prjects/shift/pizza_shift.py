# importing libraries
import cv2 
import matplotlib.pyplot as plt
import numpy as np

# reading img
image = cv2.imread('pizza.jpg')

# Translate the image by 50 pixels in the x direction and 25 in the y direction
# xOffset - offset in x direction # yOffset - offset in y direction
xOffset = 50
yOffset = 25

# define the transformation matrix m
M = np.float32([[1,0,xOffset],[0,1,yOffset]])
    
# preform the image Translation and return the results
dst = cv2.warpAffine(image,M,(image.shape[1], image.shape[0]))

# comparing the images
plt.subplot(121),plt.imshow(image),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

# saving the scaled img
# plt.imsave('pizza_shift.jpg', dst )

# Show the results 