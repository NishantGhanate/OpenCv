import numpy as np
import cv2

cap = cv2.VideoCapture('H:/Github/OpenCv/Research/videos/pen.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((3,3),np.uint8)

while(1):
    ret, img = cap.read()
    img = np.rot90(img)
    img = np.rot90(img)
    img = np.rot90(img) 
    fgmask = fgbg.apply(img)
    
    # dilation = cv2.dilate(fgmask,kernel,iterations = 2)
    erosion = cv2.erode(fgmask,kernel,iterations = 3)

    cv2.imshow('oG',img)
    cv2.imshow('backminus',fgmask)
    cv2.imshow('erosion',erosion)
    
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
   

          
cap.release()
cv2.destroyAllWindows()