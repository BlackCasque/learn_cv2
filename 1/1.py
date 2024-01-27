import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)

# Для отображения изображений используется метод imshow. Первый аргумент – заголовок отображаемого изображения, а второй – сама переменная изображения
cv2.imshow("Image", image)
cv2.waitKey(0)
# cv2.waitKey(0) будет ждать, пока пользователь не нажмет любую клавишу, после чего окно с изображением закроется. 

(h, w) = image.shape[:2]

# display image properties
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))






