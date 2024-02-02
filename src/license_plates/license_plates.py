# we don't use nn model, don't use it in large projects
import matplotlib.pyplot as plt
import numpy as np
import imutils
import easyocr
import cv2


img = cv2.imread("src/license_plates/carImg.jpeg")

gray_im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filter_im = cv2.bilateralFilter(gray_im, 11, 15, 15)
edges = cv2.Canny(filter_im, 30, 30)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 8, True)
    if len(approx) == 4:
        pos = approx
        break

# print(pos)

mask = np.zeros(gray_im.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, (230, 14, 78), -1)
bitwise_img = cv2.bitwise_and(img, img, mask = mask)

(x, y) = np.where(mask==230)
(x1, y1) = np.min(x), np.min(y)
(x2, y2) = np.max(x), np.max(y)

crop = gray_im[x1:x2, y1:y2]

text = easyocr.Reader(["en"])
text = text.readtext(crop)
# print(text)

res1 = text[0][-2]
res = res1[1:7]
final_img = cv2.putText(img, res, (y1 - 50, x2 - 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
final_img = cv2.rectangle(img, (y2, x1), (y1, x2), (0, 255, 0), 1)
print((x1, x2, y1, y2))

plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
plt.show()