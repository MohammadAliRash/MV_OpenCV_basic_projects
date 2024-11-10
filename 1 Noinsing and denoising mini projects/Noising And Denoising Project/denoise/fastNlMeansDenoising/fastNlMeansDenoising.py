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

# Applying the filter
fastNIMeansGaussianDeNoised = cv2.fastNlMeansDenoising(GaussianNoisyImg, None, 10, 10)
fastNIMeansImpulsiveDeNoised = cv2.fastNlMeansDenoising(ImpulsiveNoisyImg, None, 10, 10)
fastNIMeansUniformDeNoised = cv2.fastNlMeansDenoising(UniformNoisyImg, None, 10, 10)

# saving the img
cv2.imwrite('fastNIMeansGaussianDeNoised.jpg', fastNIMeansGaussianDeNoised)
cv2.imwrite('fastNIMeansImpulsiveDeNoised.jpg', fastNIMeansImpulsiveDeNoised)
cv2.imwrite('fastNIMeansUniformDeNoised.jpg', fastNIMeansUniformDeNoised)

# checking if everything is ok
print('***fininshed***'*3)