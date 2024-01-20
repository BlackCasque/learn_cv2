import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# После создания экземпляра argparse, добавим аргумент, который, по сути, сообщает, что изображение передается, как аргумент, и его нужно распарсить.
# Затем обработанный аргумент передается функции vars(), которая возвращает атрибут dict указанного объекта.
# С помощью метода imread из cv2, мы положим изображение в переменную image.

image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)

# Для отображения изображений используется метод imshow. Первый аргумент – заголовок отображаемого изображения, а второй – сама переменная изображения
cv2.imshow("Image", image)
cv2.waitKey(0)
# cv2.waitKey(0) будет ждать, пока пользователь не нажмет любую клавишу, после чего окно с изображением закроется. 

(h, w) = image.shape[:2]

# display image properties
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))






