import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("./Image/1.jpg")
A,B=100,200
without_background = np.zeros_like(img)
without_background[(img >= A) & (img <= B)] = 255
#Display results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img)
plt.subplot(1,2,2)
plt.title("Without Background")
plt.imshow(without_background)
plt.show()