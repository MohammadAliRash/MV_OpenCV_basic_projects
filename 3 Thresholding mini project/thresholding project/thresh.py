# importing the needed libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# loading the img and converting to gray scale
original_gray = cv2.imread('1c.jpg', 0)

#is img loaded
print(original_gray.shape)

# showing the original img with plt in grayScale
plt.imshow(original_gray, cmap='gray')

# saving the original_gray
cv2.imwrite('original_gray.jpg', original_gray)

##############################################  thresh 127
#thresholding with 127 as thresh
ret, thresh127 = cv2.threshold(original_gray, 127, 255, cv2.THRESH_BINARY)

# thresholding with 127 as thresh
plt.imshow(thresh127, cmap='gray')

# saving the thresh127
cv2.imwrite('thresh127.jpg', thresh127)

##############################################  thresh adaptive

#thresholding with adaptive thresh
adaptive_theresh = cv2.adaptiveThreshold(original_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

# showing thresholding with adaptive thresh
plt.imshow(adaptive_theresh, cmap='gray')

# saving the adaptive thresh
cv2.imwrite('adaptiveTheresh.jpg', adaptive_theresh)

############################################## ostu thresholding

# Otsu's thresholding
ret2, otsu_theresh = cv2.threshold(original_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# showing Otsu's thresholding
plt.imshow(otsu_theresh, cmap='gray')

# saving the Otsu's thresholding
cv2.imwrite('otsuTheresh.jpg', otsu_theresh)

############################################## band thresholding

#creating low band
ret3, band1 =cv2.threshold(original_gray, 50, 255 , cv2.THRESH_BINARY)
plt.imshow(band1, cmap='gray')

#creating high band
ret4, band2 =cv2.threshold(original_gray, 210, 255 , cv2.THRESH_BINARY_INV)
plt.imshow(band2, cmap='gray')

#band theresh old
band_theresh = cv2.addWeighted(band1, .5, band2, .5, gamma=0)

#showing band threshold
plt.imshow(band_theresh, cmap='gray')

# saving the band thresholding
cv2.imwrite('bandTheresh.jpg', band_theresh)

