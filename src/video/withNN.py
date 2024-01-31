import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 1000)
cap.set(4, 1000)

while True:
    res, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.Canny(img, 50, 50)

    faceNN = cv2.CascadeClassifier("src/faces.xml")
    resultNN = faceNN.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=1)
    
    for (x, y, w, h) in resultNN:
        cv2.rectangle(img, (x, y), (x+w, y+h), (230, 14, 78), thickness=2)

    cv2.imshow("result:", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break