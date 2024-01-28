import cv2
import numpy as np

im_square = np.zeros((600, 600, 3), dtype='uint8')

im_square[:] = 100, 210, 100

# square:
im_square = cv2.rectangle(im_square, (200, 200), (400, 400), (0, 0, 0), thickness=1)

cv2.imshow("square:", im_square)

################################################################################

im_line = np.zeros((600, 600, 3), dtype="uint8")

im_line = cv2.line(im_line, (200, 200), (400, 400), (255, 255, 255), thickness=2)

im_line = cv2.line(im_line, (0, im_line.shape[0] // 2), (im_line.shape[1], im_line.shape[0] // 2), (0, 0, 255), thickness=3)

cv2.imshow("line:", im_line)

################################################################################

im_circle = np.ones((600, 600, 3), dtype="uint8")

im_circle = cv2.circle(im_circle, (im_circle.shape[1] // 2, im_circle.shape[0] // 2), 50, (0, 255, 0), thickness=1)

cv2.imshow("circle:", im_circle)

##################################################################################

# text in image:
cv2.putText(im_circle, "Hello World", (250, 250), cv2.FONT_ITALIC, 1, (255, 0, 0), 3)
cv2.imshow("text:", im_circle)

cv2.waitKey(0)