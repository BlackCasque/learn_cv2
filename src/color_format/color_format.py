# from popular formats: "HSV" and "L*A*B"
import cv2

img = cv2.imread("src/img/images.jpeg")

# to HSV format:
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# to LAB format:
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# on the contrary cv2.COLOR_LAB2BGR and with other


cv2.imshow("img:", img)
cv2.imshow("img1:", img1)
cv2.imshow("img2:", img2)
cv2.waitKey(0)