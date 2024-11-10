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
MedianBlurDeNoisedGaussianNoisy = cv2.medianBlur(GaussianNoisyImg, 3)
MedianBlurDeNoisedImpulsiveNoisy = cv2.medianBlur(ImpulsiveNoisyImg, 3)
MedianBlurDeNoisedUniformNoisy = cv2.medianBlur(UniformNoisyImg, 3)

# saving the img
cv2.imwrite('MedianBlurDeNoisedGaussianNoisy.jpg', MedianBlurDeNoisedGaussianNoisy)
cv2.imwrite('MedianBlurDeNoisedImpulsiveNoisy.jpg', MedianBlurDeNoisedImpulsiveNoisy)
cv2.imwrite('MedianBlurDeNoisedUniformNoisy.jpg', MedianBlurDeNoisedUniformNoisy)

# checking if everything is ok
print('***fininshed***'*3)