import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("./Image/1.jpg")
t,thresholdimage = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#Display results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original (Before Threshold) Image")
plt.imshow(img, cmap="gray")
plt.subplot(1,2,2)
plt.title("Thresholded Image")
plt.imshow(thresholdimage, cmap="gray")
plt.show()