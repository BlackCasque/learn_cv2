import cv2
import argparse

# Создаем парсер аргументов 
ap = argparse.ArgumentParser() 
 
# Добавляем аргумент для ввода видео 
ap.add_argument("-v", "--video", default=0, help="path to input video, default is webcam 0 if not specified") 
args = vars(ap.parse_args()) 

# объект VideoCapture
cap = cv2.VideoCapture(args["video"])  # используем значение аргумента "video" для задания источника видео
cap.set(3, 1000)
cap.set(4, 1000)


while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 90, 90)
    cv2.imshow("Resual", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break