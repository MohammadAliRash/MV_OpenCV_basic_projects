Image Corner Detection Project
This project applies the Harris Corner Detection algorithm to detect corners in an image using OpenCV in Python.

Description
In this project, an image ('1.jpg') is read and processed to detect corners using the Harris Corner Detection algorithm. The detected corners are marked on the image, and the resulting image is saved as 'cornered.jpg'. A comparison between the original and marked images is displayed using matplotlib.

Requirements
To run this project, you need the following libraries installed:
OpenCV (cv2)
NumPy
Matplotlib

Usage
Ensure you have the required libraries installed.
Place the image file '1.jpg' in the same directory as your Python script.
Run the script to detect corners in the image using the Harris Corner Detection algorithm.
The image with marked corners will be saved as 'cornered.jpg'.
A comparison between the original and marked images will be displayed using matplotlib.

Code Explanation
The script reads the image, converts it to grayscale, applies the Harris Corner Detection algorithm, marks the detected corners on the image, and saves the result. It then displays a comparison between the original and marked images.

Files
1.jpg: Input image
cornered.jpg: Image with detected corners marked