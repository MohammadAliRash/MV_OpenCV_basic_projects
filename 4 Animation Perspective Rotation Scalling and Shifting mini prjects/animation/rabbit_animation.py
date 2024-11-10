# importing the libraries
import cv2
import numpy as np

# reading the img and setting the rows and cols 
img = cv2.imread('1.png')
rows, cols, ch = img.shape

# creating a video with 18 frame in 9 seconds
for x in range(18):
    angle = x * 20
    matrix_rotated = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 0.6)
    rotated_img = cv2.warpAffine(img, matrix_rotated, (cols, rows))

    cv2.imshow("Rotated image",rotated_img)
    cv2.waitKey(400)
    cv2.destroyAllWindows()

for x in range(20):
    xOffset = 50 + x*20
    yOffset = 25 + x*10

    # define the transformation matrix m
    M = np.float32([[1,0,xOffset],[0,1,yOffset]])
        
    # preform the image Translation and return the results
    dst = cv2.warpAffine(rotated_img ,M,(rotated_img.shape[1], rotated_img.shape[0]))

    cv2.imshow("shifted image",dst)
    cv2.waitKey(500)
    cv2.destroyAllWindows()


# cv2.imwrite('rotated_rabbit.jpg', rotated_img)

