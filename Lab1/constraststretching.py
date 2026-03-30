import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("./Image/low.jpg")
#Find the min and max pixel values
min_val = np.min(img)
max_val = np.max(img)
#Apply contrast stretching formula
#We convert to float to avoid overflow during the calculation
stretched = (img -min_val) * (255.0 / (max_val - min_val))
stretched = np.uint8(stretched)
#Display results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original (low constrast) Image")
plt.imshow(img)
plt.subplot(1,2,2)
plt.title("Contrast Stretched Image")
plt.imshow(stretched)
plt.show()

