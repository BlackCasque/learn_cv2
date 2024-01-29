import cv2

img = cv2.imread("src/img/images.jpeg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img1 = cv2.merge([b, g, r])  #объединение слоев

# cv2.imshow("color_r:", r)  # приблеженные к цвету выглядят белыми
# cv2.imshow("color_g:", g)
# cv2.imshow("color_b:", b)
cv2.imshow("img1:", img1)
cv2.waitKey(0)