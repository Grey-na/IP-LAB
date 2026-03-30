import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Image/rhino.jpg")


# Convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Normalize
img_normalized = img / 255.0

gamma = 2.2

# Gamma correction
gamma_corrected = np.power(img_normalized, gamma)

# Scale back
gamma_corrected = np.uint8(gamma_corrected * 255)

# Show images
plt.imshow(img)
plt.title("Original Image")
plt.show()

plt.imshow(gamma_corrected)
plt.title("Gamma Corrected Image")
plt.show()