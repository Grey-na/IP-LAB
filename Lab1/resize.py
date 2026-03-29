import cv2
import numpy as np
img=cv2.imread("./Image/dog.jpg")
print(img.shape)
img_resize=cv2.resize(img,(333,500))
print(img_resize.shape)
cv2.imshow("window",img_resize)
cv2.imwrite('./Image/dog_resize.jpg',img_resize)
cv2.waitKey(0)