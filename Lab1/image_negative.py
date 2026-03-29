import cv2
img=cv2.imread("./Image/xrray.jpg")
print(img.shape)
img_negative=255-img
cv2.imshow("window",img_negative)
cv2.imwrite('./Image/xrray_negative.jpg',img_negative)
cv2.waitKey(0)