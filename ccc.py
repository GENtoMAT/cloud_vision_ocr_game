
import cv2
import time


#frame = cv2.resize(frame, size)

cv2.namedWindow("camera capture", cv2.WINDOW_NORMAL)
resized_frame = cv2.resize(frame,(int(1920/3), int(1080/3)))
img = cv2.imread('./img/cap.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('camera capture', img)

time.sleep(3)

cv2.waitKey(0)
cv2.destroyAllWindows()