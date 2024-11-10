# importing libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading img
img = cv2.imread('pizza.jpg')

# scaling img
scaled_img = cv2.resize(img, None, fx=0.5, fy=0.5)

# comparing the images
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(scaled_img), plt.title('Output')
plt.show()

# saving the scaled img
# plt.imsave('pizza_scalling.jpg', scaled_img)
