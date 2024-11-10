Image Thresholding Project
This project demonstrates different image thresholding techniques using OpenCV and matplotlib in Python.

Description
In this project, we load an image ('1c.jpg'), convert it to grayscale, and apply various thresholding techniques to create binary images. The thresholding techniques used are:

Simple thresholding with a fixed threshold of 127
Adaptive thresholding using a mean-based approach
Otsu's thresholding method
Band thresholding by combining two thresholded images
Requirements
To run this project, you need to have the following libraries installed:

OpenCV (cv2)
Matplotlib
NumPy
Usage
Ensure you have the required libraries installed.
Place the image file '1c.jpg' in the same directory as your Python script.
Run the script to see the thresholded images and save them as separate files.
The thresholded images will be saved as:
original_gray.jpg (original grayscale image)
thresh127.jpg (result of thresholding with a fixed threshold of 127)
adaptiveTheresh.jpg (result of adaptive thresholding)
otsuTheresh.jpg (result of Otsu's thresholding)
bandTheresh.jpg (result of band thresholding)
Code Explanation
The script loads the image, converts it to grayscale, applies different thresholding methods, and saves the resulting images. Each thresholding method is applied and visualized using matplotlib.

Files
1c.jpg: Input image
original_gray.jpg: Grayscale version of the original image
thresh127.jpg: Binary image using a fixed threshold of 127
adaptiveTheresh.jpg: Binary image using adaptive thresholding
otsuTheresh.jpg: Binary image using Otsu's thresholding
bandTheresh.jpg: Binary image using band thresholding