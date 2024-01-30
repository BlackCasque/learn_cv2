import cv2
import numpy as np

photo = cv2.imread("src/img/images.jpeg")
img = np.zeros(photo.shape[:2], dtype="uint8")

circle = cv2.circle(img.copy(), (100, 100), 50, (255, 255, 255), -1)
square = cv2.rectangle(img.copy(), (50, 50), (550, 550), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=circle)

cv2.imshow("result:", img)
cv2.waitKey(0)