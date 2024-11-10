# importing the libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading the img 
img = cv2.imread('rabbit3.jpg')

# setting the rows and cols 
rows, cols, ch = img.shape

matrix_rotated45 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
matrix_rotated90 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.6)
matrix_rotated135 = cv2.getRotationMatrix2D((cols/2, rows/2), 135, 0.6)
matrix_rotated180 = cv2.getRotationMatrix2D((cols/2, rows/2), 180, 0.6)
rotated_img45 = cv2.warpAffine(img, matrix_rotated45, (cols, rows))
rotated_img90 = cv2.warpAffine(img, matrix_rotated90, (cols, rows))
rotated_img135 = cv2.warpAffine(img, matrix_rotated135, (cols, rows))
rotated_img180 = cv2.warpAffine(img, matrix_rotated180, (cols, rows))

# comparing 
plt.subplot(151),plt.imshow(img), plt.title('Input')
plt.subplot(152),plt.imshow(rotated_img45), plt.title('Output45')
plt.subplot(153),plt.imshow(rotated_img90), plt.title('Output90')
plt.subplot(154),plt.imshow(rotated_img135), plt.title('Output135')
plt.subplot(155),plt.imshow(rotated_img180), plt.title('Output180')
plt.show()

# saving 
# cv2.imwrite('rotated_rabbit.jpg', rotated_img90)

