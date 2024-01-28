import cv2
import numpy as np

img = cv2.imread("src/img/images.jpeg")

def offset_img(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])

    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))

img = offset_img(img, 30, 100)

cv2.imshow("result", img)
cv2.waitKey(0)