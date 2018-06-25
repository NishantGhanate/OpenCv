import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #converting color to HSV Model
    hsv =  cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #index 0= Hue 1= sat 2=value
    lower_limit = np.array([30,150,50])
    upper_limit = np.array([255,255,180])
    
    # inRnage Funtion will return 1 if the color is present range
    mask = cv2.inRange(hsv,lower_limit,upper_limit)

    # 2 frames are passed mask values will applied to 2nd frame and bitwise op
    res = cv2.bitwise_and(frame,frame,mask = mask)
    res = cv2.flip(res,1)
    cv2.imshow('Original Window' , frame)
    cv2.imshow('Result Window' ,res)
    # 27 = esc key to close the winddow
    k = cv2.waitKey(27) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
