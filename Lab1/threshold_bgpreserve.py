import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("./Image/1.jpg")

# Convert to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold to create mask
t, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Apply mask to original image (preserve background)
result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)

# Display
plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(img_rgb)

plt.subplot(1,3,2)
plt.title("Mask")
plt.imshow(mask, cmap="gray")

plt.subplot(1,3,3)
plt.title("Background Preserved")
plt.imshow(result)

plt.show()