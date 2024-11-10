import cv2 
import numpy as np  
import matplotlib.pyplot as plt

#reading the img
original = plt.imread('1.jpg')
flat_chess = cv2.imread('1.jpg')

flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
# plt.imshow(flat_chess)

gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
# plt.imshow(gray_flat_chess,cmap='gray')

# Convert Gray Scale Image to Float Values
gray = np.float32(gray_flat_chess)

# Corner Harris Detection
dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)

# result is dilated for marking the corners, not important to actual corner detection
# this is just so we can plot out the points on the image shown
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
flat_chess[dst>0.01*dst.max()]=[0,0,255]

final = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2RGB)

cv2.imwrite('cornered.jpg', final)

# while True:
#     cv2.imshow('window',final )
#     if cv2.waitKey(10) & 0xFF ==27:
#         break

# comparing the images
plt.subplot(121), plt.imshow(original), plt.title('Input')
plt.subplot(122), plt.imshow(flat_chess), plt.title('Output')
plt.show()