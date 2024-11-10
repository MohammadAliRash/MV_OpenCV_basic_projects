import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading img
img = cv2.imread('sammy_face.jpg')

#normal
#edge
edges = cv2.Canny(image=img, threshold1=45, threshold2=135)

while True:
    cv2.imshow('window',edges )
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.imwrite('normal_edge.jpg',edges )

#blurred
blurred_img = cv2.blur(img,ksize=(5,5))

#edge
blurred_edges = cv2.Canny(image=blurred_img, threshold1=45, threshold2=135)

while True:
    cv2.imshow('window', blurred_edges )
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.imwrite('blurred_edge.jpg',blurred_edges )

# comparing the images
plt.subplot(131), plt.imshow(img), plt.title('original')
plt.subplot(132), plt.imshow(edges), plt.title('normal_edge')
plt.subplot(133), plt.imshow(blurred_edges), plt.title('blurred_edge')
plt.show()