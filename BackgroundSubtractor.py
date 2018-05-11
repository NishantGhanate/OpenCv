import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg2 = cv2.createBackgroundSubtractorMOG2()


while True:
    ret, frame = cap.read()
    fgmask = fgbg2.apply(frame)

    cv2.imshow('OG' , frame)
    cv2.imshow('fg' ,fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
