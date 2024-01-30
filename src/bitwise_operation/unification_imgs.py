import cv2
import numpy as np

img = np.zeros((600, 600), dtype="uint8")

circle = cv2.circle(img.copy(), (0, 0), 100, (255, 255, 255), -1)
square = cv2.rectangle(img.copy(), (50, 50), (550, 550), 255, -1)

img1 = cv2.bitwise_and(circle, square)  # закрашивает одинаковые части
img2 = cv2.bitwise_or(circle, square)  # полное единение
img3 = cv2.bitwise_xor(circle, square)
img4 = cv2.bitwise_not(square)  # инверсия

cv2.imshow("re1:", img1)
cv2.imshow("re2:", img2)
cv2.imshow("re3:", img3)
cv2.imshow("re4:", img4)
cv2.waitKey(0)