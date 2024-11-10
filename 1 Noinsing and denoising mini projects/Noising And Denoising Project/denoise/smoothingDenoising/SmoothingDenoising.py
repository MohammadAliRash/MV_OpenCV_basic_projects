import cv2
import matplotlib.pyplot as plt
import numpy as np

# reading the img
GaussianNoisyImg = cv2.imread('GaussianNoisy.jpg')
ImpulsiveNoisyImg = cv2.imread('ImpulsiveNoisy.jpg')
UniformNoisyImg = cv2.imread('UniformNoisy.jpg')

# checking the img
print(GaussianNoisyImg.shape)
print(ImpulsiveNoisyImg.shape)
print(UniformNoisyImg.shape)

# Creating the kernel with numpy
kernel2 = np.ones((5, 5), np.float32)/25

# Applying the filter
SmoothedGaussianDeNoised = cv2.filter2D(src=GaussianNoisyImg, ddepth=-1, kernel=kernel2)
SmoothedImpulsiveDeNoised = cv2.filter2D(src=ImpulsiveNoisyImg, ddepth=-1, kernel=kernel2)
SmoothedUniformDeNoised = cv2.filter2D(src=UniformNoisyImg, ddepth=-1, kernel=kernel2)

# saving the img
cv2.imwrite('SmoothedGaussianDeNoised.jpg', SmoothedGaussianDeNoised)
cv2.imwrite('SmoothedImpulsiveDeNoised.jpg', SmoothedImpulsiveDeNoised)
cv2.imwrite('SmoothedUniformDeNoised.jpg', SmoothedUniformDeNoised)

# checking if everything is ok
print('***fininshed***'*3)
