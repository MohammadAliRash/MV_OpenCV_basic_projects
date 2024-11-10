import numpy as np
import matplotlib.pyplot as plt
import cv2

# reading img
img = cv2.imread("3.jpg")

# creating noise
uni_noise = np.zeros(img.shape, dtype=np.uint8)
cv2.randu(uni_noise, 0, 255)
uni_noise = (uni_noise*1).astype(np.uint8)

# putting noise on original picture
un_img = cv2.add(img, uni_noise)

# saving the img
cv2.imwrite('3uniformNoise.jpg', un_img)


# # gray scale showing in jupyter lab
# fig = plt.figure(dpi=300)

# fig.add_subplot(1, 3, 1)
# plt.imshow(img, cmap='gray')
# plt.axis("off")
# plt.title("Original")

# fig.add_subplot(1, 3, 2)
# plt.imshow(uni_noise, cmap='gray')
# plt.axis("off")
# plt.title("Uniform Noise")

# fig.add_subplot(1, 3, 3)
# plt.imshow(un_img, cmap='gray')
# plt.axis("off")
# plt.title("Combined")
