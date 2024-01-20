import argparse 
import cv2 
 
# Создаем парсер аргументов 
ap = argparse.ArgumentParser() 
 
# Добавляем аргумент для ввода видео 
ap.add_argument("-v", "--video", default=0, help="path to input video, default is webcam 0 if not specified") 
args = vars(ap.parse_args()) 

# объект VideoCapture
cap = cv2.VideoCapture(args["video"])  # используем значение аргумента "video" для задания источника видео

while True: 
    ret, frame = cap.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('video feed', frame) 
    cv2.imshow("gray feed", gray) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

# # Определите параметры для записи видео
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break  # если кадр не прочитался, выходим из цикла

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('video feed', frame)
#     out.write(frame)  # Записываем кадр в видео
#     cv2.imshow("gray feed", gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Определите параметры для записи видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_gray.avi', fourcc, 20.0, (640, 480), isColor=False)  # isColor=False для оттенков серого

while True:
    ret, frame = cap.read()
    if not ret:
        break  # если кадр не прочитался, выходим из цикла

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Преобразование кадра в оттенки серого
    cv2.imshow('video feed', frame)
    out.write(gray)  # Записываем оттенки серого в видео
    cv2.imshow("gray feed", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()  # Освободите объект VideoWriter
cv2.destroyAllWindows()