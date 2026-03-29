import numpy as np
import cv2
img=cv2.imread("./Image/dog.jpg")
print(img.shape)
#img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print(img_gray.shape)
#cv2.imwrite('./Image/dog_gray.jpg',img_gray)
#img[:,:,0]=0
#cv2.imshow("window",img_gray)
imgBlue=img[:,:,0]
imgGreen=img[:,:,1]
imgRed=img[:,:,2]
new_img=np.hstack((imgBlue,imgGreen,imgRed))
cv2.imshow("window",new_img)
cv2.waitKey(0)