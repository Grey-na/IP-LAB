import cv2
import numpy as np
img=cv2.imread("./Image/lina.jpg")
print(img.shape)
c=255/np.log(1+np.max(img))
log_image=c*np.log(1+img)
log_image=np.array(log_image,dtype=np.uint8)
cv2.imshow("window",log_image)
cv2.imwrite('./Image/lina_transformed.jpg',log_image)
cv2.waitKey(0)  