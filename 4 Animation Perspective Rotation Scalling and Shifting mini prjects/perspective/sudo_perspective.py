# importing libraries
import cv2  as cv
import matplotlib.pyplot as plt
import numpy as np

# reading img
img = cv.imread('sudoku.jpg')

# setting the rows and cols 
rows,cols,ch = img.shape

# original poits
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# calculated poits
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

# implementing the perspective 
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))

# comparing the images
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

# saving the scaled img
# plt.imsave('sudo_perspective.jpg', dst )