import numpy as np
import matplotlib.pyplot as plt
import cv2

# reading img
img = cv2.imread("3.jpg", 0)

# creating noise
imp_noise = np.zeros(img.shape, dtype=np.uint8)
cv2.randu(imp_noise, 0, 255)
imp_noise = cv2.threshold(imp_noise, 245, 255, cv2.THRESH_BINARY)[1]

# putting noise on original picture
in_img = cv2.add(img, imp_noise)

# saving the img
cv2.imwrite('grayImpulsive3.jpg', in_img)


# # gray scale showing in jupyter lab
# fig = plt.figure(dpi=300)

# fig.add_subplot(1, 3, 1)
# plt.imshow(img, cmap='gray')
# plt.axis("off")
# plt.title("Original")

# fig.add_subplot(1, 3, 2)
# plt.imshow(imp_noise, cmap='gray')
# plt.axis("off")
# plt.title("Impulsive Noise (salt and paper)")

# fig.add_subplot(1, 3, 3)
# plt.imshow(in_img, cmap='gray')
# plt.axis("off")
# plt.title("Combined")
