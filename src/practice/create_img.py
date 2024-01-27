import cv2
import numpy as np
photo = np.zeros((500, 500, 3), dtype='uint8')

# BGR in OpenCV:

# background
photo[:] = 55, 0, 55

# square
cv2.rectangle(photo, (150, 150), (350, 350), (252, 252, 3), thickness=1)  # thickness = cv2.FILLED закрасит всё пространство в фигуре

cv2.imshow("Photo", photo)
cv2.waitKey(0)