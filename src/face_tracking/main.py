# ready made NN: https://github.com/opencv/opencv/tree
import cv2

img = cv2.imread("src/face_tracking/1.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceNN = cv2.CascadeClassifier('src/faces.xml')
results = faceNN.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=3)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (230, 14, 78), thickness=1)

cv2.imshow("Result:", img)
cv2.waitKey(0)