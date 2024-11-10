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
fastNIMeansColoredGaussianDeNoised = cv2.fastNlMeansDenoisingColored(GaussianNoisyImg, None, 20, 20, 7, 21)
fastNIMeansColoredImpulsiveDeNoised = cv2.fastNlMeansDenoisingColored(ImpulsiveNoisyImg, None, 20, 20, 7, 21)
fastNIMeansColoredUniformDeNoised = cv2.fastNlMeansDenoisingColored(UniformNoisyImg, None, 20, 20, 7, 21)

# saving the img
cv2.imwrite('fastNIMeansColoredGaussianDeNoised.jpg', fastNIMeansColoredGaussianDeNoised)
cv2.imwrite('fastNIMeansColoredImpulsiveDeNoised.jpg', fastNIMeansColoredImpulsiveDeNoised)
cv2.imwrite('fastNIMeansColoredUniformDeNoised.jpg', fastNIMeansColoredUniformDeNoised)

# checking if everything is ok
print('***fininshed***'*3)