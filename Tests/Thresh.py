import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    r,threshold = cv2.threshold(frame,12,255,cv2.THRESH_BINARY)
    cv2.imshow("",threshold)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
