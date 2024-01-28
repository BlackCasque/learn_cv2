import cv2

img1 = cv2.imread("src/img/images.jpeg")

img2 = cv2.flip(img1, 1)

img3 = cv2.flip(img1, 0)

img4 = cv2.flip(img1, -1)

cv2.imshow("1original:", img1)
cv2.imshow("2mirroring:", img2)
cv2.imshow("3mirroring:", img3)
cv2.imshow("4mirroring:", img4)
cv2.waitKey(0)