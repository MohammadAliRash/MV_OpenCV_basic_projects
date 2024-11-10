Contour Detection Project
This project demonstrates how to detect external and internal contours in an image using OpenCV in Python.

Description
In this project, we load an image ('internal_external.png'), find contours in the image, and differentiate between internal and external contours based on the hierarchy of the contours. External contours are contours that do not have any other contours inside them, while internal contours are contours that lie inside another contour.

Requirements
To run this project, you need to have the following libraries installed:
OpenCV (cv2)
NumPy
Matplotlib

Usage
Make sure you have the required libraries installed.
Place the image file 'internal_external.png' in the same directory as your Python script.
Run the script to detect and visualize external and internal contours.
The detected contours will be saved as:
external_contours.jpg: Image with only the external contours drawn
image_internal.jpg: Image with only the internal contours drawn

Code Explanation
The script loads the image, finds contours, separates external and internal contours based on the contour hierarchy, and then draws and saves the external and internal contours as separate images.

Files
internal_external.png: Input image
external_contours.jpg: Image with only the external contours drawn
image_internal.jpg: Image with only the internal contours drawn