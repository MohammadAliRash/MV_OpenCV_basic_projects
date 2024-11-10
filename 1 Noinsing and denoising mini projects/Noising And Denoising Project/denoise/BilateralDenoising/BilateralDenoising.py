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
bilateralGaussianNoisyImg = cv2.bilateralFilter(GaussianNoisyImg, 9, 75, 75)
bilateralImpulsiveNoisyImg = cv2.bilateralFilter(ImpulsiveNoisyImg, 9, 75, 75)
bilateralUniformNoisyImg = cv2.bilateralFilter(UniformNoisyImg, 9, 75, 75)


# saving the img
cv2.imwrite('bilaterallyGaussianNoisyImg.jpg', bilateralGaussianNoisyImg)
cv2.imwrite('BilaterallyImpulsiveNoisyImg.jpg', bilateralImpulsiveNoisyImg)
cv2.imwrite('BilaterallyUniformNoisyImg.jpg', bilateralUniformNoisyImg)

# checking if everything is ok
print('***fininshed***'*3)
