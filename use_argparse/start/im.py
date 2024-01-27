import cv2
import numpy as np

img = cv2.imread("img/images.jpeg")

new_img = cv2.resize(img, (500, 500))
# new_img = cv2.resize(img, (img.shape[1]// 2, img.shape[0] // 2))
# new_img = img[0:100, 0:150]
# new_img = cv2.GaussianBlur(new_img, (9, 9), 0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 90, 90)

kernal = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernal, iterations=10)

# cv2.imshow("resualt", new_img)
cv2.imshow("resualt", img)

# print(img.shape)

cv2.waitKey(0)

