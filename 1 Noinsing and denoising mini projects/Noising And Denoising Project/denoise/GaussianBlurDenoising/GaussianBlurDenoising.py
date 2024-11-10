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
GaussianBlurdGaussianDeNoised = cv2.GaussianBlur(GaussianNoisyImg, (3, 3), 0)
GaussianBlurdImpulsiveDeNoised = cv2.GaussianBlur(ImpulsiveNoisyImg, (3, 3), 0)
GaussianBlurdUniformDeNoised = cv2.GaussianBlur(UniformNoisyImg, (3, 3), 0)

# saving the img
cv2.imwrite('GaussianBlurdGaussianDeNoised.jpg', GaussianBlurdGaussianDeNoised)
cv2.imwrite('GaussianBlurdImpulsiveDeNoised.jpg', GaussianBlurdImpulsiveDeNoised)
cv2.imwrite('GaussianBlurdUniformDeNoised.jpg', GaussianBlurdUniformDeNoised)

# checking if everything is ok
print('***fininshed***'*3)
