Image Edge Detection Project
This project demonstrates edge detection on an image using Canny edge detection algorithm with OpenCV in Python.

Description
In this project, we read an image ('sammy_face.jpg'), apply Canny edge detection on the original image, and compare it with the result obtained after blurring the image. The goal is to showcase the difference in edge detection between the original and blurred images.

Requirements
To run this project, you need to have the following libraries installed:
OpenCV (cv2)
NumPy
Matplotlib

Usage
Ensure you have the required libraries installed.
Place the image file 'sammy_face.jpg' in the same directory as your Python script.
Run the script to apply edge detection on the original and blurred versions of the image.
The edge-detected images will be saved as:
normal_edge.jpg: Edge-detected image using the original image
blurred_edge.jpg: Edge-detected image using the blurred image

Code Explanation
The script loads the image, applies Canny edge detection on the original image, blurs the image, and then applies edge detection on the blurred image. It then displays and saves the edge-detected images for comparison.

Files
sammy_face.jpg: Input image
normal_edge.jpg: Edge-detected image using the original image
blurred_edge.jpg: Edge-detected image using the blurred image