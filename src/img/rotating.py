import cv2

img = cv2.imread("src/img/images.jpeg")

def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)  # point of rotating

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    # last parameter indicates how many times do we increase it
    return cv2.warpAffine(img_param, mat, (width, height))

img = rotate(img, 40)

cv2.imshow("result:", img)
cv2.waitKey(0)