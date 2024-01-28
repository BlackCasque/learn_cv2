import cv2
import numpy as np

img = cv2.imread("src/img/images.jpeg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 100)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# RETR_LIST - all contours
# CHAIN_APPROX_NONE find all point in contours line

print(con)  # give coordinates all point

cv2.imshow("result:", img)
cv2.waitKey(0)